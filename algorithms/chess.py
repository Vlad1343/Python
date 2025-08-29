EMPTY = '.'
KNIGHT_MOVES = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
LINE_DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
ROOK_DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
BISHOP_DIRECTIONS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def get_piece_color(piece_char):
    if piece_char == EMPTY:
        return None
    return 'white' if piece_char.isupper() else 'black'

def is_on_board(r, c):
    return 0 <= r < 8 and 0 <= c < 8

class ChessPosition:
    def __init__(self, board_rows_str):
        self.board = [list(row) for row in board_rows_str]
        self.white_king_pos = self._find_king_initial('K')
        self.black_king_pos = self._find_king_initial('k')

    def _find_king_initial(self, king_char):
        for r in range(8):
            for c in range(8):
                if self.board[r][c] == king_char:
                    return r, c
        return None 

    def _is_path_clear(self, r1, c1, r2, c2):
        dr = 0 if r1 == r2 else (1 if r2 > r1 else -1)
        dc = 0 if c1 == c2 else (1 if c2 > c1 else -1)
        
        curr_r, curr_c = r1 + dr, c1 + dc
        while curr_r != r2 or curr_c != c2:
            if not is_on_board(curr_r, curr_c): return False 
            if self.board[curr_r][curr_c] != EMPTY:
                return False
            curr_r += dr
            curr_c += dc
        return True

    def _get_raw_moves_for_piece(self, r_from, c_from):
        moves = []
        piece = self.board[r_from][c_from]
        color = get_piece_color(piece)
        ptype = piece.lower()

        if ptype == 'p':
            direction = 1 if color == 'black' else -1
            start_row = 1 if color == 'black' else 6

            r_one_step, c_one_step = r_from + direction, c_from
            if is_on_board(r_one_step, c_one_step) and self.board[r_one_step][c_one_step] == EMPTY:
                moves.append((r_one_step, c_one_step))
                if r_from == start_row:
                    r_two_steps = r_from + 2 * direction
                    if is_on_board(r_two_steps, c_from) and self.board[r_two_steps][c_from] == EMPTY:
                        moves.append((r_two_steps, c_from))
            
            for dc_capture in [-1, 1]:
                r_to, c_to = r_from + direction, c_from + dc_capture
                if is_on_board(r_to, c_to):
                    target_piece = self.board[r_to][c_to]
                    if target_piece != EMPTY and get_piece_color(target_piece) != color:
                        moves.append((r_to, c_to))
        
        elif ptype == 'n':
            for dr, dc in KNIGHT_MOVES:
                r_to, c_to = r_from + dr, c_from + dc
                if is_on_board(r_to, c_to):
                    target_piece = self.board[r_to][c_to]
                    if target_piece == EMPTY or get_piece_color(target_piece) != color:
                        moves.append((r_to, c_to))

        elif ptype == 'k':
            for dr, dc in LINE_DIRECTIONS:
                r_to, c_to = r_from + dr, c_from + dc
                if is_on_board(r_to, c_to):
                    target_piece = self.board[r_to][c_to]
                    if target_piece == EMPTY or get_piece_color(target_piece) != color:
                        moves.append((r_to, c_to))
        
        else: 
            current_directions = []
            if ptype == 'r': current_directions = ROOK_DIRECTIONS
            elif ptype == 'b': current_directions = BISHOP_DIRECTIONS
            elif ptype == 'q': current_directions = LINE_DIRECTIONS

            for dr, dc in current_directions:
                for k_dist in range(1, 8):
                    r_to, c_to = r_from + k_dist * dr, c_from + k_dist * dc
                    if not is_on_board(r_to, c_to): break
                    
                    target_piece = self.board[r_to][c_to]
                    if target_piece == EMPTY:
                        moves.append((r_to, c_to))
                    else:
                        if get_piece_color(target_piece) != color:
                            moves.append((r_to, c_to))
                        break 
        return moves

    def is_square_attacked(self, r_target, c_target, attacker_color):
        for r_piece in range(8):
            for c_piece in range(8):
                piece_char = self.board[r_piece][c_piece]
                if piece_char == EMPTY or get_piece_color(piece_char) != attacker_color:
                    continue

                ptype = piece_char.lower()
                
                if ptype == 'p':
                    pawn_dir = 1 if attacker_color == 'black' else -1
                    if r_target == r_piece + pawn_dir and \
                       (c_target == c_piece - 1 or c_target == c_piece + 1):
                        return True
                elif ptype == 'n':
                    for dr_knight, dc_knight in KNIGHT_MOVES:
                        if r_piece + dr_knight == r_target and c_piece + dc_knight == c_target:
                            return True
                elif ptype == 'k':
                    for dr_king, dc_king in LINE_DIRECTIONS:
                        if r_piece + dr_king == r_target and c_piece + dc_king == c_target:
                            return True
                else: 
                    correct_line = False
                    if ptype == 'r':
                        if r_piece == r_target or c_piece == c_target: correct_line = True
                    elif ptype == 'b':
                        if abs(r_piece - r_target) == abs(c_piece - c_target): correct_line = True
                    elif ptype == 'q':
                        if r_piece == r_target or c_piece == c_target or \
                           abs(r_piece - r_target) == abs(c_piece - c_target): correct_line = True
                    
                    if correct_line and self._is_path_clear(r_piece, c_piece, r_target, c_target):
                        return True
        return False

    def get_all_legal_moves(self, color_to_move):
        legal_moves = []
        opponent_color = 'black' if color_to_move == 'white' else 'white'
        
        # Store original king position for restoration if the king itself moves
        original_king_pos_r, original_king_pos_c = self.white_king_pos if color_to_move == 'white' else self.black_king_pos
        
        for r_from in range(8):
            for c_from in range(8):
                piece_moved_char = self.board[r_from][c_from]
                if piece_moved_char == EMPTY or get_piece_color(piece_moved_char) != color_to_move:
                    continue

                is_king_the_one_moved = (piece_moved_char.lower() == 'k')
                raw_moves = self._get_raw_moves_for_piece(r_from, c_from)
                
                for r_to, c_to in raw_moves:
                    original_piece_at_target = self.board[r_to][c_to] # Piece to be captured
                    
                    # Make the move
                    self.board[r_to][c_to] = piece_moved_char
                    self.board[r_from][c_from] = EMPTY
                    
                    # Determine current king's position after this move
                    king_pos_to_check_r, king_pos_to_check_c = original_king_pos_r, original_king_pos_c
                    if is_king_the_one_moved:
                        king_pos_to_check_r, king_pos_to_check_c = r_to, c_to
                        # Temporarily update the central king position tracker
                        if color_to_move == 'white': self.white_king_pos = (r_to, c_to)
                        else: self.black_king_pos = (r_to, c_to)
                    
                    # Check if the king of 'color_to_move' is now attacked by 'opponent_color'
                    if not self.is_square_attacked(king_pos_to_check_r, king_pos_to_check_c, opponent_color):
                        legal_moves.append(((r_from, c_from), (r_to, c_to)))
                    
                    # Undo the move
                    self.board[r_from][c_from] = piece_moved_char
                    self.board[r_to][c_to] = original_piece_at_target 
                    if is_king_the_one_moved: # Restore king's position if it was moved
                        if color_to_move == 'white': self.white_king_pos = (original_king_pos_r, original_king_pos_c)
                        else: self.black_king_pos = (original_king_pos_r, original_king_pos_c)
        return legal_moves

