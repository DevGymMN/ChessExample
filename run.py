import sys, chess.pgn, random, io

pgn = io.StringIO(sys.argv[1])
game = chess.pgn.read_game(pgn)
board = game.board()
move = random.sample(list(board.legal_moves), 1)[0]

print(move.uci())
