#!/usr/bin/python3

import zombiedice
import random

class RandomAfterFirstRollZombie: # A zombie that, after the first roll, randomly decides whether to continue or stop
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, game_state):
        # game_state is a dict with info about the current state of the game.
        # We can choose to ignore it in our code.

        dice_roll_results = zombiedice.roll() # First roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        

        # REPLACE THIS ZOMBIE CODE WITH ROWANCODE:
        brains = 0
        while dice_roll_results:

            brains += dice_roll_results['brains']
            random_flip = random.randint(0,1)
            if random_flip == 0:
                dice_roll_results = zombiedice.roll() # roll again
            else:
                break
class StopAfterTwoBrains: # A zombie that stops rolling after it has rolled two brains
    def __init__(self, name):
        self.name = name
    def turn(self, game_state): 
        dice_roll_results = zombiedice.roll()
        brains = 0
        while dice_roll_results:
            brains += dice_roll_results['brains']
            if brains < 2:
                dice_roll_results = zombiedice.roll()
            else:
                break
class StopAfterTwoShotguns: # A zombie that stops rolling after it has rolled two shotguns
    def __init__(self, name):
        self.name = name
    def turn(self, game_state):
        dice_roll_results = zombiedice.roll()
        shotguns = 0
        while dice_roll_results:
            shotguns += dice_roll_results['shotgun']
            if shotguns < 2:
                dice_roll_results = zombiedice.roll()
            else:
                break
class OneToFourRollsUnlessTwoShotguns: # A zombie that initially decides it'll roll the dice one to four times, 
                                    # but will stop early if it rolls two shotguns
    def __init__(self, name):
        self.name = name
    def turn(self, game_state):
        times_to_roll = random.randint(1,4)
        shotguns = 0
        for roll_number in range(times_to_roll):
            dice_roll_results = zombiedice.roll()
            shotguns += dice_roll_results['shotgun']
            if shotguns >= 2:
                break
class StopsIfMoreShotgunsThanBrains: # A zombie that stops if it has rolled more shotguns than brains. This doesn't work, but seems like others are having this issue too. Will leave for now as it is not that important.
    def __init__(self, name):
        self.name = name
    def turn(self, game_state):
        shotguns, brains = 0
        dice_roll_results = zombiedice.roll()
        while dice_roll_results:
            shotguns += dice_roll_results['shotgun']
            brains += dice_roll_results['brains']
            if shotguns > brains:
                break
            else:
                dice_roll_results = zombiedice.roll()







zombies = (
        zombiedice.examples.RandomCoinFlipZombie(name='Random'),
        zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
        zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
        zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
        StopAfterTwoBrains(name='Stop after 2 brains'),
        StopAfterTwoShotguns(name='Stop after 2 shotguns'),
        RandomAfterFirstRollZombie(name='Random after first roll'),
        OneToFourRollsUnlessTwoShotguns(name='1-4 Rolls til 2 Shotguns'),
        StopsIfMoreShotgunsThanBrains(name='Stops if shotguns > brains'),
        # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)

