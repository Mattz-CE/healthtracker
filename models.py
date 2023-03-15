from __main__ import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return '<Task %r>' % self.id


class UserAuth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return '<User %r>' % self.id
