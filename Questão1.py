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
#Caso já haja aviões cadastrados, a função mostra os aviões.
def add_avioes(lista_aviao):
    if verificar_lista(lista_aviao):
        for i in range(4):
            while True:
                try:
                    aviao = int(input(f"Digite o número do {i+1}º Avião.\n"))
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
        print("---lista de aviões disponíveis---")
        for i in lista_aviao():
            print(f"-Avião {lista_aviao[i]}")

def add_assentos(lista_assento, lista_aviao):
    if verificar_lista(lista_aviao):
        print("Ainda não há aviões cadastrados")
    
    elif verificar_lista(lista_assento):
        for i in range(4):
            while True:
                try:
                    quantidade_assentos = int(input(f"Digite o número de assentos disponiveis no avião {lista_aviao[i]}\n"))
                    lista_assento.append(quantidade_assentos)
                    os.system("cls")
                    break
                except ValueError:
                    print("Entrada inválida.")
                    time.sleep(1)
                    os.system("cls")
                    continue
    
    else:
        print("Quantidade de assentos em cada avião já cadastrada. Reinicie o programa caso queira recadastrar.")
        print("---Lista de assentos disponíves")
        for i in range(4):
            print(f"-Avião: {lista_aviao[i]}")
            print(f"Número de assentos disponíveis: {lista_assento[i]}\n\n")



            




            

