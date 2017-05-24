# PyShips

1. Project description
2. Game rules
3. Description of the strategies
4. Code + walkthrough of code
5. Results
6. Conclusion

# Battleships Project Description
We have created a game that's meant for being analyzed. Therefore we can't have a real person playing, as it would take too long to get any usefull data. Therefore we have made various levels of AI's, that will "fight" against randomly placed ships on a board. Where the data then will be shown on a plot afterwards.

## Game rules
The game is played on a 10 by 10 grid. One player places the five ships of varying sizes randomly and the other player shots at it. The ship lengts are 5, 4, 3, 3 and 2. This results in 17 targets out of 100. The game is over when all the ships have been sunk or 100 shots have been fired.

## Analysis strategy
In order to analyse the efficiency of the different AIs, at the beginning of each round we place the ships randomly. Then we call the method `get_shot_position()` of the AI to shoot at. In the `hit_feedback()` method we tell the AI whether the shot was a hit or miss. It also provides the remaining ships on the board. This information is used to calculate later shot positions.

The smarter the AI is, the less shots it needs to win a game.

When all the rounds are finished, we return a dictionary of the number of shots that were fired to win a game. We can use this data to plot a graph of the results.

# AI Strategies
## Random Shooter
The simplest computer algorythm we can start with is one that shots at random positions. We use a two dimensional array to keep track of the previous shots and avoid shooting at the same place twice. Then we simply return the random position.

```python 
 def get_shot_position(self, ships):
        while True:
            position_x = random.randint(0, self.BOARD_SIZE - 1)
            position_y = random.randint(0, self.BOARD_SIZE - 1)

            if not self.shots[position_x][position_y]:
                self.shots[position_x][position_y] = True
                break

        return position_x, position_y
```

After firing all 100 shoots it is guaranteed that we hit all ships. Needless to say, this is a rather inefficient strategy. 

The x-axis shows the number of shots fired and the y-axis shows the number of games that were completed with the respective number of shots.

![Random Shooter](/images/random_shooter.png)

## Hunter Shooter
In this strategy we are going to greatly improve the efficiency of our AI. 

First the computer is in __Hunt__ mode, firing at random positions until it hits a ship. Once it finds out that the shot was a hit, it stacks the sorrounding squares (up, down, left and right) into a pool of targets.

![Sorrounding ships](/images/target_ships.jpg)

As long as we have potential targets in this pool, we will keep firing at them. Once we run out, we get back to hunting mode.

This strategy becomes much better, as we do not waste our shots at random positions, but instead we have a much higher chance of hitting the other parts of the ship once we found one.

![Hunter Shooter](/images/hunter_shooter.png)

Since we still rely a lot on random positions to find the ships in hunt mode, some games are only finished by firing all the shots.

## Parity Shooter
It is rather easy to improve the __Hunter Shooter__ even further. Since every ship takes up at least to positions, we don't need to fire at each square. It is enough to target every second one, as shown with blue on the board below. 

The blue squares on the board are even while the white ones are odd parity. 

![Parity board](/images/parity_board.png)

With this strategy the game is always won before firing 80 shots, with an average of 65.

![Parity Shooter](/images/parity_shooter.png)

## Probability Shooter
The Probablity Shooter is the best way of winning in Battleships, as it will calculate the most likely place an enemy ship will be placed at. It can do this, as it uses the knowledge of the board. Since the ships that are hit and sunk will be returned, then it knows what ships are still alive and can calculate where the best odds are of hitting one.

This Image shows how the board looks to the Probablity AI in the beginning of a game

![Probability Shooter](/images/Screenshot_2.jpg)

This Image shows how it looks to the AI after a lot of shots have been fired. The dark grey areas are the high valued targets and the white ones have no value, as no ships can be there due to the size in both horizontal and vertical position. The colours in between are rated from light to dark, where darker is higher value of there being a ship. So it will always go after the darkest places first. This image will of course change for every shot, as it can rule out an area due to lack of space for the ships that are left.

![Probability Shooter](/images/Screenshot_3.jpg)


