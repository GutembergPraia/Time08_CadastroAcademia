from src.functions import cadastraClientes, printTable

def main():
  clientes = list()
  cadastraClientes(clientes)
  printTable(clientes)
    
if __name__ == "__main__":
    main()
