import unittest
from unittest.mock import MagicMock
import gas_calc

class TestCalculadoraCombustivel(unittest.TestCase):

    def setUp(self):
        self.root = MagicMock()  # Simula a janela raiz

    def test_calculo_combustivel(self):
        # Teste a função de cálculo de combustível
        result = gas_calc.calcular_combustivel_porshce_911_gt3(10, 5, 60, 5, 40)
        self.assertEqual(result, (50, 200))

    def test_converter_segundos_para_minutos_segundos(self):
        # Teste a função de conversão de segundos para minutos e segundos
        result = gas_calc.converter_segundos_para_minutos_segundos(3600)
        self.assertEqual(result, (60, 0))

    def test_calculo_combustivel_button(self):
        # Teste a função de cálculo de combustível ao clicar no botão
        entry_mock = MagicMock()
        entry_mock.get.side_effect = [10, 5, 60, 5, 40]  # Valores de entrada simulados
        resultado_text_mock = MagicMock()
        resultado_text_mock.delete = MagicMock()
        resultado_text_mock.insert = MagicMock()

        gas_calc.entry_consumo = entry_mock
        gas_calc.entry_voltas = entry_mock
        gas_calc.entry_tanque = entry_mock
        gas_calc.entry_reserva = entry_mock
        gas_calc.entry_tempo = entry_mock
        gas_calc.resultado_text = resultado_text_mock

        gas_calc.calcular_combustivel()

        resultado_text_mock.delete.assert_called_once_with("1.0", gas_calc.tk.END)
        resultado_text_mock.insert.assert_called()

    def test_limpar_campos_button(self):
        # Teste a função de limpar campos ao clicar no botão
        entry_mock = MagicMock()
        entry_mock.delete = MagicMock()

        gas_calc.entry_consumo = entry_mock
        gas_calc.entry_voltas = entry_mock
        gas_calc.entry_tanque = entry_mock
        gas_calc.entry_reserva = entry_mock
        gas_calc.entry_tempo = entry_mock

        gas_calc.limpar_campos()

        entry_mock.delete.assert_called()

if __name__ == '__main__':
    unittest.main()
