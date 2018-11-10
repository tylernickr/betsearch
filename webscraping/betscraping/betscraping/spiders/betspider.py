from scrapy.spiders import Spider, Request
from bs4 import BeautifulSoup, SoupStrainer
from re import match
from time import sleep

class Betspider(Spider):
    COUNT = 1
    name = 'betspider'

    def start_requests(self):
        urls = [
            'http://www.bovada.com/',
            'https://www.draftkings.com/',
            'https://electionbettingodds.com/',
            'https://www.bookmaker.eu/',
            'https://www.5dimes.eu/',
            'https://www.heritagesports.eu/',
            'https://www.betonline.ag/',
            'https://www.youwager.eu/',
            'https://www.gamblingsites.com/'
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        for img in soup.findAll('img'):
            img.decompose()
        # for script in soup.findAll('script'):
        #     script.decompose()
        open('/media/nick/WebFiles/scraped_files/' + str(Betspider.COUNT) + '.html', 'w').write(str(soup))
        Betspider.COUNT += 1
        for link in BeautifulSoup(response.text, 'html.parser', parse_only=SoupStrainer('a')):
            try:
                if not match('.*ikipedia.*|.*twitter.*|.*sourceforge.*|.i*', link['href']):
                    yield response.follow(link['href'], self.parse)
            except:
                pass

