import chess

piece_values = {
    chess.PAWN: 100,
    chess.KNIGHT: 310,
    chess.BISHOP: 320,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000,
}

PHASE_WEIGHTS = {
    chess.KNIGHT: 1,
    chess.BISHOP: 1,
    chess.ROOK: 2,
    chess.QUEEN: 4,
}
MAX_PHASE = 24

PAWN_MG_TABLE = [
     0,  0,  0,  0,  0,  0,  0,  0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
     5,  5, 10, 25, 25, 10,  5,  5,
     0,  0,  0, 20, 20,  0,  0,  0,
     5, -5,-10,  0,  0,-10, -5,  5,
     5, 10, 10,-20,-20, 10, 10,  5,
     0,  0,  0,  0,  0,  0,  0,  0
]
KNIGHT_MG_TABLE = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20,   0,   0,   0,   0, -20, -40,
    -30,   0,  10,  15,  15,  10,   0, -30,
    -30,   5,  15,  20,  20,  15,   5, -30,
    -30,   0,  15,  20,  20,  15,   0, -30,
    -30,   5,  10,  15,  15,  10,   5, -30,
    -40, -20,   0,   5,   5,   0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50,
]
BISHOP_MG_TABLE = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10,   0,   0,   0,   0,   0,   0, -10,
    -10,   0,   5,  10,  10,   5,   0, -10,
    -10,   5,   5,  10,  10,   5,   5, -10,
    -10,   0,  10,  10,  10,  10,   0, -10,
    -10,  10,  10,  10,  10,  10,  10, -10,
    -10,   5,   0,   0,   0,   0,   5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20,
]
ROOK_MG_TABLE = [
      0,   0,   0,   0,   0,   0,   0,   0,
      5,  10,  10,  10,  10,  10,  10,   5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
      0,   0,   0,   5,   5,   0,   0,   0,
]
QUEEN_MG_TABLE = [
    -20, -10, -10,  -5,  -5, -10, -10, -20,
    -10,   0,   0,   0,   0,   0,   0, -10,
    -10,   0,   5,   5,   5,   5,   0, -10,
     -5,   0,   5,   5,   5,   5,   0,  -5,
      0,   0,   5,   5,   5,   5,   0,  -5,
    -10,   5,   5,   5,   5,   5,   0, -10,
    -10,   0,   5,   0,   0,   0,   0, -10,
    -20, -10, -10,  -5,  -5, -10, -10, -20,
]
KING_MG_TABLE = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
     20,  20,   0,   0,   0,   0,  20,  20,
     20,  30,  10,   0,   0,  10,  30,  20,
]

PAWN_EG_TABLE = [
     0,  0,  0,  0,  0,  0,  0,  0,
    80, 80, 80, 80, 80, 80, 80, 80,
    50, 50, 50, 50, 50, 50, 50, 50,
    30, 30, 30, 30, 30, 30, 30, 30,
    20, 20, 20, 20, 20, 20, 20, 20,
    10, 10, 10, 10, 10, 10, 10, 10,
    10, 10, 10, 10, 10, 10, 10, 10,
     0,  0,  0,  0,  0,  0,  0,  0
]

KING_EG_TABLE = [
    -50, -40, -30, -20, -20, -30, -40, -50,
    -30, -20, -10,   0,   0, -10, -20, -30,
    -30, -10,  20,  30,  30,  20, -10, -30,
    -30, -10,  30,  40,  40,  30, -10, -30,
    -30, -10,  30,  40,  40,  30, -10, -30,
    -30, -10,  20,  30,  30,  20, -10, -30,
    -30, -30,   0,   0,   0,   0, -30, -30,
    -50, -30, -30, -30, -30, -30, -30, -50,
]

