import scrapy

class bulkExport(scrapy.Spider):
    name = 'export'
    start_urls = ['http://10.99.1.137:9280/admin/config.php?display=did']

    def parse(self, response):
        yield {'data': response.text}