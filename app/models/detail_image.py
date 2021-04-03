from .db import db

detail_image = db.Table(
  'detail_images',
  db.Column(
    'event_id',
    db.Integer,
    db.ForeignKey('events.id'),
    primary_key=True
  ),
  db.Column(
    'image_id',
    db.Integer,
    db.ForeignKey('images.id'),
    primary_key=True
  )
)
