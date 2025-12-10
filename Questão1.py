import os 
os.system("cls")
from dataclasses import dataclass
import time

lista_aviao = []
lista_assentos = []
lista_reservas = []

@dataclass
class Reserva:
    numero_aviao: int
    nome_passageiro: str
    
    def mostrar_reserva_aviao(self):
        print(f"Encontrada reserva para avião nº {self.numero_aviao}\n")
    
    def mostrar_reserva_passageiro(self):
        print(f"-Nome: {self.nome_passageiro}\n ")



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


def buscar_aviao(lista_aviao,numero_buscar):
    for aviao in lista_aviao:
        if aviao == numero_buscar:
            return aviao
    return None

def buscar_numero_aviao(lista_reservas,numero_buscar):
    for aviao in lista_reservas:
        if aviao.numero_aviao == numero_buscar:
            return aviao
    return None

def buscar_passageiro(lista_reservas, nome_buscar):
    nome_lower = nome_buscar.lower()
    for passageiro in lista_reservas:
        if passageiro.nome_passageiro.lower() == nome_lower:
            return passageiro
    return None




def reservar_passagem(lista_aviao, lista_assento, lista_reservas):
    if verificar_lista(lista_aviao):
        print("Não há aviões cadastrados.")
        return
    if verificar_lista(lista_assento):
        print("Não há assentos cadastrados.")
        return
    while True:
        try:
            numero_busca = int(input("Digite o número do Avião no qual você deseja fazer uma reserva"))
            break
        except ValueError:
            print("valor inválido")
            time.sleep(1)
            os.system("cls")
            continue

    numero_aviao = buscar_aviao(lista_aviao, numero_busca)
    if numero_aviao:
        indice = lista_aviao.index(numero_aviao)
        if lista_reservas.numero_aviao.count(numero_aviao) == 20:
            print("Você atingiu o limite de reservas neste avião")
        else: 
            print("Não há avião cadastrado com esse número.")
            return
    quantidade_assentos = lista_assento.index(indice)

    if quantidade_assentos == 0:
        print("Não há assentos disponívies para esse avião.")
    else:
        reserva = Reserva(nome_passageiro= input("Digite o nome do passageiro.\n"),
                              numero_aviao= numero_busca)
        lista_reservas.append(reserva)
        quantidade_assentos -= 1
        lista_assento.index(indice = quantidade_assentos)
        print("Reserva realizada com sucesso.")

def consulta_aviao(lista_aviao,lista_reservas):
    if verificar_lista(lista_aviao):
        print("Não há aviões cadastrados.")
        return
    if verificar_lista(lista_reservas):
        print("Não há reservas cadastradas.")
        return
    
    while True:
        try:
            numero_busca = int(input("Digite o número do Avião no qual você deseja fazer uma reserva"))
            break
        except ValueError:
            print("valor inválido")
            time.sleep(1)
            os.system("cls")
            continue
    
    confirm = buscar_aviao(lista_aviao , numero_busca)

    if confirm:

        numero_aviao = buscar_numero_aviao(lista_reservas=lista_reservas,numero_buscar= numero_busca)

        if numero_aviao:
            print("Os seguintes passageiros têm reserva neste avião:\n")
            for aviao in lista_reservas:
                if aviao.numero_aviao == numero_aviao:
                    aviao.mostrar_reserva_passageiro()
        else:
            print("Não há reservas para este avião..")
    else:
        print("Avião não encontrado.") 






    
    


            





            

