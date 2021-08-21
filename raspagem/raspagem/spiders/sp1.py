import re

import scrapy
import csv


class Raspagem1(scrapy.Spider):
    name = "raspar"

    start_urls = [
        "https://www.archdaily.com.br/br/tag/urbanismo"
    ]

    def parse(self, response):
        titulos_brutos = response.xpath('*//a/span/text()').getall()
        links_brutos = response.xpath('*//a/@href').getall()
        titulos = []
        links = []
        f = open('dados.csv', 'w', newline='', encoding='utf-8')
        w = csv.writer(f)

        for titulo in titulos_brutos:
            if len(titulo) > 14:
                titulos.append(titulo)
        print(titulos)

        cont = 0
        for link in links_brutos:
            pass
#        print(titulos)
        print(links)


