from random import randint, shuffle
from wolfrabbit.objects import Objects
from wolfrabbit.move_action import MoveAction
from wolfrabbit.game_status import GameStatus

class Environment:

    def __init__(self, grid_size):
        self.status = GameStatus.PLAYING
        # the grid is always square
        self.N = grid_size
        self.grid = []
        # initialize the grid to nothing
        for x in range(self.N):
            self.grid.append([])
            for y in range(self.N):
                self.grid[x].append(Objects.NOTHING)
        # place the objects at random locations
        self.randomly_place_object(Objects.RABBIT)
        self.randomly_place_object(Objects.WOLF)
        self.randomly_place_object(Objects.HOLE)

    def randomly_place_object(self, obj):
        search = True
        while search:
            x = randint(0, self.N - 1)
            y = randint(0, self.N - 1)
            if self.grid[x][y] == Objects.NOTHING:
                self.grid[x][y] = obj
                search = False

    def randomly_move_object(self, obj):
        moves = [MoveAction.LEFT, MoveAction.RIGHT, MoveAction.UP, MoveAction.DOWN]
        shuffle(moves)
        moved = False
        while not moved and len(moves) > 0:
            move = moves.pop()
            if self.is_legal_move(obj, move):
                return self.move_obj(obj, move)
        # no legal moves!
        raise RuntimeError

    def is_legal_move(self, obj, move):
        within_bounds = False
        x, y = self.find_object(obj)
        x1 = x
        y1 = y
        # check if the move is within the grd
        if move == MoveAction.LEFT and x > 0:
            x1 = x - 1
            within_bounds = True
        elif move == MoveAction.RIGHT and x < self.N - 1:
            x1 = x + 1
            within_bounds = True
        elif move == MoveAction.UP and y > 0:
            y1 = y - 1
            within_bounds = True
        elif move == MoveAction.DOWN and y < self.N - 1:
            y1 = y + 1
            within_bounds = True
        # check that the wolf does not move on the hole
        # or the rabbit does not move on the wolf
        if within_bounds:
            if obj == Objects.WOLF:
                return self.grid[x1][y1] != Objects.HOLE
            if obj == Objects.RABBIT:
                return self.grid[x1][y1] != Objects.WOLF
        return False

    def move_obj(self, obj, move):
        # TODO: verify its a legal move, throw exception
        x, y = self.find_object(obj)
        if move == MoveAction.LEFT:
            touched = self.grid[x - 1][y]
            self.grid[x - 1][y] = obj
        elif move == MoveAction.RIGHT:
            touched = self.grid[x + 1][y]
            self.grid[x + 1][y] = obj
        elif move == MoveAction.UP:
            touched = self.grid[x][y - 1]
            self.grid[x][y - 1] = obj
        elif move == MoveAction.DOWN:
            touched = self.grid[x][y + 1]
            self.grid[x][y + 1] = obj
        self.grid[x][y] = Objects.NOTHING
        if obj == Objects.RABBIT and touched == Objects.HOLE:
            self.status = GameStatus.RABBIT_WON
        elif obj == Objects.WOLF and touched == Objects.RABBIT:
            self.status = GameStatus.WOLF_WON
        return touched

    def get_observation(self):
        return self.status, self.grid

    def find_object(self, obj):
        for x in range(self.N):
            for y in range(self.N):
                if self.grid[x][y] == obj:
                    return x, y
        # could not find the object
        raise RuntimeError
