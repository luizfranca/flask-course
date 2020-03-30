from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    items = db.relationship('ItemModel', lazy='dynamic') ## with lazy it wont create the items 

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'id': self.id,
            'name': self.name, 
            'items': [item.json() for item in self.items.all()]
            }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def upsert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
