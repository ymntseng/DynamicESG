import scrapy
import pandas as pd
from bs4 import BeautifulSoup


class BusinessTodaySpider(scrapy.Spider):
    name = 'business_today'
    allowed_domains = ['esg.businesstoday.com.tw']
    start_urls = ['http://esg.businesstoday.com.tw/catalog/180686/']

    def __init__(self):
        # args: dataset = 'Train' or 'Dev'
        self.data = pd.read_json(f'DynamicESG_dataset.json')

    def parse(self, response):
        urls = self.data.URL.to_list()

        for url in urls:
            yield scrapy.Request(url, self.parse_content, dont_filter=True)


    def parse_content(self, response):
        news_url = response.request.url
        news_content_html = response.xpath("//div[@class='cke_editable font__select-content']/div").getall()
        news_content = self.clean_data(news_content_html[0])

        idx = self.data[self.data.URL == news_url].index[0]

        EsgCrawlerItem = {
            "URL": news_url,
            "News_Headline": str(self.data.News_Headline[idx]),
            "Impact_Type": list(self.data.Impact_Type[idx]),
            "Impact_Duration": list(self.data.Impact_Duration[idx]),
            "ESG_Category": list(self.data.ESG_Category[idx]),
            "news_content_html": news_content_html,
            "news_content": news_content
        }

        yield EsgCrawlerItem


    def clean_data(self, content_html):
        soup = BeautifulSoup(content_html, 'html.parser')
        content = soup.get_text()

        content = content.replace('\n', ' ')
        content = content.replace('\r', '')
        content = content.replace('\xa0', '')

        return content