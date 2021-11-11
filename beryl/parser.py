# BerylDB - A modular database.
# http://www.beryldb.com
#
# Copyright (C) 2021 Carlos F. Ferry <cferry@beryldb.com>
# 
# This file is part of BerylDB. BerylDB is free software: you can
# redistribute it and/or modify it under the terms of the BSD License
# version 3.
#
# More information about our licensing can be found at https://docs.beryl.dev

from beryl.protocol import Protocol

def CheckFail(code):
    if code == Protocol.ERR_INPUT:
        raise QueryFailed(tokens[1].decode("utf-8"), tokens[3].decode("utf-8")[1:])
    elif code == Protocol.ERR_INPUT2:
        raise QueryFailed(tokens[1].decode("utf-8"), tokens[4].decode("utf-8")[1:])

def GetItem(response):
    tokens = response.split()
    del tokens[:3]
    listToStr = ' '.join([str(elem.decode("utf-8")) for elem in tokens])
    return listToStr[1::1][1::1][:-1] 

def GetKeyVal(response):
    tokens = response.split()
    del tokens[:3]
    listToStr = ' '.join([str(elem.decode("utf-8")) for elem in tokens])
    split2 = listToStr[1::1].split()
    key = split2[0]
    split2.pop(0)
    value = ' '.join([str(elem) for elem in split2])
    return key, value
    

def GetVal2(response):
    tokens = response.split()
    CheckFail(tokens[1])
    del tokens[:4]
    listToStr = ' '.join([str(elem.decode("utf-8")) for elem in tokens])
    return listToStr[1::1] 

def GetVal(response):
    tokens = response.split()
    CheckFail(tokens[1])
    del tokens[:3]
    listToStr = ' '.join([str(elem.decode("utf-8")) for elem in tokens])
    return listToStr[1::1][1::1][:-1] 

def GetSimple(response):
    tokens = response.split()
    CheckFail(tokens[1])
    del tokens[:3]

    listToStr = ' '.join([str(elem.decode("utf-8")) for elem in tokens])
    return listToStr[1::1]

def Handle(response):
    tokens = response.split()
    CheckFail(tokens[1])
    return "OK"

def escape(string):
    if string is None:
        return ""
    return '"' + string.replace('"', '\\"').replace('\r\n', ' ') + '"'

class QueryFailed(Exception):
    def __init__(self, code, m):
        self.message = m
        self.code = code
    def __str__(self):
        return self.message