# Turkish NLP Mini Projects


## [N-grams Science Columnist Project:](https://github.com/taylankabbani/Turkish_NLP_Mini_Projects/tree/master/N-grams_Science_columnist)
In this project, N-gram models are being created from a scraped initial corpus of Science Column articles written in the Turkish language (https://www.biomedya.com/). N-grams models are being used to generated random sentence samples.

### Python Required Libraries
1. [Scrapy](https://scrapy.org/) 
2. [Corpus-py](https://github.com/taylankabbani/Corpus-Py.git)
3. [N-Gram-py](https://github.com/taylankabbani/NGram-Py.git)

   1. Scraping the Corpus data:
      * 94 science column articles were crawled from https://www.biomedya.com/.
      * article_spyder.py file is a spider object which returns CSV file with three columns (Title, Url, Text).
      * In the terminal navigate to :\
        `cd //..../N-grams_Science_columnist/Scrapy/Science_Columnist_Articles`\
        `conda activate`\
        `scrapy runspider article_spyder.py -o raw_articles.csv`
   2. N-gram:
      * The scraped corpus contain 95 science columnist articles, 39759 words. For turkish language Corpus package is used
