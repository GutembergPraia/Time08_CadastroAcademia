
#Imprime o erro encontrado
def printErro(codErro: int):

  listErros = ['sucesso',
             '!ERRO! - Aplicativo não possui cliente cadastrado',
             '!ERRO! - Apenas Numeros int e positivos',
             '!ERRO! - Apenas Numeros float',
             '!ERRO! - Cliente já cadastrado',
             '!ERRO! - Altura min: 0.1 max: 4',
             '!ERRO! - Peso min: 0.1 max:450',
             '!ERRO! - Codigo de erro invalido',
             '!ERRO! - Falha na impressão dos valores',
             '!ERRO! - Falha no cadastro verifique os dados de entrada']

  if(codErro < len(listErros)):
    print(listErros[codErro])
    return listErros[codErro]
  else:
    print(listErros[6])
    return listErros[6]

# Verifica se num e um numero inteiro valido
# entrada: num: string       
# Return: valor, erro
# erro: 2 - '!ERRO! - Apenas Numeros int e positivos'
#       0 - Sucesso
def validaNumInt(num):
  if num.isdigit():
    return int(num),0
  else:
    return -1,2

# Verifica se num e um numero flutuante valido
# entrada: num: string     
# Return: valor, erro
# erro: 3 - !ERRO! - Apenas Numeros float'    
#       0 - Sucesso
def validaNumFloat(num):
  try:
    num = float(num)
    return num,0
  except ValueError:
    return -1,3

# verifica de cod e um codigo de cliente valido e se o mesmo esta cadastrado
# entrada: cod:int
# Return: valor, erro
#erro: 4 - Cliente já cadastrado
def validaCod(cod:int,codigo:list):
  if(cod in codigo and cod > 0):
    return -1,4  
  else:
    return cod,0

# valida o valor da Altura
# entrada: alt:float
# Return: valor, erro
#erro: 5 - '!ERRO! - Altura min: 0.1 max: 4'
def validaAlt(alt:float):
  if(alt>0 and alt<=4):
    return alt,0
  else:
    return 0,5

# Adiciona cod a lista de codigo, alt a lista de altura, pes a lista de peso e
#imc_temp a lista de imc
# entrada: cod:int, alt:float, pes:float, imc_temp:float
# return: boolean = 1 - Sucesso/ 0 - Falha, erro
#erro: 9 - '!ERRO! - Falha no cadastro verifique os dados de entrada'
def cadastraClient( cod:int, alt:float, pes:float, imc_temp:float, codigo:list, altura:list, peso:list, imc:list):
  try:
    #add cliente a lista
    codigo.append(cod)
    altura.append(alt)
    peso.append(pes)
    imc.append(imc_temp)

    return True,0
  
  except:
    return False,9

#  imprime uma tabela com o codigo dos usuarios mais alto, mais baixo, mais pesado,
# mais leve, mais gordo e mais magro
# entrada: codigo:list, altura:list, peso:list, imc:list
# return: boolean, Erro
# boolean: 1 - sucesso / 0 - falha
# Erro: 8 - Falha na impressão dos valores     
#            
def printTable(codigo:list, altura:list, peso:list, imc:list):
  try: 
    print('-'*50)
    print(f'{"":<13}{"Codigo":<5}{"Valor":>10}')
    print(f'{"mais alto:":<13}{codigo[altura.index(max(altura))]:>4}{round(max(altura),2):>11}{"m":<12}')
    print(f'{"mais baixo:":<13}{codigo[altura.index(min(altura))]:>4}{round(min(altura),2):>11}{"m":<12}')
    print(f'{"mais pesado:":<13}{codigo[peso.index(max(peso))]:>4}{round(max(peso),2):>11}{"kg":<12}')
    print(f'{"mais leve:":<13}{codigo[peso.index(min(peso))]:>4}{round(min(peso),2):>11}{"Kg":<12}')
    print(f'{"mais gordo:":<13}{codigo[imc.index(max(imc))]:>4}{round(max(imc),2):>11}{"kg/m^2":<12}')
    print(f'{"mais magro:":<13}{codigo[imc.index(min(imc))]:>4}{round(min(imc),2):>11}{"kg/m^2":<12}')
    print(f'{"media altura:":<13}{round(sum(altura)/len(altura),2):>15}{"m":<12}')
    print(f'{"media peso:":<13}{round(sum(peso)/len(peso),2):>15}{"kg":<12}')
    return True
  except ValueError:
      return False,8
