# it is library used to request web pages from the internet.
import requests
from bs4 import BeautifulSoup
import re


# Example 1
# Choose a webpage to look through & store it in a variable
url = 'https://www.ebay.com/b/Athletic-Shoes/15709?US%2520Shoe%2520Size=13%7C13%252E5&US%2520Shoe%2520Size%2520%2528Men%2527s%2529=6%7C6%252E5&rt=nc&mag=1&_udlo=100'

# This commands mimics a browser request in order to pass through blockers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# It then sends a request to retrieve the url with the .get feature
website = requests.get(url, headers=headers)

# It parses through the HTML content of the page
soup = BeautifulSoup(website.text, 'html.parser')

# And begins the count of "Nike" mentions starting from 0
nike_count = 0

# It starts by searching for all text in the HTML
html = soup.find_all(string=re.compile('Nike', re.IGNORECASE))

# Then I created a for loop which counts the amount of times nike was said in the html
for occurrence in html:
    nike_count += 1

# Finally it Print the total amount times nike was in the HTML
print(f'The word "Nike" was found {nike_count} times on Ebay.')


#Example 2

# It scrapes and holds all the hyperlinks in the HTML and store it in the variable
links = soup.find_all('a')

# This is a list to store the amount of URLs the website has
valid_urls = []

# I created a for loop through and looked specially for <a> tags for hyperlinks
for link in links:
    # I grab href attributes which creates a link to another page.
    href = link.get('href')
    if href:  # Check if href is not None or empty
        valid_urls.append(href)

print(f'Found {len(valid_urls)} valid URLs.')

#Example 3

# It holds the ebay listing based on the class on the html search results
listings = soup.find_all('li', class_='s-item')

# It then loops through all the listings found
for listing in listings:
    
    # and takes the shoe name
    title = listing.find('h3', class_='s-item__title')
    
    # and takes the shoe's price
    price = listing.find('span', class_='s-item__price')
    
    # If both the title and price are found
    if title and price:
        # Print both the title and the price of the shoes
        print(f'Item: {title.text}, Price: {price.text}')

    else:
        print("No listings")