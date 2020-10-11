from src.functions import *

codigo = list()
altura = list()
peso = list()
imc = list()

#função principal
def main():

  while True:
    
    cod, codErro = validaNumInt(input("Código do Aluno ou 0 - Sair: "))
    
    if(codErro==0):
      cod, codErro = validaCod(cod,codigo)

    if(cod == 0):
      break
    elif(cod>0):

      while True:
        alt, codErro = validaNumFloat(input("Altura metros : "))
        if(codErro == 0):
          alt, codErro = validaAlt(alt)
        if(codErro != 0):
          printErro(codErro)
        else:
          break

      while True:
        pes, codErro = validaNumFloat(input("Peso : "))
        if(pes>0 and pes<=450 and codErro == 0):
          break
        else:
          codErro = 6
          printErro(codErro)
    
      imc_temp = pes/(alt*alt)

      valor, codErro = cadastraClient(cod,alt,pes, imc_temp,codigo,altura,peso,imc)
      if(valor):
        print("SUCESSO - Usuario Cadastrado")
      else:
        printErro(codErro)
          
    printErro(codErro)

  if(len(codigo)):
    printTable(codigo, altura, peso, imc)
  else:
    codErro = 1
    printErro(codErro)

if __name__ == "__main__":
    main()
