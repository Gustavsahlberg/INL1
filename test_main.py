import unittest
from main import *

class Testafunktioner(unittest.TestCase):
    def setUp(self):
        self.konto_arkiv = {'konto0000': 
                       {'saldo': 1100, 
                    'transaktioner':
                      ['+100(2024-09-12(12:31.00))',
                        '+100(2024-09-12(12:31:01))', 
                        '-100(2024-09-12(12:31:02))',
                          '+1000(2024-09-19(08:40:54))']},
                    'konto0001': 
                    {'saldo': 100, 
                     'transaktioner':
                       ['+100(2024-09-12(12:31:00))', 
                        '+100(2024-09-12(12:31:02))', 
                        '-100(2024-09-12(12:31:04))']},
                     'konto0002': 
                     {'saldo': 450,
                        'transaktioner':
                          ['+500(2024-09-19(08:41:48))',
                            '-50(2024-09-19(08:41:52))']}}


    def finns_konto_test(self):
        self.assertTrue(finns_konto("konto000", self.konto_arkiv))




if __name__ == "__main__":
    main()
    