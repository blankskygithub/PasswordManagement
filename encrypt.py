#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-25 14:17:59
# @Author  : Zhilin Shuai (zhilin_shuai@trendmicro.com.cn)
# @Link    : http://www.example.com.cn/
# @Version : $Id$
import CustomException as ce


def row_column_transposition(plaintext, key):
    """
    Description: row/column transposition cipher
    Restriction: num_rows * num_columns = length of plaintext(without space)
    Arguments:
        plaintext: plain text
        key: [num_rows, num_columns]
    Example:
        plaintext="This is a secret message"
        key=[4, 5]
        T h i s i
        s a s e c
        r e t m e
        s s a g e
        ciphertext="Tsrshaesistasemgicee"
    """
    ciphertext = ""
    plaintext = ''.join(plaintext.split())
    row = key[0]
    column = key[1]
    if row * column != len(plaintext):
        raise ce.EncryptKeyErrorException(
            "encrypt key error: num_row * num_column != plaintext.__len__(without spaces)")
    for i in xrange(0, column):
        for j in xrange(0, row):
            ciphertext += plaintext[i + j * column]
    return ciphertext
