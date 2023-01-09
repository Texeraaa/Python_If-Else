import math
import os
import random
import re
import sys



if __name__ == '__main__':
    i = 1

    def verifica_par(n):
        if n % 2 == 0:
            return True
        else:
            return False

    def verifica_notweird(n):
        if n in range(2,6):
            return True
        else:
            return False

    def verifica_weird(n):
        if n in range(6,21) and n % 2 == 0:
            return True
        else:
            return False

    while(i <= 24):
        n = int(input().strip())
        print(i)

        if verifica_weird(n):
            print("Weird")
        elif verifica_par(n) or verifica_notweird(n):
            print("Not Weird")
        elif not verifica_par(n):
            print("Weird")
        elif verifica_par(n > 20):
            print("Not Weird")

        if(n):
            i += 1

#Se for ímpar, imprima Weird
#Se for par e estiver no intervalo inclusivo de 2 to 5, imprima Not Weird
#Se for par e estiver no intervalo inclusivo de 6 to 20, imprima Weird
#Se for par e maior que 20, imprima Not Weird