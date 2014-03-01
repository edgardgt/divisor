vDividendo = raw_input("Dividendo? ")
vDivisor = raw_input("Divisor? ")
vPuntoEncontrado = False
vExpDividendo = 0
vExpDivisor = 0

lDividendo = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lDivisor = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lCociente = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lAbajo = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lResto = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


print 'Dividendo desglosado:'
i = 0
for digito in vDividendo:
	if digito==".":
		vPuntoEncontrado = True
		
	if vPuntoEncontrado==True:
		vExpDividendo+=1
	else:
		vExpDivisor+=1
	
	lDividendo[i] = digito
	i+=1

print lDividendo
print vExpDividendo

	
	
print''

print 'Divisor desglosado:'
for digito in vDivisor:
	print digito
	

print "Dividendo y Divisor: "
print vDividendo
print vDivisor
