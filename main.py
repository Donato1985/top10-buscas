from client import tela, Casa
from consts import fundo

"""
Desenvolvido por Donato luz, o uso desse software é livre
qualquer dúvida ou sugestão, entre em contato
Esse é o módulo que roda toda a estrutura pro trás que foi desenvolvida
mais informações podem ser encontraddas dentro de cada um dos arquivos .py
e no LEIAME.txt
"""


if __name__=="__main__":
	"""
    Essa linha de cima diz o seguinte: se esse módulo estiver rodando como o principal,
    não como parte de uma importação ou algo assim, rode o que está aqui embaixo
	"""
	quadro=Casa(tela, bg=fundo, highlightbackground='black', highlightthickness=1)
	tela.mainloop()