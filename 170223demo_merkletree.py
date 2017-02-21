# -*- coding: utf-8 -*-
"""
Created on Thu Feb 9 2017

@author: fukuharakichinosuke
"""
import json
import sys
import requests
import math
import numpy as np
from blockchainapi_mod import *
from blockchain import blockexplorer

block_hash = str(sys.argv[1])

cl00 = RequestModelResponse # RequestModelResponse class
cl01 = SingleBlock # SingleBlocke class
cl02 = SingleTransaction # SingleTransaction class
cl03 = TransactionInputs # TransactionInputs class
cl04 = TransactionOut # TransactionOut class
cl05 = TransactionHashes # TransactionHashes class
cl06 = MerkleTree # MerkleTree class

def Main(block_hash):

    singleblock_resp = cl01.getsingleBlock(block_hash)
    singleblock_set = cl01.getsingleblockSet(singleblock_resp)
    singletransactionList = cl02.getsingleTransaction(singleblock_set)
    print("transactionList length:",len(singletransactionList))
    hashList = []
    for i in range(len(singletransactionList)):
        singletransactionDict = singletransactionList[i]
        v = singletransactionDict['hash']
        hashList.append(v.encode('utf-8'))
    sub_t = cl06.m_tree1(hashList)
    while len(sub_t) > 1:
        print(len(sub_t))
        sub_t = cl06.m_tree2(sub_t)
    print(sub_t)

if __name__ == "__main__":
    Main(block_hash)
