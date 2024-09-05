from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration
ENV = 'prod'  # Change to 'prod' for production environment
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/lexus2'
else:
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:kcpl2024sqlda@flaskdb.c6jqnuecx3su.us-east-2.rds.amazonaws.com/outreach_db_test'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()

# Models
class OutreachStat(db.Model):
    __tablename__ = 'outreach_stat'
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(100))
    program_cat = db.Column(db.String(100))
    activity = db.Column(db.String(100))
    stats = db.Column(db.Integer)
    month_year = db.Column(db.String(100))

    def __init__(self, department, program_cat, activity, stats, month_year):
        self.department = department
        self.program_cat = program_cat
        self.activity = activity
        self.stats = stats
        self.month_year = month_year

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    department = request.form.get('department')
    program_cat = request.form.get('program_cat')
    activity = request.form.get('activity')
    stats = request.form.get('stats')
    month_year = request.form.get('month_year')
    
    if not (department and program_cat and activity and stats and month_year):
        return render_template('index.html', message='All fields are required.')
    
    new_stat = OutreachStat(department, program_cat, activity, int(stats), month_year)
    db.session.add(new_stat)
    db.session.commit()
    
    return render_template('success.html')

# Run the app
if __name__ == '__main__':
    app.run()
