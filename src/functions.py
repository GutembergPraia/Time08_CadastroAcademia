class Cliente:
  #Definindo o creat
  def __init__(self, codigo):
    if codigo.isdigit():
      if(int(codigo) > 0):
        self.codigo = codigo
      else:
        raise ValueError(-1)
    else:
      raise ValueError('Codigo deve conter apenas numeros inteiros e possitivos')
  
  #Definindo o get altura
  @property
  def altura(self):
    return self._altura

  #Definindo o set altura
  @altura.setter
  def altura(self,altura):
    if(validaNumFloat(altura)):
      altura = float(altura)
      if(altura > 0 and altura <= 4):
        self._altura = altura
      else:
        raise ValueError('Altura min: 0.1 max: 4')
    else:
      raise ValueError('Apenas numeros flutuantes')
  
  #Definindo o get peso
  @property
  def peso(self):
    return self._peso

  #Definindo o set peso
  @peso.setter
  def peso(self,peso):
    if(validaNumFloat(peso)):
      peso = float(peso)
      if(peso>0 and peso<=450):
        self._peso = peso
      else:
        raise ValueError('Peso min: 0.1 max:450')
    else:
      raise ValueError('Apenas numeros flutuantes')
  
  #Definindo o get imc
  @property
  def imc(self):
    if(self.peso > 0 and self.altura > 0):
      return self.peso/(self.altura**2) 
    else:
      raise ValueError('Dados insuficientes para imc')
    
  '''
  def __str__(self):
    return str(self.__class__) + ": " + str(self.__dict__)
  '''

# Verifica se num e um numero flutuante valido
# entrada: num: string     
# Return: valor 
#         False 
# 
def validaNumFloat(num):
  try:
    num = float(num)
    return num  
  except ValueError:
    return False

# verifica se o codigo esta cadastrado
# entrada: cliente:object, clientes:list
# Return: True
#         False 
#
def verificaCod(cliente,clientes:list):
  if(cliente.codigo in (client.codigo for client in clientes)):
    raise ValueError(-2)

#  imprime uma tabela com o codigo dos usuarios mais alto, mais baixo, mais pesado,
# mais leve, mais gordo e mais magro
# entrada: codigo:list, altura:list, peso:list, imc:list
# return: boolean, Erro
# boolean: 1 - sucesso / 0 - falha
# Erro: 8 - Falha na impressão dos valores     
#       
def printTable(clientes:list):
  if(len(clientes)):  
    print('-'*50)
    print(f'{"":<13}{"Codigo":<5}{"Valor":>10}')
    print(f'{"mais alto:":<13}{clientes[[client.altura for client in clientes].index(max(client.altura for client in clientes))].codigo:>4}{max(client.altura for client in clientes):>11.2f}{"m":<12}')
    print(f'{"mais baixo:":<13}{clientes[[client.altura for client in clientes].index(min(client.altura for client in clientes))].codigo:>4}{min(client.altura for client in clientes):>11.2f}{"m":<12}')
    print(f'{"mais pesado:":<13}{clientes[[client.peso for client in clientes].index(max(client.peso for client in clientes))].codigo:>4}{max(client.peso for client in clientes):>11.2f}{"kg":<12}')
    print(f'{"mais leve:":<13}{clientes[[client.peso for client in clientes].index(min(client.peso for client in clientes))].codigo:>4}{min(client.peso for client in clientes):>11.2f}{"Kg":<12}')
    print(f'{"mais gordo:":<13}{clientes[[client.imc for client in clientes].index(max(client.imc for client in clientes))].codigo:>4}{max(client.imc for client in clientes):>11.2f}{"kg/m^2":<12}')
    print(f'{"mais magro:":<13}{clientes[[client.imc for client in clientes].index(min(client.imc for client in clientes))].codigo:>4}{min(client.imc for client in clientes):>11.2f}{"kg/m^2":<12}')
    print(f'{"media altura:":<13}{sum(client.altura for client in clientes)/len(clientes):>15.2f}{"m":<12}')
    print(f'{"media peso:":<13}{sum(client.peso for client in clientes)/len(clientes):>15.2f}{"kg":<12}')

  else:
    print('dados  insuficientes')

def cadastraClientes(clientes:list):
  while True:
    try:
      if not 'cliente' in locals():
        cliente = Cliente(input('Código do aluno ou 0 - Sair: '))
        verificaCod(cliente,clientes)
      if not hasattr(cliente, 'altura'):
        cliente.altura = input('Altura do aluno em metros: ')
      if not hasattr(cliente, 'peso'):
        cliente.peso = input('Peso do aluno em kg: ')

      clientes.append(cliente)
      del cliente

    except Exception as erro:
      if(erro.args[0]==-1):
        break
      elif (erro.args[0]==-2):
        del cliente
        print('Cliente ja Cadastrado')
      else:
        print(erro)
