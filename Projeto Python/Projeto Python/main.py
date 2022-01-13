import os
import pandas as pd
import matplotlib as plt
import requests

planilha = pd.read_excel('dados_Covid.xlsx')

print("----------------------------------------------")
print("= DADOS https://www.seade.gov.br/coronavirus/=")
print("----------------------------------------------")
print("=       Dados coletados do site              =")
print("----------------------------------------------")
print("=        1 - Gráfico Total de Casos          =")
print("=        2 - Gráfico Casos por Dia           =")
print("=        3 - Gráfico Óbitos por Dia          =")
print("----------------------------------------------")
opc = int(input("Escolha a opção: "))

if opc == 1:
    # Mostra o gráfico com o Total de Casos
    plt(planilha['TOTAL DE CASOS'])
    plt.show()
    #print(planilha['Total de casos'])
elif opc == 2:
    # Mostra o gráfico com o Total de Casos por Dia
    print(planilha['Casos por dia'])
else:
    # Mostra o gráfico com o Total de Óbitos
    print(planilha['Obitos por dia'])


# Passo a passo de solução

#Abrir o arquivo excel
#lista_estados = ['SP', 'MG', 'PR', 'RS', 'RJ', 'BA', 'SC', 'CE', 'GO', 'PE', 'ES', 'AM', 'DF', 'MA', 'MS', 'PB', 'RN', 'PI', 'RO', 'SE', 'AL', 'TO', 'RR', 'AP', 'AC']

taxa_obitos = pd.read_excel('dados_covid_por_estado.xlsx')

print(taxa_obitos)

# Verificar e pegar o valor total da coluna de taxa de óbitos

os.system("pause")