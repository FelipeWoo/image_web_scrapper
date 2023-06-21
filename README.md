# Image Web Scraper

The Image Web Scraper is a Python script that allows you to collect all the images from a website and save them in a designated folder for later use. It utilizes the `requests` library for sending HTTP requests, the `BeautifulSoup` library for parsing HTML content, and the `os` module for file operations.

## Features

- Extracts all image URLs from a specified website
- Downloads and saves the images in a local folder
- Handles error cases, such as invalid URLs or inaccessible images
- Automatically skips downloading images if they already exist in the designated folder
- Provides a user-agent header to mimic a regular web browser and bypass certain restrictions

## Requirements

- python==3.9.2
- beautifulsoup4==4.12.2
- certifi==2023.5.7
- charset-normalizer==3.1.0
- idna==3.4
- requests==2.31.0
- soupsieve==2.4.1
- urllib3==2.0.3

## Usage

1. Install the required libraries by running the following command:
```
    pip install requests beautifulsoup4
```

2. Clone the repository or download the Python script.

3. In the script, modify the `webpage_url` variable to specify the URL of the website from which you want to extract images.

4. Set the `save_folder` variable to specify the folder where you want to save the downloaded images.

5. Run the script using the following command:
```
    python image_scraper.py
```

6. The script will extract the image URLs from the specified website and save them in the designated folder. Existing images will be skipped to avoid duplicates.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

## Disclaimer

Please use this tool responsibly and respect the terms of service of the websites you scrape. Be aware of any legal restrictions or permissions required before scraping images from a website.

## Acknowledgements

The Image Web Scraper script is built upon the foundation of the `requests` and `BeautifulSoup` libraries, which are essential tools for web scraping and HTML parsing in Python.

## References

- [Python Requests Library Documentation](https://docs.python-requests.org/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [OpenAI GPT-3.5](https://openai.com/research/gpt-3-5)
