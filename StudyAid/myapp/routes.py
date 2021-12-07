from myapp import myobj, db
import pyttsx3

from myapp.forms import NotesForm, RegisterForm, LoginForm, OptionsForm, DeleteForm, SearchForm, SearchClassroomsForm, CreateClassroomForm, MessageForm, QuestionForm, AnswerForm
from myapp.models import User, Classroom, Chat, Questions, Note

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
        On form validate, checks credentials user entered to see if they exist in the database and that the
        password they entered was correct.

        returns:
            render_template: Webpage for users to enter credentials and login
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
    '''
        Logs current user out.
        returns:
            redirect: Returns user to homepage after being logged out

    '''


    logout_user()
    return redirect("/")

@myobj.route("/register", methods=["GET", "POST"])
def register():
    '''
        Creates register page for users to create an account, creating a user login form.
        On form validate, checks to make sure the credentials they added are valid.

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
        Creates an options page for users to change account settings.
        On form validate, sets all the values user assigned in database.

        Returns: 
            render_template: Webpage with information to display options form.
    '''
    form = OptionsForm(obj=current_user)
    if (form.validate_on_submit()):
        current_user.setPublic(form.public.data)
        return redirect('/')
        
    return render_template('options.html', form=form, current_user=current_user)

@myobj.route("/delete", methods=["GET", "POST"])
def delete():
    '''
        Creates a delete setting on the options page for users.
        On form submit, deletes the user's account from the database.

        returns:
            render_template: Webpage with information that allows users to delete their account.
    '''
    form = DeleteForm()
    user_to_delete = current_user
    
    if (form.validate_on_submit()):
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect('/logout')
        
    return render_template('delete.html', form=form, current_user=current_user)

@myobj.route("/search", methods=["GET","POST"])
def search():
	'''
	Creates a search page for users to search other public users,
        On form validate: queries database for users with username like user input.

        Returns:
            render_template: search webpage with form for user to fill out on user they want to search for.
        
	'''
	form = SearchForm()
	users = None
	if(form.validate_on_submit()):
		input = form.search.data
		users = User.query.filter(User.username.like("%" + input + "%"))
		if users.first() is None:
			flash('No users found!')
	return render_template('search.html', form=form, users=users)

@myobj.route("/classrooms", methods=["GET", "POST"])
def classrooms():
    '''
    Creates a webpage for navigating to classrooms. Will list every classroom a user has joined,
    otherwise they can search or create a new classroom which will bring them to a new webpage, displayed
    on form validate.

    Returns:
        render_template: Webpage for viewing the user's joined classrooms,

    '''

    user_classrooms = current_user.classrooms


    return render_template('classrooms.html', user_classrooms=user_classrooms)

@myobj.route("/classrooms/<classroom_id>", methods=["GET", "POST"])
def classroom(classroom_id):
    '''
        The currently selected classroom. Todo: add messages here
    '''
    classroom = Classroom.query.filter_by(id=classroom_id).first()
    if(classroom is None):
        flash("classroom not found")
        return redirect('/classrooms')
   
    if(not classroom in current_user.classrooms):
        flash ("You are not a member of this classroom.")
        return redirect("/classrooms")

    invite_dir = classroom.id
    classroom_name = classroom.name
    form = MessageForm()
    if form.validate_on_submit():
        message = Chat(current_user.username, form.message.data)
        classroom.messages.append(message)
        db.session.commit()

    messages = classroom.messages	
	

    return render_template("classroom.html", invite_dir=invite_dir, classroom_name=classroom_name, form=form, messages=messages)
        

@myobj.route("/findClassroom", methods=["GET", "POST"])
def find_classroom():
    '''
    lets the user search for a classroom. If the classroom they are searching for cannot be found,
    they can navigate to the "create classroom" field.

    Returns:
        render_template: Webpage for searching for classrooms by form.
    '''


    search_classrooms = SearchClassroomsForm()
    hits = None
    if(search_classrooms.validate_on_submit()):
        hits = Classroom.query.filter(Classroom.name.like("%" + search_classrooms.name.data + "%"))
    

    return render_template('findClassroom.html', searchClassroom=search_classrooms, hits=hits)
        
