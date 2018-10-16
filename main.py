from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2 
#try not activing flask ? 
template_dir=os.path.join(os.path.dirname(__file__), 'templates') 
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask (__name__)
app.config['DEBUG'] = True
  
@app.route("/") #default method=GET
def index():
    template = jinja_env.get_template('user_home.html')
    return template.render() 

@app.route('/', methods=['POST']) # aded 'userhome #post actually checks validations
def user_input(): 
    username=request.form['username']
    password=request.form['password'] #
    confirmation=request.form['confirmation'] #
    email=request.form['email']  
    email_error='' 
    username_error=''
    password_error=''
    confirmation_error=''
    atsign_index = email.find('@')
    atsign_present = atsign_index >=0
    domain_dot_index = email.find('.', atsign_index)
    domain_dot_present = domain_dot_index >=0
    template = jinja_env.get_template('user_home.html')
    welcome_template = jinja_env.get_template('welcome.html')
    if len(username) < 3: 
        username_error = "Must be greater than 3 characters"
        return template.render(username_error=username_error, username=username) 
    elif len(username) > 20:
        username_error = "Must be less than 20 characters"
        return template.render(username_error=username_error, username=username) 
    elif len(password) < 3: 
        password_error = "Must be greater than 3 characters"
        return template.render(password_error=password_error, password=password) 
    elif len(password) > 20:
        password_error = "Must be less than 20 characters"
        return template.render(password_error=password_error, password=password)   
    elif not password==confirmation:
        confirmation_error ="Password confirmation does not match password"
        return template.render(confirmation_error=confirmation_error, confirmation=confirmation)
    elif email=='':  # how to ignore if no email present 
        return welcome_template.render()
    elif not atsign_present:
        email_error="Email is not valid"
        return template.render(email_error=email_error, email=email)
    elif not domain_dot_present:
        email_error="Email is not valid"
        return template.render(email_error=email_error, email=email)
    else:
        return welcome_template.render(username=username)

app.run()