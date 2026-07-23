from parser import cleaning





def recommendation(website_data):
    combined_data="".join(str(val) for val in website_data.values()).lower()

    
    strength=[]
    weakness=[]

    services = {
    "SEO": ["seo", "search engine optimization"],
    "Google Ads": ["google ads", "ppc"],
    "Social Media": ["social media", "instagram", "facebook"],
    "Email Marketing": ["email marketing"],
    "Website Development": ["website development", "web development"],
    "UI/UX": ["ui", "ux", "figma"]
    }
    for service_name,keywords in services.items():
        if any(keyword in combined_data for keyword in keywords):
            strength.append(service_name)
        else:
            weakness.append(service_name)            
        
    print(f"Your strenghts are {strength}")
    print(f"Your weakness are {weakness}")                   




        