@myobj.route("/createClassroom", methods=["GET", "POST"])
def create_classroom():
    '''
        webpage that lets users create new classrooms by filling out a form for classroom name.

        Returns:
            render_template: webpage for creating a classroom
    '''
    create_classroom = CreateClassroomForm()
    if(create_classroom.validate_on_submit()):
        if(Classroom.query.filter_by(name=create_classroom.name.data).first() is not None):
            flash("Error: this classroom already exists. Please try again.")
        else:

            newClassroom = Classroom(create_classroom.name.data)
            db.session.add(newClassroom)
            current_user.classrooms.append(newClassroom)
            db.session.commit()

            flash("Classroom creation successful!")

            return redirect(f"classrooms/{newClassroom.id}")

    return render_template('createClassroom.html', create_classroom=create_classroom)

@myobj.route("/invite/<classroom_id>")
def join_classroom(classroom_id):
    '''
        Webpage that adds user to a classroom based on the id in the URL.

            returns: redirect to classroom
    '''
    classroom = Classroom.query.filter_by(id=classroom_id).first()
    if(classroom is None):
        flash("Error: this classroom does not exist. Please try again.")
    else:
        if(not classroom in current_user.classrooms):
            flash("Joined classroom!")
            current_user.classrooms.append(classroom)
        else:
            flash("You are already a member of this classroom.")
        db.session.commit()

    return redirect(f'/classrooms/{classroom_id}')


@myobj.route("/notes/create", methods=["GET", "POST"])
def create_note():
    '''
        Webpage which allows users to create their own notes.

            returns: render template for creating notes page
    '''
    form = NotesForm()
    if(form.validate_on_submit()):
        newNote = Note(form.title.data, form.body.data)
        current_user.notes.append(newNote)
        db.session.commit()
        return redirect("/notes")
    return render_template("createNote.html", form=form)

@myobj.route("/notes")
def view_notes():
    '''
        Webpage allows user to view their created notes.

            returns: render template for notes page
    '''
    notes = current_user.notes
    return render_template('notes.html', notes=notes)

@myobj.route('/classroom/<classroom_id>/faq', methods=["GET","POST"])
def questions(classroom_id):
	'''
		Webpage that allows user to post questions
	'''
	form = QuestionForm()
	classrooms = Classroom.query.filter_by(id = classroom_id).first()
	if(form.validate_on_submit()):
		questions = Questions(form.question.data)
		classrooms.questions.append(questions)
		db.session.commit()

	questions = classrooms.questions
	return render_template('questions.html', questions = questions, classroom_name = classrooms.name, form=form)

@myobj.route('/classroom/answers/<question_id>', methods=["GET","POST"])
def answers(question_id):
	'''
		Webpage that allows user to answer questions
	'''
	form = AnswerForm()

	if(form.validate_on_submit()):
		question = Questions.query.filter_by(id = question_id).first()
		question.answerQuestion(form.answer.data)
		db.session.commit()
		return redirect(f'/classroom/{question.classroom.id}/faq')

	return render_template('answers.html', form = form)

@myobj.route('/PomodoroTimer', methods = ['GET', 'POST'])
def pomodoro ():
    form = pomorodoTimerForm()
    title = 'Start Timer'
    if request.method == 'POST':
        try: 
            study_time = (request.form ["study_time"])
            #break_time = (request.form ["break_time"])
            timer (int(study_time))
            return redirect ("/timer")
        except:
            return flash ('Fail to load timer')
    else: 
        return render_template ("Ptimer.html", form = form,title=title)

def timer (t):
    # t = 25*60
    while t:
        mins, secs = divmod (t, 60)
        timer = '{:02d}: {:02d}'.format (mins, secs)
        print (timer, end = "\r")
        time.sleep(1)
        t -=1
    pyttsx3.speak ("beep beep beep beep time to work")
    return t


