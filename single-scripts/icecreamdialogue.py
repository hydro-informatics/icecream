## ice-cream-dialogue.py
flavors = ["vanilla", "chocolate", "bread"]
size_scoops = {1: "small", 2: "medium", 3: "this is too much ice..."}
price_scoops = {1: "two euros", 2: "three euros", 3: "your health"}
welcome_msg = "Hi, I only have " + flavors[0] + ". How many scoops do you want?"


def get_size_price(scoops):
    size = " " + str(size_scoops[scoops])
    price = str(price_scoops[scoops])
    return size, price


for k in size_scoops.keys():
    print(get_size_price(k))
