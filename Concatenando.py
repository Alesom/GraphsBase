import sqlite3
import math
from random import *
from sets import *

MAX_TAM = 100000
MIN_TAM = 1000

class GraphNucleo:
	N, M, Edge, Adj, Ciclico = None, None, None, list([]), False

	def __init__(self, n, m, Edg):
		self.N=n
		self.M=m
		self.Edge=Edg
		self.Adj=ListaAdj(Edg, self.N)
		self.Ciclico = findCiclo(self.Adj, self.N)



class Graph:
	N, M, Edges, Delta, Nucleo, Adj = 0, 0, "", 0, None, list([])
	
	def __init__(self, n, m, edges):
		self.N=n 
		self.M=m
		self.Edges=edges
		self.Adj = ListaAdj(edges, self.N)
		self.Delta = self.FindDelta(self.Adj)
		self.Nucleo = self.FindNucleo(self.Adj, self.Delta)


	def FindNucleo(self, adj, delta):
		if not adj:
			return GraphNucleo(0, 0, "")
		
		index=[-1]*(self.N+3)

		cont=0
		for i in xrange(0, self.N):
			if adj[i] and len(adj[i])==delta:
				index[i]=cont
				cont=cont+1

		
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
							edg=str(index[i])+" "+str(index[j])	
						else:
							edg+=" "+ str(index[i])+" "+str(index[j])	
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



conta, pai, pre = 0, list([]), list([])

def DFS(adj, v):
	
	global pre
	global conta
	global pai

	pre[v] = pre[v]+conta
	conta=conta+1

	for i in adj[v]:
		if pre[int(i)] == -1:
			pai[int(i)]=v
			if DFS(adj, int(i))==True:
				return True
		elif int(i)!=pai[v]:
		 	return True
	return False


def findCiclo(Adj, N):
	if not Adj:
		return False

	global pre
	global conta
	global pai
	
	pre=[-1]*(N+5)
	pai=[0]*(N+5)
	conta=0
	
	for i in xrange (0, N):
		if pre[i]==-1:
			pre[i]=i
			if DFS(Adj, i)==True:
				return True
	return False


def ListaAdj(Edg, N):
	if N <= 2 :
		if (len(Edg)>2):	
			return [[1], [0]]	
		else:
			return None
	
	if len (Edg) < 2:
		return None


	L=list([])
	for i in xrange(0, N+10): 
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



def BuildGraphsAndInsert (Quantidade):
	 
	while Quantidade > 0:
		N = randint(MIN_TAM, MAX_TAM)

		
		M=0

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
					
					cont+=1
			
			M=M+len(Ll)

		print "N->"+str(N) +" M->"+str(M)

		G=Graph(N, M, edg)
		
		try:
			con = sqlite3.connect("GraphsBase.db")
			cur = con.cursor();
			
			cur.execute('''INSERT INTO NucleoBig (N, M, Edges, ciclico)
								VALUES(?,?,?,?)''', (G.Nucleo.N, G.Nucleo.M, G.Nucleo.Edge, G.Nucleo.Ciclico))
			
			cur.execute('SELECT max(id) FROM NucleoBig')

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


BuildGraphsAndInsert(1000)

#for i in xrange(12, 14):
#	MIN_TAM=i
#	BuildGraphsAndInsert(80000)

'''con = sqlite3.connect("GraphsBase.db")
c=con.cursor();
c.execute('SELECT * FROM Nucleo')
allR=c.fetchall()
for i in allR:
	print i '''
