from modules.inventory import unique_product_list
from modules.inventory import create_overview

def test_unique_product_list():
    assert unique_product_list() == {'appel', 'melon', 'orange', 'grape'}

