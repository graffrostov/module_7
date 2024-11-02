# ---------------------------------------------------------------------------------
class Product:

    def __init__(self, name:str, weight:float, category:str):
        # Принудительно формат значений приводим к требуемому виду, хотя можно и без этого.
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight},{self.category}'
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
class Shop:

    __file_name = 'products.txt'

    def __init__(self):
        file = open(self.__file_name, 'a')
        file.close()

    def __str__(self):
        return 'class Shop'

    def get_products(self):

        work_file = open(self.__file_name, 'r')
        exist_product = work_file.read()
        work_file.close()
        return exist_product

    def add(self, *products:object):

        ex_product = self.get_products()

        for product in products:

            if product.name in ex_product:
                print(f'Продукт {product.name} уже есть в магазине')

            else:
                work_file = open(self.__file_name, 'a')
                work_file.write(f'{product}\n')
                work_file.close()
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())