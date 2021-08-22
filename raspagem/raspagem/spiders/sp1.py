import re

import scrapy
import csv

endereco = "/home/antonio/PycharmProjects/web-scp/dados/"

class Raspagem1(scrapy.Spider):
    name = "raspar"

    start_urls = [
        "https://www.archdaily.com.br/br/tag/urbanismo"
    ]

    def parse(self, response):
        titulos_brutos = response.xpath('*//a/span/text()').getall()
        links_brutos = response.xpath('*//a/@href').getall()
        links_imagem_brutos = response.xpath('*//a/img/@data-src').getall()

        titulos = []
        links = []
        links_imagens = []

        f = open(endereco + "dados.csv", 'w', newline='', encoding='utf-8')
        w = csv.writer(f)
        w.writerow(["titulo", "links", "links_imagem"])

        #   Titulos
        for titulo in titulos_brutos:
            if len(titulo) > 14:
                titulos.append(titulo)
        print(titulos)

        #   Links
        cont = 0
        for link in links_brutos:
            if link[:32] == "https://www.archdaily.com.br/br/":
                if link[len(link)-1] == titulos[cont][len(titulos[cont])-1]:
                    links.append(link)
                    cont = cont + 1
        print(links)

        #   Links das imagens
        cont2 = 0
        for link_imagem in links_imagem_brutos:

            if cont2 != 0:
                if link_imagem[69:79] == 'newsletter' and link_imagem != links_imagens[cont2-1]:
                    links_imagens.append(link_imagem)
                    cont2 = cont2 + 1
            else:
                if link_imagem[69:79] == 'newsletter':
                    links_imagens.append(link_imagem)
                    cont2 = cont2 + 1
        print(links_imagens)
        print(len(links_imagens), "itens")

        #   Escever no dados.csv

        for i in range(1, len(titulos)):
            w.writerow([titulos[i], links[i], links_imagens[i]])
