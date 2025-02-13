
"""
Empacotamento e desempacotamento de dicionários
"""

pokedex_data = {
    'National' : 3,
    'Type' : 'Grass/Poison',
    'Species' : 'Seed Pokemon',
    'Height ' : 2.0,
    'Weight' : 100,
    'Abilities' : 'Overgrow/Chlorophyll'
}

base_stats = {
    'HP' : 80,
    'Attack' : 82,
    'Defense' : 83,
    'Sp.Atk' : 100,
    'Sp.Def': 100,
    'Speed' : 80
}

venusaur_info = {**pokedex_data,  **base_stats}

#Exemplo de desempacotamento

# for etiqueta, info in venusaur_info.items():
#     print(etiqueta, info)

#print(venusaur_info)


def InfoPKM(*args, **kwargs):
    print(f"Não nomeados: {args} ")
    print()
    print()
    print("Nomeados:")
    for etiqueta, info in kwargs.items():
        print(etiqueta, info)

Treinador = "Henry José"

InfoPKM(**venusaur_info)