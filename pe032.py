from common import is_unique

products = []

for a in range(2, 10):
    for b in range(1234, 9877):
        product = a * b
        temp = str(product) + str(a) + str(b)
        if '0' not in temp and is_unique(temp) and product not in products:
            products.append(product)

for a in range(12, 99):
    for b in range(123, 988):
        product = a * b
        temp = str(product) + str(a) + str(b)
        if '0' not in temp and is_unique(temp) and product not in products:
            products.append(product)

print(sum(products))