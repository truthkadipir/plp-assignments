def calculate_discount(price, discount_percent):
    price=int(input("Enter original price: "))
    discount_percent=int(input("Enter discount percent: "))
    if (discount_percent < 20):
        return price
    else:
        return price - (price*discount_percent/100)
print(calculate_discount(100, 20))
