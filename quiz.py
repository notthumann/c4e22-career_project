from mongoengine import Document, StringField, ListField, IntField, ReferenceField

class Answer(Document):
    link = StringField()
    point = IntField()
class Question(Document):
    answer = ListField(ReferenceField(Answer))
class PersonType(Document):
    name = StringField()
    des = StringField()
    suited = StringField()
    total_points = IntField()