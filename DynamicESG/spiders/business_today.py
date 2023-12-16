import os
import scrapy
import pandas as pd
from bs4 import BeautifulSoup


class BusinessTodaySpider(scrapy.Spider):
    name = 'business_today'
    allowed_domains = ['esg.businesstoday.com.tw']
    start_urls = ['http://esg.businesstoday.com.tw/catalog/180686/']

    def __init__(self, dataset='All'):
        """Initialize the spider with the dataset to be crawled.
        Args:
            dataset (str, optional): . Defaults to 'All'.
            - 'All': whole DynamicESG dataset
            - '<shared-task-number>_<mode>': the dataset for the shared task
                - shared-task-number: 1, 2, 3
                - mode: Train, Dev, Test, or Test-ans
                - e.g., '1_Train', '2_Dev', '3_Test-ans'
        """
        self.dataset = dataset
        if '_' in dataset:
            self.task_num = int(dataset.split('_')[0])
            self.mode = dataset.split('_')[1]
        else:
            self.task_num = -1

        if dataset == 'All':
            self.data = pd.read_json(f'DynamicESG_dataset.json')
        elif os.path.isfile(f'./data/ML-ESG-{self.task_num}_Chinese/{self.mode}.json'):
            self.data = pd.read_json(f'./data/ML-ESG-{self.task_num}_Chinese/{self.mode}.json')
        else:
            raise Exception(f'No such dataset: {dataset}. Please check the dataset name. Possible dataset names: "All", "ML-ESG-<shared-task-number>_Chinese_<mode>"')


    def parse(self, response):
        urls = self.data.URL.to_list()

        for url in urls:
            yield scrapy.Request(url, self.parse_content, dont_filter=True)


    def parse_content(self, response):
        news_url = response.request.url
        news_content_html = response.xpath("//div[@class='cke_editable font__select-content']/div").getall()
        news_content = self.clean_data(news_content_html[0])
        news_hashtags = response.xpath("/html/body/section/div/div[3]/ul[1]/li/a/text()").getall()

        idx = self.data[self.data.URL == news_url].index[0]

        EsgCrawlerItem = {}
        if self.dataset != 'All': EsgCrawlerItem['pk'] = int(self.data.pk[idx])
        EsgCrawlerItem["URL"] = news_url
        EsgCrawlerItem["News_Headline"] = str(self.data.News_Headline[idx])

        if (self.task_num==2) or (self.dataset=='All'): EsgCrawlerItem["Impact_Type"] = list(self.data.Impact_Type[idx])
        if (self.task_num==3) or (self.dataset=='All'): EsgCrawlerItem["Impact_Duration"] = list(self.data.Impact_Duration[idx])
        if (self.task_num==1) or (self.dataset=='All'): EsgCrawlerItem["ESG_Category"] = list(self.data.ESG_Category[idx])

        EsgCrawlerItem["news_content_html"] = news_content_html
        EsgCrawlerItem["news_content"] = news_content
        EsgCrawlerItem["news_hashtags"] = news_hashtags

        yield EsgCrawlerItem


    def clean_data(self, content_html):
        soup = BeautifulSoup(content_html, 'html.parser')
        content = soup.get_text()

        content = content.replace('\n', ' ')
        content = content.replace('\r', '')
        content = content.replace('\xa0', '')

        return content