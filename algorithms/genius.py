##Task 1

# def calculate(a, b, c):
#     if a+b>c and a+c>b and b+c>a:
#         if a == b == c:
#             return "Equilateral"
#         elif a == b or b == c or a == c:
#             return "Isosceles"
#         elif a != b != c:
#             return "Scalene"
#     else:
#         return "Not a triangle"
# def main():
#     case = int(input())
#     results = []

#     for _ in range(case):
#         parts = input().split(",")
#         a = int(parts[0])
#         b = int(parts[1])
#         c = int(parts[2])
#         #a, b, c = map(int, parts)
#         results.append(calculate(a, b, c))

#     print()
#     for res in results:
#         print(res)

# if __name__ == "__main__":
#     main()




# #Task 2
# def calculate(x, y):
#     return x + y if x != y else 2 * (x + y)

# def main():
#     case = int(input())
#     results = []

#     for _ in range(case):
#         parts = input().split()
#         x = int(parts[0])
#         y = int(parts[1])
#         # x, y = map(int, parts)
#         results.append(calculate(x, y))

#     print()
#     for res in results:
#         print(res)

# if __name__ == "__main__":
#     main()




# #Task 3 
# def calculate(can, plastic, glass):
#     full = ((can * 31 * 5) + (plastic * 15 * 10) + (glass / 2 * 20))/100
#     return (f"${full:.2f}")

# def main():
#     case = int(input())
#     results = []

#     for _ in range(case):
#         parts = input().split()
#         can = int(parts[0]) if len(parts) > 0 else 0
#         plastic = int(parts[1]) if len(parts) > 1 else 0
#         glass = int(parts[2]) if len(parts) > 2 else 0
#         results.append(calculate(can, plastic, glass))
        
#     print()
#     for res in results:
#         print(res)
        
# if __name__ == "__main__":
#     main()



## Task 4 list of people, somehow broken input

# import ast

# def fix_input_data(data_line):
#     fixed = ''
#     i = 0
#     word = ''
#     while i < len(data_line):
#         c = data_line[i]
#         if c in '[,]':
#             if word:
#                 word = word.strip()
#                 if not word.replace('.', '').isdigit():
#                     word = f'"{word}"'
#                 fixed += word
#                 word = ''
#             fixed += c
#         elif c in '\n ':
#             if word:
#                 word += ' '
#         else:
#             word += c
#         i += 1
#     if word:
#         word = word.strip()
#         if not word.replace('.', '').isdigit():
#             word = f'"{word}"'
#         fixed += word
#     return fixed

# T = int(input())

# for _ in range(T):
#     num_people = int(input())
#     raw_data = ''
#     bracket_count = 0
#     while True:
#         line = input().strip()
#         raw_data += line
#         bracket_count += line.count('[')
#         bracket_count -= line.count(']')
#         if bracket_count == 0 and raw_data.count('[') == raw_data.count(']'):
#             break

#     fixed_data = fix_input_data(raw_data)
#     parsed = ast.literal_eval(fixed_data)

#     names = parsed[0]
#     ages = parsed[1]
#     instagrams = parsed[2]
#     twitters = parsed[3]
#     phones = parsed[4]
#     emails = parsed[5]

#     people = {}
#     for i in range(num_people):
#         people[names[i]] = {
#             'Age': ages[i],
#             'Instagram': instagrams[i],
#             'Twitter': twitters[i],
#             'Phone': ''.join(c for c in str(phones[i]) if c.isdigit()),
#             'Email': emails[i]
#         }

#     for _ in range(num_people):
#         person = input().strip()
#         data = people[person]
#         print(f"Name: {person}")
#         print(f"Age: {data['Age']}")
#         print(f"Instagram: {data['Instagram']}")
#         print(f"Twitter: {data['Twitter']}")
#         print(f"Phone: {data['Phone']}")
#         print(f"Email: {data['Email']}")




# Task 5 Pascal's Triangle largest number in a row

# def calculate(n):
#     k = n // 2
#     if k > n - k:
#         k = n - k
#     res = 1
#     for i in range(1, k + 1):
#         res = res * (n - k + i) // i
#     return res

# def main():
#     case = int(input())
#     results = []

#     for _ in range(case):
#         parts = input().split()
#         n = int(parts[0]) if len(parts) > 0 else 0
#         results.append(calculate(n))

#     print()
#     for ans in results:
#         print(ans)

# if __name__ == "__main__":
#     main()



