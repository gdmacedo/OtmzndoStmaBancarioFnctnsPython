''' 
DIO - Digital Innovation One
Author....: Macedo, Glener Diniz - Full Stack Developer
Orientador: Guilherme Carvalho - Python Consultant, Oak Solutions

Sistema...: Otimizando o Sistema Bancário com Funções Python

Módulo....: Inicial do Sistema

Objetivo..: Neste sistema, teremos a oportunidade de otimizar o Sistema Bancário 
            previamente desenvolvido com o uso de funções Python. 
            
            O objetivo é aprimorar a estrutura e a eficiência do sistema, 
            implementando as operações de depósito, saque e extrato em funções específicas. 
            
            Teremos a chance de refatorar o código existente, dividindo-o em funções 
            reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo. 
            
            Prepare-se para aplicar conceitos avançados de programação e demonstrar
            sua habilidade em criar soluções mais elegantes e eficientes utilizando Python.

'''

# Funções Externas
# Esta função fornece o nome do módulo do sistema operacional que ela importa.
# As funções que o módulo OS fornece nos permitem operar em tarefas subjacentes 
# do sistema operacional, independentemente de ser uma plataforma Windows, 
# Macintosh ou Linux. Nesta lição, revisaremos essas funções e o que podemos fazer com elas. 
import os


# Importa do arquivo funcoes.py
from funcoes import *


# Define a função inicial.
def main():

    while True:
        initial_menu()

        opcao = input("=> ")
        limpar_tela()

        if opcao == "1":
            login()

        elif opcao == "2":
            criar_user()

        elif opcao == "3":
            print("Volte sempre!!\n")
            break

        else:
            print("Digite uma opção válida: ")



if __name__ == "__main__":
    main()

