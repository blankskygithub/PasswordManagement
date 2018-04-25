#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-25 15:03:09
# @Author  : Zhilin Shuai (zhilin_shuai@trendmicro.com.cn)
# @Link    : http://www.example.com.cn/
# @Version : $Id$

import unittest
import encrypt
import decrypt


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


class TestDecryptModule(unittest.TestCase):

    def testRowColumnTransposition(self):
        """
        Test Row ColumnTransposition
        """
        ciphertext = "Tsrshaesistasemgicee"
        key = [4, 5]
        self.assertEqual('Thisisasecretmessage',
                         decrypt.row_column_transposition(ciphertext, key))


if __name__ == '__main__':
    encryptSuite = unittest.TestLoader().loadTestsFromTestCase(TestEncryptModule)
    decryptSuite = unittest.TestLoader().loadTestsFromTestCase(TestDecryptModule)
    unittest.TextTestRunner(verbosity=2).run(encryptSuite)
    unittest.TextTestRunner(verbosity=2).run(decryptSuite)
