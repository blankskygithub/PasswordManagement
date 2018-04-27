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

    def testColumnTransposition(self):
        """
                Test Column Transposition
        """
        plaintext = "this is a secret message"
        key = [4, 5, [2, 3, 5, 1, 4]]
        ciphertext = ""
        try:
            ciphertext = encrypt.column_transposition(plaintext, key)
        except Exception as e:
            print(e.message)
            raise e
        self.assertEqual('sthiiesacsmreetgssea', ciphertext)

    def testCaesarSubstitution(self):
        """
        Test CAESAR substitution
        """
        plaintext = "this is a secret meXYZge"
        key = 3
        ciphertext = ""
        try:
            ciphertext = encrypt.caesar_substitution(plaintext, key)
        except Exception as e:
            print(e.message)
            raise e
        self.assertEqual("wklvlvdvhfuhwphABCjh", ciphertext)


class TestDecryptModule(unittest.TestCase):

    def testRowColumnTransposition(self):
        """
        Test Row/ColumnTransposition
        """
        ciphertext = "Tsrshaesistasemgiceetestraandom"
        key = [4, 5]
        self.assertEqual('Thisisasecretmessage',
                         decrypt.row_column_transposition(ciphertext, key))

    def testColumnTransposition(self):
        """
        Test Column Transposition
        """
        ciphertext = "sthiiesacsmreetgssea"
        key = [4, 5, [2, 3, 5, 1, 4]]
        plaintext = ""
        try:
            plaintext = decrypt.column_transposition(ciphertext, key)
        except Exception as e:
            print e.message
            raise e
        self.assertEqual('thisisasecretmessage', plaintext)

    def testCaesarSubstitution(self):
        ciphertext = "wklvlvdvhfuhwphABCjh"
        key = 3
        plaintext = ""
        try:
            plaintext = decrypt.caesar_substitution(ciphertext, key)
        except Exception as e:
            print e.message
            raise e
        self.assertEqual("thisisasecretmeXYZge", plaintext)


if __name__ == '__main__':
    encryptSuite = unittest.TestLoader().loadTestsFromTestCase(TestEncryptModule)
    decryptSuite = unittest.TestLoader().loadTestsFromTestCase(TestDecryptModule)
    unittest.TextTestRunner(verbosity=2).run(encryptSuite)
    unittest.TextTestRunner(verbosity=2).run(decryptSuite)