MG_TABLES = {
    chess.PAWN: PAWN_MG_TABLE,
    chess.KNIGHT: KNIGHT_MG_TABLE,
    chess.BISHOP: BISHOP_MG_TABLE,
    chess.ROOK: ROOK_MG_TABLE,
    chess.QUEEN: QUEEN_MG_TABLE,
    chess.KING: KING_MG_TABLE
}
EG_TABLES = {
    chess.PAWN: PAWN_EG_TABLE,
    chess.KNIGHT: KNIGHT_MG_TABLE,
    chess.BISHOP: BISHOP_MG_TABLE,
    chess.ROOK: ROOK_MG_TABLE,
    chess.QUEEN: QUEEN_MG_TABLE,
    chess.KING: KING_EG_TABLE
}


class ChessBot:
    def __init__(self, depth):
        self.depth = depth

    def get_game_phase(self, board: chess.Board) -> int:
        phase = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece and piece.piece_type in PHASE_WEIGHTS:
                phase += PHASE_WEIGHTS[piece.piece_type]
        return phase

    def evaluate_board(self, board: chess.Board) -> int:
        if board.is_checkmate():
            return -9999 if board.turn == chess.WHITE else 9999
        if board.is_stalemate() or board.is_insufficient_material() or board.can_claim_threefold_repetition():
            return 0

        mg_score =0
        eg_score =0

        for square in chess.SQUARES:
           piece = board.piece_at(square)
           if piece:
               val = piece_values[piece.piece_type]
               pst_square = square if piece.color == chess.WHITE else chess.square_mirror(square)

               mg_val = val + MG_TABLES[piece.piece_type][pst_square]
               eg_val = val + EG_TABLES[piece.piece_type][pst_square]

               if piece.color == chess.WHITE:
                   mg_score += mg_val
                   eg_score += eg_val
               else:
                   mg_score -= mg_val
                   eg_score -= eg_val

        phase = self.get_game_phase(board)
        final_score = ((mg_score*phase)+(eg_score*(MAX_PHASE-phase)))// MAX_PHASE

        return final_score

    def alpha_beta(self, board: chess.Board, depth: int, alpha: float, beta: float, is_maximizing: bool) -> int:
        if depth ==0 or board.is_game_over():
            return self.evaluate_board(board)

        if is_maximizing:
            max_eval = -float('inf')
            for move in self.order_moves(board):
                board.push(move)

                if board.can_claim_threefold_repetition():
                    board.pop()
                    continue

                eval_val = self.alpha_beta(board, depth-1, alpha, beta, False)
                board.pop()
                max_eval = max(max_eval, eval_val)
                alpha = max(alpha, eval_val)
                if beta<=alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.order_moves(board):
                board.push(move)
                if board.can_claim_threefold_repetition():
                    board.pop()
                    continue

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
        for move in self.order_moves(board):
            board.push(move)

            if board.can_claim_threefold_repetition():
                board.pop()
                continue

            board_value = self.alpha_beta(board, self.depth-1, -float("inf"), float("inf"),not is_maximizing)
            board.pop()

            if is_maximizing and board_value > best_value:
                best_value = board_value
                best_move = move
            elif not is_maximizing and board_value < best_value:
                best_value = board_value
                best_move = move

        if best_move is None and list(board.legal_moves):
            best_move = list(board.legal_moves)[0]
        return best_move

    def score_move(self, board:chess.Board, move: chess.Move) -> int:
        move_score =0

        if board.is_capture(move):
            attacker = board.piece_at(move.from_square)
            victim = board.piece_at(move.to_square)

            victim_val = piece_values[victim.piece_type] if victim else 100
            attacker_val = piece_values[attacker.piece_type] if attacker else 100

            move_score += 1000 + ( victim_val*10 - attacker_val )

        board.push(move)
        if board.is_check():
            move_score += 500
        board.pop()

        return move_score

    def order_moves(self, board: chess.Board):
        moves = list(board.legal_moves)
        moves.sort(key=lambda m: self.score_move(board, m), reverse=True)
        return moves


