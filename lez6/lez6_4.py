'''
1. Write a new class called Food, it should have name, price and
description as attributes.
2. Instantiate at least three different foods you know and like.
3. Create a new class called Menu, it should have a list (of Foods) as attribute.
__init__ should take a list of Foods as optional parameters (default=[])
4. Create a addFood() and removeFood() for the Menu
5. Create a few new Food instances. Add each to the Menu using the respective
Method.
6. Add a method printPrices() that list all items on the Menu with their
prices.
7. Add a Menu method getAveragePrice() that returns the average Food
price of the Menu
'''

class Food:
    def __init__(self, name :str, price :float, description :str) -> None:
        self.name=name
        self.price=price
        self.description=description

lasagna=Food("Lasagna",15.0,"It's made by multiple layers of pasta sheets with inbetween them ragù and parmesan,\
              it's cooked in he oven")

tuna_taretare=Food("Tuna taretare",10.0,"")


class Menu:
    def __init__(self,foods=[]) -> None:
        self.foods=foods
    
    def Addfood(self,food :Food):
        self.foods.append(food)

    def Removefood(self,food :Food):
        if food in self.foods:
            self.foods.remove(food)
    
    def printPrices(self):
        for i in self.foods:
            print(i.name,"-->",i.price)
        print()
    
    def getAvaragePrice(self):
        sum=0
        for i in self.foods:
            sum+=i.price

        return sum/len(self.foods)

soute_mussels=Food("Mussels soutè",15.0,"")

menu=Menu([lasagna])
menu.Addfood(tuna_taretare)
menu.Addfood(soute_mussels)
menu.printPrices()
print("Avarege menu prices",menu.getAvaragePrice())
menu.Removefood(lasagna)
menu.printPrices()
