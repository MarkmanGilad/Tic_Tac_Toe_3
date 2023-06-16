from Graphics import *
import numpy as np


class State:
    def __init__(self, board = None, player = 1):
        if board is not None:
            self.board = board
        else:
            self.board = self.init_board()
        self.player = player
        self.end_of_game = 0

    def init_board (self):
        board = np.zeros((ROWS, COLS))
        return board
                