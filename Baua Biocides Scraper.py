"""Script for extact biocides data from Baua Bicides pages.
    1. Get biocides pages URL through Baua bicides list in Json file with ''Requests'' module
    2. Scraping data on every biocide pages and save in the 'Baua_Biosides_Scrapping' csv file with ''Scrapy'' framework

    Attributes:
        start_time (float): Current time in seconds of the script beginning.
        biocides_urls (list of str): List of baua biocides pages URL extracted.
        process (CrawlerProcess): Scrapy execution variable.
    """ 

import time, datetime
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Baua_Scrapy.spiders.Baua_Spider import BauaSpider

def main():
    print(
    """

    BAUA BIOCIDES SCRAPER
    https://github.com/3r1cd3ma/Baua-Biocides-Scraper
        
    """)
    start_time = time.time()
    print("SCRAPING START ... ")
    process = CrawlerProcess(get_project_settings())
    process.crawl(BauaSpider)
    process.start()
    print(f"SCRAPING COMPLETED    -   {str(datetime.timedelta(seconds=time.time() - start_time))}")
    print('Baua biosides data is in the file "baua_biosides_scraping.csv"')
    input("Press <Enter> to exit the program")
    SystemExit()
    
if __name__ == '__main__':
    main()