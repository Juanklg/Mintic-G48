data = "De stepehn.marqua@utc.ac.za sat jan 5 09:15:16 2008"
#Encuntra la posicion del arroba(@)
indexArroba = data.find("@")
print(indexArroba)

#Encuntra el primer esoacio despues del arroba(@)
primerEspacio = data.find(' ',indexArroba)
print(primerEspacio)

#captura el host del correo
host = data[indexArroba+1:primerEspacio]
print(host)