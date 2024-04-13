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


def obter_valor(tipo='depósito'):
    while True:
        valor_str = input(f"Informe o valor do {tipo}: ").replace(',', '.')
        if valor_str.replace('.', '', 1).isdigit():
            return float(valor_str)
        else:
            print(f"Valor inválido! Por favor, informe um número válido para {tipo}.")


def main():

    lista_transacoes = []

    while True:
        opcao = input(VAR_MENU).lower()

        if opcao == "d":
            valor = obter_valor()
            if valor > 0:
                data_hora = datetime.datetime.now()
                lista_transacoes.append((data_hora, "Depósito", valor))
            else:
                print(f"Operação falhou! O valor [{valor}] informado é inválido.")

        elif opcao == "s":
            valor = obter_valor('saque')

            saldo_atual = sum(valor for _, _, valor in lista_transacoes)
            numero_saques = sum(1 for _, tipo, _ in lista_transacoes if tipo == "Saque")

            excedeu_limite = valor > VAR_LIMITE_SAQUE_VALOR
            excedeu_saques = numero_saques >= VAR_LIMITE_SAQUE_QTD

            if valor > saldo_atual:
                print(f"Operação falhou! Você não tem saldo [{valor}] suficiente.")
            elif excedeu_limite:
                print(f"Operação falhou! O valor do saque excede o limite [{VAR_LIMITE_SAQUE_VALOR}].")
            elif excedeu_saques:
                print(f"Operação falhou! Número máximo [{VAR_LIMITE_SAQUE_QTD}] de saques excedido.")
            elif valor > 0:
                data_hora = datetime.datetime.now()
                lista_transacoes.append((data_hora, "Saque", -valor))
                numero_saques += 1
            else:
                print(f"Operação falhou! O valor [{valor}] informado é inválido!")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            if not lista_transacoes:
                print("Não foram realizadas movimentações.")
            else:
                saldo_atual = 0
                for data_hora, tipo, valor in lista_transacoes:
                    saldo_atual += valor
                    print(f"{data_hora.strftime('%d/%m/%Y %H:%M:%S')} - {tipo}: R$ {abs(valor):.2f}")
                print(f"\nSaldo: R$ {saldo_atual:.2f}")
            print(f"==========================================")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == '__main__':
    main()