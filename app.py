from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.secret_key = 'lvw7wWFytfTRZ6e2PJkrjxRsNi2U7xU0'

posts = [
   {
      'author': 'Brad Mendolla',
      'title': 'First post',
      'content': 'Blog post 1. Motherfucker',
      'date_posted': 'September 5, 2019'
   },
   {
      'author': 'Zach Mendolla',
      'title': 'Woot',
      'content': "I charge people for stuff that should be free. I'm a horrible person!",
      'date_posted': 'September 6, 2019'
   }
]

@app.route('/')
@app.route('/home')
def hello():
   return render_template("home.html", posts=posts)

@app.route('/about')
def about():
   return render_template("about.html", title="About")

@app.route('/register', methods= ["GET", "POST"])
def register():
   form = RegistrationForm()
   if form.validate_on_submit()
   return render_template("register.html", title="Register", form=form)

@app.route('/login')
def login():
   form = LoginForm()
   return render_template("login.html",title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)