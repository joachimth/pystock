import requests, re, os
from bs4 import BeautifulSoup

class Stock_Class:
    def __init__(self, symbol):
        self.symbol = symbol

        url = f"https://in.finance.yahoo.com/quote/{symbol}?s={symbol}"
        soup = BeautifulSoup(requests.get(url).text, "html.parser")

        ##Find current value..
        ##
        class_ = "My(6px) Pos(r) smartphone_Mt(6px)"
        self.currentvalue = soup.find("div", class_=class_).find("span").text

        ##Find current currency..
        ##
        class_ = ""
        self.currency = "NONE"

    def say_hi(self):
        print(self.symbol, ' ... ', self.currentvalue, ' .... ', self.currency)


def getraw_stock(symbol: str = "ABCDEFGHIJKLMNOPQRSTUV") -> str:
##
##
## Check if file exists..If it does, remove it.
## Create log file, name based on STOCK symbol..
## Soup.prettify everything and dump it raw in this file..

    myrawfile = f"{symbol}_raw.raw"
    if os.path.exists(myrawfile):
        #print("The file already exists..Will be overwritten..")
        os.remove(myrawfile)
    else:
        print("")

    url = f"https://in.finance.yahoo.com/quote/{symbol}?s={symbol}"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")

    with open(myrawfile, "w") as filerawdata:
        filerawdata.write(soup.prettify())
    return myrawfile  #Return the resulting filename..


if __name__ == "__main__":
    #print ("\n\nStock extractor...\n")
    #for symbol in "CRAYON.OL ORK.OL".split():
    #    print (f"..We are getting stocks for you.. {symbol:<15}   {stock_price(symbol):<8}\n")
    firststock = Stock_Class('CRAYON.OL')
    firststock.say_hi()
    print (f"{Stock_Class('ORK.OL').currentvalue}")
