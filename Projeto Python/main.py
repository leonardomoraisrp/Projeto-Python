import os
from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt

# GERANDO PDF
pdf = FPDF('p', 'mm', 'A4')
pdf.add_page()
pdf.set_font('arial', '', 16)

# ABRINDO PLANILHA ABAIXO
dadosEstado = pd.read_excel(r'C:\Users\Note\Desktop\Projeto Python\Dados-covid-19-estado.xlsx')
# print(dadosEstado)

# PEGANDO INFORMAÇÕES DA COLUNA
totalDeCasos = dadosEstado["Total de casos"]
casosDia = dadosEstado["Casos por dia"]
obitosDia = dadosEstado["Óbitos por dia"]

plt.plot(totalDeCasos, '--')
plt.xlabel('Total de casos')
plt.savefig("grafico_01.png")
plt.close()

pdf.multi_cell(w=0, h=8, txt="Grafico Total de Casos no estado de São Paulo", ln=1, align='C')
pdf.image(x=20, y=30, w=180, h=80, name='exemplo.png')
plt.plot(casosDia)
plt.xlabel('Casos por dia')
plt.savefig("grafico_02.png")
plt.close()
pdf.multi_cell(w=0, h=230, txt="Grafico de Casos por Dia no estado de São Paulo", ln=1, align='C')
pdf.image(x=20, y=140, w=180, h=80, name='exemplo2.png')
plt.plot(obitosDia)
plt.xlabel('Obitos por dia')
plt.savefig("grafico_03.png")
plt.close()
pdf.multi_cell(w=0, h=30, txt="Grafico Óbitos por Dia no estado de São Paulo", ln=1, align='C')
pdf.image(x=20, y=50, w=180, h=80, name='exemplo3.png')
pdf.output('relatorio.pdf')

os.system("pause")