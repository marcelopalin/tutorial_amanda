from meteorologia import calculos

import sys
# Definir o limite de tracebacks para zero
sys.tracebacklimit = 0

def main():    
    """
    Função principal do programa.
    Imprime a mensagem "Hello World" no console.
    """
    resp = calculos.soma("letra", "teste")
    print(resp)
 
    

# Por onde o programa começa a ser executado
if __name__ == "__main__":
    main()
