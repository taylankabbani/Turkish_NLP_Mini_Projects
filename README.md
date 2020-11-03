# Turkish NLP Mini Projects

## N-grams_Science_columnist Project:
In this project, N-gram models are being created from a scraped initial corpus of Science Column articles written in the Turkish language (https://www.biomedya.com/). N-grams models are being used to generated random sentence samples.

1. Scrapy:
* used to scrape the science columnists articles from https://www.biomedya.com/, spider object will return CSV file with three column (Title, Url, Text).

* In the terminal navigate to :
cd //..../N-grams_Science_columnist/Scrapy/Science_Columnist_Articles

* Activate anaconda in case Scrapy is not in pip.
conda activate

* Run article_spyder.py spider object
scrapy runspider article_spyder.py -o raw_articles.csv

2. N-gram:
The scraped corpus contain 95 science columnist articles, 39759 words. For turkish language Corpus package is used
