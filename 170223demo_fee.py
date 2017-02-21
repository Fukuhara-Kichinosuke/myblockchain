def calculateDifficulty(difficuty):
    print("")

def calculateFee(fee):
    value = fee/10000
    print('BTC:',value)
    print('satoshi:',fee)


import sys
fee = int(sys.argv[1])
calculateFee(fee)
