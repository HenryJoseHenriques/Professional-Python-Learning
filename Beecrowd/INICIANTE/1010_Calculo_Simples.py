#https://judge.beecrowd.com/pt/problems/view/1010

codPeca, numPeca, valorPeca = map(float, input().split())
codPeca2, numPeca2, valorPeca2 = map(float, input().split())

total = numPeca*valorPeca + numPeca2*valorPeca2

print(f"VALOR A PAGAR: R$ {total:.2f}")