# agent_base.py

class Agent:
    def get_action(self, state, depth=None):
        """
        Given a GameState, return an integer action (0..8).
        depth: optional search depth limit (None means full search).
        """
        raise NotImplementedError("Override in subclass")
