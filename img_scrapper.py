import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}


def sanitize_filename(filename):
    # Remove invalid characters from the filename
    invalid_chars = r'\/:*?"<>|'
    for char in invalid_chars:
        filename = filename.replace(char, '')
    return filename


def extract_images_url(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception if a HTTP error occurred (e.g., 404, 500)
            
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the title tag
        title_tag = soup.find('title')
    
        # Extract the title text
        title = title_tag.text.strip()
        
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

        return title, image_urls

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
def save_images(folder_path, img_urls, title):
        
    for index,img_url in enumerate(img_urls):
        # Send a GET request to the image URL
        img_response = requests.get(img_url)
        
        # Extract the filename from the image URL
        filename = os.path.basename(img_url)
        sanitized_filename = sanitize_filename(filename)

        # Extract the file extension using regular expressions
        extension = re.search(r'\.([^.]+)$', sanitized_filename).group(1)
        
        new_filename = f"{title}_{index+1}.{extension}"

        # Construct the file path to save the image
        file_path = os.path.join(folder_path, new_filename)
        
        # Save the image file
        with open(file_path, 'wb') as f:
            f.write(img_response.content)  

    print("Images saved successfully!")




# Example usage
webpage_url = 'https://tumanhwas.com/news/reborn-ranker-gravity-user-1.00'  # Replace with the URL of the webpage you want to extract images from
save_folder = 'images'  # Replace with the desired folder name

# Create the folder if it doesn't exist
os.makedirs(save_folder, exist_ok=True)

title, image_urls = extract_images_url(webpage_url)

if title and image_urls is not None:
    save_images(save_folder, image_urls, title)


