# NLP_Mini_Projects
## N-grams_Science_columnist
### Scrapy:
* used to scrape the science columnists articles from https://www.biomedya.com/, spider object will return CSV file with three column (Title, Url, Text).

* In the terminal navigate to :
cd //..../N-grams_Science_columnist/Scrapy/Science_Columnist_Articles

* Activate anaconda in case Scrapy is not in pip.
conda activate

* Run article_spyder.py spider object
scrapy runspider article_spyder.py -o raw_articles.csv

### N-gram:
The scraped corpus contain 95 science columnist articles, 39759 words. For turkish language Corpus package is used
