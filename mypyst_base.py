import requests, re, os
from bs4 import BeautifulSoup

def stock_price(symbol: str = "ABCDEFGHIJKLMNOPQRSTUV") -> str:
    myrawfile = f"{symbol}_raw.raw"

    if os.path.exists(myrawfile):
        os.remove(myrawfile)
    else:
        print("No current raw data, will create then..")


    url = f"https://in.finance.yahoo.com/quote/{symbol}?s={symbol}"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    class_ = "My(6px) Pos(r) smartphone_Mt(6px)"

    with open(myrawfile, "w") as filerawdata:
        filerawdata.write(soup.prettify())

    return soup.find("div", class_=class_).find("span").text


if __name__ == "__main__":
    for symbol in "CRAYON.OL ORK.OL".split():
        print(f"Current {symbol:<15} stock price is {stock_price(symbol):>8}")
