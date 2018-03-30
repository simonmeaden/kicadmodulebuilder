from flask import Flask, render_template
from config import Config

app = Flask(__name__)      
app.config.from_object(Config)
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def home():
	user = {'username': 'Simon'}
	return render_template('home.html', title='Home', user=user)
  
@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
 
if __name__ == '__main__':
	app.run(debug=True)
