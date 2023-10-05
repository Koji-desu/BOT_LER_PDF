# Import for the Desktop BOT
import pathlib

from botcity.document_processing import *
import pathlib
import pandas as pd

dados = []

def lerPDF(arquivo):
    reader = PDFReader()
    parser = reader.read_file(arquivo)
    _bill_to = parser.get_first_entry("Bill to:")
    value_bill_to = parser.read(_bill_to, 1.148148, -1.916667, 6.296296, 4)
    _contact = parser.get_first_entry("Contact:")
    value_contact = parser.read(_contact, 1.171053, -1.166667, 5.710526, 3.75)
    _balance_due = parser.get_first_entry("Balance due:")
    value_balance_due = parser.read(_balance_due, 1.093333, -2, 1.813333, 4.142857)
    _date = parser.get_first_entry("Date:")
    value_date = parser.read(_date, 1.4, -1.416667, 3.2, 3)
    print('Date: ' + value_date)
    print('Contact: ' + value_contact)
    print('Bill To: ' + value_bill_to)
    print('Balance Due: '+ value_balance_due)

    dados.append([value_date, value_contact, value_bill_to, value_balance_due])


arquivos = pathlib.Path(r"C:\Users\Administrator\PycharmProjects\PythonBOTS\lerPDF\docs\docs").glob('*.pdf')

for arquivo in arquivos:
    lerPDF(arquivo)

df = pd.DataFrame(dados, columns=['Date', 'Contact', 'Bill to','Balance due'])
df.to_csv('dados_pdf.csv', sep=',', index=False)