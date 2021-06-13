import random

def lineal_search (list, objetive):
    match = False

    for element in list: # O(n) lineal_search
        if element == objetive:
            match = True
            break
    return match

if __name__ == '__main__':
    list_size = int(input('¿De que tamaño será tu lista?: '))
    objetive = int(input('¿Que número quieres encontrar?: '))

    list = [random.randint(0,100) for i in range(list_size)]

    finded = lineal_search (list, objetive)
    print(list)
    print(f'El elemento {objetive} {"está" if finded else "no está"} en la lista ')