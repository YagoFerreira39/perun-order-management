from src.domain.models.product_model import ProductModel


def format_product(pk: str):
    product = ProductModel.get(pk)

    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }


class ProductRepository:
    @classmethod
    def get_all_products(cls):
        products = ProductModel.all_pks()

        return [format_product(pk) for pk in products]

    @classmethod
    def create_product(cls, product: ProductModel):
        return product.save()

    @classmethod
    def get_product_by_id(cls, pk: str):
        return ProductModel.get(pk)

    @classmethod
    def delete_product_by_id(cls, pk: str):
        return ProductModel.delete(pk)