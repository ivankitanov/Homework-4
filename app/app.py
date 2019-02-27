from flask import Blueprint, render_template

app == Blueprint('app', __name__,  template_folder='templates')


@app.route('/')
def home():
     return render_template('home.html')

@app.route('/students')
def students():
    return render_template('students.html', students=students)

@app.route('/courses')
def courses():
    return render_template('courses.html', courses=courses)

@app.route('/events')
def events():
    return render_template('events.html', events=events)
