print('RGP SOLVER')
print('Risolutore di Luoghi Geometrici Parametrici')

def program():
  print('')
  
  print('ax = bt + c')
  print('dy = et + f')
  print('Dove t è il parametro')
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
  print('La soluzione è:')
  print('y = (' + str(e*a) + 'x + ' +  str(-c+f*b) + ')/' + str(b*d) )
  
  print('')
  print('')
  print('############################')
  program()
  
program()
