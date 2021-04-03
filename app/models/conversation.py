from .db import db
from .notification import notification
from .roster_entry import roster_entry

class Conversation(db.Model):
  __tablename__ = 'conversations'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  owner = db.relationship('User', back_populates='owned_convos')
  messages = db.relationship('Message', back_populates='conversation')
  chatting_users = db.relationship('User', secondary=roster_entry)
  notified_users = db.relationship('User', secondary=notification)

  def to_public(self):
    return {
      'ChatOwner': self.owner.to_public(),
      'ChattingUsers': [chatr.to_public() for chatr in self.chatting_users],
      'Messages': [chat.to_public() for chat in self.messages]
    }
