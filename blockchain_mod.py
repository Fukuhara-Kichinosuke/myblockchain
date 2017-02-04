# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 2017

@author: fukuharakichinosuke
"""
from blockchain import blockexplorer

class blockDict():

    def getBlockDict(blockIndex):
        block = blockexplorer.get_block(blockIndex)
        Hash = block.hash
        version = block.version
        previous_block = block.previous_block
        merkle_root = block.merkle_root
        time = block.time
        bits = block.bits
        fee = block.fee
        nonce = block.nonce
        n_tx = block.n_tx
        size = block.size
        block_index = block.block_index
        main_chain = block.main_chain
        height = block.height
        received_time = block.received_time
        relayed_by = block.relayed_by
        transactions = block.transactions[0]
    
        blockDict = {
            "hash" : Hash,
            "version" : version,
            "previous_block" : previous_block,
            "merkle_root" : merkle_root,
            "time" : time,
            "bits" : bits,
            "fee" : fee,
            "nonce" : nonce,
            "n_tx" : n_tx,
            "size" : size,
            "block_index" : block_index,
            "main_chain" : main_chain,
            "height" : height,
            "received_time" : received_time,
            "relayed_by" : relayed_by,
            "transactions" : transactions
            }
            
        return blockDict
            
    def getTransactionDict(transactions):
        double_spend = transactions.double_spend #bool
        block_height = transactions.block_height#int (if -1, the tx is unconfirmed)
        time = transactions.time#int
        relayed_by = transactions.relayed_by #str
        Hash = transactions.hash#str
        tx_index = transactions.tx_index#int
        version = transactions.version#int
        size = transactions.size#int
        inputs = transactions.inputs[0]#array of Input objects
        outputs = transactions.outputs[0]#array of Output objects
        
        transactionDict = {
        
            "double_spend":double_spend,
            "block_height" : block_height,
            "time" : time,
            "relayed_by" : relayed_by,
            "hash" : Hash,
            "tx_index" : tx_index,
            "version" : version,
            "size" : size,
            "inputs" : inputs,
            "outputs" : outputs
            
            }

        return transactionDict

    def getInputDict(inputs):
        
        n = inputs.n #int
        value = inputs.value #int
        address = inputs.address #str
        tx_index = inputs.tx_index #int
        Type = inputs.type #int
        script = inputs.script #str
        script_sig = inputs.str #str
        sequence = inputs.sequence
        
        inputDict = {
        
            "n" : n,
            "value" : value,
            "address" : address,
            "tx_index" : tx_index,
            "type" : Type,
            "script" : script,
            "script_sig" : script_sig,
            "sequence" : sequence
            
            }

        return inputDict

    def getOutputDict(outputs):
        
        n = outputs.n #int
        value = outputs.value #int
        address = outputs.address #str
        tx_index = outputs.tx_index #int
        script = outputs.script #str
        spent = outputs.spent #bool
        
        outputDict = {
        
            "n" : n,
            "value" : value,
            "address" : address,
            "tx_index" : tx_index,
            "script" : script,
            "spent" : spent
            
            }

        return outputDict

    def getAddressDict(address):
    
        hash160 = address.hash160 #str
        address = address.address #str
##        n_tx = address.n_tx #int
##        total_received = address.total_received #int
##        total_sent = address.total_sent #int
##        final_balance = address.final_balance #int
        transactions = address #array of Transaction objects

        addressDict = {
            "hash160" : hash160,
            "address" : address,
##            "n_tx" : n_tx,
##            "total_received" : total_received,
##            "total_sent" : total_sent,
##            "final_balance" : final_balance,
            "transactions" : transactions,
            }

        return addressDict

    def getUnspentoutputsDict(outs):
        tx_hash = outs.tx_hash
        tx_index = outs.tx_index
        tx_output_n = outs.tx_output_n
        script = outs.script
        value = outs.value
        value_hex = outs.value_hex
        confirmations = outs.confirmations

        unspentOutputDict = {
            "tx_hash" : tx_hash,
            "tx_index" : tx_index,
            "tx_output_n" : tx_output_n,
            "script" : script,
            "value" : value,
            "value_hex" : value_hex,
            "confirmations" : confirmations,
            }

        return unspentOutputDict

    def getLatestBlockDict():
        hash = LatestBlock.hash #str
        time = LatestBlock.time #int
        block_index = LatestBlock.block_index #int
        height = LatestBlock.height #int
        tx_indexes = LatestBlock.height #array of TX indexes (intergers)

        latestBlockDict = {}
            
    
    def printDictvalue(Dict):
        for i in Dict:
            print(i,":",Dict[i])
