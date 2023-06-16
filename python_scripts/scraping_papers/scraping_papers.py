import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Send a GET request and retrieve the webpage content
url = "https://paperswithcode.com/"
response = requests.get(url)
content = response.content

# Parse the webpage content using BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# Get all the paper cards
papers = soup.find_all("div", class_="row infinite-item item paper-card")

# Iterate over each paper card and retrieve the title, abstract, and release date
for paper in papers:
    # Extract the paper title
    title = paper.find("h1").text.strip()
    
    # Extract the paper abstract
    abstract = paper.find("p", class_="item-strip-abstract").text.strip()
    
    # Extract the paper release date
    released_date = paper.find("span", class_="author-name-text item-date-pub").text.strip()

    # Extract the paper link
    link = paper.find("a", class_="badge badge-light")['href']
   
    # Append the correct protocol if the link starts with "//"
    if link.startswith("//"):
        link = "https:" + link
    
    # Combine the URL and the link to form the full link
    full_link = urljoin(url, link)
    
    # Display the paper information
    print("Title:", title)
    print("Abstract:", abstract)
    print("Released Date:", released_date)
    print("Link:", full_link)
    print("--------------------")
