# The code has been copied from https://realpython.com/python-minimax-nim/#lose-the-game-of-nim-against-a-python-minimax-player
# and edited by me.

def minimax(state, max_turn):
    # returns the minimax score
    # `state` represents the current counters
    # `max_turn` represents if it is Maximillian's turn or not
    
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

def best_move(state):
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
