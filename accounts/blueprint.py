from flask import Blueprint,render_template


users = Blueprint('users', __name__, template_folder='templates')


@users.route('/')
def index():
    """ main page with list of users """
    name = 'Root'
    return render_template('deloitte/main.html', name=name)


@users.route('/login')
def login():
    return render_template('deloitte/login.html')


@users.route('/logout')
def logout():
    return 'logout'