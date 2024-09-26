#!/usr/bin/python3

""""""


class SwimMixin():
    """"""
    def swim(self):
        """"""
        print("The creature swims!")

class FlyMixin():
    """"""
    def fly(self):
        """"""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """"""
    def roar(self):
        """"""
        print("The dragon roars!")
    
    def description(self):
        """"""
        print("An inferior specimen based on the perfect design,"
              " workable, but not suited for the grand plan.")
        
dragon = Dragon()
dragon.swim()
dragon.fly()
dragon.roar()
dragon.description()