import json
from db import db, StudyGroup, User
from flask import Flask, request

app = Flask(__name__)
# TODO make a more creative database name
db_filename = 'study.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/api/study_groups/')
def get_all_groups():
    # TODO do we want to call this groups?
    groups = StudyGroup.query.all()
    res = {'success': True, 'data': [g.serialize() for g in groups]}
    return json.dumps(res), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)