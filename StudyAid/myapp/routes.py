from myapp import myobj, db
from myapp.forms import RegisterForm
from myapp.models import User
from flask import render_template, flash, redirect


@myobj.route("/")
def main():
    '''
        Routes the main directory of the website to home.html. Passes in form for user to login when not logged in, otherwise will reroute to logged in page.

        returns:
            render_template: Webpage information for main page
    '''
    return render_template('home.html')


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
    



        

        

        

        





