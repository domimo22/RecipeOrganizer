from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c20fc0c610f1e16a1cd73c6ea06fbbed'

posts = [ 
    {
        'author': 'Adam Cooks',
        'title': 'Deviled Eggs',
        'content': 'Eggs and mayo I guess',
        'date_posted': 'April 13th 2021'
    },
    {
        'author': 'Adam Cooks',
        'title': 'BLT',
        'content': 'Bacon lettuce and tomato',
        'date_posted': 'April 17th 2021'
    }   
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
           flash(f'Login failed, please check username and password', 'danger') 
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)