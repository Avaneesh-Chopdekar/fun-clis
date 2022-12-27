import sys
from bs4 import BeautifulSoup
import requests

stock_name = ""
URL = "https://www.google.com/search?client=firefox-b-d&q=stock+"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"}
stock_class = "aMEhee"
price_class = "IsqQVc"
diff_jsname = "qRSVye"
diff_by_class = "jBBUv"

def stock():
  try:
      try:
          stock_name = sys.argv[1]
      except IndexError:
          stock_name = input("Enter Stock Name: ")

      if " " in stock_name:
          stock_name.replace(" ", "+")
      elif "-" in stock_name:
          stock_name.replace("-", "+")

      r = requests.get(f"{URL}{stock_name}", headers=headers)
      content = r.content
      soup = BeautifulSoup(content, "html.parser")

      stock_company = soup.find("span", class_=stock_class).get_text()
      price = soup.find("span", class_=price_class).get_text()
      diff = soup.find("span", jsname=diff_jsname).get_text()
      diff = diff[:1] + "₹" + diff[1:]  # To display -₹10 or +₹10
      diff_by = soup.find("span", class_=diff_by_class).get_attribute_list("aria-label")[0]
      print(f"Price of {stock_company} Stock is ₹{price}")
      print(f"It is {diff_by} i.e. {diff} as of Today")
  except KeyboardInterrupt:
    exit(0)

if __name__ == "__main__":
    stock()
