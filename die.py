import random
class Die:
    """
    Represents a single die.

    Attributes:
        _sides (int): number of sides of the die (default 6).
        _value (int): current rolled value of the die.
    """
    def __init__(self,sides = 6):
        # Initialize the die with given (default is 6-sided die).
        self._sides = sides
        # Roll the die once at creation to get an initial value.
        self._value = self.roll()
    
    # Generate a random number between 1 and number of sides.
    def roll(self):
        self._value = random.randint(1,self._sides)
        return self._value

    # String representation of the die's current value.
    def __str__(self):
        return str(self._value)
    # Less-than comparison: allows dice to be sorted by value.
    def __lt__(self,other):
        if(self._value < other._value):
            return True
        else:
            return False
    # Equality comparison: checks if two dice have the same value.
    def __eq__(self, other):
        if(self._value == other._value):
            return True
        else:
            return False
    # Subtraction operator: returns the difference between two dice values.
    def __sub__(self,other): 
       return self._value - other._value
    