class OutreachStat(db.Model):
    __tablename__ = 'outreach_stat'
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(10))
    program_cat = db.Column(db.String(10))
    activity = db.Column(db.String(10))
    stats = db.Column(db.Integer)
    month_year = db.Column(db.String(20))

    def __init__(self, department, program_cat, activity, stats, month_year):
        self.department = department
        self.program_cat = program_cat
        self.activity = activity
        self.stats = stats
        self.month_year = month_year