def solve_case():
    board_str = [input() for _ in range(8)]
    game = ChessPosition(board_str)

    if not game.white_king_pos or not game.black_king_pos:
        # This implies an invalid board state (e.g., missing king)
        # Problem constraints usually guarantee valid setups for king-related checks.
        # If kings are missing, the concept of check/checkmate is ill-defined.
        print("NO CHECKMATE") 
        return

    w_king_r, w_king_c = game.white_king_pos
    b_king_r, b_king_c = game.black_king_pos
    
    white_is_checked = game.is_square_attacked(w_king_r, w_king_c, 'black')
    black_is_checked = game.is_square_attacked(b_king_r, b_king_c, 'white')

    player_to_move = None
    checkmate_winner_color_str = None

    if white_is_checked:
        player_to_move = 'white'
        checkmate_winner_color_str = 'BLACK' # If white is checkmated, black wins
    elif black_is_checked:
        player_to_move = 'black'
        checkmate_winner_color_str = 'WHITE' # If black is checkmated, white wins
    else:
        # Neither player is in check, so no checkmate by problem definition
        print("NO CHECKMATE")
        return
    
    legal_moves_for_player = game.get_all_legal_moves(player_to_move)

    if not legal_moves_for_player: # Player in check has no legal moves
        print(f"CHECKMATE {checkmate_winner_color_str}")
    else:
        print("NO CHECKMATE")

if __name__ == "__main__":
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        solve_case()