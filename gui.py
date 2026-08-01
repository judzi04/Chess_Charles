import chess
import pygame

BOARD_SIZE = 600
SQUARE_SIZE = BOARD_SIZE // 8
LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)

UNICODE_PIECES = {
    "P": "♟",
    "N": "♞",
    "B": "♝",
    "R": "♜",
    "Q": "♛",
    "K": "♚",
    "p": "♟",
    "n": "♞",
    "b": "♝",
    "r": "♜",
    "q": "♛",
    "k": "♚",
}


class ChessGUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
        pygame.display.set_caption("Chess Board")
        self.font = pygame.font.SysFont("segoeuisymbol", int(SQUARE_SIZE * 0.8))

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
                rect = (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(self.screen, color, rect)

    def draw_pieces(self, board: chess.Board):
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece is not None:
                col = chess.square_file(square)
                row = 7 - chess.square_rank(square)

                symbol = UNICODE_PIECES[piece.symbol()]
                color = (255, 255, 255) if piece.color == chess.WHITE else (20, 20, 20)

                text_surface = self.font.render(symbol, True, color)
                text_rect = text_surface.get_rect(
                    center=(
                        col * SQUARE_SIZE + SQUARE_SIZE // 2,
                        row * SQUARE_SIZE + SQUARE_SIZE // 2,
                    )
                )
                self.screen.blit(text_surface, text_rect)

    def get_square_from_pos(self, pos):
        x, y = pos
        col = x // SQUARE_SIZE
        row = y // SQUARE_SIZE

        rank = 7-row
        file = col

        return chess.square(file, rank)

    def draw_game_over(self, message:str):
        overlay = pygame.Surface((BOARD_SIZE, BOARD_SIZE))
        overlay.set_alpha(100)
        overlay.fill((0,0,0))
        self.screen.blit(overlay, (0, 0))

        banner_font = pygame.font.SysFont("arial", 36, bold=True)
        text_surface = banner_font.render(message, True, (255,255,255))

        text_rect = text_surface.get_rect(center=(BOARD_SIZE//2, BOARD_SIZE//2))
        padding_rect = text_rect.inflate(40, 20)
        pygame.draw.rect(self.screen, (40,40,40), padding_rect, border_radius=10)
        pygame.draw.rect(self.screen, (200,200,200), padding_rect, width=2, border_radius=10)

        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()

    def update(self, board: chess.Board):
        self.draw_board()
        self.draw_pieces(board)
        pygame.display.flip()

    def close(self):
        pygame.quit()
