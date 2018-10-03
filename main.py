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

@app.route('/user_input')
def user_input():
    return inputs.format(username='', username_error='',
    password='', password_error='',
    confirmation='', confirmation_error='',
    email='', email_error='') 
    no_space=[username, password, verify, email]

def check_for_spaces(no_space):
    for i in range (len (no_space)):
        if no_space[i] == ' ':
            return "cannot contain space(s)" 
        else: 
            return True 
     
@app.route('/user_input', methods=['POST'])
def validate_username():
    username=request.form['username']
    # email=request.form['email']
    username_error=''

    if len(username) < 3:
        username_error = "Must be longer than 3 characters"
    else:
        if len(username) > 20:
            username_error="Must be less than 20 characters"
    else:
        if username ==""
            blank_error="Please enter input in field" #? not sure if this will work 

        if not username_error or blank_error:
            template=jinja_env.get_template('welcome.html')
            return template.render(username_error=username_error, username=username)

def validate_password():
    password=request.form['password']
    password_error='' 
    if len (password<) 3:
        password_error = "Must be longer than 3 characters"
    else:
        if len(password) > 20:
            password_error="Must be less than 20 characters"
    else:
        if password ==""
            blank_error="Please enter input in field" #? not sure if this will work 
            #return True 

def confirm_password():
    confirmation=request.form['confirmation']
    confirmation_error=''
    if confirmation !=password:
        confirmation_error="Passwords do no match"
    else:
        #
#can above be combined in this way or do I need to split up?  
#     if verify != password:
#         error="Passwords do not match"
#     else: 
#         verify= password 
#     if not username_error and not password_error and not verify_error:

# def confirm_email(email):
#     if email=='':
#         return True 
#     else: 
#         if i in range (len(email)):
#             i==['a', '.']
#             return True
#         else:
#             error="Password not valid"

@app.route('/user_input')
def valid_username():
    return template.render('welcome.html')

app.run()