from typing import List, Dict
from models.classe_produto import Produto
from time import sleep
from utils.help import mostra_loja, mostra_carrinho, formata_preco, add_carrinho, add_loja

loja: List[Produto] = []  # lista que contém objetos 'Produto'.
carrinho: List[Dict[Produto, int]] = [] # lista que contem dicionários com chave 'Produto' e valor 'quantidade'.

def menu():
    while True:
        print("================================")
        print("========= BEM-VINDO(A) =========")
        print("========= LOJA VIRTUAL =========")
        print("================================")


        print("1 - Visualizar loja\n2 - Visualizar carrinho\n3 - Cadastrar produto na loja\n4 - Adiciona produto ao carrinho")
        print("5 - Finalizar compra\n6 - Sair")
        
        while True:
            try:
                op: int = int(input())
                break
            except ValueError:
                print("Comando inválido!")

        if op == 1:
            #imprimi produtos da  loja.
            mostra_loja(loja)

        elif op == 2:
            # imprimi itens do carrinho.
            mostra_carrinho(carrinho)

        elif op == 3:
            nome = input("Insira o nome do produto: ")
            # Loop para tratar o erro'ValueError' para a variável 'valor'. 
            while True:
                
                try:
                    valor = float(input("Insira o preço do produto: "))
                    break

                except ValueError:
                    print("O preço deve ser um número real!")

            novo_produto = Produto(nome.title(), valor) # Cria novo produto.
            add_loja(loja, novo_produto) # Função que insere produto na loja.

        elif op == 4:
            
            if loja == []:
                print("Ainda não existem produtos da loja!")
                sleep(2)
            else:
                
                id_encontrado = False
                mostra_loja(loja)

                # Loop para tratar 'ValueError' para id.
                while True:
                    try:
                        id: int = int(input("Digite o ID do produto: "))
                        break
                    except ValueError:
                        print("O ID deve ser um inteiro!")
                
                for produto_loja in loja:
                # Procura um produto com id igual ao id digitado pelo usuário.
                    if produto_loja.id == id:
                        id_encontrado = True
                        add_carrinho(carrinho, produto_loja) # Função que insere produtos no carrinho.
                    
                # Caso não seja encontrado nenhum produto com id igual ao fornecido pelo usuário.    
                if id_encontrado == False:
                    print("ID não encontrado!")
                    sleep(2)


        elif op == 5:

            # Caso carrinho esteja vazio, imprimi 'Carrinho vazio!' apenas.
            if carrinho == []:
                print('Carrinho vazio!')
                sleep(2)

            else:
                print("compra finalizada!")
                valor_total = 0
                for produto_carrinho in carrinho:
                    # itera sobre os items do carrinho.
                    for produto, quantidade in produto_carrinho.items():
                        # Pega cada chave(produto) e valor(quantidade) para calcular o valor total.
                        valor_total += produto.valor * quantidade

                print(f"Valor total: R${formata_preco(valor_total)}") # imprimi o valor total formatado.
                carrinho.clear() # esvazia o carrinho.
                sleep(3)

        elif op == 6:
            # Sai do loop e o programa encerra.
            print("Volte sempre...")
            break
        
        else:
            print("Comando inválido!")
        


            


    

def main():
    menu()




if __name__ == '__main__':

    main()