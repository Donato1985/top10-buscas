import tkinter as tk
from consts import titulo, fundo, fundo2, links
from api import tratar
import json
import webbrowser as wb

"""
front.py, gerencia toda a parte de apresentação e iteração com o cliente através 
de interface GUI, através de POO é possível simular todas as 'Páginas'
do aplicativo e mexer com tranqüilidade para a fase de desenvolvimento. Mais informações,
consulte o LEIAME.txt
"""





tela=tk.Tk()
#Seta para tela cheia
altura=str(tela.winfo_screenheight())
largura=str(tela.winfo_screenwidth())
tela.geometry(largura+'x'+altura)
tela.title(titulo)
tela.configure(background=fundo)
#tela.configure(cursor="pencil")#Se estiver curioso(a), basta descomentar o código ao lado

class _Quadro():
	"""
    Classe utilizada para manejar a classe Frame do tkinter. Fiz uma classe pai
    nesse caso pois senti a necessidade de padronizar alguns comportamentos de
    toda e qualquer tela que venha a ser criada, dando a sensação de dinamismo
    ao aplicativo, é nele que "penduramos" todos os outros widgets e fazemos retornar
	"""
	def __init__(self, tela, **kwargs):
		self.tela=tela
		self.frame=tk.Frame(self.tela, **kwargs)
		self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

	def mudar_quadro(self, quadro, **kwargs):
		"""
		Classe utilizada para manejar a classe Frame do tkinter. 
		Fiz uma classe pai nesse caso pois senti a necessidade de padronizar alguns 
		comportamentos de toda e qualquer tela que venha a ser criada, 
		dando a sensação de dinamismo ao aplicativo, é nele que "penduramos" 
		todos os outros widgets e fazemos retornar
		"""
		self.frame.destroy()
		quadro(self.tela,**kwargs)

class Resposta(_Quadro):
	def __init__(self, tela, **kwargs):
		super().__init__(tela,**kwargs)

		

		self.bt_voltar=tk.Button(self.frame, text=" Voltar ", command=self.voltar)
		self.bt_voltar.place(relx=0, rely=0)

		
		
		self.printar()
		"""
		exemplo bem aqui embaixo
		self.desc=tk.Label(self.frame, text="Angra - LETRAS.MUS.BR", bg=fundo2, bd=0)
		self.link=tk.Label(self.frame, text="[https://www.letras.mus.br/angra/]", bg=fundo2, bd=0, cursor="hand2",fg=links)
		self.link.bind("<Button-1>", lambda e: self.redirecionar(self.link['text']))
		self.desc.place(relx=0, rely=0.1)
		self.link.place(relx=0, rely=0.12)
		"""

	def printar(self):
		""""""
		with open('temps.json') as f:
			res=json.load(f)

		espaco=0.06
		for k, v in res.items():
			self.desc=tk.Label(self.frame,text=k,bg=fundo2, bd=0)
			self.desc.place(relx=0,rely=espaco)
			self.link=tk.Label(self.frame, text=v, bg=fundo2, bd=0, cursor="hand2", fg=links)
			self.link.bind("<Button-1>",lambda e:self.redirecionar(self.link['text']))
			self.link.place(relx=0,rely=espaco+0.025)
			espaco+=0.07
		



	def redirecionar(self, link):
		wb.open_new_tab(link.replace('[','').replace(']',''))


	def voltar(self):
		self.mudar_quadro(Casa, bg=fundo, highlightbackground='black', highlightthickness=1)


class Casa(_Quadro):
	def __init__(self,tela, **kwargs):
		super().__init__(tela, **kwargs)
		self.aviso=tk.Label(self.frame, text="Faça sua busca aqui", bg=fundo,bd=0, font=('Times',30,'bold'),fg="white")
		self.aviso.place(relx=0.1,rely=0.2, relwidth=0.8,relheight=0.2)
		self.entrada=tk.Entry(self.frame,bd=2)
		self.entrada.place(relx=0.2,rely=0.35,relwidth=0.6)
		self.bt=tk.Button(self.frame,text=" Buscar ", command=self.pegar)
		self.bt.place(relx=0.45,rely=0.4)


	def pegar(self):
		""""""
		tratar(self.entrada.get())

		self.mudar_quadro(Resposta, bg=fundo2, highlightbackground='black', highlightthickness=1)


if __name__=="__main__":
	quadro=Casa(tela, bg=fundo, highlightbackground='black', highlightthickness=1)
	tela.mainloop()










