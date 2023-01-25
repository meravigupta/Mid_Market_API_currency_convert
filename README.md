#	

#
# Technical Specification
Mid-Market Currency Converter API




This is a simple Python/FAST application intended to provide a working example of Mid-Market Currency Converter APIs. The goal of these endpoints is to provide a base for developers to develop other applications.
# Table of Contents


[*Technical Specification](#_w6q4rrwwts2q)*	

[*Table of Contents](#_tyjcwt)*	

[*Integrating ](#_b3elmwdy9suj)*currency converter**	

[API Authentication](#_2s8eyo1)	

Mid-Market Currency Converter[ APIs](#_16jvfqowcqsw)	

Currency Convert[ API](#_3rdcrjn)

`      `URL : /convert

Currency Codes API

`      `URL : /currencies
History of all Convert[ ](#_3rdcrjn)Currency API

`      `URL : /history

`       `How To Use This	



#
#
#       
# Integrating
## API Authentication

POST API /token, this endpoint enables user to generate authentication token by passing necessary information such as user name and password which w be used to authenticate other API to  endpoints

Given a token *bearer\_token*,


|**KEY**|**Value**|
| :- | :- |
|Username|name|
|Password|name|


##
##
##
##
##
##
##
##

## Mid-Market Currency Converter APIs
### 1. Currencies API

`      `This API will be used to get all the Currencies Code  

`       `URL : ***<host>/**currencies*


|Url|<host>/currencies|
| :- | :- |
|Body|<p>{</p><p>}</p>|
|Method|GET|
|Response Body|{ "currency": [ "EUR", "GBP", "USD", "INR", "CAD", "AUD", "CHF", "MXN", "FJD", "SCR", "BBD", "GTQ", "CLP", "HNL", "UGX", "ZAR", "TND", "BSD", "SLL", "GMD", "TWD", "RSD", "DOP", "KMF", "MYR", "FKP", "XOF", "GEL", "UYU", "MAD", "CVE", "TOP", "AZN", "OMR", "PGK", "KES", "SEK", "BTN", "UAH", "GNF", "MZN", "SVC", "ARS", "QAR", "CNY", "THB", "UZS", "XPF", "MRU", "BDT", "BMD", "KWD", "PHP", "RUB", "PYG", "ISK", "JMD", "COP", "MKD", "DZD", "PAB", "GGP", "SGD", "ETB", "JEP", "KGS", "VUV", "LAK", "BND", "XAF", "LRD", "HRK", "ALL", "DJF", "ZMW", "TZS", "VND", "ILS", "GHS", "GYD", "BOB", "KHR", "MDL", "IDR", "KYD", "AMD", "BWP", "SHP", "TRY", "LBP", "TJS", "JOD", "AED", "HKD", "RWF", "LSL", "DKK", "BGN", "MMK", "MUR", "NOK", "IMP", "GIP", "RON", "LKR", "NGN", "CRC", "CZK", "PKR", "XCD", "ANG", "HTG", "BHD", "KZT", "SRD", "SZL", "SAR", "TTD", "MVR", "AWG", "KRW", "NPR", "JPY", "MNT", "AOA", "PLN", "SBD", "BYN", "HUF", "MWK", "MGA", "BZD", "BAM", "EGP", "MOP", "NAD", "NIO", "PEN", "NZD", "WST", "TMT", "BRL" ] }|
|Response Code|200|
#### Error Codes

|**Code**|**Scenario**|**Response**|
| :- | :- | :- |
|401|Unauthorized|<p>{</p><p>`    `""msg": "unauthorized access"</p><p>}</p>|
|400|Bad request|<p>{</p><p>`   `"msg": "parameters are wrong or missing"</p><p>}</p>|



### Convert API

This API will be used to get converted amount and Mid-Market rate

URL : ***<host>/convert***


|Url|<host>/currencies|
| :- | :- |
|Body|<p>{</p><p>“from\_currency” : USD,</p><p>“to\_currency” : INR,</p><p>“amount”: 200</p><p>}</p>|
|Method|GET|
|Response Body|<p>{</p><p>`       `"converted\_amount": 16314.7,</p><p>`       `"rate": 81.5735,</p><p>`       `"metadata":</p><p>`            `{</p><p>`             `"time\_of\_conversion": "2023-01-25T16:59:51.954381",</p><p>`             `"from\_currency": "USD",</p><p>`               `"to\_currency": "INR"</p><p>`             `}</p><p>`  `}</p>|
|Response Code|200|
#### Error Codes

|**Code**|**Scenario**|**Response**|
| :- | :- | :- |
|401|Unauthorized|<p>{</p><p>`    `""msg": "unauthorized access"</p><p>}</p>|
|400|Bad request|<p>{</p><p>`   `"msg": "parameters are wrong or missing"</p><p>}</p>|
###
###
###
### History API

This API will be used to get all Converted Amount and Mid-Market Rate History

URL : ***<host>/**history*


|Url|<host>/history|
| :- | :- |
|Body|<p>{</p><p>}</p>|
|Method|GET|
|Response Body|<p>[</p><p>{</p><p>`       `"converted\_amount": 16314.7,</p><p>`       `"rate": 81.5735,</p><p>`       `"metadata":</p><p>`            `{</p><p>`             `"time\_of\_conversion": "2023-01-25T16:59:51.954381",</p><p>`             `"from\_currency": "USD",</p><p>`               `"to\_currency": "INR"</p><p>`             `}</p><p>`  `}</p><p>]</p>|
|Response Code|200|
#### Error Codes

|**Code**|**Scenario**|**Response**|
| :- | :- | :- |
|401|Unauthorized|<p>{</p><p>`    `""msg": "unauthorized access"</p><p>}</p>|
|400|Bad request|<p>{</p><p>`   `"msg": "parameters are wrong or missing"</p><p>}</p>|

How To Use This

---------------

1. Install all the required libraries.

   *Requests*

   *BeautifulSoup*

   *fastapi*

   *python-multipart*


2. Install uvcon to run the API : command - "uvicorn scraper:app –reload"

3. <host>/docs will give the index page for the API.

4. To use the API you are required to authenticate using username and password (currently will work for any username and password).

5. After authentication you can use other API requests (without authentication APIs will not work).

