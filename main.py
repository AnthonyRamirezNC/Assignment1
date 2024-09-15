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
        coinAmount += int(input("how many large dollars?: "))
        coinAmount += (.5 * int(input("how many half dollars?: ")))
        coinAmount += (.25 * int(input("how many quarters?: ")))
        coinAmount += (.05 * int(input("how many nickels?: ")))
        return coinAmount


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for coins input"""
        if coins < cost:
            return False
        else: 
            change = coins - cost
            print(f'Here is ${change} in change')
            return True
            

    def make_sandwich(self, sandwich_size, order_ingredients):
        for key in order_ingredients.keys():
            self.machine_resources[key] -= order_ingredients.get(key)
        print(f'{sandwich_size} sandwich is ready. Bon appetit!')

    def processInput(self, userInput):
        #check if resources are sufficient to make requested  recipe
        if(self.check_resources(self.recipes[userInput]["ingredients"])):
            #able to make recipe
            #process coin input
            coins = self.process_coins()

            #process transaction
            if(self.transaction_result(coins, self.recipes[userInput].get("cost"))):

                #make the resource
                self.make_sandwich(userInput, self.recipes[userInput]["ingredients"])
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources")

    def printReport(self):
        for key in self.machine_resources.keys():
            if key == "ham":
                print(f'Ham: {self.machine_resources.get(key)} slice(s)')
            elif key == "bread":
                print(f'Bread: {self.machine_resources.get(key)} slice(s)')
            else:
                print(f'Cheese: {self.machine_resources.get(key)} pound(s)')


### Make an instance of SandwichMachine class and write the rest of the codes ###
machine = SandwichMachine(resources, recipes)
userInput = ""

while(userInput != "off"):
    userInput = input("What would you like? (small/ medium/ large/ off/ report): ")
    if(userInput == "small"):
        machine.processInput(userInput)
        

    elif(userInput == "medium"):
        #check if resources are sufficient
        machine.processInput(userInput)

    elif(userInput == "large"):
        #check if resources are sufficient
        machine.processInput(userInput)
    
    elif(userInput == "report"):
        #check if resources are sufficient
        machine.printReport()

    elif(userInput == "off"):
        break
    else: 
        print("Invalid User Input")

