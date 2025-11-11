# Functions for implementing the rules of the game of Nim
def possible_new_states_simple(state):
    return [state - take for take in (1, 2, 3) if take <= state]

def evaluate_simple(state, is_maximizing):
    """Calculates the score if the game ends in this turn

    Args:
        state (int): The current number of counters on the table

    Returns:
        int: 1 if the current player has won and -1 o.w.
    """

    if state == 0:
        return 1 if is_maximizing else -1

# Function for the minimax algorithm
def minimax_simple(state, is_maximizing):
    """Calculates the minimax score

    This function takes the current state and whose turn it is and calculates the minimax score.
    It first investigates if the game has ended, where in that case returns the evaluation of the game.
    When there remain some counters on the table yet:
        

    Args:
        state (int): The current number of counters on the table
        is_maximizing (bool): The indicator that tells whether the current player is in the maximizing position or not
    
    Returns:
        int: The calculated minimax score
    """
    
    # Check if the game ends in this turn
    if (score := evaluate_simple(state, is_maximizing)) is not None:
        return score
    
    # If the current player is maximizing, then the maximum possible score is bubbled up from children states.
    # Otherwise, the minimum possible score is bubbled up.
    scores = [
        minimax_simple(new_state, is_maximizing=not is_maximizing) for new_state in possible_new_states_simple(state)
    ]
    return (max if is_maximizing else min)(scores)

# The bot implementing Nash-Equilibrium for the game of simple nim.
def best_move_simple(state):
    """Returns the best move for the maximizing player with an indicator that tells he will win or not.
    
    If the return is:
        (1, x), then taking state - x counters will lead him to win;
        (-1, x), then he can't win.
    
    Args:
        state (int): The current number of counters on the table

    Returns:
        (int, int): The maximum score (-1 or 1) and the corresponding new state
    """

    if not possible_new_states_simple(state):
        return 1, 0
    
    for new_state in possible_new_states_simple(state):
        score = minimax_simple(new_state, is_maximizing=False)
        if score > 0:
            break
    return score, new_state
