class scene:
    # For the bad ending we print the bedroom (cause we lost)
    # Note: I'm tabing out the output and using 0,0 just to make it easier to read here
    bedroom = """
      | [---------]  
      | [---------]  
      |  .........
      |   (⊙ ʖ ⊙)
      |  #########    
      |  #########
      |  #########  
      | {---------}
      |-----------------
    """

    grue = "(◣_◢)و ̑̑"
    mob = ".-. .-. .-."
    # Decisions will point to a json file to load (might add access functions to this)
    # currently leaving as just a list of dictionaries
    decisions = []

    def __init__(self, color):
        self.scene = 0
        self.color = color

    # Might make this a property with a @scene.setter if we move past the binary tree
    def next_scene(self):
        if self.scene + 1 < len(self.decisions):
            self.scene += 1


# Might move to different files but might not (not sure how inheritence will work out)
class castlescene(scene):
    # Both of these will become full classes (cause we will inherit them for others)
    # This will fill out as we go but for now we're using this more as a structure over a true class
    # Need to either make castle a list of scenes or seperate scenes or load each string from file (like image)
    # ... Then could just load images but I like the ascii feel for now

    castle = """
               *                /^\   *   /^\   *      *
        *                      /   \     /   \           *
                    *         /_|_|_\ * /_|_|_\      *
             *          _   _   | |   _   | |  _    _
       *               | |_| |__| |__| |__| |_| |__| |    *
                  *    |                             |  *
         _             |___   [ ]          [ ]    ___|
        (@)                |          *          |
         |                 |         / \         |
         |                 |        (   )        |
      ----------------------------------------------------------
      ----------------------------------------------------------"""

    # Decisions hold a list of initial statements for the DM to make with their answer options
    # These will be moved to a json at some point - however first is to use numpy for a fun maze option
    # We are also using the simplest decision tree ever: 0 = You lose, 1+ = Move to next

    # okay time to fix this
    decisions = [
        {"statement": """
            You blink and night falls in that instant.
              You begin to doubt your eyes as a giant castle has appeared out of nowhere!
              Next to a small lantern, an even smaller elf flips a coin while whistling a happy tune.
              He looks at you and it feels as if every secret you've ever had is written on your face.
              "Welcome to our land traveler, you're late." the elf huffs as he turns
                 and walks towards the immense door of the castle.""",
         "answers": ["Do you run?", "Do you enter?"]},
        {"statement": """
                 Walking through the dark doorway, you jump as the doors snap close. 
                   When you look back ahead the elf has disappeared but a chest sits in his place.""",
         "answers": ["Leave it alone.", "Open the chest?"]},
        {"statement": "You find a small knife dripping with poison in the chest. Just in time as here comes the GRUE!",
         "answers": ["Run from the GRUE", "Swing the knife."]}
    ]

    def __init__(self, color):
        super().__init__(color)
