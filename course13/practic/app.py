from flask import Flask, jsonify, request, flash
from flask_sqlalchemy import SQLAlchemy
import config as config
from datetime import date

from sqlalchemy.sql import func

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


class GuestBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(3000), nullable=False)
    date = db.Column(db.Date, default=date.today)
    is_visible = db.Column(db.Boolean, default=True, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'content': self.content,
            'date_created': self.date,
            'is_visible': self.is_visible
        }


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # It is pretty easy for some tasks:
        people = GuestBookItem.query.all()
        # by_name = GuestBookItem.query.filter_by(name='Ivan').first()
        # by_age = Person.query.filter(Person.age >= 30)
        # by_job = Person.query.filter(Person.job == 'HR')

        # And not so easy for others:
        # sub = db.session.query(
        #    func.min(GuestBookItem.age).label('min_age')
        # ).subquery()
        #
        # youngest = GuestBookItem.query.join(
        #    sub, sub.c.min_age == GuestBookItem.age
        # ).first()

        # return jsonify([p.to_dict() for p in people])
        return jsonify({
            'people': [p.to_json() for p in people],
            # 'by_name': by_name.to_json(),
        })
    if request.method == 'POST':
        form = GuestBookItem(request.form)

        if form.validate():
            post = GuestBookItem(**form.data)
            db.session.add(post)
            db.session.commit()

            flash('Post created!')

        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))


if __name__ == '__main__':
    db.create_all()

    # Deleting all records:
    GuestBookItem.query.delete()

    # Creating new ones:
    ivan = GuestBookItem(name='Ivan', content='BlaBla')

    db.session.add(ivan)

    db.session.commit()  # note

    # Running app:
    app.run()
