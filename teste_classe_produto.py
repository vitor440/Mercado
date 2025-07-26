from models.classe_produto import Produto
import unittest




class TestProduto(unittest.TestCase):

    def setUp(self):
        self.p1 = Produto('Xbox 360', 2400.99)
        

        self.loja = []

    def test_get_id(self):
        self.assertEqual(
            self.p1.id,
            1
        )

    def test_get_nome(self):
        self.assertEqual(
            self.p1.nome,
            "Xbox 360"
        )

    def test_get_valor(self):
        self.assertEqual(
            self.p1.valor,
            2400.99
        )

     

if __name__ == '__main__':

  
    
    unittest.main()
