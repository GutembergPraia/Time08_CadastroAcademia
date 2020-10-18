import unittest

from unittest.mock import patch

import os,sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from src.functions import cadastraClientes

class TestCadastro(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['0'])
    def test_castroClienteCod0(self, mock_input):
        teste = list()
        cadastraClientes(teste)
        self.assertEqual(len(teste),0)
    
    @patch('builtins.input', side_effect=['10','1','1','0'])
    def test_castroClienteCodInvalid(self, mock_input):
        teste = list()
        cadastraClientes(teste)
        self.assertEqual(len(teste),1)

if __name__ == '__main__':
    unittest.main()