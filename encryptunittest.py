#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-25 15:03:09
# @Author  : Zhilin Shuai (zhilin_shuai@trendmicro.com.cn)
# @Link    : http://www.example.com.cn/
# @Version : $Id$

import unittest
import encrypt


class TestEncryptModule(unittest.TestCase):

    def testRowColumnTransposition(self):
        """
        Test Row ColumnTransposition
        """
        plaintext = "This is a secret message"
        key = [4, 5]
        ciphertext = ""
        try:
            ciphertext = encrypt.row_column_transposition(plaintext, key)
        except Exception as e:
            print(e.message)
            raise e
        self.assertEqual('Tsrshaesistasemgicee', ciphertext)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEncryptModule)
    unittest.TextTestRunner(verbosity=2).run(suite)
