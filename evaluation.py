# evaluation.py

from game import GameState

def betterEvaluationFunction(state: GameState):
    """
    Heuristic for non-terminal Tic-Tac-Toe states.
    Score from the perspective of X (MAX).
    """
    # If terminal, just return utility
    if state.is_terminal():
        return state.utility()

    score = 0

    # Feature: center control
    center = 4
    if state.board[center] == 'X':
        score += 1
    elif state.board[center] == 'O':
        score -= 1

    # Feature: corners
    corners = [0, 2, 6, 8]
    for c in corners:
        if state.board[c] == 'X':
            score += 0.5
        elif state.board[c] == 'O':
            score -= 0.5

    # Feature: open lines (three in a row not blocked)
    lines = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for (i,j,k) in lines:
        line = [state.board[i], state.board[j], state.board[k]]
        if 'X' in line and 'O' not in line:
            # only X present
            score += 3
        elif 'O' in line and 'X' not in line:
            score -= 3

    return score