from time import sleep
from typing import List, Dict



def formata_preco(preco: float):
    """Formata o preço do produto:

        ex: 2000 -> 2,000.00
        ex: 4321 -> 4,321.00
        ex 1245.12 -> 1,245.12
    """
    return f'{preco:,.2f}'


from models.classe_produto import Produto
def mostra_loja(loja):
    
    """
    imprimi os produtos da loja individualmente na tela. Se a loja não tiver produtos ([]), imprimi "Loja vazia!"

    ex:
        Loja:
        ================================
        Id: id do produto1
        Nome: nome do produto1
        Preço: preço do produto1
        ================================

    """

    print("Loja:")
    print("================================")

    if loja == []:
        print('Loja vazia!')
        sleep(2)

    else:
        for produto in loja:
            print(produto)
            print("================================")
            sleep(1)
        sleep(2)


def mostra_carrinho(carrinho: List[Dict[Produto, int]]):

    """
    Imprimi os produtos do carrinho + quantidade. Se o carrinho estiver vazio ([]), imprimi "Carrinho vazio!"

    ex:
        Carrinho:
        ================================
        Id: id do produto1
        Nome: nome do produto1
        Preço: preço do produto1
        Quantidade: quantidade do produto1
        ================================
    """

    print("Carrinho:")
    print("================================")

    if carrinho == []:
        print("Carrinho vazio!")
        sleep(2)

    else:
        for item in carrinho:
            for produto, quantidade in item.items():
                print(produto)
                print(f'Quantidade: {quantidade}')
                print("================================")
                sleep(1)
            sleep(2)




def add_loja(loja: List[Produto], novo_produto: Produto):

    """
    Finalidade: adicionar um objeto 'novo_Produto' na lista 'Loja' caso não exista nenhum produto
    na loja com o mesmo nome de novo_produto.

    parâmetros: lista 'loja' e um objeto Produto 'novo_produto'. 
    """

    # lista contendo apenas os nomes dos produtos da loja.
    # Ex: [Produto1, Produto2, Produto3] -> ['Notebook', 'Geladeira', 'Televisão']
    nomes_produtos_loja = list(map(lambda x: x.nome, loja))

    # Verifica se o nome de novo_produto já está na lista de nomes dos produtos. 
    if novo_produto.nome in nomes_produtos_loja:
        print("Produto já está cadastrado na loja!")
        sleep(2)

    else:
        # Adiciona novo_produto na lista 'loja'
        loja.append(novo_produto)
        print(f"{novo_produto.nome} Cadastrado na loja!")
        sleep(2)


def add_carrinho(carrinho: List[Dict[Produto, int]], novo_produto: Produto):

    """
    Finalidade: adicionar produto da loja no carrinho. Se o carrinho 
    já tiver esse produto, então a quantidade é acrescida.

    Parâmetros: lista de dicionários 'carrinho' e um objeto Produto 'novo_produto'
    """
    # Se carrinho estiver vazio é criado um item {novo_produto: 1} que é adicionado ao carrinho.
    if carrinho == []:
        item = {novo_produto : 1}
        carrinho.append(item)
        print(f"{novo_produto.nome} adicionado ao carrinho!")
        sleep(2)

    else:
        # Itera sober os itens do carrinho.
        for item in carrinho:
            # Verifica diretamente se o produto é uma chave no dicionário
            if novo_produto in item:
                item[novo_produto] += 1 # aumenta a quantidade do item no carrinho.
                print(f"{novo_produto.nome} foi acrescido no carrinho!")
                sleep(2)
                return
                    
        # Se o produto que queremos adicionar não está no carrinho então criamos {novo_produto: 1} e adicionamos no carrinho.
        
        item = {novo_produto: 1}
        carrinho.append(item)
        print(f"{novo_produto.nome} adicionado ao carrinho!")
        sleep(2)
