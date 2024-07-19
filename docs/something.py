import pandas as pandas
import numpy

print('hello')

def ReadOnboard(OnboardFile, line, cell):
    Data=pandas.read_excel(OnboardFile,sheet_name='Sheet1',engine='openpyxl')
    Data=Data.replace(numpy.nan,'End',regex=True)
    List=Data.values.tolist()
    return(List[line][cell])

print('hello')
print(ReadOnboard('docs\\Book1.xlsx', 1, 2))