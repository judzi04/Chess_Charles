import chess
import pygame
import sys
import time
from Charles import ChessBot
from gui import ChessGUI


def main():
    board = chess.Board()
    gui = ChessGUI()
    bot = ChessBot(depth=3)

    clock = pygame.time.Clock()
    running = True
    game_over_reason = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not board.is_game_over() and not game_over_reason:
            move = bot.get_best_move(board)
            if move:
                board.push(move)

                if board.can_claim_threefold_repetition():
                    game_over_reason = "Three fold repetition"
                elif board.can_claim_fifty_moves():
                    game_over_reason = "Fifty moves"
                elif board.is_game_over():
                    if board.is_checkmate():
                        winner = "Black" if board.turn == chess.WHITE else "White"
                        game_over_reason = "Checkmate"
                    elif board.is_stalemate():
                        game_over_reason = "Stalemate"
                    elif board.is_insufficient_material():
                        game_over_reason = "Insufficient material"
                time.sleep(0.5)

        gui.update(board)

        if game_over_reason:
            print(game_over_reason)
            time.sleep(2)
            running = False
        clock.tick(30)

    gui.close()
    sys.exit()


if __name__ == "__main__":
    main()
