# scrapyを使って画像をクロールする
# インストールはanacondaで
# $conda install -c conda-forge scrapy
# 参考) https://doc.scrapy.org/en/latest/intro/install.html#pre-requisites

import scrapy

class GmSpider(scrapy.Spider):
    name = 'gm_spider'

    start_urls = ['http://gifmagazine.net/']

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
    }

    def parse(self, response):
        for src in response.css('.home20160502-wrap-list-top-link > img::attr(src)'):
            url = response.urljoin(src.extract())

            yield {
                'src': url
            }
