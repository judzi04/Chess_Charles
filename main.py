import chess
import pygame
import sys
import time
from Charles import ChessBot
from gui import ChessGUI

PLAYER_VS_BOT = True
PLAYER_COLOR = chess.WHITE

def main():
    board = chess.Board()
    gui = ChessGUI()
    bot = ChessBot(depth=3)

    clock = pygame.time.Clock()
    running = True
    game_over_reason = None
    selected_square = None

    while running:
        is_human_turn = PLAYER_VS_BOT and (board.turn == PLAYER_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and is_human_turn and not board.is_game_over():
                clicked_square = gui.get_square_from_pos(event.pos)

                if selected_square is None:
                    piece = board.piece_at(clicked_square)
                    if piece and piece.color == PLAYER_COLOR:
                        selected_square = clicked_square

                else:
                    move = chess.Move(selected_square, clicked_square)

                    promotion_move = chess.Move(selected_square, clicked_square, promotion=chess.QUEEN)

                    if promotion_move in board.legal_moves:
                        move = promotion_move
                    if move in board.legal_moves:
                        board.push(move)

                    selected_square = None

        if not game_over_reason:
            if board.is_checkmate():
                winner = "Black" if board.turn == chess.WHITE else "White"
                game_over_reason = f"Checkmate! {winner} wins!"
            elif board.is_stalemate():
                game_over_reason = "Draw: Stalemate"
            elif board.is_insufficient_material():
                game_over_reason = "Draw: Insufficient Material"
            elif board.can_claim_threefold_repetition():
                game_over_reason = "Draw: Threefold Repetition"
            elif board.can_claim_fifty_moves():
                game_over_reason = "Draw: Fifty-Move Rule"

        if not is_human_turn and not board.is_game_over():
            if PLAYER_VS_BOT:
                time.sleep(0.2)
            bot_move = bot.get_best_move(board)
            if bot_move:
                board.push(bot_move)


        gui.update(board)

        if game_over_reason:
            gui.draw_game_over(game_over_reason)
        clock.tick(30)

    gui.close()
    sys.exit()


if __name__ == "__main__":
    main()