## Another Task 5 variant: Pascal's Triangle 

# def generate(numRows):
#     """
#     Return the first numRows of Pascal's Triangle as a list of lists.
#     Row 0 = [1], row 1 = [1, 1], etc.
#     """
#     if numRows == 0:
#         return []
#     res = [[1]]
#     for _ in range(numRows - 1):
#         prev = res[-1]
#         temp = [0] + prev + [0]
#         row = [temp[j] + temp[j+1] for j in range(len(prev) + 1)]
#         res.append(row)
#     return res

# def main():
#     numRows = int(input().strip())
#     triangle = generate(numRows)
#     print(triangle)

# if __name__ == "__main__":
#     main()



## Task 6
# def calculate(numbers):
#     """
#     Return True if there is any "triplet" (an element occurring >= 3 times).
#     Otherwise return False.
#     """
#     counts = {}
#     for x in numbers:
#         counts[x] = counts.get(x, 0) + 1         # tally occurrences
#         if counts[x] >= 3:
#             return True                          # found a triplet
#     return False                                 # no triplets found

# def main():
#     case = int(input().strip())
#     results = []
#     for _ in range(case):
#         numbers = input().split()               
#         results.append(calculate(numbers))      

#     print()
#     for res in results:
#         print(res)

# if __name__ == "__main__":
#     main()



# # Task 7. Chess

# # Constants for piece characters
# EMPTY = '.'
# WHITE_PIECES = "PRNBQK"
# BLACK_PIECES = "prnbqk"

# # Knight move offsets (dr, dc)
# KNIGHT_MOVES = [
#     (-2, -1), (-2, 1), (-1, -2), (-1, 2),
#     (1, -2), (1, 2), (2, -1), (2, 1)
# ]

# # King and general line piece move offsets (8 directions)
# LINE_DIRECTIONS = [
#     (-1, -1), (-1, 0), (-1, 1), (0, -1),
#     (0, 1), (1, -1), (1, 0), (1, 1)
# ]
# ROOK_DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# BISHOP_DIRECTIONS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


# def get_piece_color(piece_char):
#     """Determines the color of a piece."""
#     if piece_char == EMPTY:
#         return None
#     return 'white' if piece_char.isupper() else 'black'

# def find_king(board, color):
#     """Finds the king of a given color on the board."""
#     king_char = 'K' if color == 'white' else 'k'
#     for r in range(8):
#         for c in range(8):
#             if board[r][c] == king_char:
#                 return r, c
#     return None # Should not happen in a valid game

# def is_on_board(r, c):
#     """Checks if coordinates are within the board."""
#     return 0 <= r < 8 and 0 <= c < 8

# def is_path_clear(board, r1, c1, r2, c2):
#     """
#     Checks if the path between (r1, c1) and (r2, c2) is clear (exclusive of endpoints).
#     Assumes (r1, c1) and (r2, c2) are on the same line (horizontal, vertical, or diagonal).
#     """
#     dr = 0 if r1 == r2 else (1 if r2 > r1 else -1)
#     dc = 0 if c1 == c2 else (1 if c2 > c1 else -1)
    
#     curr_r, curr_c = r1 + dr, c1 + dc
#     while curr_r != r2 or curr_c != c2: # Iterate until one step before the target
#         if not is_on_board(curr_r, curr_c): # Should not happen if r2,c2 is on board and on line
#             return False 
#         if board[curr_r][curr_c] != EMPTY:
#             return False  # Path is blocked
#         curr_r += dr
#         curr_c += dc
#     return True

# def get_raw_moves_for_piece(board, r_from, c_from):
#     """
#     Generates all mechanically possible moves for a piece at (r_from, c_from),
#     including captures, ignoring check rules for now.
#     Returns a list of (r_to, c_to) tuples.
#     """
#     moves = []
#     piece = board[r_from][c_from]
#     if piece == EMPTY:
#         return []

#     color = get_piece_color(piece)
#     ptype = piece.lower()

#     # Pawn moves
#     if ptype == 'p':
#         direction = 1 if color == 'black' else -1  # Black pawns move down (row index increases), white up
#         start_row = 1 if color == 'black' else 6

#         # Move one step forward
#         if is_on_board(r_from + direction, c_from) and board[r_from + direction][c_from] == EMPTY:
#             moves.append((r_from + direction, c_from))
#             # Move two steps forward from starting position
#             if r_from == start_row and board[r_from + 2 * direction][c_from] == EMPTY:
#                 moves.append((r_from + 2 * direction, c_from))
        
