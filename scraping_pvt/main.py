from bs4 import BeautifulSoup
import requests
import csv
import logging

from random import randint
from time import sleep
import re
from requests.exceptions import HTTPError

base_link = 'https://www.park.by'


def scr_residents_page(link):
    """
    Request one page on park.by with query:
    >>Разработка программного обеспечения (ПО)
    >>Page Number

    Gather company names and their page link.
    Returns them in list.
    
    Formating:
    [[company names, page link], ...]
    """
    try:
        source = requests.get(link)
        source.raise_for_status()
    except HTTPError:
        return None

    soup = BeautifulSoup(source.text, 'lxml')
    companies = []

    for div in soup.body.find_all('div', class_='news-item'):
        company = []
        # handle errors
        try:
            # company name
            company.append(div.find('a').text)
            # page link
            company.append(div.find('a')['href'])
        except:
            logging.debug('Exception occured during parsing')
            continue
        companies.append(company)
    
    return companies


def scr_mult_residents_pages():
    """
    Request all pages on park.by with query:
    >>Разработка программного обеспечения (ПО)

    Gather company names and their page link.
    Returns them in list.
    
    Formating:
    [[company names, page link], ...]
    """
    
    companies = []
    page_i = 1
    while True:
        page_num = f'PAGEN_1={page_i}'
        query = f'/?q=&UNP=&save=Найти&search=Y&STAFF=&EXPER=&TARGET[]=614&{page_num}'
        full_link = f'{base_link}/residents{query}'

        new_companies = scr_residents_page(full_link)
        common = has_common(companies, new_companies)
        if common:

            logging.debug(f'Common companies: {common}')
            logging.debug(f'New companies: {new_companies}')
            logging.info('Scraper achieved end of list on iteration %d', page_i-1)
            break
        companies.extend(new_companies)
        page_i += 1

    return companies


def has_common(l1, l2):
    """
    Takes 2 lists of format:
    [[company names, page link], ...]

    Checks if there any common company names.
    If there are returns true else false. 
    """
    def index0(l):
        return l[0]
    
    s1 = set(map(index0, l1))
    s2 = set(map(index0, l2))
    
    return bool(s1.intersection(s2))


def write_to_csv(file_dir, companies, header):
    """
    Writes 'companies' list argument to csv file 
    'file_dir' - file directory, where headers are
    'headers'
    """
    with open(file_dir, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        csv_writer.writerows(companies)


def read_csv(file_dir):
    """
    Reads 'file_dir' csv file, without headers.
    Returns list of rows.
    """
    with open(file_dir, 'r') as csv_file:
        csvreader = csv.reader(csv_file)
        next(csvreader)
        data = [row for row in csvreader if row]

    return data


def scrap_residents_website(sec_part_link):
    """
    Takes second part link 'sec_part_link' arg
    that leads to some company page.
    Extracts from page company website and
    returns it.
    """
    full_link = f'{base_link}{sec_part_link}'

    try:
        source = requests.get(full_link)
        source.raise_for_status()
    except HTTPError:
        return None

    soup = BeautifulSoup(source.text, 'lxml')

    try:
        news_detail = soup.body.main.find('div', class_='news-detail')
        block_unde = news_detail.find('div', class_='block-unde')
        divs = block_unde.find_all('div')

        thediv = None

        for div in divs:
            if div.find(string=re.compile("Веб-сайт: ")):
                thediv = div
                break

        href = thediv.find('a')['href']
    except Exception as e:
        href = None
    
    return href


def scrap_mul_residents_website(companies):
    """
    Takes 'companies' list with formating:
    [[company names, page link], ...]
    
    Goes to each company page and extracts website
    link.

    Returns 'upd_companies' list with new company data.
    Formating:
    [[company names, page link, website link], ...]
    And 'not_found' list with company which websites not found.
    Formating:
    [[company names, page link], ...]
    """
    upd_companies, not_found = [], []

    for company in companies:
        company = company.copy()
        website = scrap_residents_website(company[1])
        if website:
            company.append(website)
            upd_companies.append(company)
        else:
            not_found.append(company)
    
    return upd_companies, not_found


def full_scrap_residents_names():
    """
    Aquire company names from park.by.
    Writes them to csv file.
    """

    companies = scr_mult_residents_pages()
    write_to_csv('cms_scrape.csv', companies, ['name', 'page_link'])


def full_scrap_residents_websites():
    """
    Aquire company websites from park.by.
    Writes them to csv file.
    """
    
    companies = read_csv('cms_scrape.csv')
    upd_companies, not_found = scrap_mul_residents_website(companies)
    write_to_csv('cms_scrape_extended.csv', upd_companies, ['name', 'page_link', 'website'])
    write_to_csv('cms_not_found.csv', not_found, ['name', 'page_link'])


if __name__=="__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG,
                        datefmt="%H:%M:%S")
    