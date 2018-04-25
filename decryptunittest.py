#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-25 15:22:34
# @Author  : Zhilin Shuai (zhilin_shuai@trendmicro.com.cn)
# @Link    : http://www.example.com.cn/
# @Version : $Id$

import unittest
import decrypt


class TestDecryptModule(unittest.TestCase):

    def testRowColumnTransposition(self):
        """
        Test Row ColumnTransposition
        """
        ciphertext = "Tsrshaesistasemgicee"
        key = [5, 4]
        self.assertEqual('Thisisasecretmessage',
                         decrypt.row_column_transposition(ciphertext, key))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDecryptModule)
    unittest.TextTestRunner(verbosity=2).run(suite)
