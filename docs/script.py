from flask import Flask, render_template
import pandas as pandas
import numpy

app = Flask('testapp', template_folder='docs', static_folder='docs\static')
num = 0

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
    
    electricalBlurb = ReadOnboard('docs\\Book1.xlsx', 0, 2)
    electricalImage=ReadOnboard('docs\\Book1.xlsx', 0, 4)
    mechanicalBlurb = ReadOnboard('docs\\Book1.xlsx', 1, 2)
    mechanicalImage = ReadOnboard('docs\\Book1.xlsx', 1, 4)
    programmingBlurb = ReadOnboard('docs\\Book1.xlsx', 2, 2)
    programmingImage = ReadOnboard('docs\\Book1.xlsx', 2, 4)
    businessBlurb = ReadOnboard('docs\\Book1.xlsx', 3, 2)
    businessImage = ReadOnboard('docs\\Book1.xlsx', 3, 4)
    
    return render_template('projects-grid.html', electricalBlurb=electricalBlurb, 
    electricalImage=electricalImage,
                           mechanicalBlurb=mechanicalBlurb, 
                           mechanicalImage=mechanicalImage,
                           programmingBlurb=programmingBlurb, 
                           programmingImage=programmingImage,
                           businessBlurb=businessBlurb,
                           businessImage=businessImage)  

@app.route('/projects/electrical')
def electrical():
    num = 0

    def ReadOnboard(OnboardFile, line, cell):
        Data=pandas.read_excel(OnboardFile,sheet_name='Sheet1',engine='openpyxl')
        Data=Data.replace(numpy.nan,'End',regex=True)
        List=Data.values.tolist()
        return(List[line][cell])
    
    title = ReadOnboard('docs\\Book1.xlsx', num, 0)
    littleTitle = ReadOnboard('docs\\Book1.xlsx', num, 1)
    littleBlurb = ReadOnboard('docs\\Book1.xlsx', num, 2)
    bigBlurb = ReadOnboard('docs\\Book1.xlsx', num, 3)
    impressiveNumber1 = ReadOnboard('docs\\Book1.xlsx', num, 4)
    
    return render_template('Other Test.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, impressiveNumber1=impressiveNumber1)  

@app.route('/projects/mechanical')
def mechanical():
    num = 1

    def ReadOnboard(OnboardFile, line, cell):
        Data=pandas.read_excel(OnboardFile,sheet_name='Sheet1',engine='openpyxl')
        Data=Data.replace(numpy.nan,'End',regex=True)
        List=Data.values.tolist()
        return(List[line][cell])
    
    title = ReadOnboard('docs\\Book1.xlsx', num, 0)
    littleTitle = ReadOnboard('docs\\Book1.xlsx', num, 1)
    littleBlurb = ReadOnboard('docs\\Book1.xlsx', num, 2)
    bigBlurb = ReadOnboard('docs\\Book1.xlsx', num, 3)
    impressiveNumber1 = ReadOnboard('docs\\Book1.xlsx', num, 4)
    
    return render_template('Other Test.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, impressiveNumber1=impressiveNumber1)  

@app.route('/projects/programming')
def programming():
    num = 2

    def ReadOnboard(OnboardFile, line, cell):
        Data=pandas.read_excel(OnboardFile,sheet_name='Sheet1',engine='openpyxl')
        Data=Data.replace(numpy.nan,'End',regex=True)
        List=Data.values.tolist()
        return(List[line][cell])
    
    title = ReadOnboard('docs\\Book1.xlsx', num, 0)
    littleTitle = ReadOnboard('docs\\Book1.xlsx', num, 1)
    littleBlurb = ReadOnboard('docs\\Book1.xlsx', num, 2)
    bigBlurb = ReadOnboard('docs\\Book1.xlsx', num, 3)
    impressiveNumber1 = ReadOnboard('docs\\Book1.xlsx', num, 4)
    
    return render_template('Other Test.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, impressiveNumber1=impressiveNumber1)  

@app.route('/projects/marketing')
def marketing():
    num = 3

    def ReadOnboard(OnboardFile, line, cell):
        Data=pandas.read_excel(OnboardFile,sheet_name='Sheet1',engine='openpyxl')
        Data=Data.replace(numpy.nan,'End',regex=True)
        List=Data.values.tolist()
        return(List[line][cell])
    
    title = ReadOnboard('docs\\Book1.xlsx', num, 0)
    littleTitle = ReadOnboard('docs\\Book1.xlsx', num, 1)
    littleBlurb = ReadOnboard('docs\\Book1.xlsx', num, 2)
    bigBlurb = ReadOnboard('docs\\Book1.xlsx', num, 3)
    impressiveNumber1 = ReadOnboard('docs\\Book1.xlsx', num, 4)
    
    return render_template('Other Test.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, impressiveNumber1=impressiveNumber1)  

    
       

if __name__ == '__main__':
    app.run()