def imprimir_matriz(matriz):
   print (matriz[0])
   print (matriz[1])
   print (matriz[2])

def interacao(op):
   if(op == 1):
      jordan(op)
   elif(op ==2):
      print('Agradecemos por utilizar nosso software! >_<')
          
   
def jordan(op):
   cobre = zinco = vidro = m21 = m31 = m32 = m12 = m13 = m23 = aux = 0 
   cobre = input('Entre com a quantidade de cobre: ')
   zinco = input('Entre com a quantidade de zinco: ')
   vidro = input('Entre com a quantidade de vidro: ')
   matriz = [[4, 3, 2, int(cobre)], [1, 3, 1, int(zinco)], [2, 1, 3, int(vidro)]]
   
   print('Matriz ampliada: ')
   
   imprimir_matriz(matriz) 
   
   print('\n1ª parte:\n1- Calculando m21 = m21/m11 e m31 = m31/m11 \n2- Fazendo (L2- m21*L1) e (L3 - m23*L1) \n')
   
   m21 = matriz[1][0]/matriz[0][0]

   #print (m21)

   m31 = matriz[2][0]/matriz[0][0]

   #print (m31)

#fazendo (L2- m21*L1) e (L3 - m23*L1) para zerar as posições [1][0] e [2][0]
   for x in range(4):
      matriz[1][x] = matriz[1][x] -(m21 * matriz[0][x])
      matriz[2][x] = matriz[2][x] -(m31 * matriz[0][x])
   

   imprimir_matriz(matriz)
   
   print('\n2ª parte:\n1- Calculando m32 = m32/m22 e m12 = m12/m22 \n2-Fazendo (L1 - m12*L2) e (l3 - m32*L2)\n')
   
   m32 = matriz[2][1]/matriz[1][1]
   #print(m32)
   m12 = matriz[0][1]/matriz[1][1]
   #print(m12)
   
   #fazendo (L1 - m12*L2) e (l3 - m32*L2) para zerar as posições [0][1] e [2][1]
   for x in range(4):
      matriz[0][x] = matriz[0][x] -(m12 * matriz[1][x])   
      matriz[2][x] = matriz[2][x] -(m32 * matriz[1][x])
   
   imprimir_matriz(matriz)
   
   print('\n3ª parte:\n1- Calculando m13 = m3/m33 e m23 = m23/m33 \n2- Fazendo (L1 - m13*L3) e (L2 - m23*L3)\n')
  
   m13 = matriz[0][2]/matriz[2][2]
   #print(m13)
   m23 = matriz[1][2]/matriz[2][2]
   #print(m23)

   #fazendo (L1 - m13*L3) e (L2 - m23*L3) para zerar as posições [0][2] e [1][2]
   for x in range(4):
      matriz[0][x] = matriz[0][x] -(m13 * matriz[2][x])
      matriz[1][x] = matriz[1][x] -(m23 * matriz[2][x])
   
   imprimir_matriz(matriz)

   print('\n4ª parte:\nFazendo operações elementares para que nossa matriz "reduzida" seja unitária\n')

#fazendo os trequinhos para a diagonal principal ficar apenas com 1

   aux = 1/matriz[0][0]
   #print(aux)
   matriz[0][0] = matriz[0][0] * aux
   matriz[0][3] = matriz[0][3] * aux
   
   aux = 1/matriz[1][1]
   #print(aux)
   matriz[1][1] = matriz[1][1] * aux
   matriz[1][3] = matriz[1][3] * aux
   
   aux = 1/matriz[2][2]
   #print(aux)
   matriz[2][2] = matriz[2][2] * aux
   matriz[2][3] = matriz[2][3] * aux

   imprimir_matriz(matriz)
   
   print('\nA matriz produziu o seguinte vetor resultado:')
   print('|',(matriz[0][3]),'|')
   print('|',(matriz[1][3]),'|')
   print('|',(matriz[2][3]),'|')
   
   print("\nA resolução das equações nos fornece os seguintes dados: ")
   print('-> Transistores:', round(matriz[0][3], 2),' unidades')
   print('-> Resistores:', round(matriz[1][3], 2),' unidades')
   print('-> Chips de computador:', round(matriz[2][3], 2),' unidades')
   
   op = 0
   while (int(op)<1):
      print('\n| 1 - Realizar novo cálculo |')
      print('| 2 - Sair                  |')
      op= input('Entre com a opção desejada: ')
       
   interacao(int(op))
 
op = 0
print('| Programa de resolução de equações pelo método Jordan |')  
jordan(op)
