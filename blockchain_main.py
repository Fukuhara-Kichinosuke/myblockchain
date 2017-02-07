# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 2017

@author: fukuharakichinosuke
"""
from blockchain_mod import blockDict
from blockchain import blockexplorer

class_00 = blockDict # blockDict class

def Main():

    print("***block data components***")
    hashValue = '000000000000000016f9a2c3e0f4c1245ff24856a79c34806969f5084f410680'
    blockDict = class_00.getBlockDict(hashValue)
    class_00.printDictvalue(blockDict)

    print("***transaction data components***")
    transactionDict = class_00.getTransactionDict(blockDict['transactions'])
    class_00.printDictvalue(transactionDict)

    print("***transaction output data***")
    outputDict = class_00.getOutputDict(transactionDict['outputs'])
    class_00.printDictvalue(outputDict)    

    print("***address data components***")
    address = blockexplorer.get_address('1HS9RLmKvJ7D1ZYgfPExJZQZA1DMU3DEVd')
    addressDict = class_00.getAddressDict(address)
    class_00.printDictvalue(addressDict)

    print("***unspentoutputs data components***")
    outs = blockexplorer.get_unspent_outputs('1HS9RLmKvJ7D1ZYgfPExJZQZA1DMU3DEVd')
    unspentoutputDict = class_00.getUnspentoutputsDict(outs[0])
    class_00.printDictvalue(unspentoutputDict)

if __name__ == "__main__":
    Main()
