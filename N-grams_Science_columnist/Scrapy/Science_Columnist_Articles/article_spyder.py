import scrapy
class articlespider(scrapy.Spider):
    name = 'articles'
    start_urls = ['https://www.biomedya.com/kose-yazilari']

    def parse(self, response):
        parent_url = 'https://www.biomedya.com/'
        for article in response.xpath('//*[@id="inner-wrap"]/article/div[2]/div/div[1]/div[2]/div/ul/li'):
            name = article.xpath('div/a/@title').get()
            link = parent_url + str(article.xpath('div/a/@href').get())
            text = scrapy.Request(url= link, callback = self.parse_Inlink)
            yield scrapy.Request(url= link, callback = self.parse_Inlink)
    def parse_Inlink(self, response):
        title = response.xpath('//div[@id = "print-block"]/h1/text()').get()
        link = str(response.url)
        text = ''
        for graph in response.xpath('//div[@id="print-block"]/p/text()'):
            text += graph.get()
        yield {"Title" : title,
               "URL" : link,
               "Text" : text}
