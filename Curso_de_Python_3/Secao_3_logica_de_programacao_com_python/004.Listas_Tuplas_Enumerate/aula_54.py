
import os

listaDeCompras = []
while True:
    print("Selecione uma opção:")
    opcao = input("[i]nserir [a]pagar [l]istar: ").lower()

    if opcao == "i":
        os.system("cls")
        item = input("Digite o item que deseja inserir:")
        listaDeCompras.append(item)
    elif opcao == "a":
        os.system("cls")
        if listaDeCompras == []:
                print("Lista vázia")
                continue
        item = input("Digite o índice do item que deseja apagar:")
        try:
            item_int = int(item)
            del listaDeCompras[item_int]
        except ValueError:
            print("Erro. Entrada inválida")
            continue
        except IndexError:
            print("Erro. índice não existe na lista")
            continue
        except Exception:
            print("Erro desconhecido")
    
    elif opcao == "l":
            os.system("cls")
            listaDeComprasEnumerate = enumerate(listaDeCompras)
            if listaDeCompras == []:
                print("Lista vázia")
                continue
            for item in listaDeComprasEnumerate:
                print(item)
    else:
        os.system("cls")
        print("Por favor, digite uma opção válida")
        continue