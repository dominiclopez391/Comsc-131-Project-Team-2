# Routes.py: Provides server with information for webpage to be displayed


def main():


    '''
        Routes the main directory of the website to home.html. Passes in form for user to login when not logged in, otherwise will reroute to logged in page.

        returns:
            render_template: Webpage information for main page
    '''


def login():


    '''
        creates a login page for users to login to their account.
        On form validate, checks credentials user entered to see if they exist in the database and that the
        password they entered was correct.

        returns:
            render_template: Webpage for users to enter credentials and login
    '''


def logout():


    '''
        Logs current user out.
        returns:
            redirect: Returns user to homepage after being logged out

    '''



def register():


    '''
        Creates register page for users to create an account, creating a user login form.
        On form validate, checks to make sure the credentials they added are valid.

        returns:
            render_template: Webpage information for register page including form
    '''



def options():


    '''
        Creates an options page for users to change account settings.
        On form validate, sets all the values user assigned in database.

        Returns:
            render_template: Webpage with information to display options form.
    '''



def delete():


    '''
        Creates a delete setting on the options page for users.
        On form submit, deletes the user's account from the database.

        returns:
            render_template: Webpage with information that allows users to delete their account.
    '''



def search():


        '''
        Creates a search page for users to search other public users,
        On form validate: queries database for users with username like user input.

        Returns:
            render_template: search webpage with form for user to fill out on user they want to search for.

        '''


def classrooms():


    '''
    Creates a webpage for navigating to classrooms. Will list every classroom a user has joined,
    otherwise they can search or create a new classroom which will bring them to a new webpage, displayed
    on form validate.

    Returns:
        render_template: Webpage for viewing the user's joined classrooms,

    '''



def find_classroom():


    '''
    lets the user search for a classroom. If the classroom they are searching for cannot be found,
    they can navigate to the "create classroom" field.

    Returns:
        render_template: Webpage for searching for classrooms by form.
    '''



def create_classroom():


    '''
        webpage that lets users create new classrooms by filling out a form for classroom name.

        Returns:
            render_template: webpage for creating a classroom
    '''


def join_classroom(classroom_id):
    
    '''
        Webpage that adds user to a classroom based on the id in the URL.

        Returns: 
            redirect to classroom
    '''
