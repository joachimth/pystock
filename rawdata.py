import requests, re, os
from bs4 import BeautifulSoup

def stock_price(symbol: str = "ABCDEFGHIJKLMNOPQRSTUV") -> str:

    url = f"https://in.finance.yahoo.com/quote/{symbol}?s={symbol}"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    class_ = "My(6px) Pos(r) smartphone_Mt(6px)"

    return soup.find("div", class_=class_).find("span").text



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
    print ("\n\nDump raw BeatifulSoup into file...\n")
    for symbol in "CRAYON.OL ORK.OL".split():
        print (f"..We are getting raw stocks for you.. {symbol:<15}")
        print (f".................Saved into raw log.. {getraw_stock(symbol)}\n")
