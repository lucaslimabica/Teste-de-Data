# Tema 6 - a82451 - Lucas Bica

import unittest
from data import Data, AnoInvalido, MesInvalido, DiaInvalido


class TestData(unittest.TestCase):
    def test_data_valida(self):
        self.assertEqual(str(Data(2024, 2, 29)), "2024/02/29")

    def test_ano_invalido(self):
        with self.assertRaises(AnoInvalido) as context:
            Data(0, 1, 1)
        self.assertEqual(str(context.exception), "Ano inválido: 0. Não existe ano 0.")

    def test_mes_invalido(self):
        with self.assertRaises(MesInvalido) as context:
            Data(2023, 13, 1)
        self.assertEqual(
            str(context.exception), "Mês inválido: 13. O mês deve estar entre 1 e 12."
        )

    def test_dia_invalido(self):
        with self.assertRaises(DiaInvalido) as context:
            Data(2023, 2, 30)
        self.assertEqual(str(context.exception), "Dia inválido: 30, para o mês 2.")

    def test_ano_bissexto(self):
        self.assertTrue(Data.is_bissexto(2024))
        self.assertFalse(Data.is_bissexto(2023))


if __name__ == "__main__":
    unittest.main()