import subprocess

class pila:
	def __init__(self):
		self.cabeza = None
		self.auxiliar = None

	def insertar(self, numero):
		self.auxiliar = nodopila(numero)
		if(self.cabeza == None):
			print ("esta vacia")
			self.cabeza = self.auxiliar	# setcabeza(auxiliar)
		else:
			self.auxiliar.siguiente = self.cabeza
			self.cabeza= self.auxiliar

	def Sacar(self):
		self.auxliar = self.cabeza
		self.cabeza = self.cabeza.siguiente
		return self.auxiliar

	def GraficarPila(self):
		file= open('graficapila.dot', 'w')
		file.write("digraph Pila{\n label=\"Pila\"\n \tnode [fontcolor=\"red\",height=0.5,color=\"black\"]\n \tedge [color=\"black\", dir=fordware]\n " )
		self.Recorrer(file)
		file.write("\n}")
		file.close()
		subprocess.call(["dot","graficapila.dot","-Tpng","-o","pila.png"])

	def Recorrer(self, file):
		nodito= self.cabeza
		texto=""
		contador= 0
		while (nodito != None):
			texto = "nodo" + str(contador)+ "[label= \"" + str(nodito.numero) + "\"];\n"
			file.write(texto)
			nodito = nodito.siguiente
			contador += 1
		contador=0
		nodito= self.cabeza
		while (nodito.siguiente != None):
			texto= "nodo"+ str(contador) +"-> nodo" + str(contador+1)+";\n"
			file.write(texto)
			nodito= nodito.siguiente
			contador+=1
        	


class nodopila:
	def __init__(self, numero):
		self.numero = numero
		self.siguiente = None


class cola:
	def __init__ (self):
		self.cabeza= None
		self.cola= None
		self.auxiliar=None
	def insertar(self, numero):
		self.auxiliar = nodocola(numero)
		if(self.cabeza == None):
			self.cabeza= self.auxiliar
		else:
			self.cola.siguiente = self.auxiliar
		self.cola=self.auxiliar

	def Desencolar(self):
		self.auxiliar= self.cabeza
		self.cabeza(self.cabeza.siguiente)
		return auxiliar

	def GraficaCola(self):
		file= open('graficaCola.dot', 'w')
		file.write("digraph cola{\n label=\"cola\"\n \tnode [fontcolor=\"red\",height=0.5,color=\"black\"]\n \tedge [color=\"black\", dir=fordware]\n " )
		self.RecorrerCola(file)
		file.write("\n}")
		file.close()
		subprocess.call(["dot","graficaCola.dot","-Tpng","-o","cola.png"])

	def RecorrerCola(self, file):
		nodito= self.cabeza
		texto=""
		contador= 0
		while (nodito != None):
			texto = "nodo" + str(contador)+ "[label= \"" + str(nodito.numero) + "\"];\n"
			file.write(texto)
			nodito = nodito.siguiente
			contador += 1
		contador=0
		nodito= self.cabeza
		while (nodito.siguiente != None):
			texto= "nodo"+ str(contador) +"-> nodo" + str(contador+1)+";\n"
			file.write(texto)
			nodito= nodito.siguiente
			contador+=1

class nodocola:
	def __init__(self, numero):
		self.numero= numero
		self.siguiente= None

class nodolista:
	def __ini__ (self):
		self.palabra=""
		self.siguiente=None
		self.tamanio= None

class lista:
	def __init__ (self):
		self.cabeza = None
		self.actual= None
		self.auxiliar= None

	def insertar(self, palabra):
		self.auxiliar = nodolista(palabra)
		if(self.cabeza==None):
			self.cabeza=self.auxiliar
		else:
			self.actual.siguiente= self.auxiliar
		self.actual= self.auxiliar
		tamanio+=1

	def EliminarPosicion(self,numero):
		self.auxiliar= self.cabeza
		self.cabeza= self.cabeza.siguiente
		tamanio-=1
		return self.auxiliar
	def GraficaLista(self):
		file= open('graficaCola.dot', 'w')
		file.write("digraph cola{\n label=\"cola\"\n \tnode [fontcolor=\"red\",height=0.5,color=\"black\"]\n \tedge [color=\"black\", dir=fordware]\n " )
		self.RecorrerLista(file)
		file.write("\n}")
		file.close()
		subprocess.call(["dot","graficaLista.dot","-Tpng","-o","Lista.png"])

	def RecorrerLista(self, file):
		nodito= self.cabeza
		texto=""
		contador= 0
		while (nodito != None):
			texto = "nodo" + str(contador)+ "[label= \"" + str(nodito.palabra) + "\"];\n"
			file.write(texto)
			nodito = nodito.siguiente
			contador += 1
		contador=0
		nodito= self.cabeza
		while (nodito.siguiente != None):
			texto= "nodo"+ str(contador) +"-> nodo" + str(contador+1)+";\n"
			file.write(texto)
			nodito= nodito.siguiente
			contador+=1
cola = cola()
cola.insertar(3)
cola.insertar(2)
cola.insertar(1)
cola.GraficaCola()

pila= pila()
pila.insertar(3)
pila.insertar(2)
pila.GraficarPila()

lista = lista()
lista.insertar("hola")
lista.insertar("es")
lista.insertar("prueba")


		








