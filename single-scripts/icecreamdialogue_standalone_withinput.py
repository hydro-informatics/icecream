## icecreamdialogue_standalone_withinput.py
flavors = ["vanilla", "chocolate", "bread"]
price_scoops = {1: "two euros", 2: "three euros", 3: "your health"}
welcome_msg = "Hi, I only have " + flavors[0] + ". How many scoops do you want?"

def dialogue(scoops_wanted): #formerly in the __main__ statement
    print(welcome_msg)
    print("That makes {0} please".format(price_scoops[scoops_wanted]))

if (__name__ == '__main__'):
    import sys  # we need sys here
    if len(sys.argv) > 1: # make sure input is provided
        # if true: call the dialogue function with the input argument
        dialogue(int(sys.argv[1]))