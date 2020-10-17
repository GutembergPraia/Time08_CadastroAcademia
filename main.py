from src.functions import *

clientes = list()

def main():
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

  printTable(clientes)
    
if __name__ == "__main__":
    main()
