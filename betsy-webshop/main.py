__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import db, User, Product, Tag, ProductTag

def search(term):
    ...


def list_user_products(user_id):
    ...


def list_products_per_tag(tag_id):
    ...


def add_product_to_catalog(user_id, product):
    ...


def update_stock(product_id, new_quantity):
    ...


def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(product_id):
    ...

if __name__ == "__main__":
    db.drop_tables([User, Product, Tag, ProductTag])
    db.create_tables([User, Product, Tag, ProductTag], safe=True)

    users = [('Joe', 'Wallstreet', 122, 'New York', 'Wells Fargo', 'U03.894.903.044'), ('Theresa', 'Downingstreet', 12, 'London', 'Bank of England', 'E23.354.532.555'), ('Alexander', 'Naamsesteenweg', '5','Brussel', 'KBC', 'B45.369.664.001' )]

    products = [('Shampoo', 'Soft gell to wash your hair', 1.25, 100,1), ('Toothbrush', 'Crosshaired brush with softgrip in various colors', 1.00, 50,2), ('Eau de Toilette', 'Parfum in glass bottle of 100ml', 24.95, 20,3), ('Rolls Roys', 'The perfect wedding car. Needs some tlc', 45000, 1, 2 )]

    tags = ['soft', 'hair', 'dental', 'hygiene', 'shower', 'parfume', 'brush', 'bottle', 'second_hand', 'cars']


    for user in users:
        name, street, number, place, bank, account_number = user
        User.create(name=name, street=street, number=number, place=place, bank=bank, account_number=account_number)
  
    for product in products:
        name, description, unit_price, stock_quantity, seller_id  = product
        Product.create(name=name, description=description, unit_price=unit_price, stock_quantity=stock_quantity, seller_id=seller_id)

    for tag in tags:
        Tag.create(tag_name = tag)

    product_tag = Product.select().where(Product.name == 'Shampoo').get()
    product_tag.tags = 1,2,4,5
    product_tag = Product.get(Product.name == 'Toothbrush')
    product_tag.tags = 3,4,7,9
    product_tag = Product.get(Product.name == 'Eau de Toilette')
    product_tag.tags = 6,8
    product_tag = Product.get(Product.name == 'Rolls Roys')
    product_tag.tags = 9,10

   