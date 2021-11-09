from myapp import myobj, db
from myapp.forms import RegisterForm, LoginForm
from myapp.models import User
from flask import render_template, flash, redirect
from flask_login import login_user, logout_user, current_user

from myapp import login


@myobj.route("/")
def main():
    '''
        Routes the main directory of the website to home.html. Passes in form for user to login when not logged in, otherwise will reroute to logged in page.

        returns:
            render_template: Webpage information for main page
    '''
    return render_template('home.html', user=current_user)

@myobj.route("/login", methods=['GET', 'POST'])
def login():
    '''
        creates a login page for users to login to their account.

        returns:
            render_template: Webpage for users to enter credentails and login
    '''
    form = LoginForm()

    if(form.validate_on_submit()): #login attempt

        username = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data

        user = User.query.filter_by(username = username).first()

        if(user is None or not user.check_password(form.password.data)):
            flash('incorrect password, try again')
            return redirect('/login')

        login_user(user, remember = remember_me)
        return redirect('/')

    return render_template('login.html', form=form)


@myobj.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@myobj.route("/register", methods=["GET", "POST"])
def register():
    '''
        Creates register page for users to create an account, creating a user login form.

        returns:
            render_template: Webpage information for register page including form
    '''    

    form = RegisterForm()

    if (form.validate_on_submit()): #register attempt

        username = form.username.data
        email = form.email.data
        password = form.password.data
        reenterPassword = form.reenterPassword.data

        credentials_check = User.check_valid_credentials(username=username, email=email, password=password, reenterPassword=reenterPassword)

        if(credentials_check[0] == False):
            flash(f'{credentials_check[1]} Try again.')
            return redirect('/register')

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('User created! Now try logging in.')
        return redirect('/')

    return render_template('register.html', form=form)

@myobj.route("/options", methods=["GET", "POST"])
def options():

	'''
	Creates an options page for users to change account settings
	'''
	form = OptionsForm()

	if (form.validate_on_submit()):

		current_user.setPublic(form.public.data)

	return redirect('/')





        

        

        

        





