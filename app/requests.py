import urllib.request,json
import requests 


# Getting api key
api_key = None


def configure_request(app):
    global api_key
    api_key = app.config['API_KEY']

def get_currencies():
    '''
    Function that gets the json response to our url request
    '''
    get_currencies_url = f"https://free.currconv.com/api/v7/currencies?apiKey={api_key}"
    currency_data = requests.get(get_currencies_url).json()["results"]
    
    currencies = []
    for data in currency_data:
         currencies.append(data)
   

    return currencies
    
def get_currency_rates(initalCurrency,ConvertToCurrency):
    '''
    Function that gets the json response to our url request
    '''
    rates_url = f"https://free.currconv.com/api/v7/convert?q={initalCurrency}_{ConvertToCurrency}&compact=ultra&apiKey={api_key}"
    rate = requests.get( rates_url).json()
    
    return rate

    
    
