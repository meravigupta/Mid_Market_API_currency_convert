import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

session = requests.Session()
for_history = []
app = FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def token_generate(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {"access_token": form_data.username, "token_type":"bearer"}


def _generate_url(from_currency:str, to_currency:str, amount:int):
    url = f"https://wise.com/gb/currency-converter/{from_currency}-to-{to_currency}-rate?amount={amount}"
    return url

def _get_page(url:str):
    response = session.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'lxml')
    return soup

def event_of_the_day(from_currency:str, to_currency:str, amount:int):
    url = _generate_url(from_currency, to_currency, amount)
    page = _get_page(url)
    return page

def country_currency_list():
    url = "https://wise.com/gb/currency-converter/"
    payload={}
    response = session.request("GET", url, data=payload)
    soup = BeautifulSoup(response.content, 'lxml')

    data = soup.find("script", id="__NEXT_DATA__", type="application/json")
    country_currency_code_list = []
    coin_data = json.loads(data.contents[0])
    listings = coin_data["props"]["pageProps"]["model"]["currencies"]
    for country_currency in listings:
        code = country_currency['code']
        country_currency_code_list.append(code)

    return country_currency_code_list

def currency_converter(from_currency:str, to_currency:str, amount:int):
    amount_value = float(0.0)
    rate_value = float(0.0)
    date_time = datetime.now()
    country_currency_code_list = country_currency_list()
    if from_currency not in country_currency_code_list:
            return amount_value, rate_value, date_time
    soup = event_of_the_day(from_currency, to_currency, amount)
    if not soup:
        return amount_value, rate_value, date_time
    try:
        amount_value = soup.find_all("div",{"class":"form-group"})[1].text.replace(",", "")
    except:
        return amount_value, rate_value, date_time
    m = re.search(r'converted\s*to\s*([\d\.?\w?\-?\+?]+)\s*[a-z]+', amount_value, flags=re.I)
    if m:
        amount_value = m.group(1)
    else:
        return amount_value, rate_value, date_time
    rate_value = soup.find("input", {"type":"number","class":"RateAlertsSignup_rateAlertsSignup__currencyInput__input__Chm0k form-control"})['value']
    return amount_value, rate_value, date_time


@app.get("/currencies")
async def read_item(token: str = Depends(oauth_scheme)):
    list_of_country = country_currency_list()
    return {"currency": list_of_country}

@app.get("/convert")
async def read_item(from_currency: str, to_currency: str, amount: int, token: str = Depends(oauth_scheme)):
    amount_value, rate_value, _datetime = currency_converter(from_currency, to_currency, amount)
    result = {
        "converted_amount": float(amount_value),
        "rate": float(rate_value),
        "metadata" : {
        "time_of_conversion" : _datetime,
        "from_currency" : str(from_currency),
        "to_currency" : str(to_currency)
            }
    }
    for_history.append(result)
    return result
# for history
@app.get("/history")
async def read_root(token: str = Depends(oauth_scheme)):
    return for_history
