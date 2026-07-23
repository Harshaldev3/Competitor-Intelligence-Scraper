import requests



headers={
    "User-Agent":"Mozilla/5.0"
}
html_pages=[]
def html_text_full(website_urls):    
    for url in website_urls:
        try:
            response=requests.get(url,headers=headers)
            print(f"Status Code:{response.status_code}")
            html_pages.append(response.text)
            
            
            

        except requests.exceptions.RequestException:
            print(f"Final Url:{url}")
            print("Fake Website ❌ Connection Failed") 
                
            print()
    return html_pages
