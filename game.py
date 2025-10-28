# game.py

class GameState:
    """
    Represents a Tic-Tac-Toe board.
    Board is a list of length 9, indices 0..8.
    'X' for MAX, 'O' for MIN, or None for empty.
    """

    def __init__(self, board=None, to_move='X'):
        if board is None:
            self.board = [None] * 9
        else:
            self.board = board[:]
        self.to_move = to_move  # 'X' or 'O'

    def get_legal_actions(self):
        return [i for i, v in enumerate(self.board) if v is None]

    def generate_successor(self, action):
        newb = self.board[:]
        newb[action] = self.to_move
        next_to = 'O' if self.to_move == 'X' else 'X'
        return GameState(newb, next_to)

    def is_terminal(self):
        return (self.winner() is not None) or (all(v is not None for v in self.board))

    def winner(self):
        wins = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for (i,j,k) in wins:
            if self.board[i] is not None and self.board[i] == self.board[j] == self.board[k]:
                return self.board[i]
        return None

    def utility(self):
        w = self.winner()
        if w == 'X':
            return +1
        elif w == 'O':
            return -1
        else:
            return 0

    def __str__(self):
        def v(i):
            return self.board[i] if self.board[i] is not None else ' '
        s = ""
        for r in range(3):
            s += f"{v(3*r)}|{v(3*r+1)}|{v(3*r+2)}\n"
            if r<2:
                s += "-+-+-\n"
        return s
