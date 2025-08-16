from Clases.Animal import*

A = animal ('Masha', '5 kg','Fabiana', '15-marzo', '20-enero-2023')

#get
print(A._nombre)
print(A.peso)
print(A._propietario)
print(A.fecha_cumpleaños)
print(A._fecha_ultima_vacuna)

#set
A.nombre = 'sasha'
A.peso = '4'
A.propietario = 'fabian'
A.fecha_cumpleaños = '20-febrero'
A.fecha_ultima_vacuna = '30-octubre-2023'

#luego de los cambios
print(A._nombre)
print(A.peso)
print(A._propietario)
print(A.fecha_cumpleaños)
print(A._fecha_ultima_vacuna)