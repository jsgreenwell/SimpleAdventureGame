import pyxel
from scene import castlescene
import CastleBoard


class App:
    # Both of these will become full classes (as we will inherit them for others)
    player = {
        "x": 5,
        "y": 145,
        "image": "\\@/"
    }

    choice = 0
    alive = True

    def __init__(self):
        pyxel.init(500, 225, title="L = first choice, R = second choice")
        self.cs = castlescene(11)
        self.cb = CastleBoard
        pyxel.run(self.update, self.draw)

    def update(self):
        # Reminder to self: ESC also quits
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.alive = False
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.cs.next_scene()
            self.player["x"] += 50

    def draw(self):
        pyxel.cls(0)
        # 10 = yellow-ish where using a changing frame_count gives a random number

        # Print statements and possible answers if still alive
        if self.alive:

            pyxel.text(0, 0, self.cs.castle, self.cs.color)
            pyxel.text(0, 85, self.cs.decisions[self.cs.scene]["statement"], 5)
            pyxel.text(0, 135,
                       self.cs.decisions[self.cs.scene]["answers"][0], 7)
            pyxel.text(120, 135,
                       self.cs.decisions[self.cs.scene]["answers"][1], 7)

            # Print out character progression
            pyxel.text(self.player["x"], self.player["y"], self.player["image"], pyxel.frame_count % 16)

        else:
            pyxel.text(0, 0, self.cs.bedroom, self.cs.color)
            pyxel.text(0, 0, "You awake in your bed. Was it all a dream?", 15)
            # should sleep then exit here


App()
