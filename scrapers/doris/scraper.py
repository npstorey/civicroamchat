from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver', options=options)

import csv
import os
import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def extract_documents(html):
    soup = BeautifulSoup(html, 'html.parser')
    documents = soup.find_all(class_='document')
    return documents

def scrape_page(url):
    try:
        driver.get(url)
        documents = driver.find_elements(By.CSS_SELECTOR, '.document')
        document_info_list = [extract_document_info(doc, driver) for doc in documents]
        print(f"Extracted {len(document_info_list)} documents")
        return document_info_list
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

def extract_document_info(document, driver):
    try:
        title_link = document.find_element(By.CSS_SELECTOR, 'a')
        title = title_link.text.strip()
        link = title_link.get_attribute('href')
        download_link = document.find_element(By.CSS_SELECTOR, '.underline-link')
        download_url = download_link.get_attribute('href')
        print(f"Extracted document: {title}")
        return {"title": title, "link": link, "download_url": download_url}
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

total_pages = 2
base_url = "https://a860-gpp.nyc.gov/catalog?page={page_number}&additional_creators=&agency=&all_fields=&associated_place=&borough=&calendar_year=&community_board_district=&date_published=&description=&f%5Bagency_sim%5D%5B%5D=Transportation%2C+Department+of+%28DOT%29&f_inclusive%5Breport_type_sim%5D%5B%5D=Report&fiscal_year=&language=&locale=en&op=AND&report_type=&required_report_name=&school_district=&search_field=advanced&sort=score+desc%2C+date_published_ssi+desc&sub_title=&subject=&title="

all_documents = []
for page_number in range(1, total_pages + 1):
    page_url = base_url.format(page_number=page_number)
    document_info_list = scrape_page(page_url)
    all_documents.extend([doc for doc in document_info_list if doc is not None])
    print(f"Scraped page {page_number}")

print(f"Total documents: {len(all_documents)}")

def get_pdf_link(document_url):
    response = requests.get(document_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    pdf_links = soup.find_all('a', href=True)

    for link in pdf_links:
        if '/downloads/' in link['href']:
            return link['href']

    return None

def download_file(url, folder, file_name):
    base_url = "https://a860-gpp.nyc.gov"
    if not url.startswith("http"):
        url = base_url + url
    response = requests.get(url)
    file_path = os.path.join(folder, file_name)

    with open(file_path, 'wb') as file:
        file.write(response.content)

destination_folder = "data/Downloaded_Documents"

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

with open('data/documents.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['title', 'link', 'download_url']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    for document in all_documents:
        if document:
            unique_id = document['link'].split('/')[-2]
            download_url = get_pdf_link(document['link'])
            document['download_url'] = download_url
            writer.writerow(document)

            if download_url:
                file_name = f"DORIS_{document['title'].replace(' ', '_')}_{unique_id}.pdf"
                download_file(download_url, destination_folder, file_name)