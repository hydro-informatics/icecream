## icecreamdialogue_standalone.py
flavors = ["vanilla", "chocolate", "bread"]
price_scoops = {1: "two euros", 2: "three euros", 3: "your health"}
welcome_msg = "Hi, I only have " + flavors[0] + ". How many scoops do you want?"


if (__name__ == '__main__'):
    print(welcome_msg)
    scoops_wanted = 2
    print("That makes {0} please".format(price_scoops[scoops_wanted]))