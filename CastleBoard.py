
""" so a maze is a matrix...so might use numpy later
    Also look at making it more random (using numpy random)
    starting with 10 by 10 matrix will expand if works
    9 = Closed space (not walkable, cause false)
    0 = Open space (walkable)
    1 = Treasure
    2 = Event item (key, lady, door)
    3 = Mob or Boss
"""


# special event functions below TODO: finish them
def fight_boss():
    return "Fight the boss"


def door():
    return "Came to a door"


def fight_mob():
    return "you fight a mob"


def key_npc():
    return "You meet an old lady"


def get_treasure():
    return "Treasure!"


class CastleBoard:
    _board = ((9, 9, 9, 9, 9, 9, 9, 9, 9, 3),
              (9, 9, 9, 9, 9, 9, 3, 9, 9, 2),
              (9, 9, 9, 9, 9, 9, 0, 9, 9, 0),
              (9, 9, 2, 9, 9, 9, 0, 9, 9, 0),
              (9, 9, 0, 9, 9, 9, 0, 0, 0, 0),
              (9, 9, 0, 9, 9, 9, 0, 9, 9, 9),
              (3, 0, 0, 0, 0, 0, 0, 0, 0, 1),
              (9, 9, 0, 9, 9, 9, 9, 9, 9, 9),
              (9, 9, 0, 9, 9, 9, 9, 9, 9, 9),
              (0, 0, 0, 0, 0, 0, 1, 9, 9, 9))

    # special items and events with position...maybe position as key
    _specials = {(0, 9): fight_boss(),
                 (1, 9): door(),
                 (1, 6): fight_mob(),
                 (3, 2): key_npc(),
                 (6, 0): fight_mob(),
                 (6, 9): get_treasure(),
                 (9, 6): get_treasure()
                 }

    _position = [0, 0]

    def __init__(self, position=None):
        if position is None:
            self._position = [9, 0]
        self._position = position

    # If manual changes need to position will setup property
    @property
    def position(self) -> list:
        return self._position

    # Ensure position is set as a 2 element list
    @position.setter
    def position(self, new_pos: list = None):
        old_pos = self._position
        if new_pos is None:
            pass
        try:
            self._position[0] = new_pos[0]
            self._position[1] = new_pos[1]
        except IndexError:
            self._position = old_pos

    # change position based on movement, if value in index and if adjacent position open
    # to be fair - could do an offset dictionary here but want to check for walls
    def move_right(self):
        if self._position[1] < 9 and self._board[self._position[0]][self._position[1] + 1] < 9:
            self._position[1] += 1

    def move_up(self):
        if self._position[0] < 9 and self._board[self._position[0] + 1][self._position[1]] < 9:
            self._position[0] += 1

    def move_left(self):
        if self._position[1] > 0 and self._board[self._position[0]][self._position[1] - 1] < 9:
            self._position[1] -= 1

    def move_down(self):
        if self._position[0] > 0 and self._board[self._position[0] - 1][self._position[1]] < 9:
            self._position[0] -= 1

    # Check position to see if special
    def check_position(self) -> str:
        return self._specials[tuple(self._position)]
        # TODO: setup these functions
        # For now they just print that they worked
        # also add inventory
