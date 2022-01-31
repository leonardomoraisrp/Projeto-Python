import os
from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt

class PDF(FPDF):
    def header(self):
        self.image("Logo_kick.png", 10, 8, 33)

        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(
            30, 10, 'PROJETO PYTHON #KICK', 0, 0, 'C')
        
        self.ln(10)
        self.line(75, 20, 135, 20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# ABRINDO PLANILHA ABAIXO
dadosEstado = pd.read_excel(r'C:\Users\Note\Desktop\Projeto Python\Dados-covid-19-estado.xlsx')
# print(dadosEstado)

pdf = PDF()
pdf.add_page()
texto_1 = 'CONSEQUÊNCIAS DA PANDEMIA: CRIANÇAS ÓRFÃS .'
pdf.image(name='grafico_01.png', x=50, y=50, w=100, h=55)
pdf.image(name='grafico_02.png', x=50, y=120, w=100, h=55)
pdf.image(name='grafico_03.png', x=50, y=190, w=100, h=55)

pdf.cell(w=0, h=30, txt=texto_1, align='C')
pdf.set_font('Times', '', 30)

# TEXTO
pdf.add_page()
pdf.set_font('Times', '', 15)
pdf.image(name='covid-19.png', x=83, y=220, w=50)
pdf.set_margins(10, 40, 0)
texto = "A situação de vulnerabilidade das crianças que perderam os pais ou resposáveis na pandemia e como sucedem os fatos após o trágico evento.\n\nOs números de óbito foram coletados do site e através dele conseguimos mensurar (por projeção) quantas crianças perderam seus responsáveis. https://www.seade.gov.br/coronavirus/# . A covid-2019 deixou cerca de mais de 130 mil crianças de até 17 anos em situação de desamparo e vulnerabilidade social. \n\nÉ esperado que as crianças afetadas recebessem do Congresso Nacional algum fundo coletivo de qual seria proposto um sistema de pensões para ajuda-las em seu momento de fragilidade financeira, econômica e psicossocial com incentivos ao CAPS (Centro de Atenção Psicossocial)\n\n\n\n\n\n\nNome: Leonardo Morais\nTurma: B."

pdf.multi_cell(w=185, h=8, txt=texto, align='J')
pdf.output('relatorio.pdf', 'F')

# PEGANDO INFORMAÇÕES DA COLUNA
totalDeCasos = dadosEstado["Total de casos"]
casosDia = dadosEstado["Casos por dia"]
obitosDia = dadosEstado["Óbitos por dia"]

# Gráfico Total de Casos
plt.plot(totalDeCasos, '--')
plt.xlabel('Total de casos')
plt.savefig("grafico_01.png")
plt.close()

# Gráfico Casos por dia
#pdf.multi_cell(w=0, h=8, txt="Grafico Total de Casos no estado de São Paulo", ln=1, align='C')
#pdf.image(x=20, y=30, w=180, h=80, name='grafico_01.png')
#plt.plot(casosDia)
#plt.xlabel('Casos por dia')
#plt.savefig("grafico_02.png")
#plt.close()

# Gráfico Obitos por dia
#pdf.multi_cell(w=0, h=230, txt="Grafico de Casos por Dia no estado de São Paulo", ln=1, align='C')
#pdf.image(x=20, y=140, w=180, h=80, name='grafico_02.png')
#plt.plot(obitosDia)
#plt.xlabel('Obitos por dia')
#plt.savefig("grafico_03.png")
#plt.close()

#pdf.multi_cell(w=0, h=30, txt="Grafico Óbitos por Dia no estado de São Paulo", ln=1, align='C')
#pdf.image(x=20, y=50, w=180, h=80, name='grafico_03.png')
#pdf.output('relatorio.pdf')

os.system("pause")