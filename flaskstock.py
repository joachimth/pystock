from flask import Flask, render_template,request,redirect,url_for # For flask implementation
import requests, re, os
from bs4 import BeautifulSoup
#from datetime import datetime
import time

##
##Flask Main init section
##
app = Flask(__name__)
title = "Stocks shown by Flask, with python assistance"
heading = "Stock Getter"

def redirect_url():
    return request.args.get('next') or \
        request.referrer or \
        url_for('index')


##
##Static py app..
##

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
        class_ = "C($tertiaryColor) Fz(12px)"
        self.currency = soup.find("div", class_=class_).find("span").text.split("Currency in ")[1]

    def say_hi(self):
        print(f"{self.symbol:<20}", ' ... ', f"{self.currentvalue:<8}", ' .... ', f"{self.currency:<4}")

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


@app.route("/")
def mainindex ():
#Display the Main site..
    return render_template('index.html',t=title,h=heading)


@app.route("/about")
def about():
    return render_template('credits.html',t=title,h=heading)

@app.route("/getstock")
def getstock():
    for symbol in "CRAYON.OL ORK.OL".split():
        Stock_Class(symbol).say_hi()
    return render_template('index.html',t=title,h=heading)

if __name__ == "__main__":
    #start_time = time.time()
    #print ("\n\nStock extractor...\n")
    #for symbol in "CRAYON.OL ORK.OL".split():
    #    Stock_Class(symbol).say_hi()
    #e = time.time() - start_time
    #print("%02d:%02d:%02d" % (e // 3600, (e % 3600 // 60), (e % 60 // 1)))

    env = os.environ.get('APP_ENV', 'development')
    port = int(os.environ.get('PORT', 5000))
    debug = False if env == 'production' else True
    app.run(host='0.0.0.0', port=port, debug=debug)
    # Careful with the debug mode..
