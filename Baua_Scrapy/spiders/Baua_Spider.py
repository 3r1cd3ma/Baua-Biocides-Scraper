import scrapy, json, requests
from Baua_Scrapy import settings

"""Scrapy Spider for Baua product page scraping.

Attributes:
    name (str, required): Define the name for this spider. The spider name is how the spider is located (and instantiated) by Scrapy, so it must be unique.
    start_urls (list of str): List of URLs where the spider will begin to crawl from.

"""
class BauaSpider(scrapy.Spider):
    
    name = "Baua"
       
    """Download the json file from the Baua website containing the list of biocides per 1000, and extract for each the URL of their Baua page.

    Attributes:
        DOMAIN (str): Domain of baua website used
        urls(list of str): List of baua biocides pages URL extracted from `response`.
        response(requests.Response): Result of Baua products list request.
    
    Parameter:
        header(Dictionnaty of str): Header to used for request

    Return:
        list of str : List of baua biocides pages URL extracted from `response`.
        
    """
    def start_requests(self):
        DOMAIN = 'https://www.baua.de/'
        urls = []
        for i in range(0,100000,1000):
            print(f"... get products from {i} to {i+999}")
            response = requests.get(
                url = DOMAIN + 'DE/Biozid-Meldeverordnung/Offen/datatable_produkte_formular.json',
                headers = {'User-Agent':settings.USER_AGENT},
                params ={
                    'start':i,
                    'length':'1000'
                    }
                )

            if response.status_code !=200 :
                response.raise_for_status()
                SystemExit(requests.exceptions)

            for iter, obj in enumerate(json.loads(response.text)['data']):
                print(f"... scrapping product {i+iter}")
                yield scrapy.Request(DOMAIN + obj[4].split('"')[1], self.parse)

    def parse(self, response):
        
        """Process the response and returning scraped data

        Parameters:
            response (scrapy.http.Response): Downloaded response to the current URL request

        Yields:
            Dictionary of str: Scraped data

        """
        table_Biocidal_Product = response.css('.data-medium')[0].css('td')
        table_Substances = response.css('.data-medium')[1].css('td::text')
        table_Details = response.css('.data-medium')[2].css('td')
        yield{
            'Link': response.request.url,
            #Data of products table
            'Handelsname': table_Biocidal_Product[0].css('strong::text').get() if len(table_Biocidal_Product) >= 0+1 and table_Biocidal_Product[0].css('strong::text').get() is not None else '',
            'Registriernummer' :  table_Biocidal_Product[1].css('::text').get().strip() if len(table_Biocidal_Product) >= 1+1 and table_Biocidal_Product[1].css('::text').get() is not None else '',
            'Meldedatum':  table_Biocidal_Product[2].css('::text').get() if len(table_Biocidal_Product) >= 2+1 and table_Biocidal_Product[2].css('::text').get() is not None else '',
            'Maximale Verkehrsfähigkeit': table_Biocidal_Product[3].css('span::text').get() if len(table_Biocidal_Product) >= 3+1 and table_Biocidal_Product[3].css('span::text').get() is not None else '',
            '(ChemBiozidMeldeV)': table_Biocidal_Product[3].css('div div::text').get().strip() if len(table_Biocidal_Product) >= 3+1 and table_Biocidal_Product[3].css('div div::text').get() is not None else '',
            #Data of substances table
            'Wirkstoffname_1': table_Substances[0].get() if len(table_Substances) >= 0+1 and table_Substances[0].get() is not None else '',
            'CAS-Nr._1': table_Substances[1].get() if len(table_Substances) >= 1+1 and table_Substances[1].get() is not None else '',
            'EC-Nr._1': table_Substances[2].get() if len(table_Substances) >= 2+1 and table_Substances[2].get() is not None else '',
            'PT_1': table_Substances[3].get() if len(table_Substances) >= 3+1 and table_Substances[3].get() is not None else '',
            'Produktart_1': table_Substances[4].get() if len(table_Substances) >= 4+1 and table_Substances[4].get() is not None else '',
            'Wirkstoffname_2': table_Substances[5].get() if len(table_Substances) >= 5+1 and table_Substances[5].get() is not None else '',
            'CAS-Nr._2': table_Substances[6].get() if len(table_Substances) >= 6+1 and table_Substances[6].get() is not None else '',
            'EC-Nr._2': table_Substances[7].get() if len(table_Substances) >= 7+1 and table_Substances[7].get() is not None else '',
            'PT_2': table_Substances[8].get() if len(table_Substances) >= 8+1 and table_Substances[8].get() is not None else '',
            'Produktart_2': table_Substances[9].get() if len(table_Substances) >= 9+1 and table_Substances[9].get() is not None else '',
            'Wirkstoffname_3': table_Substances[10].get() if len(table_Substances) >= 10+1 and table_Substances[10].get() is not None else '',
            'CAS-Nr._3': table_Substances[11].get() if len(table_Substances) >= 11+1 and table_Substances[11].get() is not None else '',
            'EC-Nr._3': table_Substances[12].get() if len(table_Substances) >= 12+1 and table_Substances[12].get() is not None else '',
            'PT_3': table_Substances[13].get() if len(table_Substances) >= 13+1 and table_Substances[13].get() is not None else '',
            'Produktart_3': table_Substances[14].get() if len(table_Substances) >= 14+1 and table_Substances[14].get() is not None else '',
            'Wirkstoffname_4': table_Substances[15].get() if len(table_Substances) >= 15+1 and table_Substances[15].get() is not None else '',
            'CAS-Nr._4': table_Substances[16].get() if len(table_Substances) >= 16+1 and table_Substances[16].get() is not None else '',
            'EC-Nr._4': table_Substances[17].get() if len(table_Substances) >= 17+1 and table_Substances[17].get() is not None else '',
            'PT_4': table_Substances[18].get() if len(table_Substances) >= 18+1 and table_Substances[18].get() is not None else '',
            'Produktart_4': table_Substances[19].get() if len(table_Substances) >= 19+1 and table_Substances[19].get() is not None else '',
            #Data of details table
            'Firmenname': table_Details[0].css('strong::text').get() if len(table_Details) >= 0+1 and table_Details[0].css('strong::text').get() is not None else '',
            'Anschrift': table_Details[1].css('::text').get() if len(table_Details) >= 1+1 and table_Details[1].css('::text').get() is not None else '',
            'Land': table_Details[2].css('::text').get() if len(table_Details) >= 2+1 and table_Details[2].css('::text').get() is not None else ''
        }
    
    def warn_on_generator_with_return_value_stub(spider, callable):
        pass

    scrapy.utils.misc.warn_on_generator_with_return_value = warn_on_generator_with_return_value_stub
    scrapy.core.scraper.warn_on_generator_with_return_value = warn_on_generator_with_return_value_stub