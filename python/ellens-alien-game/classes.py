"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        # This is class variable which is incremented every time an instance of the class is created.
        Alien.total_aliens_created+=1


    def hit(self):
        self.health -= 1
        return self.health

    def is_alive(self):
        print(f"self.health: {self.health}")
        if self.health <= 0:
            return False
        return True

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other_object):
        pass



def new_aliens_collection(alien_start_positions):
    empty_list = []
    for item in alien_start_positions:
        empty_list.append(Alien(item[0], item[1]))
    return empty_list


alien_start_positions = [(4, 7), (-1, 0)]

print(new_aliens_collection(alien_start_positions))


# alien = Alien(2, 3)
# print(alien.total_aliens_created)
# alien2 = Alien(2, 3)
# print(alien2.total_aliens_created)
#
# print(alien.x_coordinate)
# print(alien.y_coordinate)
# print(f"alien.hit() : {alien.hit()}")
# print(f"alien.is_alive() :{alien.is_alive()}")
# print(alien.teleport(5, -4))
# print(alien.x_coordinate)
# print(alien.y_coordinate)


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
