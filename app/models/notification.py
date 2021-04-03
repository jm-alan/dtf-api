from .db import db

notification = db.Table(
  'notifications',
  db.Column(
    'converstation_id',
    db.Integer,
    db.ForeignKey('conversations.id'),
    primary_key=True
  ),
  db.Column(
    'user_id',
    db.Integer,
    db.ForeignKey('users.id'),
    primary_key=True
  )
)
