from .db import db

class Message(db.Model):
  __tablename__ = 'messages'

  id = db.Column(db.Integer, primary_key=True)
  sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  content = db.Column(db.Text)

  sender = db.relationship('User', back_populates='sent_messages')
  conversation = db.relationship('Conversation', back_populates='messages')

  def to_public(self):
    return {
      'Sender': self.sender.to_public(),
      'Converstaion': self.conversation.to_public()
    }