#         # Captures
#         for dc_capture in [-1, 1]:
#             r_to, c_to = r_from + direction, c_from + dc_capture
#             if is_on_board(r_to, c_to):
#                 target_piece = board[r_to][c_to]
#                 if target_piece != EMPTY and get_piece_color(target_piece) != color:
#                     moves.append((r_to, c_to))
    
#     # Knight moves
#     elif ptype == 'n':
#         for dr, dc in KNIGHT_MOVES:
#             r_to, c_to = r_from + dr, c_from + dc
#             if is_on_board(r_to, c_to):
#                 target_piece = board[r_to][c_to]
#                 if target_piece == EMPTY or get_piece_color(target_piece) != color:
#                     moves.append((r_to, c_to))

#     # King moves
#     elif ptype == 'k':
#         for dr, dc in LINE_DIRECTIONS: # King moves one step in any of 8 directions
#             r_to, c_to = r_from + dr, c_from + dc
#             if is_on_board(r_to, c_to):
#                 target_piece = board[r_to][c_to]
#                 if target_piece == EMPTY or get_piece_color(target_piece) != color:
#                     moves.append((r_to, c_to))
    
#     # Rook, Bishop, Queen moves (line pieces)
#     else: # 'r', 'b', 'q'
#         current_directions = []
#         if ptype == 'r':
#             current_directions = ROOK_DIRECTIONS
#         elif ptype == 'b':
#             current_directions = BISHOP_DIRECTIONS
#         elif ptype == 'q':
#             current_directions = LINE_DIRECTIONS # All 8 directions

#         for dr, dc in current_directions:
#             for k in range(1, 8): # Max 7 steps
#                 r_to, c_to = r_from + k * dr, c_from + k * dc
#                 if not is_on_board(r_to, c_to):
#                     break 
                
#                 target_piece = board[r_to][c_to]
#                 if target_piece == EMPTY:
#                     moves.append((r_to, c_to))
#                 else:
#                     if get_piece_color(target_piece) != color: # Opponent piece
#                         moves.append((r_to, c_to))
#                     break # Path blocked by own or opponent piece

#     return moves


# def is_square_attacked(board, r_target, c_target, attacker_color):
#     """Checks if the square (r_target, c_target) is attacked by any piece of attacker_color."""
#     for r_piece in range(8):
#         for c_piece in range(8):
#             piece_char = board[r_piece][c_piece]
#             if piece_char == EMPTY or get_piece_color(piece_char) != attacker_color:
#                 continue

#             ptype = piece_char.lower()
            
#             # Pawn attacks are specific (diagonal forward)
#             if ptype == 'p':
#                 pawn_dir = 1 if attacker_color == 'black' else -1
#                 if r_target == r_piece + pawn_dir:
#                     if c_target == c_piece - 1 or c_target == c_piece + 1:
#                         return True
#             # For other pieces, we can check if their raw moves can reach the target square
#             # This requires careful handling of line-of-sight for R, B, Q
#             elif ptype == 'n':
#                  for dr_knight, dc_knight in KNIGHT_MOVES:
#                     if r_piece + dr_knight == r_target and c_piece + dc_knight == c_target:
#                         return True
#             elif ptype == 'k':
#                 for dr_king, dc_king in LINE_DIRECTIONS:
#                      if r_piece + dr_king == r_target and c_piece + dc_king == c_target:
#                         return True
#             else: # Rook, Bishop, Queen
#                 is_line_piece = False
#                 correct_direction = False
#                 if ptype == 'r':
#                     if r_piece == r_target or c_piece == c_target:
#                         is_line_piece = True
#                         correct_direction = True
#                 elif ptype == 'b':
#                     if abs(r_piece - r_target) == abs(c_piece - c_target):
#                         is_line_piece = True
#                         correct_direction = True
#                 elif ptype == 'q':
#                     if r_piece == r_target or c_piece == c_target or \
#                        abs(r_piece - r_target) == abs(c_piece - c_target):
#                         is_line_piece = True
#                         correct_direction = True
                
#                 if is_line_piece and correct_direction:
#                     if is_path_clear(board, r_piece, c_piece, r_target, c_target):
#                         return True
#     return False


# def get_all_legal_moves(current_board, color_to_move):
#     """
#     Generates all legal moves for the player 'color_to_move'.
#     A move is legal if it does not leave the player's own king in check.
#     Returns a list of ((from_r, from_c), (to_r, to_c)) tuples.
#     """
#     legal_moves = []
#     opponent_color = 'black' if color_to_move == 'white' else 'white'

