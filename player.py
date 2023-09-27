class Player:
    def play(self):
        print("the player is playing cricket.")

class batsman(Player):
    def play(self):
        print("the batsman is batting.")

class bowler(Player):
    def play(self):
        print("the bowler is bowling.")

# creating objects of batsman and bowler classes
batsman = batsman()
bowler = bowler()

# calling the play() method for each object
batsman.play()
bowler.play()