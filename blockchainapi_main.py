# -*- coding: utf-8 -*-
"""
Created on Thu Feb 9 2017

@author: fukuharakichinosuke
"""
import json
import requests
from blockchainapi_mod import *
from blockchain import blockexplorer

block_hash = "000000000000000000ddb8814de36334778c1762f1a42da5401633d91cbc0d5b"

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

def Main():
    print("*********singleblock*********")
    singleblock_resp = cl01.getsingleBlock(block_hash)
    singleblock_set = cl01.getsingleblockSet(singleblock_resp)
    cl01.printDictvalue(singleblock_set)

    print("*********singletransaction*********")
    singletransactionList = cl02.getsingleTransaction(singleblock_set)
    #for i in range(0,len(singletransactionList)):
    cl02.printDictvalue(singletransactionList[1])

    print("*********inputs*********")
    inputsDict = cl03.getinputsDict(singletransactionList)
    cl03.printDictvalue(inputsDict[0])
    cl03.printDictvalue(inputsDict[1])

    print("*********out*********")
    outDict = cl04.getoutDict(singletransactionList)
    cl04.printDictvalue(outDict[0])
    cl04.printDictvalue(outDict[1])
        
if __name__ == "__main__":
    Main()
