import tkinter as tk
from consts import titulo, fundo, fundo2, links
from api import tratar
import json
import webbrowser as wb

"""
Este é o módulo destinado a tratar apenas da interação com o cliente através de 
interface gui, utilizei a biblioteca tkinter para concluir o desenvolvimento
dessa parte do aplicativo. 
"""




#Instancia um objeto representando uma tela
tela=tk.Tk()
#Seta para tela cheia
altura=str(tela.winfo_screenheight())
largura=str(tela.winfo_screenwidth())
tela.geometry(largura+'x'+altura)
#dá o título
tela.title(titulo)
#configura a cor de fundo
tela.configure(background=fundo)
#tela.configure(cursor="pencil")#Se estiver curioso(a), basta descomentar o código ao lado

class _Quadro():
	"""
    Classe utilizada para manejar a classe Frame do tkinter. Fiz uma classe pai
    nesse caso pois senti a necessidade de padronizar alguns comportamentos de
    toda e qualquer tela que venha a ser criada, dando a sensação de dinamismo
    ao aplicativo, é nele que "penduramos" todos os outros widgets e fazemos retornar
    ao cliente a visualização
	"""
	def __init__(self, tela, **kwargs):
		"""
        Função que é chamada sempre que 
        for invocada uma instância de classe,
        ela que determina quais atributos a classe possui de início
		"""
		self.tela=tela
		self.frame=tk.Frame(self.tela, **kwargs)
		self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

	def mudar_quadro(self, quadro, **kwargs):
		"""
		Este método foi desenvolvido para mudar rapidamente 
		de uma instância de _Quadro para outra, tornando possivel a 
		navegação pelo aplicativo
		"""
		self.frame.destroy()
		quadro(self.tela,**kwargs)

class Link(tk.Label):
	"""
    Criei uma classe filha de tk.Label para conseguir inserir 
    um redirecionamento para o link que desejo. Instanciando a
    classe diretamente, ou acaba redirecionando apenas para o
    último link (não importa qual link clique)
    ou acaba abrindo todos os links listados na tela
	"""
	def __init__(self, frame, **kwargs):
		"""
        Função que é chamada sempre que 
        for invocada uma instância de classe,
        ela que determina quais atributos a classe possui de início
		"""
		#Esse método instancia a função __init__ do pai
		super().__init__(frame, **kwargs)
		#configura um comando para Label
		self.bind("<Button-1>", lambda e:self.redirecionar())

	def redirecionar(self):
		wb.open_new_tab(self['text'].replace('[','').replace(']',''))

class Resposta(_Quadro):
	"""
    Classe que mostra na tela o resultado das buscas, com a descrição e o link,
	podendo ser redirecionado para o site quando clica no link. O redirecionamento
	vai acontecer no browser padrão do computador.
	"""
	def __init__(self, tela, **kwargs):
		"""
        Função que é chamada sempre que 
        for invocada uma instância de classe,
        ela que determina quais atributos a classe possui de início
		"""
		#Invoca o método __init__ do pai
		super().__init__(tela,**kwargs)

		
        #Instancia um objeto de Button tkinter, esse vai retornar a tela inicial
		self.bt_voltar=tk.Button(self.frame, text=" Voltar ", command=self.voltar)
		self.bt_voltar.place(relx=0, rely=0)

		
		#veja a descrição do método dentro dele
		self.printar()
		

	def printar(self):
		"""
        Método que renderiza os resultados no arquivo temps.json na tela
        é utilizado alguns artifícios para colocar até 10 resultados,
        com seu título e link
		"""
		with open('temps.json') as f:
			res=json.load(f)



		espaco=0.06

		#faz um dicionário com chaves Label e valor Button para os links
		final={}
		for k,v in res.items():
			titulo=tk.Label(self.frame, text=k, bg=fundo2, bd=0)
			link=Link(self.frame, text=v, bg=fundo2, bd=0, fg=links, cursor="hand2")
			final[titulo]=link
		#aqui que serão posicionados cada um dos componentes
		for k,v in final.items():
			k.place(relx=0.01, rely=espaco)
			v.place(relx=0.01, rely=espaco+0.025)
			espaco+=0.07


	def voltar(self):
		"""
        Método usado para voltar para a tela de busca
        reutilizando mudar_quadro da classe pai
		"""
		self.mudar_quadro(Casa, bg=fundo, highlightbackground='black', highlightthickness=1)


class Casa(_Quadro):
	"""
    Classe que faz o início do aplicativo e usa a função da api.py

	"""
	def __init__(self,tela, **kwargs):
		super().__init__(tela, **kwargs)
		self.aviso=tk.Label(self.frame, text="Faça sua busca aqui", bg=fundo,bd=0, font=('Times',30,'bold'),fg="white")
		self.aviso.place(relx=0.1,rely=0.2, relwidth=0.8,relheight=0.2)
		self.entrada=tk.Entry(self.frame,bd=2)
		self.entrada.place(relx=0.2,rely=0.35,relwidth=0.6)
		self.bt=tk.Button(self.frame,text=" Buscar ", command=self.pegar)
		self.bt.place(relx=0.45,rely=0.4)


	def pegar(self):
		"""
        Método que escreve o arquivo temps.json 
        e muda para a tela de resposta
		"""
		tratar(self.entrada.get())

		self.mudar_quadro(Resposta, bg=fundo2, highlightbackground='black', highlightthickness=1)



