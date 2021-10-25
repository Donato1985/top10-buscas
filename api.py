import requests as req
from bs4 import BeautifulSoup as bs
from consts import site, header, arquivo
import json


"""
Toda parte lógica e de pesquisa tá aqui, são apenas duas funções
escritas de forma que seja fácil depurar ou mesmo modificar conforme a necessidade
"""




def buscar(busca):
	"""
	Função que recebe uma string de busca e faz a requisição web, recebe o html crú, e retorna
	em um objeto BeautifulSoup, que nada mais é que uma maneira fácil 
	de extrair partes de uma página html
	tanto o requests como BeautifulSoup da biblioteca bs4
	são fundamentais para web scraping no python.
	Note que usei um alias para chamar requests (req)
	e BeautifulSoup de bs, o fiz na importação (logo após a palavra 'as')

	"""
	#aqui só vai fazer um tratamento simples da string para unir a busca
	busca=busca.replace(" ","+")
	#esse é um tratamento simples para não travar o código
	#caso precise depurar nessa parte, basta adicionar print(e) na segunda except
	try:
	    #pega os dados brutos da busca no google
	    #o parâmetro headers permite que eu diga ao site que sou um browser (no caso, o chrome)
	    resposta=req.get(site+busca, headers=header)
	    #carrega um elemento contendo todas as informações do resultado da busca
	    html=bs(resposta.text,"html.parser")

	    #aqui é um 'fatiamento' do html que retorna somente containers com o título e o link
	    conteudo=html.find_all("div", class_="g")
	    return conteudo
	except req.exceptions.ConnectionError:
		print("Problemas com a internet, verifique se está conectado")
		return None

	except:
		print("Algo deu errado, entre em contato com o desenvolvedor")
		return None

def tratar(busca):
	"""
	Função que recebe uma string de entrada representando uma busca padrão
	no google. A entrada é enviada para a função buscar e com seu retorno
	é escrito um arquivo .json simples, contendo como chave uma string
	de descrição e como valor o link para o site
	"""
	dici={}
	res=buscar(busca)
	if res is None:
		print("Ocorreu algo de errado na solicitação")
	else:
		#um elemento for que captura no dicionário o título e o link
	    for x in buscar(busca):
		    if len(x['class'])==1:
			    dici[x.h3.text]=x.a['href']
			    if len(dici)==10:
				    break
    #escreve propriamente o arquivo .json (chamado aqui de temps.json)
	with open(arquivo,'w') as f:
		json.dump(dici,f)
