import MySQLdb
import csv

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="imad",
                  db="test")
x = conn.cursor()


records = csv.reader("/home/imad/Desktop/file.csv",delimiter=';')

for line in records:
	        Civ         = line[0]
                Nom         = line[0]
                Prenom      = line[0]
                Adresse1    = line[0]
                Adresse2    = line[0]
                Adresse3    = line[0]
                Adresse4    = line[0]
                Cp          = line[0]
                Ville       = line[0]
	        Email       = line[0]

   		x.execute("INSERT INTO csv VALUES(null,'"+Civ+"','"+Nom+"','"+Prenom+"','"+Adresse1+"','"+Adresse2+"','"+Adresse3+"','"+Adresse4+"','"+Cp+"','"+Ville+"','"+Email+"')")
#		x.execute("INSERT INTO csv(id,civ) VALUES(null,'"+Civ+"')")

conn.commit()


#conn.close()
