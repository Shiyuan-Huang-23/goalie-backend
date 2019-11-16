from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class StudyGroup(db.Model):
    __tablename__ = 'study_group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    # TODO participants/users
    # participants = db.relation('User', secondary=participant_association_table, backpopulates='study_groups')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Unnamed Study Group')
        # TODO change this to allow users to set a date and time
        self.time = datetime.datetime.utcnow
        # self.participants = []
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'time': self.time
            # TODO serialize participants
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    netid = db.Column(db.String, nullable=False)
    # study_groups = db.relationship('StudyGroup', secondary=participant_association_table)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Anonymous')
        self.netid = kwargs.get('netid', 'None')
        # self.study_groups = []

