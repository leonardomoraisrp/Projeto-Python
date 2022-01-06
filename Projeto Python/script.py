import os, openpyxl, pandas
from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Black')
layout = [
    [sg.Text('PORMENORES DA PANDEMIA - CRIANÇAS ÓRFÃS')],
    [sg.Text('Gráfico - Taxa de Óbitos')],
    ]

# Janela
janela = sg.Window('Trabalho de Python', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break