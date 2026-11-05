# You may implement your code in this file
# Please read the README file for the rules and implementation support

"""
Attributes of state (input):
    state.board: List[cell] = Shows the current game board as a list of cells
    state.bot_id: Int = ID number assigned to your bot
    state.is_priority_token: Bool = Tells if your bot currently has the priority token or not
    state.legal_actions: List[str] = List of all possible legal actions the bot can make for current turn

Attributes of cell (element of state.board):
    cell.occupant: Int = Bot ID of the bot currently on the cell (0 means no bot is currently on the cell)
    cell.owner: Int = Bot ID of the bot that owns the cell (0 means no bot currently owns the cell)
    cell.is_upgraded: Bool = Tells if the cell is upgraded or not
    cell.is_home: Bool = Tells if the cell is a home cell of a bot or not
    cell.base_points: Int = Gives the base points of the cell based on its position on the board
    cell.is_frozen: Bool = Tells whether the cell is currently frozen or not

Expected output:
    Exactly one of the strings in the list 'state.legal_actions'. You may assume that state.legal_actions is never empty.
"""

def act(state): # Do not change or modify this function signature
    # Write this function
    return "STAY" # Feel free to change this line

# You are allowed to add your own functions in the rest of this file.
# But only the value returned by the 'act' function will be considered as the bot's official move.
# Illegal return values are treated as "STAY" by default