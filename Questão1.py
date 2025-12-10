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

def add_or_att_aviao(lista_aviao):
    if verificar_lista(lista_aviao):
        for i in range(4):
            try:
                aviao = int(input(f"Digite o número do {i+1}º Avião."))
                lista_aviao.append(aviao)
                os.ssytem("cls")
            except ValueError:
                print("Entradad inválida. Digite um número inteiro.")

