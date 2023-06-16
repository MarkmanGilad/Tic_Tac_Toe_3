from State import State
import numpy as np

class TicTacToe:
    def __init__(self, state = None) -> None:
        self.state = state

    def move (self, action):
        self.state.board[action] = self.state.player
        self.switch_players(self.state)
        self.end_of_game(self.state)

    def switch_players (self, state):
        if state.player == 1:
            state.player = -1
        else:
            state.player = 1

    def legal (self, state: State, action):
        if state.board[action] == 0:
            return True
        return False
    
    def end_of_game (self, state: State):
        board = state.board
        row_sum = np.sum(board, axis= 1)
        col_sum = np.sum(board, axis= 0)
        diagonals = [np.trace(board), np.trace(np.fliplr(board))]
        piece_num = np.count_nonzero(board)

        # print (f'row_sum: {row_sum} col_sum: {col_sum} diagonals {diagonals}')
        if 3 in row_sum or 3 in col_sum or 3 in diagonals:
            state.end_of_game = 1
            return True
        if -3 in row_sum or -3 in col_sum or -3 in diagonals:
            state.end_of_game = -1
            return True
        if piece_num == 9:
            state.end_of_game = 2
            return True
        return False
        