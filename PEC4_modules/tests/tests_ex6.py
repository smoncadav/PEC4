import unittest
from src.exercises.ejercicio_6 import fun_total_goals
# from HTMLTestRunner import HTMLtestRunner
import pandas as pd


class Test_Ex6(unittest.TestCase):
    def test_ex6(self):
        mock_data = pd.DataFrame({
            "goles_favor": [10, 20, 30],
            "goles_contra": [5, 15, 25]
        })
        home_goals, away_goals, total_goals = fun_total_goals(mock_data)

        self.assertEqual(home_goals.sum(), 60)  # 10+20+30
        self.assertEqual(away_goals.sum(), 45)  # 5+15+25
        self.assertEqual(total_goals.sum(), 105)  # 60+45
        self.assertIsInstance(total_goals, pd.Series)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_Ex6))
  #  runner = HTMLtestRunner(log= True, verbosity=3, output='reports')

# Consulta: Consulta Anthropic. (2026). Claude (versión del 11 de junio de 2026)
# [Modelo de lenguaje grande]. https://claude.ai

