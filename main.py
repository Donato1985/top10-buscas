from client import tela, Casa
from consts import fundo




if __name__=="__main__":
	quadro=Casa(tela, bg=fundo, highlightbackground='black', highlightthickness=1)
	tela.mainloop()