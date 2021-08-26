#varios tipos de elementos en conjunto
s = {True,56.7,None,"Grupo 48",("variables","acciones","frases")}

#los set no aceptan elementos repetidos
s1 = set([1,5,9,7,3,6,7,1,5])
s2 = set(range(10))
s3 = set(["Thomas","Xavi","Abraham","Juan","Thomas"])
s4 = set('Hola Pythonista')

detailArch(s)
detailArch(s1)
detailArch(s2)
detailArch(s3)
detailArch(s4)

# print(dir(s3))

#Hacemos una copia
s5 = s3.copy()
print('copy',s5)
#Comparacion con iguales
#compara uno a uno los elementos del conjunto
print("son iguales",(s3==s5))

# add elemento
s3.add('Formador')
print('add',s3)
# Print
print("s3",s3)
print("s5",s5)
# difference
#retorna la diferencia q tiene el elemento inicial con el q sepa como argumento
print('difference s3(s5)',s3.difference(s5))
print("s3-s5",s3-s5)
#en este caso todos los elementos del s5 se encuentarn en el s3
print('difference s5(s3)',s5.difference(s3))
print("s5-s3",s5-s3)

#difference_update ->
print('difference_update',s3.difference_update(s5))
print("Nuevo s3",s3)
#discard elimina si existe o si no continua normal
print('discard',s3.discard('Xavi'))
#remove elmina pero retorna error si el elemnto no existe
# print('remove',s3.remove('Xavi'))
# intersection
print('intersection',s3.intersection(s5))
print('intersection',s5.intersection(s3))
# isdisjoint
print('isdisjoint no comparten elementos?',s3.isdisjoint(s5))
# Print
print("s1",s1)
print("s2",s2)
print('intersection',(s1 & s2))
# isdisjoint
print('isdisjoint no comparten elementos?',s1.isdisjoint(s2))
# intersection_update
print('intersection_update compa',s1.intersection_update(s2))
print("New s1",s1)
# issubset
print('issubset s1 in s2',s1.issubset(s2))
print('issubset s2 in s1',s2.issubset(s1))
# issuperset
print('issuperset s1 in s2',s1.issuperset(s2))
print('issuperset s2 in s1',s2.issuperset(s1))


print('symmetric_difference s3 y s5',s5.symmetric_difference(s3))
print('symmetric_difference_update s3 con s5',s3.symmetric_difference_update(s5))
print("nuevo s3",s3)
print('union',)
print('update',)
print('pop',)
print('clear',)