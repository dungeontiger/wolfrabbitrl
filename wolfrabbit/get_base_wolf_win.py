from wolfrabbit.env import Environment
from wolfrabbit.objects import Objects
from wolfrabbit.game_status import GameStatus

grid_size = 5
games = 10
rabbit_wins = 0
wolf_wins = 0

for game in range(games):
    game = Environment(grid_size)
    while True:
        game.randomly_move_object(Objects.RABBIT)
        status, _ = game.get_observation()
        if status == GameStatus.RABBIT_WON:
            rabbit_wins = rabbit_wins + 1
            break
        game.randomly_move_object(Objects.WOLF)
        if status == GameStatus.WOLF_WON:
            wolf_wins = wolf_wins + 1
            break
print('Wolf wins: {} Rabbit wins: {} Wolf %: {}'.format(wolf_wins, rabbit_wins, wolf_wins * 100 / (rabbit_wins + wolf_wins)))