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
        for i in range(4):
            while True:
                try:
                    aviao = int(input(f"Digite o número do {i+1}º Avião."))
                    lista_aviao.append(aviao)
                    os.system("cls")
                    break
                except ValueError:
                    print("Entrada inválida.")
                 
                    time.sleep(1)
                    os.system("cls")
                    continue
    else:
        print("4 aviões já estão cadastrados. Reinicie o programa caso deseje recadastrar.")

def add_assentos(lista_assento, lista_aviao):
    if verificar_lista(lista_aviao):
        print("Ainda não há aviões cadastrados")
    
    if verificar_lista(lista_assento):
        for i in range(4):
            quantidade_assentos = int(input("Digite o número de assentos disponiveis"))


add_avioes(lista_aviao)

            

