print('RGP SOLVER')
print('Risolutore di Luoghi Geometrici Parametrici')
print('')
print('Ottieni un sistema nella seguente forma:')
print('ax = bt + c')
print('dy = et + f')
print('Dove t è il parametro')

def program():
  print('')
  print('Definisci i valori richiesti')
  
  aa = input('a >_ ')
  bb = input('b >_ ')
  cc = input('c >_ ')
  dd = input('d >_ ')
  ee = input('e >_ ')
  ff = input('f >_ ')
  
  a = float(aa)
  b = float(bb)
  c = float(cc)
  d = float(dd)
  e = float(ee)
  f = float(ff)

  print('')
  print('Il tuo sistema è:')
  print(str(a) + 'y = ' + str(b) + 't' + ' + ' + str(c))
  print(str(d) + 'y = ' + str(e) + 't' + ' + ' + str(f))

  print('')
  print('Esplicito t nella prima equazione...')
  print('t = (' + str(a) + 'x + ' + str(-c) + ')/' + str(b))
  print(str(d) + 'y = ' + str(e) + 't' + ' + ' + str(f))
  print('')
  print('Calcolo...')
  print('')
  print('La soluzione è:')
  if b == 0:
    print('INFINITO')
  elif d == 0:
    print('INFINITO')
  else:
    print('y = (' + str(e*a) + 'x + ' +  str(-c+f*b) + ')/' + str(b*d))
  
  print('')
  print('')
  print('############################')
  print('')
  program()
  
program()