# Code + Walkthrough
In all our AI's, we start by calling BattleshipAI and self.shots.
```python 
    def __init__(self):
        BattleshipsAI.__init__(self)
        self.shots = [[False for y in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]
```
The "BattleshipAI" calls for the creation of the board and the ships. It also gets the shooting positions and feedback, which is called after every shot

The self.shots sets the whole board to false (When a location is set to true, it means the AI have shot there)

## RandomShooter code:
```python 
    def get_shot_position(self, ships):
        while True:
            position_x = random.randint(0, self.BOARD_SIZE - 1)
            position_y = random.randint(0, self.BOARD_SIZE - 1)

            if not self.shots[position_x][position_y]:
                self.shots[position_x][position_y] = True
                break

        return position_x, position_y
```
When we enter the loop, we get a random location between 0 and 9 in the x and y position. We then check if that loccation have already been shot at, if so we break and get a new position, otherwise we shoot at it. Which will keep on going until we have spend 100 shots or all the ships have been sunk 

## Hunter Shooter Walkthrough
This shooter's strategy has been explained already, but just to remind you briefly, it's a two-mode strategy of either shooting randomly in order to get a hit(hunting mode) or shooting at the nearby positions of a hit(targeting mode). 
The essential part of this shooter is remembering/storing the last hit position, which will, therefore, be the starting point of the targeting mode. In the code we have the variables "lastX" and "lastY":
``` python
class HuntTargetShooter(BattleshipsAI):
    def __init__(self):
        BattleshipsAI.__init__(self)
        self.shots = [[False for y in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]
        self.lastX = 0 ##!
        self.lastY = 0 ##!
        self.position_x = 0
        self.position_y = 0
        self.potential_targets = []

```
And then saving the last known shot:
``` python
        self.shots[position_x][position_y] = True
        self.lastX = position_x
        self.lastY = position_y
        return position_x, position_y
```



First, the "hunting" mode is based on the random shooter, so basically we hit random targets, until we have a successful hit, then we switch to the "targeting" mode:
``` python
def hit_feedback(self, is_hit, ships):
        last_x = self.lastX
        last_y = self.lastY
        if is_hit:
            # target to the left
            target_left = (last_x - 1, last_y)
            if self.validate_position(target_left[0], target_left[1]) and target_left not in self.potential_targets:
                self.potential_targets.append(target_left)
            
            # target to the right
            target_right = (last_x + 1, last_y)
            if self.validate_position(target_right[0], target_right[1]) and target_right not in self.potential_targets:
                self.potential_targets.append(target_right)
            
            # target above
            target_above = (last_x, last_y - 1)
            if self.validate_position(target_above[0], target_above[1]) and target_above not in self.potential_targets:
                self.potential_targets.append(target_above)

            # target below
            target_below = (last_x, last_y + 1)
            if self.validate_position(target_below[0], target_below[1]) and target_below not in self.potential_targets:
                self.potential_targets.append(target_below)
```

Here you can see we have four cases for the directions (left, right, up and down). We add one to the integer of the axis we would like to go to : either X or Y, from the last known random hit.

After we have no more available options for targeting, we go back to the "hunting" mode. 
All in all, this is the repetitive cycle of the hunting shooter, which switches between those two modes until all the targets are destroyed.

## Parity Shooter Walkthrough
The parity shooter is a simple mathematical upgrade to the hunter shooter. In a nutshell, it is based on the idea that each ship takes at least 2 squares, therefore, there is no need to put each position from 1 to 100 in a pool to randomize a shot. We take only half the positions as possibilities from which we randomize a shot. In the code, the parity shooter resembles the hunting shooter for the most part, except for the division of positions as available targets.
``` python
if len(self.potential_targets) == 0:
            while True:
                position_x = random.randint(0, self.BOARD_SIZE - 1)
                position_y = random.randint(0, self.BOARD_SIZE - 1)
                if not self.shots[position_x][position_y]:
                    if position_x % 2 == 0 and position_y % 2 == 0 or position_x % 2 == 1 and position_y % 2 == 1:
                        break
```
