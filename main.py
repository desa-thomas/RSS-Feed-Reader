import feedparser
"""
Gets RSS feed URL from user
"""
def getUrl(): 
    print("-"*40)
    url = input("Paste RSS feed URL (or empty to quit): ")
    print() 
    return url 

"""
Gets RSS feed information from URL 
"""
def feedInfo(url): 
    d = feedparser.parse(url)
    bozo = d.bozo

    if  bozo == True: 
        print("Invalid URL try again")
        return -1, None, None 
    
    else: 
        title = d.feed.title
        description = d.feed.description 
        link = d.feed.link 
        return title, description, link 

"""
Main function 
"""
def main(): 
    
    url = getUrl()
    while url != '': 
        title, description, link = feedInfo(url)

        if title != -1: 
            print(f"Title: {title}")
            print(f"Description: {description}")
            print(f"link: {link}")  
        
        url = getUrl()



if __name__ == "__main__": 
    main()
