import sqlite3
import math
from random import *
from sets import *

MAX_TAM = 11234
MIN_TAM = 1123


def ListaAdj(Edg, N): #gera a matriz de adj do Grafo
#	print Edg + "Arestas "+ str(N)
	if N <= 2 :
		if (len(Edg)>2):	
			return [[1], [0]]	
		else:
			return None
	
	if len (Edg) < 2:
		return None

	L=list([])
	for i in xrange(0, N+10): #cria uma lista de conjuntos que serao as linhas
		L.append(list([]))


	divide = Edg.split(' ');
	cont=0

	anterior=-1
	for j in divide:
		if str(j) != "" and str(j) != " " and str(j) != "\n":
			if (cont % 2==0):
				anterior = j
			else:
				atual=j
				e1 = int (anterior)
				e2 = int (atual)
				L[e1].append(e2)
				L[e2].append(e1)
			cont+=1
	
	return L



class GraphNucleo:
	N, M, Edge, Adj = None, None, None, list([])

	def __init__(self, n, m, Edg):
		self.N=n
		self.M=m
		self.Edge=Edg
		self.Adj=ListaAdj(Edg, self.N)


class Graph:
	N, M, Edges, Delta, Nucleo, Adj = 0, 0, "", 0, None, list([])
	
	def __init__(self, n, m, edges):
		self.N=n 
		self.M=m
		self.Edges=edges
		self.Adj = ListaAdj(edges, self.N)
		self.Delta = self.FindDelta(self.Adj)
		self.Nucleo = self.FindNucleo(self.Adj, self.Delta)
		#for i in self.Adj:
		#	print str(i) + " Linha"


	def FindNucleo(self, adj, delta):
		if not adj:
			return GraphNucleo(0, 0, "")

		Nl=list([])
		edg=""
		Nm=0
		flag=True
		for i in xrange(0, self.N):
			if adj[i] and len(adj[i])==delta:
				Nl.append(i)
				for j in adj[i]:
					if (i > j and len(adj[j])==delta):
						if flag:
							flag=False
							edg=str(i)+" "+str(j)	
						else:
							edg+=" "+ str(i)+" "+str(j)	
						Nm+=1
		
		Nn=len(Nl)
		NAdj=ListaAdj(edg, self.N)
		NNucleo=GraphNucleo(Nn, Nm, edg)
		return NNucleo
	
	def FindDelta(self, adj):
		Maior = 0
		if not adj:
			return 0

		for i in xrange(0, self.N):
			if adj[i]:
			 	if int (len(adj[i])) > Maior:
					Maior=int(len(adj[i]))
		
		return Maior

	def getNucleo(self):
		return self.Nucleo


def BuildGraphsAndInsert (Quantidade):
	 
	while Quantidade > 0:
		N = randint(MIN_TAM, MAX_TAM)

		print N
		M=0

	#	L=list([])

		cont = 0
		edg=""
		flag=True
		for i in xrange(0, N):
			Ll=list([])
			for j in xrange(i+1, N):
				if randint(0, 1) == 1:
					Ll.append(j)
					if flag:
						edg=str(i) + " " + str(j)
						flag=False
					else: 
						edg+= " "+str(i) + " " + str(j)
					
		#			print str(i) + " "+str(j)+" "+str(cont)
					cont+=1
			
			M=M+len(Ll)
		
		
		#print edg	
			#L.append(Ll)

			#Comparador = randint(0, N-i-1)
			#S=Set([])
			#while (len (S) < Comparador): 
		#		S.add(randint(i+1, N-1))
		#	M=M+len(S)
		#	L.append(S)

		
		'''cont = 0
		edg=""
		flag=True
		for i in xrange(0, len(L)):
			for j in L[i]:
				if flag:
					edg=str(i) + " " + str(j)
					flag=False
				else: 
					edg+= " "+str(i) + " " + str(j)
				
				print str(i) + " "+str(j)+" "+str(cont)
				cont+=1'''


		G=Graph(N, M, edg)
		
		try:
			con = sqlite3.connect("GraphsBase.db")
			cur = con.cursor();
			
			cur.execute('''INSERT INTO NucleoBig(N, M, Edges, aciclico)
								VALUES(?,?,?,?)''', (G.Nucleo.N, G.Nucleo.M, G.Nucleo.Edge, False))
			
			cur.execute('SELECT max(id) FROM Nucleo')

			max_id = cur.fetchone()[0]

			#print G.Edges

			cur.execute('''INSERT INTO GraphBig (N, M, Edges, Delta, NUCLEO)
	                  VALUES(?,?,?,?,?)''', (G.N, G.M, G.Edges, G.Delta, max_id))
			
			con.commit()
			print Quantidade
			Quantidade -= 1
		except Exception as e:
			con.rollback()
			print e
		finally:
			con.close()


BuildGraphsAndInsert(10)
#for i in xrange(12, 14):
#	MIN_TAM=i
#	BuildGraphsAndInsert(80000)

'''con = sqlite3.connect("GraphsBase.db")
c=con.cursor();
c.execute('SELECT * FROM Nucleo')
allR=c.fetchall()
for i in allR:
	print i '''
