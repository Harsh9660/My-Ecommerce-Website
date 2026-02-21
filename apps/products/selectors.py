from .models import Product

def get_all_products():
    return Product.objects.all()

def get_product_by_id(product_id):
    return Product.objects.filter(id=product_id).first()
