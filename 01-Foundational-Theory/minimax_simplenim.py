# The code has been copied from https://realpython.com/python-minimax-nim/#lose-the-game-of-nim-against-a-python-minimax-player
# and edited by me.

def minimax_old(state, max_turn):
    """Calculate the minimax score

    This function takes the current state and whose turn it is and calculates the minimax score

    Args:
        state (int): The current number of counters on the table
        max_turn (bool): The indicator that tells whether it is Maximillian's turn or not
    
    Returns:
        int: The calculated minimax score
    """
    
    # Maximillian wins if it is his turn and the state is zero
    if state == 0:
        return 1 if max_turn else -1
    
    # For the cases where there are >=1 counter(s)
    possible_new_states = [
        state - take for take in (1, 2, 3) if take <= state
    ]
    if max_turn: # If it is Maximillian's turn, then the maximum possible score is bubbled up
        scores = [
            minimax(new_state, max_turn=False) for new_state in possible_new_states
        ]
        return max(scores)
    else: # Otherwise, i.e., if it is Mindy's turn, then the minimum possible score is bubbled up
        scores = [
            minimax(new_state, max_turn=True) for new_state in possible_new_states
        ]
        return min(scores)

def best_move_old(state):
    # returns the maximum score and the corresponding new state
    # state is the current number of counters on the table
    # if the return is (1, x), then taking state - x counters will lead Maximillain to win
    # if the return is (-1, x), then Maximillian can't win

    for take in (1, 2, 3):
        new_state = state - take
        score = minimax(new_state, max_turn=False)
        if score > 0:
            break
    return score, new_state

"""
To be more general, separate the game rules and minimax algorithm
The following two functions implement the rules of simple-nim.
"""

def possible_new_states_simple(state):
    return [state - take for take in (1, 2, 3) if take <= state]

def evaluate_simple(state, is_maximizing):
    if state == 0:
        return 1 if is_maximizing else -1

def minimax_simple(state, is_maximizing):
    """Calculate the minimax score

    This function takes the current state and whose turn it is and calculates the minimax score.
    It first investigates if the game has ended, where in that case returns the evaluation of the game.
    When there remain some counters on the table yet:
        if the current player is maximizing, then the maximum possible score is bubbled up from children states;
        otherwise, then the minimum possible score is bubbled up.

    Args:
        state (int): The current number of counters on the table
        is_maximizing (bool): The indicator that tells whether the current player is in the maximizing position or not
    
    Returns:
        int: The calculated minimax score
    """
    
    if (score := evaluate_simple(state, is_maximizing)) is not None:
        return score
    
    scores = [
        minimax(new_state, is_maximizing=not is_maximizing) for new_state in possible_new_states_simple(state)
    ]
    return (max if is_maximizing else min)(scores)

def best_move_simple(state):
    """
    This function returns the best move for the maximizing player with an indicator that tells he will win or not.
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
        score = minimax(new_state, is_maximizing=False)
        if score > 0:
            break
    return score, new_state
