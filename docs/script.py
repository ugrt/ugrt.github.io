from flask import Flask, jsonify, render_template, request
import pandas as pandas
import numpy

app = Flask('testapp', template_folder='docs', static_folder='docs\static')
sheetName = ""
excelPath = 'docs\\Projects-Information.xlsx' 

#This allows us to change the path of the excel if we need to

# For this we can easily add more functions. This method simplifies the url and removes the html tag at the end (I personally hate it)

# The below function is the code used to read an individual cell from the excel sheet
# the variables are self explanitory. Sheet, line, and row are the only variables that are changed with different uses of the function
# OnboardFile does not change 
def ReadOnboard(OnboardFile, row, col, sheet):
    Data=pandas.read_excel(OnboardFile,sheet_name=sheet,engine='openpyxl')
    Data=Data.replace(numpy.nan,'End',regex=True)
    List=Data.values.tolist()
    return(List[row][col])
        
# This class was created to allow for variables to be collected from the webpage and shared with the appropriate web page to be. 
# https://stackoverflow.com/questions/2894946/passing-javascript-variable-to-python
class MyClass:
    num = 2
    
    @app.route('/process', methods=['POST'])
    def process():
        data = request.get_json() # retrieve the data sent from JavaScript
        # process the data using Python code
        result = data['value']
        # print(result)
        MyClass.num = result
        # print ("This is num")
        # print(MyClass.num)
        return jsonify(result=result) # return the result to JavaScript
    
    # This function is used to return the variable that is used to pick pages
    def get_var():
        return MyClass.num
    
@app.route('/') # This is the URL and function that renders the home page
def home():
    return render_template('index.html') 

@app.route('/subteams') # This is the URL and function that renders the projects grid
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
    return render_template('subteam-grid.html', electricalBlurb=electricalBlurb, 
    electricalImage=electricalImage,
                           mechanicalBlurb=mechanicalBlurb, 
                           mechanicalImage=mechanicalImage,
                           programmingBlurb=programmingBlurb, 
                           programmingImage=programmingImage,
                           businessBlurb=businessBlurb,
                           businessImage=businessImage)  

@app.route('/subteams/electrical')
def electrical():
    # This is important as num changes the line in which the information is pulled.
    # sheetName is going to change to organize the excel better. The string is the name of the sheet being called.
    num = 0
    sheetName = 'Projects'
    
    title = ReadOnboard(excelPath, num, 0, sheetName)
    littleTitle = ReadOnboard(excelPath, num, 1, sheetName)
    littleBlurb = ReadOnboard(excelPath, num, 2, sheetName)
    bigBlurb = ReadOnboard(excelPath, num, 3, sheetName)
    bigBlurb2= ReadOnboard(excelPath, num, 4, sheetName)
    imgPath = ReadOnboard(excelPath, num, 5, sheetName)
    subpageFn = ReadOnboard(excelPath, num, 6, sheetName)
    
    # This changes the sheet mid function to take the titles from the projects
    sheetName='Electrical'
    
    # This specifically pulls the title in lowercase form. 
    # We might change it so that it pulls something different then based on something else does something else, but for now this is what it does.
    proj1 = ReadOnboard(excelPath, 0, 1, sheetName)
    proj1SmallBlurb = ReadOnboard(excelPath, 0, 2, sheetName)
    proj2 = ReadOnboard(excelPath, 1, 1, sheetName)
    proj2SmallBlurb = ReadOnboard(excelPath, 1, 2, sheetName)
    proj3 = ReadOnboard(excelPath, 2, 1, sheetName)
    proj3SmallBlurb = ReadOnboard(excelPath, 2, 2, sheetName)
    proj4 = ReadOnboard(excelPath, 3, 1, sheetName)
    proj4SmallBlurb = ReadOnboard(excelPath, 3, 2, sheetName)
    proj5 = ReadOnboard(excelPath, 4, 1, sheetName)
    proj5SmallBlurb = ReadOnboard(excelPath, 4, 2, sheetName)
    proj6 = ReadOnboard(excelPath, 5, 1, sheetName)
    proj6SmallBlurb = ReadOnboard(excelPath, 5, 2, sheetName)
    
    return render_template('Subteam-Template.html', 
                           title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, bigBlurb2=bigBlurb2, imgPath=imgPath, subpageFn=subpageFn,
                           proj1=proj1, proj1SmallBlurb=proj1SmallBlurb,
                           proj2=proj2, proj2SmallBlurb=proj2SmallBlurb,
                           proj3=proj3, proj3SmallBlurb=proj3SmallBlurb,
                           proj4=proj4, proj4SmallBlurb=proj4SmallBlurb,
                           proj5=proj5, proj5SmallBlurb=proj5SmallBlurb,
                           proj6=proj6, proj6SmallBlurb=proj6SmallBlurb)  

# This is something I'm testing with dynamic URLs. The name is passed through the url_for() fn and is used in the route of the fn. 
@app.route('/subteams/electrical/<name>')
def electricalProjects(name):
    
    # This section is going to handle the electrical projects as they change
    num = MyClass.get_var() #
    sheetName = 'Electrical'
    
    title = ReadOnboard(excelPath, num, 0, sheetName)
    littleTitle = ReadOnboard(excelPath, num, 1, sheetName)
    littleBlurb = ReadOnboard(excelPath, num, 2, sheetName)
    bigBlurb = ReadOnboard(excelPath, num, 3, sheetName)
    bigBlurb2= ReadOnboard(excelPath, num, 4, sheetName)
    imgPath = ReadOnboard(excelPath, num, 5, sheetName)
    
    return render_template('Project-Template.html', title=title, littleTitle = littleTitle, littleBlurb=littleBlurb, bigBlurb=bigBlurb, imgPath=imgPath, bigBlurb2=bigBlurb2)  

# The remaining functions do the exact same things except the row changes based on the project

# @app.route('/subteams/mechanical') Mechanical num=1

# @app.route('/subteams/programming') Programming num=2

# @app.route('/subteams/marketing') Marketing num=3

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