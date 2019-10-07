from datetime import date

from app import db


class GuestBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(3000))
    date_created = db.Column(db.Date, default=date.today)
    # is_visible = db.Column(db.Boolean, default=True, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'content': self.content,
            'date_created': self.date,
            'is_visible': self.visible
        }

    def __str__(self):
        return '<Post {0}, user_id {1}>'.format(self.title, self.user_id)
