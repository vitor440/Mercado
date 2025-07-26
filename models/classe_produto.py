class Produto:

    identificador: int = 0 # Identificador individual de cada produto.
    def __init__(self, nome: str, valor: float) -> None:
        self.__id: int = Produto.identificador + 1
        self.__nome: str = nome
        self.__valor: float = valor
        Produto.identificador += 1

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def valor(self) -> float:
        return self.__valor

    def __str__(self) -> str:
        from utils.help import formata_preco
        return f'ID: {self.id}\nNome: {self.nome}\nPreço: R${formata_preco(self.valor)}'   

        """
        Formatação desejada:

        ID: id do produto
        Nome: nome do produto
        Preço : R$preço do produto(formatado pela função 'formata_preco')
        
        """
