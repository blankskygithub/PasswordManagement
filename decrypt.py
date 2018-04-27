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
        ciphertext="Tsrshaesistasemgiceetestrandomab"
        key=[4, 5]
        Reverse: [5, 4]
        T s r s
        h a e s
        i s t a
        s e m g
        i c e e
        -------
        t e s t
        r a n d
        o m a b
        plaintext="Thisisasecretmessage"
    """
    plaintext = ''
    num_rows = key[1]
    num_columns = key[0]
    if num_rows * num_columns > len(ciphertext):
        raise ce.EncryptKeyErrorException(
            "Encrypt Key Error: num_row * num_column > ciphertext.__len__")
    for i in xrange(0, num_columns):
        for j in xrange(0, num_rows):
            if (i + j * num_columns) < len(ciphertext):
                plaintext += ciphertext[i + j * num_columns]
            else:
                plaintext += ''
    return plaintext


def column_transposition(ciphertext, key):
    """
    Description: Column Transposition
    Arguments:
        ciphertext: cipher text
        key(plaintext -> ciphertext): [num_rows, num_columns, [columns_transposition]]
    Example:
        ciphertext = "sthiiesacsmreetgssea"
        key=[4, 5, [2, 3, 5, 1, 4]]
        4 1 2 5 3 (index of columns_position order by number)
        s t h i i
        e s a c s
        m r e e t
        g s s e a
        plaintext="thisisasecretmessage"
    """
    plaintext = ''
    num_rows = key[0]
    num_columns = key[1]
    columns_position = key[2]
    if (num_rows * num_columns != len(ciphertext)) or (num_columns != len(columns_position)):
        raise ce.EncryptKeyErrorException(
            "Encrypt Key Error: num_rows * num_columns != plaintext.__len__(without spaces) \
            OR num_columns != columns_position.__len__")
    for i in xrange(0, num_rows):
        for j in xrange(0, num_columns):
            index = i * num_columns + columns_position[j] - 1
            plaintext += ciphertext[index]
    return plaintext


def caesar_substitution(ciphertext, key):
    """
    Description: CAESAR Substitution
    Arguments:
        ciphertext: cipher text
        key: offset
    Example:
        ciphertext="Wklvlvdvhfuhwphvvdjh"
        key=3
        plaintext="Thisisasecretmessage"
    """
    plaintext = ""
    try:
        key = int(key)
    except Exception:
        raise ce.EncryptKeyErrorException("Encrypt Key Error: key is not an integer")
    offset = key % 26
    for character in list(ciphertext):
        if (ord(character) > ord('A') - 1 and (ord(character) - offset < ord('A'))) \
                or (ord(character) > ord('a') - 1 and (ord(character) - offset < ord('a'))):
            plaintext += chr(ord(character) - offset + 26)
        else:
            plaintext += chr(ord(character) - offset)
    return plaintext
