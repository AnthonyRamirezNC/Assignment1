### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources, recipes):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources
        self.recipes = recipes

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for key in ingredients.keys():
            if ingredients.get(key) > self.machine_resources[key]:
                #not enough to make it
                return False
            
        return True


    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        coinAmount  = 0
        print("Please insert coins")
        coinAmount += int(input("how many large dollars"))
        print()
        coinAmount += (.5 * int(input("how many half dollars")))
        print()
        coinAmount += (.25 * int(input("how many quarters")))
        print()
        coinAmount += (.05 * int(input("how many nickels")))
        print()
        return coinAmount


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for coins input"""
        if coins < cost:
            return False
        else: return True
            

    def make_sandwich(self, sandwich_size, order_ingredients):
        for key in order_ingredients.keys():
            self.machine_resources[key] -= order_ingredients.get(key)
        print(f'{sandwich_size} sandwhich is ready. Bon appetit!')

    def processInput(self, userInput):
        #check if resources are sufficient to make requested  recipe
        if(self.check_resources(self.recipes[userInput]["ingredients"])):
            #able to make recipe
            #process coin input
            coins = self.process_coins()

            #process transaction
            if(self.transaction_result(coins, self.recipes[userInput].get("cost"))):
                print("transaction processed")

                #make the resource
                self.make_sandwich(userInput, self.recipes[userInput]["ingredients"])
                print("resource made")
            else:
                print("Not enought coins inserted")
        else:
            print("Insufficient resources")

### Make an instance of SandwichMachine class and write the rest of the codes ###
machine = SandwichMachine(resources)
userInput = ""

while(userInput != "close"):
    userInput = input("What would you like? (small/ medium/ large/ off/ report): ")
    if(userInput == "small"):
        print("run small")
        machine.processInput(userInput)
        

    elif(userInput == "medium"):
        print("run medium")
        #check if resources are sufficient
        machine.processInput(userInput)

    elif(userInput == "large"):
        print("run large")
        #check if resources are sufficient
        machine.processInput(userInput)
    
    elif(userInput == "report"):
        print("run report")
        #check if resources are sufficient
    
    elif(userInput == "off"):
        print("run off")
        #check if resources are sufficient
    
    else: print("Invalid User Input")
