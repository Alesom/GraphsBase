import sqlite3
from random import *
import math
from sets import Set

con = sqlite3.connect("GraphsBase.db")
cur = con.cursor();


cur.execute('SELECT N, M , Delta FROM GraphBig ')
Line2 = cur.fetchall()
for  j in Line2:
	print j

print "Possiveis Overfulll"

cur.execute('SELECT N, Delta FROM GraphBig')
N=cur.fetchone()[0]
i=cur.fetchone()[1]
cur.execute('SELECT N, M FROM GraphBig WHERE M>= ?', (( int(N/2)*i +1) ,))
Line2 = cur.fetchall()
for  j in Line2:
	print j





'''
for i in xrange(2, 14):
	cur.execute('SELECT MAX(M) FROM Graph WHERE N==?', (i,))
	print str(i) +"  "+ str(cur.fetchone()[0])

for i in xrange(2, 14):
	cur.execute('SELECT * FROM Graph WHERE N==6 and M==12')
	print str(i) +"  "+ str(cur.fetchone()[0])

cur.execute('SELECT * FROM Graph WHERE N==6 and M==12 and NUCLEO==1751')
allLine=cur.fetchall()
for  i in allLine:
	print i

print "Nucelo"

cur.execute('SELECT * FROM NUCLEO WHERE id==1751')
allLine=cur.fetchall()
for  i in allLine:
	print i
'''

'''cur.execute('SELECT COUNT(*) FROM Graph')
print cur.fetchone()[0]
'''

#all_rows = cur.fetchall()
#for i in all_rows:
#	print i
#print "Nucleo"
#cur.execute('''SELECT * FROM Nucleo''')
#all_rows = cur.fetchall()
#for i in all_rows:
#	print i

'''
def ListaAdj(Edg, N): #gera a matriz de adj do Grafo
#	print Edg + "Arestas "+ str(N)
	if N <= 2 :
		if (len(Edg)>2):	
			return [[1], [0]]
		else:
			return None
	
	L=list([])
	for i in xrange(0, N): #cria uma lista de conjuntos que serao as linhas
		L.append(list([]))


	divide = Edg.split(' ');
	cont=0

	anterior=-1
	for j in divide:
		if str(j)!= "":
			if (cont % 2==0):
				anterior = j
			else:
				atual=j
				e1 = int (anterior)
				e2 = int (atual)
				print str(e1)+" ERS "+str(e2)
				L[e1].append(e2)
				L[e2].append(e1)
			print j+" J"
			cont+=1
	
	return L

def FindNucleo( adj, delta):
	Nl=list([])
	edg=""
	Nm=0
	flag=True
	for i in xrange(0, N):
		if len(adj[i])==delta:
			Nl.append(i)
			for j in adj[i]:
				if (i > j and len(adj[i])==delta):
					if flag:
						flag=False
						edg=str(i)+" "+str(j)	
					else:
						edg+=" "+ str(i)+" "+str(j)	
					Nm+=1

	Nn=len(Nl)
	NAdj=ListaAdj(edg, self.N)
	for j in NAdj:
		print j

L=ListaAdj("0 2 0 5 0 6 1 3 1 5 1 6 2 3 3 5 3 6 4 5 4 6", 7)
FindNucleo(L, 3)
for i in L:
	print i
'''
