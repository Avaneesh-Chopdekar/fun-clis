#!/usr/bin/env python3

import os
import sys
import requests

currency = ""
CRYPTO_API = os.environ["CRYPTO_API"]
RATE_API = os.environ["RATE_API"]
headers = {"apikey": os.environ["API_KEY"]}
help = """This is a command line interface which tells crypto currency prices

coin [ARGUMENT]
That argument can be either list or coin id.
If argument is list, it will print 20 coin names with their id.
If argument is coin id, It will print it's value in INR and USD and it's changes.
"""

def coin():
    try:
        currency = sys.argv[1]
    except IndexError:
        currency = input("Please enter a currency: ")

    if currency == "exit":
        sys.exit(0)

    try:
        if currency in ["--help", "-h"]:
            print(help)
        elif currency == "list":
            list_r = requests.get(f"{CRYPTO_API}?limit=20")
            list_data = list_r.json()["coins"]
            for i in list_data:
                print(f'{i["name"]} as {i["id"]}')
        else:
            crypto_r = requests.get(f"{CRYPTO_API}{currency}")
            data = crypto_r.json()["coin"]

            rate_r = requests.get(RATE_API, headers=headers)
            diff = rate_r.json()["result"]
            price_inr = diff * data["price"]
            price_change_1h_inr = diff * data["priceChange1h"]
            price_change_1d_inr = diff * data["priceChange1d"]
            price_change_1w_inr = diff * data["priceChange1w"]

            f_price = str(round(data["price"], 2))
            if "-" in f_price:
                f_price = f_price[:1] + "$" + f_price[1:]
            else:
                f_price = "$" + f_price

            f_price_inr = str(round(price_inr, 2))
            if "-" in f_price_inr:
                f_price_inr = f_price_inr[:1] + "₹" + f_price_inr[1:]
            else:
                f_price_inr = "₹" + f_price_inr

            f_price_change_1h = str(round(data["priceChange1h"], 2))
            if "-" in f_price_change_1h:
                f_price_change_1h = f_price_change_1h[:1] + "$" + f_price_change_1h[1:]
            else:
                f_price_change_1h = "$" + f_price_change_1h

            f_price_change_1h_inr = str(round(price_change_1h_inr, 2))
            if "-" in f_price_change_1h_inr:
                f_price_change_1h_inr = f_price_change_1h_inr[:1] + "₹" + f_price_change_1h_inr[1:]
            else:
                f_price_change_1h_inr = "₹" + f_price_change_1h_inr

            f_price_change_1d = str(round(data["priceChange1d"], 2))
            if "-" in f_price_change_1d:
                f_price_change_1d = f_price_change_1d[:1] + "$" + f_price_change_1d[1:]
            else:
                f_price_change_1d = "$" + f_price_change_1d

            f_price_change_1d_inr = str(round(price_change_1d_inr, 2))
            if "-" in f_price_change_1d_inr:
                f_price_change_1d_inr = f_price_change_1d_inr[:1] + "₹" + f_price_change_1d_inr[1:]
            else:
                f_price_change_1d_inr = "₹" + f_price_change_1d_inr

            f_price_change_1w = str(round(data["priceChange1w"], 2))
            if "-" in f_price_change_1w:
                f_price_change_1w = f_price_change_1w[:1] + "$" + f_price_change_1w[1:]
            else:
                f_price_change_1w = "$" + f_price_change_1w

            f_price_change_1w_inr = str(round(price_change_1w_inr, 2))
            if "-" in f_price_change_1w_inr:
                f_price_change_1w_inr = f_price_change_1w_inr[:1] + "₹" + f_price_change_1w_inr[1:]
            else:
                f_price_change_1w_inr = "₹" + f_price_change_1w_inr

            print(f"Price of {data['name']} is {f_price} i.e. {f_price_inr}")
            print(f"Price changed by 1 hour is {f_price_change_1h} i.e. {f_price_change_1h_inr}")
            print(f"Price changed by 1 day is {f_price_change_1d} i.e. {f_price_change_1d_inr}")
            print(f"Price changed by 1 week is {f_price_change_1w} i.e. {f_price_change_1w_inr}")
    except:
        print("Please enter a valid crypto currency.")


if __name__ == "__main__":
    try:
        coin()
    except KeyboardInterrupt:
        exit(0)
