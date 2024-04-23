from bs4 import BeautifulSoup

with open('_up_2020_pmi.xml', 'r', encoding="utf-8") as file:
    data = file.read()

soup = BeautifulSoup(data, 'html.parser')

dik = []

kafedri = soup.find_all('дисциплина')

print(dik)