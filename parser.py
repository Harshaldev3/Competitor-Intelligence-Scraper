
from scraper import html_text_full
from bs4 import BeautifulSoup
import requests
'''Website
│
├── metadata
│      ├── url
│      ├── title
│
├── content
│      ├── h1
│      ├── h2
│      ├── h3
│      ├── paragraphs
│
└── links'''




def cleaning(website_urls):                                         
    html_pages=html_text_full(website_urls)
    for html in html_pages:
        soup=BeautifulSoup(html,"html.parser")
        website_data={}
        website_data["metadata"]=soup.title.text.strip()
        website_data["URL of Website"]=website_urls
        website_data["content"]={}
        website_data["content"]["h1"]=[h1.get_text().strip() for h1 in soup.find_all('h1')]
        website_data["content"]["h2"]=[h2.get_text().strip() for h2 in soup.find_all('h2')]
        website_data["content"]["h3"]=[h3.get_text().strip() for h3 in soup.find_all('h3')]
        website_data["content"]["p"]=[p.get_text().strip() for p in soup.find_all('p')]
        website_data["links"]=[]
        for link in soup.find_all("a",href=True):
            text=link.get_text().strip()
            href=link.get("href").strip() 

            if text=="":
                continue

            website_data["links"].append({
                "text":text,
                "href":href
            })
            
       

        
        return website_data











        # for link in soup.find_all('a', href=True):
        #     href=link['href']
        #     text=link.text.strip()
        # website_data["links"]={}
        # website_data["links"]["href"]=href
        # website_data["links"]["text"]=text







