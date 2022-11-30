# Models go here
from peewee import *

db = SqliteDatabase('betsy.db')

class User(Model):

    name=CharField()
    street=CharField()
    number=IntegerField()
    place=CharField()
    bank=CharField()
    account_number=CharField()
    
    class Meta:
        database=db

class Tag(Model):
    tag_name=CharField()

    class Meta:
        database=db

class Product(Model):
    name=CharField()
    description=TextField()
    unit_price=FloatField()
    stock_quantity=IntegerField()
    tags=ManyToManyField(Tag)
    seller_id = ForeignKeyField(User)
    
    class Meta:
        database=db

class Transaction(Model):
    user_id=ForeignKeyField()
    product_id=ForeignKeyField()
    bought_amount=IntegerField()
    


ProductTag = Product.tags.get_through_model()