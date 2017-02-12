class RequestModelResponse():
    
    def getType(resp):
        print("resp : ",type(resp))
        print("cookies : ",type(resp.cookies))
        #print("error : ",type(resp.error))
        print("headers : ",type(resp.headers))
        print("history : ",type(resp.history))
        print("ok : ",type(resp.ok))
        print("raise_for_status : ",type(resp.raise_for_status))
        print("status_code : ",type(resp.status_code))
        print("url : ",type(resp.url))

    def gethistoryList(resp):
        historyList = resp.history

        return historyList
    
    def getStatuscode(resp):
        status_code = resp.status_code

        return status_code


class SingleBlock():
    
##{
##    "hash":"0000000000000bae09a7a393a8acded75aa67e46cb81f7acaa5ad94f9eacd103",
##    "ver":1,
##    "prev_block":"00000000000007d0f98d9edca880a6c124e25095712df8952e0439ac7409738a",
##    "mrkl_root":"935aa0ed2e29a4b81e0c995c39e06995ecce7ddbebb26ed32d550a72e8200bf5",
##    "time":1322131230,
##    "bits":437129626,
##    "nonce":2964215930,
##    "n_tx":22,
##    "size":9195,
##    "block_index":818044,
##    "main_chain":true,
##    "height":154595,
##    "received_time":1322131301,
##    "relayed_by":"108.60.208.156",
##    "tx":[--Array of Transactions--]
##{
    def getsingleBlock(block_hash):
        import requests
        url = "https://blockchain.info/ja/rawblock/" + block_hash
        singleblock_resp = requests.get(url)

        return singleblock_resp

    def getsingleblockSet(singleblock_resp):
        import json
        singleblock_set = json.loads(singleblock_resp.text)
        
        return singleblock_set
        
    def printDictvalue(Dict):

        for k,v in sorted(Dict.items()):
            if k == 'tx' or k == 'inputs' or k == 'out':
                pass
            else:
                print(k,":",v)

    def printListvalue(List):
        for i in range(0,len(List)):
            print(i,":",List[i])
            
                
class SingleTransaction(SingleBlock):

    def getsingleTransaction(singleblock_set):
        singletransactionList = singleblock_set['tx']
        return singletransactionList
    
##{
##    "hash":"b6f6991d03df0e2e04dafffcd6bc418aac66049e2cd74b80f14ac86db1e3f0da",
##    "ver":1,
##    "vin_sz":1,
##    "vout_sz":2,
##    "lock_time":"Unavailable",
##    "size":258,
##    "relayed_by":"64.179.201.80",
##    "block_height, 12200,
##    "tx_index":"12563028",
##    "inputs":[
##
##
##            {
##                "prev_out":{
##                    "hash":"a3e2bcc9a5f776112497a32b05f4b9e5b2405ed9",
##                    "value":"100000000",
##                    "tx_index":"12554260",
##                    "n":"2"
##                },
##                "script":"76a914641ad5051edd97029a003fe9efb29359fcee409d88ac"
##            }
##
##        ],
##    "out":[
##
##                {
##                    "value":"98000000",
##                    "hash":"29d6a3540acfa0a950bef2bfdc75cd51c24390fd",
##                    "script":"76a914641ad5051edd97029a003fe9efb29359fcee409d88ac"
##                },
##
##                {
##                    "value":"2000000",
##                    "hash":"17b5038a413f5c5ee288caa64cfab35a0c01914e",
##                    "script":"76a914641ad5051edd97029a003fe9efb29359fcee409d88ac"
##                }
##
##        ]
##}

class TransactionInputs(SingleTransaction):

    def getinputsDict(singletransactionList):
        inputsDict = singletransactionList[0]['inputs']

        return inputsDict

class TransactionOut(SingleTransaction):

    def getoutDict(singletransactionList):
        outDict = singletransactionList[0]['out']

        return outDict
