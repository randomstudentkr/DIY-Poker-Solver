# Variant 1: Last Taker Wins
def possible_new_states_last_win(state):
    for pile, counters in enumerate(state):
        for remain in range(counters):
            yield state[:pile] + (remain,) + state[pile + 1 :]

def evaluate_last_win(state, is_maximizing):
    if all(counters == 0 for counters in state):
        return -1 if is_maximizing else 1

# Variant 2: Split Pile
def possible_new_states_split(state):
    """
    The following are an equivalent code, provided by the author of the article:
    for pile, counters in enumerate(state):
        for take in range(1, (counters + 1) // 2):
            yield state[:pile] + (counters - take, take) + state[pile + 1 :]
    """
    for pile, counters in enumerate(state):
        for i in range(1, counters//2+counters%2):
            yield state[:pile] + (i, counters - i,) + state[pile + 1 :]

def evaluate_split(state, is_maximizing):
    if all(counters <= 2 for counters in state):
        return -1 if is_maximizing else 1

def minimax(state, is_maximizing, possible_new_states, evaluate):
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
    
    if (score := evaluate(state, is_maximizing)) is not None:
        return score
    
    scores = [
        minimax(new_state, not is_maximizing, possible_new_states, evaluate) for new_state in possible_new_states(state)
    ]
    return (max if is_maximizing else min)(scores)

def best_move(state, possible_new_states, evaluate):
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

    if not list(possible_new_states(state)):
        return 1, state
    
    for new_state in possible_new_states(state):
        score = minimax(
            new_state, False, possible_new_states, evaluate
        )
        if score > 0:
            break
    return score, new_state