#     for r_from in range(8):
#         for c_from in range(8):
#             piece = current_board[r_from][c_from]
#             if piece == EMPTY or get_piece_color(piece) != color_to_move:
#                 continue

#             raw_moves = get_raw_moves_for_piece(current_board, r_from, c_from)
            
#             for r_to, c_to in raw_moves:
#                 # Simulate the move on a temporary board
#                 temp_board = [row[:] for row in current_board] # Deep copy
#                 temp_board[r_to][c_to] = temp_board[r_from][c_from]
#                 temp_board[r_from][c_from] = EMPTY
                
#                 # Find the king of 'color_to_move' on this temporary board
#                 king_pos_after_move = find_king(temp_board, color_to_move)
#                 if king_pos_after_move is None: continue # Should not happen

#                 # Check if the king is safe after this move
#                 if not is_square_attacked(temp_board, king_pos_after_move[0], king_pos_after_move[1], opponent_color):
#                     legal_moves.append(((r_from, c_from), (r_to, c_to)))
#     return legal_moves


# def solve():
#     """Solves a single test case."""
#     board_str = [input() for _ in range(8)]
#     board = [list(row) for row in board_str]

#     white_king_pos = find_king(board, 'white')
#     black_king_pos = find_king(board, 'black')

#     if not white_king_pos or not black_king_pos:
#         print("Error: King not found. Invalid board.") # Should not happen with valid input
#         return

#     is_white_king_attacked = is_square_attacked(board, white_king_pos[0], white_king_pos[1], 'black')
#     is_black_king_attacked = is_square_attacked(board, black_king_pos[0], black_king_pos[1], 'white')

#     player_in_check = None
#     winning_color_if_mate = None

#     if is_white_king_attacked:
#         player_in_check = 'white'
#         winning_color_if_mate = 'BLACK'
#     elif is_black_king_attacked:
#         player_in_check = 'black'
#         winning_color_if_mate = 'WHITE'
#     else:
#         print("NO CHECKMATE")
#         return

#     # Now, 'player_in_check' is the one whose turn it is (because they are in check)
#     # We need to see if they have any legal moves to get out of check.
    
#     all_possible_legal_moves = get_all_legal_moves(board, player_in_check)

#     if not all_possible_legal_moves: # No legal moves to escape check
#         print(f"CHECKMATE {winning_color_if_mate}")
#     else:
#         print("NO CHECKMATE")


# # Main part of the script
# if __name__ == "__main__":
#     num_test_cases = int(input())
#     for _ in range(num_test_cases):
#         solve()






##Task 8. Surveillance
## This task involves checking if a line of sight between a spy and a camera is blocked by walls.

# class Point:
#     __slots__ = ('x', 'y')

#     def __init__(self, x_coord, y_coord):
#         self.x = int(x_coord)
#         self.y = int(y_coord)

# def on_segment(p, q, r):
#     return (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and
#             q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y))

# def orientation(p, q, r):
#     val = (q.y - p.y) * (r.x - q.x) - \
#           (q.x - p.x) * (r.y - q.y)
#     if val == 0: return 0  # Collinear
#     return 1 if val > 0 else 2  # Clockwise or Counterclockwise

# def do_segments_intersect(p1, q1, p2, q2):
#     o1 = orientation(p1, q1, p2)
#     o2 = orientation(p1, q1, q2)
#     o3 = orientation(p2, q2, p1)
#     o4 = orientation(p2, q2, q1)

#     if o1 != 0 and o2 != 0 and o3 != 0 and o4 != 0:
#         if (o1 != o2) and (o3 != o4):
#             return True
#     else: 
#         if o1 == 0 and on_segment(p1, p2, q1): return True
#         if o2 == 0 and on_segment(p1, q2, q1): return True
#         if o3 == 0 and on_segment(p2, p1, q2): return True
#         if o4 == 0 and on_segment(p2, q1, q2): return True
            
#     return False

# def solve_test_case():
#     line1_parts = input().split()
#     spy_x, spy_y = int(line1_parts[0]), int(line1_parts[1])
#     cam_x, cam_y = int(line1_parts[2]), int(line1_parts[3])
#     num_walls = int(line1_parts[4])
    
#     spy = Point(spy_x, spy_y)
#     camera = Point(cam_x, cam_y)
    
