# PyShips

1. Project description
2. Game rules
3. Description of the strategies
4.  Code + walkthrough of code
5. Results
6. Conclusion

# Battleships Project Description
## Game rules
The game is played on a 10 by 10 grid. One player places the five ships of varying sizes randomly and the other player shots at it. The ship lengts are 5, 4, 3, 3 and 2. This results in 17 targets out of 100. The game is over when all the ships have been sunk or 100 shots have been fired.

## Analysis strategy
In order to analyse the efficiency of the different AIs, at the beginning of each round we place the ships randomly. Then we call the method `get_shot_position()` of the AI to shoot at. In the `hit_feedback()` method we tell the AI whether the shot was a hit or miss. It is also provided the remaining ships on board. This information is used to calculate later shot positions.

The AI is smarter the less shots it needs to fire to win a game.

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