"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

import decimal

num1 = decimal.Decimal(3.147) #pela biblioteca (impreciso, problema da linguagem)
num2 = decimal.Decimal(9.7854639)
num3 = round(num2) #pelo método