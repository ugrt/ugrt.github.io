from flask import Flask, render_template
import pandas as pandas
import numpy

app = Flask('testapp', template_folder='docs', static_folder='docs\static')
num = 0
sheetName = ""
excelPath = 'docs\\Projects-Information.xlsx' 

#This allows us to change the path of the excel if we need to

# For this we can easily add more functions. This method simplifies the url and removes the html tag at the end (I personally hate it)

# The below function is the code used to read an individual cell from the excel sheet
# the variables are self explanitory. Sheet, line, and row are the only variables that are changed with different uses of the function
# OnboardFile does not change 
def ReadOnboard(OnboardFile, line, row, sheet):
        Data=pandas.read_excel(OnboardFile,sheet_name=sheet,engine='openpyxl')
        Data=Data.replace(numpy.nan,'End',regex=True)
        List=Data.values.tolist()
        return(List[line][row])

@app.route('/') # This is the URL and function that renders the home page
def home():
    return render_template('index.html') 

@app.route('/projects') # This is the URL and function that renders the projects grid
def projects():
    sheetName = 'Projects'
    
    # The below lines call the global function at the top of the page and 
    # and are pin pointed to specific cells in the excel sheet
    electricalBlurb = ReadOnboard(excelPath, 0, 2, sheetName)
    electricalImage=ReadOnboard(excelPath, 0, 4, sheetName)
    mechanicalBlurb = ReadOnboard(excelPath, 1, 2, sheetName)
    mechanicalImage = ReadOnboard(excelPath, 1, 4, sheetName)
    programmingBlurb = ReadOnboard(excelPath, 2, 2, sheetName)
    programmingImage = ReadOnboard(excelPath, 2, 4, sheetName)
    businessBlurb = ReadOnboard(excelPath, 3, 2, sheetName)
    businessImage = ReadOnboard(excelPath, 3, 4, sheetName)
    
    # This renders the html page in question and passes the above variables into the page. There are tags on the page that match the variables. This is where the variables are printed
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
    
    # This is important as num changes the line in which the information is pulled.
    # sheetName is going to change to organize the excel better. The string is the name of the sheet being called.
    num = 0
    sheetName = 'Projects'
    
    title = ReadOnboard(excelPath, num, 0, sheetName)
    littleTitle = ReadOnboard(excelPath, num, 1, sheetName)
    littleBlurb = ReadOnboard(excelPath, num, 2, sheetName)
    bigBlurb = ReadOnboard(excelPath, num, 3, sheetName)
    impressiveNumber1 = ReadOnboard(excelPath, num, 4, sheetName)
    
    return render_template('Projects Template.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, impressiveNumber1=impressiveNumber1)  

# This is something I'm testing with dynamic URLs. The name is passed through the url_for() fn and is used in the route of the fn. 
@app.route('/projects/electrical/<name>')
def electricalProjects(name):
    
    #
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