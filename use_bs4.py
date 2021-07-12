import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print ('success')
        #print (response.text)
        soup = BeautifulSoup(response.text , 'html.parser')
        print (soup.title)
except Exception as e:
    print (f'error  {e}')



