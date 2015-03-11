import sqlite3 

con = sqlite3.connect("GraphsBase.db")
cur = con.cursor();

cur.execute('DROP TABLE if exists NucleoBig')

cur.execute('''CREATE TABLE NucleoBig (id INTEGER PRIMARY KEY AUTOINCREMENT, N INTEGER , M INTEGER, Edges TEXT, ciclico BOOLEAN)''')

cur.execute('DROP TABLE if exists GraphBig')

cur.execute('''CREATE TABLE GraphBig (N INTEGER, M INTEGER, Edges TEXT, Delta INTEGER, NUCLEO INTEGER, 
		PRIMARY KEY(N, M, Edges), 
		FOREIGN KEY(NUCLEO) REFERENCES Nucleo(id)
)''')

