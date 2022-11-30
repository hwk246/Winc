from peewee import SqliteDatabase, CharField, IntegerField, Model, TextField, DecimalField, ManyToManyField, ForeignKeyField, DateField, DateTimeField
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
    tag_name=CharField(unique=True)

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

''' option 1 standard with autofield primary key

class Transaction(Model):
    user_id=ForeignKeyField(User)
    product_id=ForeignKeyField(Product)
    bought_amount=IntegerField()
    transaction_date=DateField(default=datetime.now())
    
    class Meta:
            database=db
'''

'''
    option 2 combined indexes as primary - multiple combination user_id and product_id possible by different datetime
'''
class Transaction(Model):
    user_id=IntegerField()
    product_id=IntegerField()
    bought_amount=IntegerField()
    transaction_date=DateTimeField(default=datetime.now())
    
    class Meta:
            database=db
            primary_key=False
            indexes =(
                (('user_id', 'product_id', 'transaction_date'), True),
                (('user_id', 'product_id'), False)
            )
            

ProductTag = Product.tags.get_through_model()

db.create_tables([User, Product, Tag, Transaction, ProductTag], safe=True)