setup and run docker example env
-- docker volume create my-vol
-- docker build -t test ./path/to/your/engine/
-- docker run -v my-vol:/workspace -e pgn="[Site "Chess.com"]
[Date "2019.05.26"]
[Event "Vs. Computer"]
[Round "1"]
[White "Guest"]
[Black "Computer Level 2"]
[Result "*"]
[ECO "A41"]
[CurrentPosition "rnbqkbnr/ppp1ppp1/3p3p/8/1P1P4/8/P1P1PPPP/RNBQKBNR w KQkq - 0 3"]

1.d4 d6 2.b4 h6  *" --net=none test
