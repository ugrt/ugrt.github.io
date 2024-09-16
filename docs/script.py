from flask import Flask, render_template
import pandas as pandas
import numpy

app = Flask('testapp', template_folder='docs', static_folder='docs\static')
num = 0
sheet = ""
excelPath = 'docs\\Projects-Information.xlsx' #This allows us to change the path of the excel if we need to

# For this we can easily add more functions. This method simplifies the url and removes the html tag at the end (I personally hate it)

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/projects')
def projects():

    def ReadOnboard(OnboardFile, line, cell):
        Data=pandas.read_excel(OnboardFile,sheet_name='Projects',engine='openpyxl')
        Data=Data.replace(numpy.nan,'End',regex=True)
        List=Data.values.tolist()
        return(List[line][cell])
    
    electricalBlurb = ReadOnboard(excelPath, 0, 2)
    electricalImage=ReadOnboard(excelPath, 0, 4)
    mechanicalBlurb = ReadOnboard(excelPath, 1, 2)
    mechanicalImage = ReadOnboard(excelPath, 1, 4)
    programmingBlurb = ReadOnboard(excelPath, 2, 2)
    programmingImage = ReadOnboard(excelPath, 2, 4)
    businessBlurb = ReadOnboard(excelPath, 3, 2)
    businessImage = ReadOnboard(excelPath, 3, 4)
    
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
        Data=pandas.read_excel(OnboardFile,sheet_name='Projects',engine='openpyxl')
        Data=Data.replace(numpy.nan,'End',regex=True)
        List=Data.values.tolist()
        return(List[line][cell])
    
    title = ReadOnboard(excelPath, num, 0)
    littleTitle = ReadOnboard(excelPath, num, 1)
    littleBlurb = ReadOnboard(excelPath, num, 2)
    bigBlurb = ReadOnboard(excelPath, num, 3)
    impressiveNumber1 = ReadOnboard(excelPath, num, 4)
    
    return render_template('Projects Template.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, impressiveNumber1=impressiveNumber1)  

@app.route('/projects/mechanical')
def mechanical():
    num = 1

    def ReadOnboard(OnboardFile, line, cell):
        Data=pandas.read_excel(OnboardFile,sheet_name='Projects',engine='openpyxl')
        Data=Data.replace(numpy.nan,'End',regex=True)
        List=Data.values.tolist()
        return(List[line][cell])
    
    title = ReadOnboard(excelPath, num, 0)
    littleTitle = ReadOnboard(excelPath, num, 1)
    littleBlurb = ReadOnboard(excelPath, num, 2)
    bigBlurb = ReadOnboard(excelPath, num, 3)
    impressiveNumber1 = ReadOnboard(excelPath, num, 4)
    
    return render_template('Projects Template.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, impressiveNumber1=impressiveNumber1)  

@app.route('/projects/programming')
def programming():
    num = 2

    def ReadOnboard(OnboardFile, line, cell):
        Data=pandas.read_excel(OnboardFile,sheet_name='Projects',engine='openpyxl')
        Data=Data.replace(numpy.nan,'End',regex=True)
        List=Data.values.tolist()
        return(List[line][cell])
    
    title = ReadOnboard(excelPath, num, 0)
    littleTitle = ReadOnboard(excelPath, num, 1)
    littleBlurb = ReadOnboard(excelPath, num, 2)
    bigBlurb = ReadOnboard(excelPath, num, 3)
    impressiveNumber1 = ReadOnboard(excelPath, num, 4)
    
    return render_template('Projects Template.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, impressiveNumber1=impressiveNumber1)  

@app.route('/projects/marketing')
def marketing():
    num = 3
    sheet = "Projects"

    def ReadOnboard(OnboardFile, line, cell):
        Data=pandas.read_excel(OnboardFile,sheet_name='Projects',engine='openpyxl')
        Data=Data.replace(numpy.nan,'End',regex=True)
        List=Data.values.tolist()
        return(List[line][cell])
    
    title = ReadOnboard(excelPath, num, 0)
    littleTitle = ReadOnboard(excelPath, num, 1)
    littleBlurb = ReadOnboard(excelPath, num, 2)
    bigBlurb = ReadOnboard(excelPath, num, 3)
    impressiveNumber1 = ReadOnboard(excelPath, num, 4)
    
    return render_template('Projects Template.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, impressiveNumber1=impressiveNumber1)  

@app.route('/about-us')
def about():
    return render_template('about-us.html')
       
@app.route('/sponsorship')
def sponsorship():
    return render_template('about-us.html')
       
@app.route('/contact-us')
def contact():
    return render_template('about-us.html')
       

    
    
if __name__ == '__main__':
    app.run()