#     line_of_sight_p1 = spy
#     line_of_sight_q1 = camera

#     is_hidden = False
#     for _ in range(num_walls):
#         wall_parts = input().split()
#         wall_x1, wall_y1 = int(wall_parts[0]), int(wall_parts[1])
#         wall_x2, wall_y2 = int(wall_parts[2]), int(wall_parts[3])
        
#         if not is_hidden: # Only check if not already confirmed hidden
#             wall_p1 = Point(wall_x1, wall_y1)
#             wall_q2 = Point(wall_x2, wall_y2)
#             if do_segments_intersect(line_of_sight_p1, line_of_sight_q1, wall_p1, wall_q2):
#                 is_hidden = True
#         # If already hidden, we still need to consume the input line for the current wall,
#         # which is done by the input().split() call above.
    
#     if is_hidden:
#         print("NO")
#     else:
#         print("YES")

# num_test_cases = int(input())
# for _ in range(num_test_cases):
#     solve_test_case()



## Task 9. Infix to RPN (Reverse Polish Notation) conversion

# def get_precedence(op):
#     if op == '^':
#         return 4  # Higher precedence for exponentiation
#     if op == '*' or op == '/':
#         return 3
#     if op == '+' or op == '-':
#         return 2
#     if op == '(' or op == ')': # Parentheses have lowest precedence in this context
#         return 1
#     return 0 # For operands or unknown characters

# def is_operator(char):
#     return char in ['+', '-', '*', '/', '^']

# def is_right_associative(op):
#     return op == '^'

# def infix_to_rpn(exp):
#     out = []
#     operator = []

#     for token in exp:
#         if token.isalnum():  # Operand (letter or number)
#             out.append(token)
#         elif is_operator(token):
#             while (operator and is_operator(operator[-1]) and
#                    operator[-1] != '(' and
#                    (get_precedence(operator[-1]) > get_precedence(token) or
#                     (get_precedence(operator[-1]) == get_precedence(token) and not is_right_associative(token)))):
#                 out.append(operator.pop())
#             operator.append(token)
#         elif token == '(':
#             operator.append(token)
#         elif token == ')':
#             while operator and operator[-1] != '(':
#                 if not operator:
#                     pass
#                 out.append(operator.pop())
#             if operator and operator[-1] == '(':
#                 operator.pop() # Pop the '('
#             else:
#                 pass
    
#     while operator:
#         if operator[-1] == '(' :
#              operator.pop() # Discard mismatched parenthesis
#         else:
#             out.append(operator.pop())
            
#     return out

# def solve_single_expression():
#     expression_str = input()
#     tokens = expression_str.split(' ')
#     rpn_expression = infix_to_rpn(tokens)
#     print(" ".join(rpn_expression))

# def solve_test_case():
#     num_expressions = int(input())
#     for _ in range(num_expressions):
#         solve_single_expression()

# num_test_cases = int(input())
# for _ in range(num_test_cases):
#     solve_test_case()









## Other -----------------------------------------------------------------------

## Calculate the change

# def make_change(amount, coins):
#     coins.sort(reverse=True)
#     result = []
#     for c in coins:
#         count = amount // c
#         if count:
#             result += [c] * count
#             amount -= c * count
#     return result if amount == 0 else None

# def main():
#     amt = int(input().strip())
#     coins = list(map(int, input().split()))
#     solution = make_change(amt, coins)
#     if solution is None:
#         print("No solution")
#     else:
#         print(solution)

# if __name__ == "__main__":
#     main()




## D&C Algorithm --------------------------------------------------------

# def sum(arr):
#     total = 0
#     for x in arr:
#         total += x
#         return total
# print(sum([1, 2, 3, 4]))



# def sum_list(lst):
#     if lst == []:
#         return 0
#     return lst[0] + sum_list(lst[1:])

# print(sum_list([2, 4, 6]))



# def count_items(lst):
#     if lst == []:
#         return 0
#     return 1 + count_items(lst[1:])

# print(count_items([2, 4, 6]))



# def find_max(lst):
#     if len(lst) == 1:
#         return lst[0]
#     max_of_rest = find_max(lst[1:])
#     return lst[0] if lst[0] > max_of_rest else max_of_rest

# print(find_max([2, 4, 6, 8, 1]))




