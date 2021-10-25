import requests as req
from bs4 import BeautifulSoup as bs
from consts import site, header
import json

#classe contendo o Título e a tag a de redirecionamento: "g"
"""Com esse código já consegui pegar toda a folha do google, só com bibliotecas nativas
do python 3.9

"""




def buscar(busca):
	"""
	Essa é a função que efetivamente irá fazer a pesquisa através da biblioteca requests,
	e vai retornar um conjunto de divs com a classe 'kCrYT', que é a classe 
	mais usada no contexto para formatar cada resultado em separado

	"""
	#aqui só vai fazer um tratamento simples para unir a busca
	busca=busca.replace(" ","+")
	#pega os dados brutos da busca no google
	resposta=req.get(site+busca, headers=header)
	#carrega um elemento contendo todas as informações do resultado da busca
	html=bs(resposta.text,"html.parser")

	#aqui é um 'fatiamento' do html que retorna somente containers com o título e o link
	conteudo=html.find_all("div", class_="g")
	return conteudo

def tratar(busca):
	"""
	Função que vai tratar uma requisição de busca no google até trazer um dicionário
	contendo na chave o título, e no valor o link para o site. Por questão de conveniência,
	embuti buscar dentro da função, assim basta colocar string de busca que será feita,
	além de ficar mais fácil para depurar e corrigir se preciso futuramente 
	1- if len(x['class']==1)
	print(x.h3.text+'\n'+x.a['href']+'\n\n')
	"""
	dici={}
	for x in buscar(busca):
		if len(x['class'])==1:
			dici[x.h3.text]=x.a['href']
			if len(dici)==10:
				break

	with open('temps.json','w') as f:
		json.dump(dici,f)
