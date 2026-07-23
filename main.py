from scraper import html_text_full
from parser import cleaning
from analyzer import recommendation
\
def main():
    website_urls=["https://github.com/"]

    print("Scraping started...")
    html_pages=html_text_full(website_urls)

    print("Cleaning data...")
    website_data=cleaning(website_urls)

    print("Analyzing data...")
    recommendation(website_data)

if __name__=="__main__":
    main()                                                          