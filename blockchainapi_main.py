# -*- coding: utf-8 -*-
"""
Created on Thu Feb 9 2017

@author: fukuharakichinosuke
"""
import json
import sys
import requests
from blockchainapi_mod import *
from blockchain import blockexplorer

block_hash = str(sys.argv[1])

cl00 = RequestModelResponse # RequestModelResponse class
cl01 = SingleBlock # SingleBlocke class
cl02 = SingleTransaction # SingleTransaction class
cl03 = TransactionInputs # TransactionInputs class
cl04 = TransactionOut # TransactionOut class

##def checkType(resp):
##
##    print("*********RequestModelResponese type*********")
##    class_00.getType(resp)
##    print("*********RequestModelResponese.history*********")
##    historyList = class_00.gethistoryList(resp)
##    print(historyList)
##    print("*********RequestModelResponese.status_code*********")
##    status_code = class_00.getStatuscode(resp)
##    print(status_code)
##    class_00.printListvalue(historyList)
##
##checkType(resp)

def Main(block_hash):
    print("*********singleblock*********")
    singleblock_resp = cl01.getsingleBlock(block_hash)
    singleblock_set = cl01.getsingleblockSet(singleblock_resp)
    cl01.printDictvalue(singleblock_set)

    print("*********singletransaction*********")
    singletransactionList = cl02.getsingleTransaction(singleblock_set)
    #for i in range(0,len(singletransactionList)):
    #    cl02.printDictvalue(singletransactionList[i])
    cl02.printDictvalue(singletransactionList[0])
    print("*********inputs*********")
    inputsDict = cl03.getinputsDict(singletransactionList)
    for i in range(len(inputsDict)):
        cl03.printDictvalue(inputsDict[i])

    print("*********out*********")
    outDict = cl04.getoutDict(singletransactionList)
    for i in range(len(outDict)):
        cl04.printDictvalue(outDict[i])
        
if __name__ == "__main__":
    Main(block_hash)
