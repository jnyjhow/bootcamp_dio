# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:28:41 2024
Modificado em: 13/04/2024

@author: jny_jhow
"""

import datetime

VAR_MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

VAR_LIMITE_SAQUE_VALOR = 500
VAR_LIMITE_SAQUE_QTD = 3

def main():

    lista_transacoes = []
    saldo = 0
    numero_saques = 0

    while True:
        opcao = input(VAR_MENU).lower()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                data_hora = datetime.datetime.now()
                lista_transacoes.append((data_hora, f"Depósito: R$ {valor:.2f}"))
            else:
                print(f"Operação falhou! O valor [{valor}] informado é inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > VAR_LIMITE_SAQUE_VALOR
            excedeu_saques = numero_saques >= VAR_LIMITE_SAQUE_QTD

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print(f"Operação falhou! O valor do saque excede o limite [{VAR_LIMITE_SAQUE_VALOR}].")
            elif excedeu_saques:
                print(f"Operação falhou! Número máximo [{VAR_LIMITE_SAQUE_QTD}] de saques excedido.")
            elif valor > 0:
                saldo -= valor
                data_hora = datetime.datetime.now()
                lista_transacoes.append((data_hora, f"Saque: R$ {valor:.2f}"))
                numero_saques += 1
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            if not lista_transacoes:
                print("Não foram realizadas movimentações.")
            else:
                for data_hora, movimentacao in lista_transacoes:
                    print(f"{data_hora.strftime('%d/%m/%Y %H:%M:%S')} - {movimentacao}")
            print(f"\nSaldo: R$ {saldo:.2f}")
            print(f"==========================================")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == '__main__':
    main()