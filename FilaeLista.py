class ListaEncadeada():
	def __init__(self):
		self._inicio = None
		self._fim = None
		self.prox = None
		self.ant = None

	def isVazia(self):
		return self._inicio is None and self._fim is None

	def inserirNoInicio(self,dado):
		novo_no = No(dado)
		if self.isVazia():
			self._inicio = novo_no
			self._fim = novo_no
		else:
			novo_no.prox = self._inicio
			self._inicio.ant = novo_no
			self._inicio = novo_no

	def inserirNoFim():
	
	def removerDoInicio(dado):

	def removerDoFim(self):
		if not self.isVazia():
			if self._fim.ant is not None:
				penultimo = self._fim.ant
				penultimo.prox = None
				self._fim = penultimo
				return ultimo
			else:
				self._inicio = self._fim = None
				return ultimo
		return ultimo

	def buscar(self,dado):
		i = self._inicio
		while i != None:
			if i.dado == x:
				return i
			else:
				i = i.prox
		return i


class pilha(ListaEncadeada):
	def __init__(self):
		super(Pilha).__init__():
		print('blablabla')