from bs4 import BeautifulSoup
import requests
from csv import writer


url = "https://www.jumia.com.ng/laptops/dell/?gclid=Cj0KCQjwhY-aBhCUARIsALNIC05Qzfwkjz6kTO06FtQWG8zH3H1bBv6y8YrPDKCvmG4DSZ0jykZ1yl4aAoEREALw_wcB"
page = requests.get(url).text
soup = BeautifulSoup(page, "lxml")
name = soup.find_all("h3", class_="name")
price = soup.find_all("div", class_="prc")

with open("Dell computer Jumia Store.csv", "w", encoding="utf8", newline="") as f:
    my_writer = writer(f)
    header = ["name and specs", 'price']
    my_writer.writerow(header)
    for n, p in zip(name, price):
        info = [n.text, p.text]
        my_writer.writerow(info)

