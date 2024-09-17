from flask import Flask, render_template
import pandas as pandas
import numpy

app = Flask('testapp', template_folder='docs', static_folder='docs\static')
num = 0
sheetName = ""
excelPath = 'docs\\Projects-Information.xlsx' 

#This allows us to change the path of the excel if we need to

# For this we can easily add more functions. This method simplifies the url and removes the html tag at the end (I personally hate it)

def ReadOnboard(OnboardFile, line, cell, sheet):
        Data=pandas.read_excel(OnboardFile,sheet_name=sheet,engine='openpyxl')
        Data=Data.replace(numpy.nan,'End',regex=True)
        List=Data.values.tolist()
        return(List[line][cell])

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/projects')
def projects():
    sheetName = 'Projects'

    electricalBlurb = ReadOnboard(excelPath, 0, 2, sheetName)
    electricalImage=ReadOnboard(excelPath, 0, 4, sheetName)
    mechanicalBlurb = ReadOnboard(excelPath, 1, 2, sheetName)
    mechanicalImage = ReadOnboard(excelPath, 1, 4, sheetName)
    programmingBlurb = ReadOnboard(excelPath, 2, 2, sheetName)
    programmingImage = ReadOnboard(excelPath, 2, 4, sheetName)
    businessBlurb = ReadOnboard(excelPath, 3, 2, sheetName)
    businessImage = ReadOnboard(excelPath, 3, 4, sheetName)
    
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
    sheetName = 'Projects'
    
    title = ReadOnboard(excelPath, num, 0, sheetName)
    littleTitle = ReadOnboard(excelPath, num, 1, sheetName)
    littleBlurb = ReadOnboard(excelPath, num, 2, sheetName)
    bigBlurb = ReadOnboard(excelPath, num, 3, sheetName)
    impressiveNumber1 = ReadOnboard(excelPath, num, 4, sheetName)
    
    return render_template('Projects Template.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, impressiveNumber1=impressiveNumber1)  

@app.route('/projects/electrical/<name>', methods=['GET', 'POST'])
def electricalProjects(name):
    num=1
    sheetName = 'Projects'
    title = "This is a test"
    
    # title = ReadOnboard(excelPath, num, 0, sheetName)
    littleTitle = ReadOnboard(excelPath, num, 1, sheetName)
    littleBlurb = ReadOnboard(excelPath, num, 2, sheetName)
    bigBlurb = ReadOnboard(excelPath, num, 3, sheetName)
    impressiveNumber1 = ReadOnboard(excelPath, num, 4, sheetName)
    
    return render_template('Projects Template.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, impressiveNumber1=impressiveNumber1)  

@app.route('/projects/mechanical')
def mechanical():
    num = 1
    sheetName = 'Projects'
    
    title = ReadOnboard(excelPath, num, 0, sheetName)
    littleTitle = ReadOnboard(excelPath, num, 1, sheetName)
    littleBlurb = ReadOnboard(excelPath, num, 2, sheetName)
    bigBlurb = ReadOnboard(excelPath, num, 3, sheetName)
    impressiveNumber1 = ReadOnboard(excelPath, num, 4, sheetName)
    
    return render_template('Projects Template.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, impressiveNumber1=impressiveNumber1)  

@app.route('/projects/programming')
def programming():
    num = 2
    sheetName = 'Projects'
    
    title = ReadOnboard(excelPath, num, 0, sheetName)
    littleTitle = ReadOnboard(excelPath, num, 1, sheetName)
    littleBlurb = ReadOnboard(excelPath, num, 2, sheetName)
    bigBlurb = ReadOnboard(excelPath, num, 3, sheetName)
    impressiveNumber1 = ReadOnboard(excelPath, num, 4, sheetName)
    
    return render_template('Projects Template.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, impressiveNumber1=impressiveNumber1)  

@app.route('/projects/marketing')
def marketing():
    num = 3
    sheetName = 'Projects'
    
    title = ReadOnboard(excelPath, num, 0, sheetName)
    littleTitle = ReadOnboard(excelPath, num, 1, sheetName)
    littleBlurb = ReadOnboard(excelPath, num, 2, sheetName)
    bigBlurb = ReadOnboard(excelPath, num, 3, sheetName)
    impressiveNumber1 = ReadOnboard(excelPath, num, 4, sheetName)
    
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