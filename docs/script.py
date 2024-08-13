from flask import Flask, render_template
import pandas as pandas
import numpy

app = Flask('testapp', template_folder='docs', static_folder='docs\styles')
num = 3

@app.route('/')
def home():
    
    return render_template('index.html') 

@app.route('/projects')
def projects():

    def ReadOnboard(OnboardFile, line, cell):
        Data=pandas.read_excel(OnboardFile,sheet_name='Sheet1',engine='openpyxl')
        Data=Data.replace(numpy.nan,'End',regex=True)
        List=Data.values.tolist()
        return(List[line][cell])
    
    title = ReadOnboard('docs\\Book1.xlsx', num-1, 0)
    littleTitle = ReadOnboard('docs\\Book1.xlsx', num-1, 1)
    littleBlurb = ReadOnboard('docs\\Book1.xlsx', num-1, 2)
    bigBlurb = ReadOnboard('docs\\Book1.xlsx', num-1, 3)
    impressiveNumber1 = ReadOnboard('docs\\Book1.xlsx', num-1, 4)
    
    return render_template('Other Test.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, impressiveNumber1=impressiveNumber1)  

    
       

if __name__ == '__main__':
    app.run()