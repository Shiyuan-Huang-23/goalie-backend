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

@app.route('/api/study_groups/', methods=['POST'])
def create_group():
    post_body = json.loads(request.data)
    name = post_body.get('name', '')
    date = post_body.get('date', datetime.datetime.now())
    time = post_body.get('time', dateTime.datetime.now())
    duration = post_body.get('duration', 1)
    location = post_body.get('location', 'Nowhere')
    description = post_body.get('description', '')

    group = Group(
        name=name,
        date=date,
        time=time,
        duration=duration,
        location=location,
        description=description
    )

    db.session.add(group)
    db.session.commit()
    data = group.serialize()
    data['participants'] = []
    return json.dumps({'success': True, 'data': data}), 201

@app.route('/api/study_group/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    group = StudyGroup.query.filter_by(id=group_id).first()
    if not group:
        return json.dumps({'success': False, 'error': 'Study group not found'}), 404
    db.session.delete(group)
    db.session.commit()
    return json.dumps({'success': True, 'data': grouop.serialize()}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)