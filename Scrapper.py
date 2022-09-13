import requests
from bs4 import BeautifulSoup
class Scrapper:    
    def bbc_scrapper(self, url):
        data = []
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')        
        title = soup.find(id="main-heading").text
        img = soup.find('img')['src']
        subtitle = soup.find('b',class_ = 'ssrcss-hmf8ql-BoldText e5tfeyi3').text
        body = soup.find('article', class_='ssrcss-pv1rh6-ArticleWrapper e1nh2i2l6').text        

        x = {
            'Title':title,
            'Sub Title':subtitle,
            'Image' : img,
            'Body': body
        }
        data.append(x)
        return data

    
