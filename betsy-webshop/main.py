__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import db, User, Product, Tag, Transaction, ProductTag

def populate_test_database():

    db.drop_tables([User, Product, Tag, Transaction, ProductTag])
    db.create_tables([User, Product, Tag, Transaction, ProductTag], safe=True)

    users = [('Joe', 'Wallstreet', 122, 'New York', 'Wells Fargo', 'U03.894.903.044'), ('Theresa', 'Downingstreet', 12, 'London', 'Bank of England', 'E23.354.532.555'), ('Alexander', 'Naamsesteenweg', '5','Brussel', 'KBC', 'B45.369.664.001' )]

    products = [('Shampoo', 'Soft gell to wash your hair', 1.25, 100,1), ('Toothbrush', 'Crosshaired brush with softgrip in various colors', 1.05, 50,2), ('Eau de Toilette', 'Parfum in glass bottle of 100ml', 25.954, 20, 3), ('Rolls Roys', 'The perfect wedding car. Needs some tlc', 45000, 1, 2 ),('Sweater', 'Homemade longsleeve from alpaca woll', 10, 4, 2), ('Applejuice', 'from appels out of my backyard', 2.50, 30, 3)]

    tags = ['soft', 'soft', 'hair', 'dental', 'hygiene', 'shower', 'parfume', 'brush', 'soft', 'bottle', 'second_hand', 'cars', 'woll', 'homemade', 'liquid']


    for user in users:
        name, street, number, place, bank, account_number = user
        User.create(name=name, street=street, number=number, place=place, bank=bank, account_number=account_number)
  
    for product in products:
        name, description, unit_price, stock_quantity, seller_id  = product
        Product.create(name=name, description=description, unit_price=unit_price, stock_quantity=stock_quantity, user_id=seller_id)

    for tag in tags:
        Tag.get_or_create(tag_name = tag)
       

    product_tag = Product.select().where(Product.name == 'Shampoo').get()
    product_tag.tags = 1,2,4,5
    product_tag = Product.get(Product.name == 'Toothbrush')
    product_tag.tags = 3,4,7,9
    product_tag = Product.get(Product.name == 'Eau de Toilette')
    product_tag.tags = 6,8
    product_tag = Product.get(Product.name == 'Rolls Roys')
    product_tag.tags = 9,10
    product_tag = Product.get(Product.name == 'Sweater')
    product_tag.tags = 11,12
    product_tag = Product.get(Product.name == 'Applejuice')
    product_tag.tags = 8,13

def search(term):
    product_term = [product.name for product in Product.select().where(Product.name == term)]
    print('product naam op zoekterm ->',term, product_term)
    return product_term


def list_user_products(user_id):
    product_user = [prod.name for prod in Product.select().where(Product.user_id == user_id)]
    print('lijst met gebruikers in hun producten ->',user_id, product_user)
    return product_user
   

def list_products_per_tag(tag_id):
    product_tag = [prod.name for prod in Product.select() if tag_id in [p.tag_name for p in prod.tags]]  
    print('producten op basis van tag -> ',tag_id, product_tag)      
    return product_tag

def add_product_to_catalog(user_id, product):
    Product.create(name=product, unit_price=0,  user_id=user_id)


def update_stock(product_id, new_quantity):
    quantity = Product.select().where(Product.id == product_id).get()
    quantity.stock_quantity = new_quantity
    quantity.save()
    

def purchase_product(product_id, buyer_id, quantity):
    Transaction.create(user_id=buyer_id, product_id=product_id, bought_amount=quantity)


def remove_product(product_id):
    (Product.get(Product.id == product_id)).delete_instance(recursive=True)
    

if __name__ == "__main__":

    populate_test_database()
    search('Shampoo')
    search('Sweater')
    list_user_products(3)
    list_user_products(2)
    list_products_per_tag('second_hand')
    list_products_per_tag('bottle')
    add_product_to_catalog(2, 'Strawberry jam')
    purchase_product(1, 2, 10)
    update_stock(1, 90)
    purchase_product(4, 1, 1)
    remove_product(4)

   