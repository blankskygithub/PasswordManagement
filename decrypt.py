#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-25 15:09:38
# @Author  : Zhilin Shuai (zhilin_shuai@trendmicro.com.cn)
# @Link    : http://www.example.com.cn/
# @Version : $Id$
import CustomException as ce


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
    row = key[1]
    column = key[0]
    if row * column != len(ciphertext):
        raise ce.EncryptKeyErrorException(
            "encrypt key error: num_row * num_column != ciphertext.__len__")
    for i in xrange(0, column):
        for j in xrange(0, row):
            if (i + j * column) < len(ciphertext):
                plaintext += ciphertext[i + j * column]
            else:
                plaintext += ''
    return plaintext
