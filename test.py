




	



	


if __name__=="__main__":
	busca=input("Digite aqui\n")
	tratar(busca)
	with open('temps.json','r') as f:
		b=json.load(f)

	for k,v in b.items():
		print(k+'\n'+v+'\n\n')