# def binary_search(lst, target, low=0, high=None):
#     if high is None:
#         high = len(lst) - 1
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     if lst[mid] == target:
#         return mid
#     elif lst[mid] > target:
#         return binary_search(lst, target, low, mid - 1)
#     else:
#         return binary_search(lst, target, mid + 1, high)

# print(binary_search([1, 3, 5, 7, 9], 5))






## Quick Sort -------------------------------------------------------------------

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
# def main():
#     arr = list(map(int, input("Enter numbers separated by space: ").split()))
#     sorted_arr = quick_sort(arr)
#     print("Sorted array:", sorted_arr)
# if __name__ == "__main__":
#     main()



# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)
# print(quicksort([10, 5, 2, 3]))



## The knapsack problem -------------------------------------------------------------------

# def knapsack_01(weights, values, capacity):
#     n = len(values)
#     dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         for w in range(1, capacity + 1):
#             if weights[i - 1] <= w:
#                 dp[i][w] = max(
#                     values[i - 1] + dp[i - 1][w - weights[i - 1]],
#                     dp[i - 1][w]
#                 )
#             else:
#                 dp[i][w] = dp[i - 1][w]

#     return dp[n][capacity]

# weights = [10, 20, 30]
# values = [60, 100, 120]
# capacity = 35

# max_value = knapsack_01(weights, values, capacity)
# print("Maximum value:", max_value)






# states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
# stations = {
#     "kone": {"id", "nv", "ut"},
#     "ktwo": {"wa", "id", "mt"},
#     "kthree": {"or", "nv", "ca"},
#     "kfour": {"nv", "ut"},
#     "kfive": {"ca", "az"},
# }
# final_stations = set()
# while states_needed:
#     best_station = None
#     states_covered = set()
#     for station, states in stations.items():
#         covered = states_needed & states
#         if len(covered) > len(states_covered):
#             best_station = station
#             states_covered = covered
#     states_needed -= states_covered
#     final_stations.add(best_station)

# print("Selected stations:", final_stations)




## Similar Task 1

# def calculate(a, b, c, d):
#     sides = [a, b, c, d]
#     unique = set(sides)
#     if len(unique) == 1:
#         return "Square"
#     elif len(unique) == 2 and (sides.count(list(unique)[0]) == 2 or sides.count(list(unique)[1]) == 2):
#         return "Rectangle"
#     else:
#         return "Not a Rectangle"


# def main():
#     case = int(input())
#     results = []
#     for _ in range(case):
#         parts = input().replace(" ", "").split(",")
#         a, b, c, d = map(int, parts)
#         results.append(calculate(a, b, c, d))
#     print()
#     for res in results:
#         print(res)


# if __name__ == "__main__":
#     main()




## Similar Task 2

# def calculate(x, y): 
#     if abs(x-y) > 10:
#         return min(x, y)
#     else:
#         return (x+y)**2
# def main():
#     case = int(input())
#     results = []
#     for _ in range(case):
#         parts = input().split()
#         x, y = map(int, parts)
#         results.append(calculate(x, y))
#     print()
#     for res in results:
#         print(res)

# if __name__ == "__main__":
#     main()




## Similar Task 3

# def calculate(food, yard, paper):
#     half = (food*3) + (yard*2) + (paper/2)
#     full = half*0.15
#     return f"${full:.2f}"
# def main():
#     case = int(input())
#     results = []
#     for _ in range(case):
#         parts = input().split()
#         food = int(parts[0]) if len(parts) > 0 else 0
#         yard = int(parts[1]) if len(parts) > 1 else 0
#         paper = int(parts[2]) if len(parts) > 2 else 0
#         results.append(calculate(food, yard, paper))
        
#     print()
#     for res in results:
#         print(res)
# if __name__ == "__main__":
#     main()



## Similar Task 5

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)

# def main():
#     case = int(input())
#     results = []
#     for _ in range(case):
#         n = int(input().strip())
#         results.append(fib(n))
#     print()
#     for res in results:
#         print(res)

# if __name__ == "__main__":
#     main()
    
    
    
    
    

def fibRec(n, memo):
    if n <= 1:
        return n
    if memo[n] != -1:
        return memo[n]
    memo[n] = fibRec(n - 1, memo) + fibRec(n - 2, memo)

    return memo[n]

def fib(n):
    memo = [-1] * (n + 1)
    return fibRec(n, memo)

def main():
    case = int(input())
    results = []
    for _ in range(case):
        n = int(input().strip())
        results.append(fib(n))
    print()
    for res in results:
        print(res)
        
if __name__ == "__main__":
    main()