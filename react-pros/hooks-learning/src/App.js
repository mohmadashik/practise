import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect, useReducer }from 'react';

const counterReducer = (state,action)=>{
  switch(action.type){
    case "increment":
      return {count : state.count+1};
    case "decrement":
      return {count: state.count-1};
    case "reset":
      return {count: 0};
    default:
      throw new Error("Unknown action type");
  }
}

function App() {
  const [name,setName] = useState("");
  const [isNameSaved,SetIsNameSaved] = useState(false);

  useEffect(()=>{
    document.title = name? "Hello, ${name}" : "React Hooks Demo";
  },[name]);

  const [state, dispatch] = useReducer(counterReducer)
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
