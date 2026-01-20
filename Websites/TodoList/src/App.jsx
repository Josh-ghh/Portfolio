import { useState } from "react";
import "./App.css";
import Navbar from './pages/Navbar.jsx';

function Todo() {
  const [task, setTask] = useState([]);
  const [newTask, setNewTask] = useState("");
  const [remove, setRemove] = useState("");

  const addTask = () => {
    if (newTask.trim() === "") return;
    setTask([...task, newTask]);
    setNewTask("");
  };

  const clearTask = () => {
    setTask([]);
  };

  const removeTask = () => {
    setTask(task.filter((taskItem) => taskItem !== remove));
    setRemove("");
  };

  return (
    <>
    <Navbar/>
    <div className="app">
      
      <h1>Task List</h1>

      <div className="inputs">
        <input
          type="text"
          placeholder="add a task"
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
        />

        <input
          type="text"
          placeholder="enter text to remove"
          value={remove}
          onChange={(e) => setRemove(e.target.value)}
        />
      </div>

      <div className="buttons">
        <button onClick={addTask}>Add task</button>
        <button onClick={clearTask}>Clear tasks</button>
        <button onClick={removeTask}>Remove a task</button>
      </div>

      <div className='tasks'>
      <ul>
        {task.map((taskItem, index) => (
          <li key={index}>{taskItem}</li>
        ))}
      </ul>
    </div>
    </div>
    </>
  );
}

export default Todo;