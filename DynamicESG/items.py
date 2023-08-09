import scrapy


class EsgCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # origin
    URL = scrapy.Field()
    News_Headline = scrapy.Field()
    Impact_Type = scrapy.Field()
    Impact_Duration = scrapy.Field()
    ESG_Category = scrapy.Field()

    # new add by crawler
    news_content_html = scrapy.Field()
    news_content = scrapy.Field()
    news_hashtags = scrapy.Field()