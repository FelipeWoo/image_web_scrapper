import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}



def extract_images(url):
    
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    print(response)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all image tags
    img_tags = soup.find_all('img')
    
    # Extract image URLs
    image_urls = []
    for img_tag in img_tags:
        # Get the 'src' attribute of the image tag
        img_url = img_tag.get('src')
        
        # Make the URL absolute by joining it with the base URL
        img_url = urljoin(url, img_url)
        
        # Add the absolute URL to the list of image URLs
        image_urls.append(img_url)
    
    return image_urls
print("Beginning...")
# Example usage
webpage_url = 'https://tumanhwas.com/news/reborn-ranker-gravity-user-1.00'  # Replace with the URL of the webpage you want to extract images from
print("Processing...")
image_urls = extract_images(webpage_url)
for image_url in image_urls:
    print("image_url")
    print(image_url)
print("Done!")