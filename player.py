from die import Die
class Player:
    """
    Attributes: 
        _dice (Die []): 
        _points: int
    """
    def __init__(self):
        self._dice = [Die(), Die(), Die()]
        self._points = 0

    def _get_points(self):
        return self._points

    def roll_dice(self):
        for dice in self._dice:
            dice.roll
        self._dice.sort()
    def has_pair(self):
        if(self._dice[0] == self._dice[1] 
           or self._dice[1] == self._dice[2] 
           or self._dice[0] == self._dice[2]):
            # increment points by 1
            self._points += 1
            return True
        return False
    def has_three_of_a_kind(self):
        if(self._dice[0] == self._dice[1] == self._dice[2]):
            # incremennt points by 3
            self._points += 3
            return True
        return False
    def has_series(self):
        # If the second element is equal to the first + 1
        # and the second element is equal to the second + 1
        if(self._dice[1] - self._dice[0] == 1 
           and self._dice[2] - self._dice[1] == 1):
            # then increment points by 2
            self._points += 2
            return True
        return False
    def __str__(self): 
        string = ""
        for index, value in enumerate(self._dice):
            string += f"D{index+1} = {value}"
            if(index != 2):
                string += ', '
        return string
    points = property(_get_points)