from .db import db

attending = db.Table(
  'attendees',
  db.Column(
    'attendee_id',
    db.Integer,
    db.ForeignKey('users.id'),
    primary_key=True
  ),
  db.Column(
    'event_id',
    db.Integer,
    db.ForeignKey('events.id'),
    primary_key=True
  )
)
