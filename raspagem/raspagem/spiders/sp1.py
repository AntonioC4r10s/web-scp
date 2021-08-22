import re

import scrapy
import csv

enderenco = "/home/antonio/PycharmProjects/web-scp/dados/"

class Raspagem1(scrapy.Spider):
    name = "raspar"

    start_urls = [
        "https://www.archdaily.com.br/br/tag/urbanismo"
    ]

    def parse(self, response):
        #   Usando xpath para extrair informações do código fonte da pagina
        titulos_brutos = response.xpath('*//a/span/text()').getall()
        links_brutos = response.xpath('*//a/@href').getall()
        links_imagem_brutos = response.xpath('*//a/img/@data-src').getall()
        textos_brutos = response.xpath('*//p/text()').getall()

        #   Vetores para armazenar as informações extraídas depois de filtradas
        titulos = []
        links = []
        links_imagens = []
        textos = []

        imprimir_informacoes = True    #   imprime informações durante a execução no terminal
        f = open(enderenco + 'dados.csv', 'w', newline='', encoding='utf-8')
        w = csv.writer(f)
        w.writerow(["titulo", "links", "links_imagem", "textos"])

        #   Titulos
        for titulo in titulos_brutos:
            if len(titulo) > 14:
                titulos.append(titulo)

        #   Links
        cont = 0
        for link in links_brutos:
            if link[:32] == "https://www.archdaily.com.br/br/":
                if link[len(link)-1] == titulos[cont][len(titulos[cont])-1]:
                    links.append(link)
                    cont = cont + 1

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

        #   Textos

        for texto in textos_brutos:
            if len(texto) > 20:
                if texto[0].isupper():

                    textos.append(texto)
                if texto[0].isdigit():
                    textos[len(textos) - 1] = textos[len(textos) - 1] + " " + texto
                else:
                    textos[len(textos)-1] = textos[len(textos)-1] + " " + texto

        #   Escever no dados.csv

        for i in range(0, 9):
            textos[i].replace("//xa0", "")
            w.writerow([titulos[i], links[i], links_imagens[i], textos[i]])

        if(imprimir_informacoes == True):
            print(titulos)
            print(links)
            print(links_imagens)
            print(textos)