from random import randint
import chess.pgn
import sys
import io

def main():
    pgn = io.StringIO(sys.argv[1])
    game = chess.pgn.read_game(pgn)
    board = game.board()
    legal_moves = board.legal_moves
    random_move = list(legal_moves)[(randint(0,legal_moves.count()-1))]
    print(random_move)

main()
