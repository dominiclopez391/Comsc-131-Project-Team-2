from myapp import myobj, db
from myapp.models import TopCities
from myapp.forms import TopCitiesForm

from flask import render_template


@myobj.route("/")
def main():
    '''
        Routes the main directory of the website to home.html. Passes in form for user to login when not logged in, otherwise will reroute to logged in page.

        returns:
            render_template: Webpage information for main page
    '''
    return render_template('home.html')
    


