"""
f-strings
.<número de digitos>f
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal + - ou -
Ex. : O>-100,.1f
Conversion flags - !r !s !a
"""

var = 'ABCD'
print(f"{var: >10}")
print(f"{var: <10}")
print(f"{var: ^10}")
print(f"{189.123654896:+,.1f}")

