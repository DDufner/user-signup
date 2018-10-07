from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2 

template_dir=os.path.join(os.path.dirname(__file__), 'templates')#checkon this? 
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask (__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('user_home.html')
    return template.render()

@app.route('/user_home', methods=['POST'])
def user_input():
    no_spaces=check_for_spaces('hell@ oo') #add req.form
    if not no_spaces:
        username_error=no_spaces 
    #repeat for password    
    return inputs.format(username='', username_error='',
    password='', password_error='',
    confirmation='', confirmation_error='',
    email='', email_error='') 

@app.route('/user_home', methods=['POST'])               #before_request #might work? 
#use nested for loop,  if one has spaces 
def check_for_spaces(entry):#won't exexut3
    space_found=False 
    for i in range (len (entry)):
        if entry[i] == ' ':
            space_found=True 
    if space_found==True:
        return "cannot contain space(s)" 
    else:
        return True          
     
@app.route('/user_home', methods=['POST'])
def validate_username():
    # email=valid_email(reqest.form ['email'])
    # password=reqeust.form['password']
    # veryify 
    # if validate_password(validate_password
    #     #code here.  
    username=request.form['username']
    username_error=''

    if len(username) < 3:
        print(username_error = "Must be longer than 3 characters")
    elif len(username) > 20:
            print(username_error="Must be less than 20 characters")
    elif username =="":
            blank_error="Please enter input in field" #? not sure if this will work 
    else:
        if not username_error or blank_error:
            template.render(username_error=username_error, blank_error=blank_error, 
            username=username)  ## only for errors. 
            return jinja_env.get_template('welcome.html')

def validate_password(password, verify ):
    password=request.form['password']
    #add lines to execue 
    password_error='' 
    if len (password) < 3:
        password_error = "Must be longer than 3 characters"
    elif len(password) > 20:
            password_error="Must be less than 20 characters"
    elif password =="":
            blank_error="Please enter input in field" #? not sure if this will work 
    else: 
        if not password_error or blank_error:
            template.render(password_error=username_error, blank_error=blank_error, password=password)  ## only for errors. 
            return jinja_env.get_template('welcome.html')
            #return True ? 
    
def confirm_password(password, verify):
    confirmation=request.form['confirmation']
    confirmation_error=''
    if confirmation !=password:
        confirmation_error="Passwords do no match"
    else:
        return True 

def confirm_email(email):
    email=request.form['email']
    if email=='':
        return True 
    else: 
        for i in range (len(email)):
            i==['a', '.']
            return True 
        else:
            error="Password not valid"

@app.route('/user_input')
def valid_username():
    return template.render('welcome.html')

app.run()