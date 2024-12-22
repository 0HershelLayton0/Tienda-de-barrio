import os
#ordenar por llave
def ordena1(e):
	return e[1]
def ordena2(e):
	return e[0]

#se inicializan variables
alfanumericos = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)] + [str(i) for i in range(10)]
extras='/ .'

for i in extras:
	alfanumericos.append(i)

#print(alfanumericos)

direc=os.path.join(os.getcwd(),'database')
#print(direc)
text1= open(os.path.join(direc,'text1.txt'),'r')
text2= open(os.path.join(direc,'text2.txt'),'r')
text3= open(os.path.join(direc,'text3.txt'),'r')

output=open('./output.html','w')

#se copia el texto 1
for line in text1:
	output.write(line)

#se procesan los datos
productos=[]
for line in text2:
	tmp=[]
	var=''
	for i in line:
		if(i in alfanumericos):
			var+=i
		else:
			if(len(var)>0):
				tmp.append(var)
			var=''
	productos.append(tmp)

productos=sorted(productos,key=ordena1)
productos=sorted(productos,key=ordena2)
#productos.append(0)
#print(productos)
output.write('\n\n')


#se escribe text2
it=0
p=0
while(it<len(productos)):
	p+=1
	output.write('\n<div id="subpagina'+ str(p) +'">\n')
	va=productos[it][0]
	while(productos[it][0]==va):
		line=productos[it]
		s='<figure class="figura"><img class="imagenes" src="contenedor-imagenes/'+line[0]+'/'+line[3]+'" title="'+line[1]+'" alt="Cargando" onclick="ampliarImg(this)"><h6>\n'+line[2]+' : '+line[1]+'</h6></figure>\n'
		output.write(s)
		it+=1
		if(it==len(productos)):
			break
	output.write('</div>\n')
output.write('\n\n\n\n')

#se llena con la otraparte
for line in text3:
	output.write(line)



text1.close()
text2.close()
text3.close()