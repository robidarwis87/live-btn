import pandas as pd
from bs4 import BeautifulSoup
from requests_html import HTMLSession


# filename = 'developer-page.html'

# # TODO: Replace with requests.get
# with open(filename) as file:
#     html = file.read() # string

url = 'https://www.btnproperti.co.id/developer?pg=2'

session = HTMLSession() # menyimpan cookies, login, ....

response = session.get(url) # buka situs
response.html.render() # ditunggu sampai js render
html = response.html.html # string

soup = BeautifulSoup(html, 'html.parser')

cards = soup.find_all('div', class_='col-6 col-md-4 mb-4')


developers = []

for card in cards:
    title = card.find('h3', class_='title').text
    jumlah = card.find('div', class_='jumlah').text
    link = card.find('a')['href']

    developer = {
        'title': title,
        'jumlah': jumlah,
        'link': link
    }

    developers.append(developer)

print(len(developers))
print(developers[0])

df = pd.DataFrame(developers)
df.to_csv('developers2.csv')

print("Success")

# TODO: Manage data into proper format/collection --> list of dictionary
# TODO: Manage code into functions
