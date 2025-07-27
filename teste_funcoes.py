from models.classe_produto import Produto
import unittest
from utils.help import add_loja, add_carrinho


# Testes unitários de funções.

class TestFuncoes(unittest.TestCase):

    p = Produto("Notebook gamer", 3213.43)
    p2 = Produto("Xbox 360", 2300.12)

    def setUp(self) -> None:
        self.loja = []
        self.carrinho = []

#===============================================================#
    def test_add_loja(self):
        

        add_loja(self.loja, TestProduto.p)
        self.assertListEqual(
            self.loja,
            [TestProduto.p]
        )

        add_loja(self.loja, TestProduto.p2)

        self.assertListEqual(
            self.loja,
            [TestProduto.p, TestProduto.p2]
            )

        add_loja(self.loja, TestProduto.p)

        self.assertListEqual(
            self.loja,
            [TestProduto.p, TestProduto.p2]
        )
#========================================================================#
    def test_add_carrinho(self):
        add_carrinho(self.carrinho, TestProduto.p)
        self.assertListEqual(
            self.carrinho,
            [{TestProduto.p : 1}]
        )

        add_carrinho(self.carrinho, TestProduto.p)
        self.assertListEqual(
            self.carrinho,
            [{TestProduto.p : 2}]
        )

        add_carrinho(self.carrinho, TestProduto.p2)
        self.assertListEqual(
            self.carrinho,
            [{TestProduto.p : 2}, {TestProduto.p2 : 1}]
        )
        
    


if __name__ == '__main__':

    unittest.main()
