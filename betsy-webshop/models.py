from peewee import SqliteDatabase, CharField, IntegerField, Model, TextField, DecimalField, ManyToManyField, ForeignKeyField, DateField
from datetime import datetime

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
    description=TextField(default='No description')
    unit_price=DecimalField(decimal_places=2, auto_round=True)
    tags=ManyToManyField(Tag, on_update='cascade')
    stock_quantity=IntegerField(default=1, null=False)
    user_id = ForeignKeyField(User)
    
    class Meta:
        database=db

class Transaction(Model):
    user_id=ForeignKeyField(User)
    product_id=ForeignKeyField(Product)
    bought_amount=IntegerField()
    transaction_date=DateField(default=datetime.now())
    
    class Meta:
            database=db

ProductTag = Product.tags.get_through_model()

db.create_tables([User, Product, Tag, Transaction, ProductTag], safe=True)