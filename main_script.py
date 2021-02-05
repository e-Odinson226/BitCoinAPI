import requests
try:
    url = 'http://www.geoplugin.net/currency/php.gp?from=%s&to=%s&amount=%i'
    response = requests.get( url %('EUR', 'IRR',1))
    print(response.text)
except:
    raise Exception("error")