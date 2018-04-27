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
    Expand:
        Add other extra random characters after ciphertext
        Don't need substring(ciphertext) in decryption because of key is fixed
        But it doesn't matter if you substring(ciphertext): ciphertext[:num_rows*num_columns]
        ciphertext="Tsrshaesistasemgicee[testrandomab]"
    """
    ciphertext = ""
    plaintext = ''.join(plaintext.split())
    num_rows = key[0]
    num_columns = key[1]
    if num_rows * num_columns != len(plaintext):
        raise ce.EncryptKeyErrorException(
            "encrypt key error: num_rows * num_columns != plaintext.__len__(without spaces)")
    for i in xrange(0, num_columns):
        for j in xrange(0, num_rows):
            ciphertext += plaintext[i + j * num_columns]
    return ciphertext


def column_transposition(plaintext, key):
    """
    Description: column transposition
    Restriction: num_row * num_column = length of plaintext(without space)
                 num_columns = the length of columns_position
    Arguments:
        plaintext: plain text
        key: [num_rows, num_columns, [columns_position]]
    Example:
        plaintext: this is a secrete message
        key=[4, 5, [2, 3, 5, 1, 4]]
        2 3 5 1 4
        t h i s i
        s a s e c
        r e t m e
        s s a g e
        Transposition:
        s t h i i
        e s a c s
        m r e e t
        g s s e a
        ciphertext="sthiiesacsmreetgssea"
    Expand:
        columns_position can be substituted by a string whose length equals
        num_columns and regard the alphabetical order as columns_position
        eg. BOATS ==> [2, 3, 1, 5, 4]
    """
    ciphertext = ""
    plaintext = ''.join(plaintext.split())
    num_rows = key[0]
    num_columns = key[1]
    columns_position = key[2]
    if (num_rows * num_columns != len(plaintext)) or (num_columns != len(columns_position)):
        raise ce.EncryptKeyErrorException(
            "encrypt key error: num_rows * num_columns != plaintext.__len__(without spaces) \
            OR num_columns != columns_position.__len__")
    for i in xrange(0, num_rows):
        for j in xrange(0, num_columns):
            index = i * num_columns + columns_position.index(j + 1)
            ciphertext += plaintext[index]
    return ciphertext


def caesar_substitution(plaintext, key):
    """
    Description: CAESAR substitution,
                 shift each character in the message by n(key) letters
                 eg. when key=3, A to D, Z to C
    Arguments:
        plaintext: plain text
        key: offset
    Example:
        plaintext="This is a secret message"
        key=3
        ciphertext="Wklvlvdvhfuhwphvvdjh"
    """
    ciphertext = ""
    plaintext = ''.join(plaintext.split())
    try:
        key = int(key)
    except Exception:
        raise ce.EncryptKeyErrorException("Encrypt Key Error: key is not an integer")
    offset = key % 26
    for character in list(plaintext):
        if (ord(character) < ord('z') + 1 and (ord(character) + offset > ord('z'))) \
                or (ord(character) < ord('Z') + 1 and (ord(character) + offset > ord('Z'))):
            ciphertext += chr(ord(character) + offset - 26)
        else:
            ciphertext += chr(ord(character) + offset)
    return ciphertext
