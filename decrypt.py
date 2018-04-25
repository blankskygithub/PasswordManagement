#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-25 15:09:38
# @Author  : Zhilin Shuai (zhilin_shuai@trendmicro.com.cn)
# @Link    : http://www.example.com.cn/
# @Version : $Id$


def row_column_transposition(ciphertext, key):
    """
    Description: row/column transposition cipher

    Arguments:
        ciphertext: cipher text
        key(plaintext -> ciphertext): [num_rows, num_columns]
    Example:
        ciphertext="Tsrshaesistasemgicee"
        key=[4, 5]
        Reverse: [5, 4]
        T s r s
        h a e s
        i s t a
        s e m g
        i c e e
        plaintext="Thisisasecretmessage"
    """
    plaintext = ''
    column = key[0]
    row = key[1]
    for i in xrange(0, row):
        for j in xrange(0, column):
            if (i + j * row) < len(ciphertext):
                plaintext += ciphertext[i + j * row]
            else:
                plaintext += ''
    return plaintext
