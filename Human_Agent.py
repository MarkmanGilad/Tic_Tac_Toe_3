from typing import Any
from TicTacToe import TicTacToe
from Graphics import *

class Human_Agent:
    def __init__(self, player, env : TicTacToe, graphics: Graphics):
        self.player = player
        self.env = env
        self.graphics = graphics

    def get_action (self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                action = self.graphics.calc_row_col(pos)
                if self.env.legal(self.env.state, action):
                    return action
        return None
    
    def __call__(self, events):
        return self.get_action(events)
    