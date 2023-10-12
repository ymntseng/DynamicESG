# DynamicESG

This is the GitHub repository that contains the dataset of DynamicESG.

We provide the web crawler from [Business Today](https://esg.businesstoday.com.tw/catalog/180686/) for DynamicESG.


## Environment Requirements

- Python 3.8
- Pandas 2.0.0
- Scrapy 2.8.0
- Scrapy-splash 0.8.0
- Bs4 0.0.1

## Dataset 
- There are five columns in our DynamicESG dataset, including URL, headline, and the annotations of three tasks of the news articles.


- The labels of three tasks is as follows:
    
    1. **Impact Type**: *Opportunity*, *Risk*, *CannotDistinguish*, *NotRelatedtoCompany*, *NotRelatedtoESGTopic*
    2. **Impact Duration**: *<2*, *2~5*, *>5*, *NotRelatedtoCompany*, *NotRelatedtoESGTopic*
    3. **ESG Category**: Index of 44 Key Issues in the [Guideline](https://github.com/ymntseng/DynamicESG/blob/master/Guideline%20of%20ESG%2044%20key%20issues.pdf), ex. E01, S13, G07.

- Here is an example format of one instance.

```jsonld
{
    "URL": str
    "News_Headline": str
    "Impact_Type": [Annotator 1, Annotator 2]
    "Impact_Duration": [Annotator 1, Annotator 2]
    "ESG_Category": [[Annotator 1], [Annotator 2]]
}
```



## Usage
- First, you need to install the requirements.

```bash
pip install -r requirements.txt
```

- Then, you can easily output the result into json or csv files as follows. The output will have three new columns along with the origin columns in DynamicESG dataset and the data shape will be (2220, 8). 

    - news_content：clean news content
    - news_content_html：origin HTML tags of news content
    - news_hashtags：named entity annotated by journalists that are displayed under each news article

```bash
scrapy crawl business_today -o {output.csv}
```

## Reference
