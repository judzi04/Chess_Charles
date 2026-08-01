import chess
import time

piece_values = {
    chess.PAWN: 100,
    chess.KNIGHT: 310,
    chess.BISHOP: 320,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000,
}

PAWN_TABLE = [
     0,  0,  0,  0,  0,  0,  0,  0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
     5,  5, 10, 25, 25, 10,  5,  5,
     0,  0,  0, 20, 20,  0,  0,  0,
     5, -5,-10,  0,  0,-10, -5,  5,
     5, 10, 10,-20,-20, 10, 10,  5,
     0,  0,  0,  0,  0,  0,  0,  0
]
KNIGHT_TABLE = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20,   0,   0,   0,   0, -20, -40,
    -30,   0,  10,  15,  15,  10,   0, -30,
    -30,   5,  15,  20,  20,  15,   5, -30,
    -30,   0,  15,  20,  20,  15,   0, -30,
    -30,   5,  10,  15,  15,  10,   5, -30,
    -40, -20,   0,   5,   5,   0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50,
]
BISHOP_TABLE = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10,   0,   0,   0,   0,   0,   0, -10,
    -10,   0,   5,  10,  10,   5,   0, -10,
    -10,   5,   5,  10,  10,   5,   5, -10,
    -10,   0,  10,  10,  10,  10,   0, -10,
    -10,  10,  10,  10,  10,  10,  10, -10,
    -10,   5,   0,   0,   0,   0,   5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20,
]
ROOK_TABLE = [
      0,   0,   0,   0,   0,   0,   0,   0,
      5,  10,  10,  10,  10,  10,  10,   5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
      0,   0,   0,   5,   5,   0,   0,   0,
]
QUEEN_TABLE = [
    -20, -10, -10,  -5,  -5, -10, -10, -20,
    -10,   0,   0,   0,   0,   0,   0, -10,
    -10,   0,   5,   5,   5,   5,   0, -10,
     -5,   0,   5,   5,   5,   5,   0,  -5,
      0,   0,   5,   5,   5,   5,   0,  -5,
    -10,   5,   5,   5,   5,   5,   0, -10,
    -10,   0,   5,   0,   0,   0,   0, -10,
    -20, -10, -10,  -5,  -5, -10, -10, -20,
]
KING_MIDDLEGAME_TABLE = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
     20,  20,   0,   0,   0,   0,  20,  20,
     20,  30,  10,   0,   0,  10,  30,  20,
]

KING_ENDGAME_TABLE = [
    -50, -40, -30, -20, -20, -30, -40, -50,
    -30, -20, -10,   0,   0, -10, -20, -30,
    -30, -10,  20,  30,  30,  20, -10, -30,
    -30, -10,  30,  40,  40,  30, -10, -30,
    -30, -10,  30,  40,  40,  30, -10, -30,
    -30, -10,  20,  30,  30,  20, -10, -30,
    -30, -30,   0,   0,   0,   0, -30, -30,
    -50, -30, -30, -30, -30, -30, -30, -50,
]

PIECE_TABLES = {
    chess.PAWN: PAWN_TABLE,
    chess.KNIGHT: KNIGHT_TABLE,
    chess.BISHOP: BISHOP_TABLE,
    chess.ROOK: ROOK_TABLE,
    chess.QUEEN: QUEEN_TABLE,
    chess.KING: KING_MIDDLEGAME_TABLE
}


class ChessBot:
    def __init__(self, depth=2):
        self.depth = depth

    def evaluate_board(self, board: chess.Board) -> int:
        if board.is_checkmate():
            return -9999 if board.turn == chess.WHITE else 9999
        if board.is_stalemate() or board.is_insufficient_material():
            return 0

        material=0

        for square in chess.SQUARES:
           piece = board.piece_at(square)
           if piece:
               material += piece_values[piece.piece_type] if piece.color == chess.WHITE else -piece_values[piece.piece_type]
               pst_square = square if piece.color == chess.WHITE else chess.square_mirror(square)
               material += PIECE_TABLES[piece.piece_type][pst_square] if piece.color == chess.WHITE else -PIECE_TABLES[piece.piece_type][pst_square]

        return material

    def alpha_beta(self, board: chess.Board, depth: int, alpha: int, beta: int, is_maximizing: bool) -> int:
        if depth ==0 or board.is_game_over():
            return self.evaluate_board(board)

        if is_maximizing:
            max_eval = -float('inf')
            for move in board.legal_moves:
                board.push(move)
                eval_val = self.alpha_beta(board, depth-1, alpha, beta, False)
                board.pop()
                max_eval = max(max_eval, eval_val)
                alpha = max(alpha, eval_val)
                if beta<=alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.legal_moves:
                board.push(move)
                eval_val = self.alpha_beta(board, depth-1, alpha, beta, True)
                board.pop()
                min_eval = min(min_eval, eval_val)
                beta = min(beta, eval_val)
                if beta<=alpha:
                    break
            return min_eval

    def get_best_move(self, board: chess.Board) -> chess.Move:
        best_move = None
        is_maximizing = board.turn == chess.WHITE
        best_value = -float('inf') if is_maximizing else float('inf')
        for move in board.legal_moves:
            board.push(move)
            board_value = self.alpha_beta(board, self.depth-1, -float("inf"), float("inf"),not is_maximizing)
            board.pop()

            if is_maximizing and board_value > best_value:
                best_value = board_value
                best_move = move
            elif not is_maximizing and board_value < best_value:
                best_value = board_value
                best_move = move
        return best_move

def play_chess():
    board = chess.Board()
    bot = ChessBot(depth=3)

    while not board.is_game_over():
        print(board)
        print("-" * 20)

        move = bot.get_best_move(board)
        if move:
            print(f"Move played: {move}")
            board.push(move)

        time.sleep(0.5)
        if board.can_claim_threefold_repetition():
            print(f"Three fold repetition played")
            break

    print(board)
    print("Game Over")
    print("Result:", board.result())


if __name__ == "__main__":
    play_chess()