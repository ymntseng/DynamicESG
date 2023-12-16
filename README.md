# DynamicESG

This is the official repository of our paper "DynamicESG: A Dataset for Dynamically Unearthing ESG Ratings from News Articles", *CIKM 2023*.

We provide the web crawler from [Business Today](https://esg.businesstoday.com.tw/catalog/180686/) for DynamicESG.


## Environment Requirements

- Python 3.8
- Pandas 2.0.0
- Scrapy 2.8.0
- Scrapy-splash 0.8.0
- Bs4 0.0.1

## Dataset
- The whole DynamicESG dataset is in `DynamicESG_dataset.json`. There are five columns in our DynamicESG dataset, including URL, headline, and the annotations of three tasks of the news articles.


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

## FinNLP Shared Task
- We also provide the Train/Dev/Test dataset in the `data` folder which is used in FinNLP shared task.

- The label scheme is the same as DynamicESG dataset. The only difference is the ground truth labels of **Impact Type** (ML-ESG-2), **Impact Duration** (ML-ESG-3), and **ESG Category** (ML-ESG-1) are the consensus of two annotators.

- Here is an example format of one instance in ML-ESG-3 shared task.

```jsonld
{
    "pk": int
    "URL": str
    "News_Headline": str
    "Impact_Duration": [Ground Truth]
}
```

## Usage
- First, you need to install the requirements.

```bash
pip install -r requirements.txt
```

- Then, you can easily crawl the news content with HTML tags and the clean news content of all urls in the training set by giving the argument `-a dataset=<dataset-name>`.
    - `<dataset-name>` can be one of the following:
        - `All`: the whole DynamicESG dataset (i.e., DynamicESG_dataset.json)
        -  `<shared-task-number>_<mode>`: the Train/Dev/Test dataset of which FinNLP shared task. (e.g., 1_Train, 2_Dev, 3_Test, 3_Test-ans)
            - `<shared-task-number>`: 1, 2, 3
            - `<mode>`: Train, Dev, Test, Test-ans

- Finally, you can easily output the result into json files. The output will have three new columns as follows along with the origin columns in DynamicESG dataset.

    - news_content：clean news content
    - news_content_html：origin HTML tags of news content
    - news_hashtags：named entity annotated by journalists that are displayed under each news article

```
scrapy crawl business_today -a dataset=<dataset-name> -o <output-name.json>

# e.g.,
scrapy crawl business_today -a dataset=All -o DynamicESG_dataset_output.json
scrapy crawl business_today -a dataset=3_Dev -o ML-ESG-3_Dev_output.json
```

## Reference
### ML-ESG
Please refer to FinNLP@IJCAI-2023 website for more details.

[FinNLP@IJCAI-2023] Shared Task: Multi-Lingual ESG Issue Identification (ML-ESG)：https://sites.google.com/nlg.csie.ntu.edu.tw/finnlp-2023/home


### ML-ESG-2
Please refer to FinNLP@IJCNLP-AACL-2023 website for more details.

[FinNLP@IJCNLP-AACL-2023] Shared Task: Multi-Lingual ESG Impact Type Identification (ML-ESG-2)：https://sites.google.com/nlg.csie.ntu.edu.tw/finnlp2023/home


## Citation
If you use DynamicESG dataset or the code from this repo, please kindly cite:
```
@inproceedings{tseng2023dynamicesg,
  title={DynamicESG: A Dataset for Dynamically Unearthing ESG Ratings from News Articles},
  author={Tseng, Yu-Min and Chen, Chung-Chi and Huang, Hen-Hsen and Chen, Hsin-Hsi},
  booktitle={Proceedings of the 32nd ACM International Conference on Information and Knowledge Management},
  pages={5412--5416},
  year={2023}
}
```
