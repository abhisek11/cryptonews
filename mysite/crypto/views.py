from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    #Grab crypto price data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,LTC,BCH,XLM,USDT,MIOTA,MKR,NEO&tsyms=USD,INR")
    price = json.loads(price_request.content)


    # Grab crypto news data
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request,'home.html',{'api': api,'price':price})
def prices(request):
    import requests
    import json
    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" +quote+ "&tsyms=USD")
        crypto = json.loads(crypto_request.content)

        return render(request, 'prices.html',{'quote':quote ,'crypto':crypto})
    else:
        notfound = "Enter the crypto currency Symbol into the form above... "
        return render(request, 'prices.html',{'notfound':notfound})
   