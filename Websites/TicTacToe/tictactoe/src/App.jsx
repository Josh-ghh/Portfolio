import './App.css';
import { useState } from 'react';

const WINNING_LINES = [
  [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
  [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
  [0, 4, 8], [2, 4, 6],            // diagonals
];

function calculateWinner(board) {
  for (const [a, b, c] of WINNING_LINES) {
    if (board[a] && board[a] === board[b] && board[a] === board[c]) {
      return board[a];
    }
  }
  return null;
}

function TicTacToe() {

  const [board, setBoard] = useState(Array(9).fill(""));
  const [xIsNext, setXIsNext] = useState(true);

  const winner = calculateWinner(board);

  const handleClick = (index) => {
    const newBoard = [...board];
    newBoard[index] = xIsNext ? "X" : "O";
    setBoard(newBoard);
    setXIsNext(!xIsNext);
  };

  const clearBoard = () => {
    setBoard(Array(9).fill(""));
    setXIsNext(true);
  };

  return (
    <>
      <div className="title">
        <h1>Tic Tac Toe</h1>
      </div>

      {winner && <div className="status">Winner: {winner}</div>}

      <div className="board">
        {board.map((square, index) => (
          <button
            key={index}
            className="square"
            onClick={() => handleClick(index)}
          >
            {square}
          </button>
        ))}
      </div>

      <div className="clear">
        <button onClick={clearBoard}>Clear Board</button>
      </div>

    </>
  );
}

export default TicTacToe;