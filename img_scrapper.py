from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import re
import requests

# Set the path to the ChromeDriver executable
# Download chromedriver from https://chromedriver.chromium.org/downloads
# and put it in the same folder as this script
webdriver_path = '/usr/local/bin/chromedriver'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}


def sanitize_filename(filename):
    # Remove invalid characters from the filename
    invalid_chars = r'\/:*?"<>|'
    for char in invalid_chars:
        filename = filename.replace(char, '')
    return filename

def clean_url(string):
    # Use regular expression to extract the URL starting with "https"
    match = re.search(r'https://\S+', string)
    url = match.group()
    return url


def extract_images_url(url):
    try:
        print(f"Extracting images from {url}...")
        # Set up the ChromeDriver options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')  # Run ChromeDriver in headless mode
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')

        # Set up the ChromeDriver service
        service = Service(webdriver_path)

        # Create a new instance of the ChromeDriver
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)  # Set implicit wait time (in seconds)

        # Navigate to the URL
        driver.get(url)

        # Find the title tag
        title_tag = driver.execute_script("return document.title")
        title = title_tag.strip()

        # Find all image tags
        img_tags = driver.find_elements(By.TAG_NAME, 'img')

        # Extract image URLs
        image_urls = []
        for img_tag in img_tags:
            img = clean_url(img_tag.get_attribute('src'))
            image_urls.append(img)

        # Quit the driver
        driver.quit()


        return title, image_urls

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def save_images(folder_path, img_urls, title):
    try:
        for index, img_url in enumerate(img_urls):
            # Send a GET request to the image URL
            response = requests.get(img_url, headers=headers)
            response.raise_for_status()  # Raise an exception if an HTTP error occurred (e.g., 404, 500)

            # Extract the filename from the image URL
            filename = os.path.basename(img_url)
            sanitized_filename = sanitize_filename(filename)

            # Extract the file extension using regular expressions
            extension = re.search(r'\.([^.]+)$', sanitized_filename).group(1)

            new_filename = f"{title}_{index+1}.{extension}"

            # Construct the file path to save the image
            file_path = os.path.join(folder_path, new_filename)

            # Skip saving if the file already exists
            if os.path.exists(file_path):
                continue

            # Save the image file
            with open(file_path, 'wb') as f:
                f.write(response.content)

        print("Images saved successfully!")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
    except (AttributeError, TypeError) as e:
        print(f"An error occurred during title extraction: {e}")


if __name__ == '__main__':
    DEBUG = False

    print("Starting the script...")
    # Example usage
    webpage_url = 'https://tumanhwas.com/news/reborn-ranker-gravity-user-1.00'  # Replace with the URL of the webpage you want to extract images from
    save_folder = 'images'  # Replace with the desired folder name
    
    # Obtaining the title and image urls
    title, image_urls = extract_images_url(webpage_url)

    if DEBUG:
        print(f'title = {title}')
        print(f'image_urls = {image_urls}')
        
    if not DEBUG:
        # Create the folder if it doesn't exist
        os.makedirs(save_folder, exist_ok=True)

        if title and image_urls is not None:         
            # An error occurred during the request: 403 Client Error: Forbidden for url: 'https://webpage.com/logo.png'
            # Remove the image from the list
            #image_urls.remove('https://webpage.com/logo.png')
            # Save the images to the specified folder
            save_images(save_folder, image_urls, title)
