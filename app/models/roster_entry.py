from .db import db

roster_entry = db.Table(
  'roster_entries',
  db.Column(
    'user_id',
    db.Integer,
    db.ForeignKey('users.id'),
    primary_key=True
  ),
  db.Column(
    'conversation_id',
    db.Integer,
    db.ForeignKey('conversations.id'),
    primary_key=True
  )
)
