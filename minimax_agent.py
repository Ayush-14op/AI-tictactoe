# minimax_agent.py
from agent_base import Agent
import math

class MinimaxAgent(Agent):
    def get_action(self, game_state):
        def minimax(state):
            # Base case: if the game is over, return its utility value
            if state.is_terminal():
                return state.utility(), None

            # Maximizing player (X)
            if state.player == 'X':
                best_val = -math.inf
                best_move = None
                for move in state.get_legal_actions():
                    successor = state.generate_successor(move)
                    val, _ = minimax(successor)
                    if val > best_val:
                        best_val = val
                        best_move = move
                return best_val, best_move

            # Minimizing player (O)
            else:
                best_val = math.inf
                best_move = None
                for move in state.get_legal_actions():
                    successor = state.generate_successor(move)
                    val, _ = minimax(successor)
                    if val < best_val:
                        best_val = val
                        best_move = move
                return best_val, best_move

        _, action = minimax(game_state)
        return action
