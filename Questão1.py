import os 
os.system("cls")
from dataclasses import dataclass
import time

lista_aviao = []
lista_assentos = []
lista_reservas = []

@dataclass
class Reserva:
    numero_aviao: str
    nome_passageiro: str
    
    def mostrar_reserva(self):
        print(f"Encontrada reserva para avião nº {self.numero_aviao}")



def verificar_lista(lista):
    if not lista:
        return True
    return False

#Função para adicionar 4 aviões, feita de modo que ela só aceite números e peça novamente caso a pessoa digite um valor inválido
def add_avioes(lista_aviao):
    if verificar_lista(lista_aviao):
        contador = 0
        for i in range(4):
            try:
                aviao = int(input(f"Digite o número do {i+1}º Avião."))
                lista_aviao.append(aviao)
                os.system("cls")
            except ValueError:
                print("Entrada inválida.")
                contador += 1 
                time.sleep(1)
                os.system("cls")
                continue
    if contador > 0:
        print("houveram 1 ou mais aviões inválidos.")
        while True:
            try:
                for i in range(contador):
                    aviao = int(input("Digite o número do avião inválido novamente."))
                    lista_aviao.append(aviao)
                    contador = contador - 1
                    os.system("cls")
            except ValueError:
                print("Entrada inválida.")
                time.sleep(1)
                os.system("cls")
                continue
            if contador == 0:
                break



add_avioes(lista_aviao)

print(f"{lista_aviao}")


            

