

import logo from './logo.svg';
import './App.css';
import UserCard  from './components/User';
import Item from './components/Item';
import Check from './components/Check';
import CounterApp from './components/Counter';
import UserInputForm from './components/Form';
import ToggleButton  from './components/Toggle';
function Greeting(props){
  let age = null;
  if (props.age == null)
    {
      age = 10;
    }
  else
  { 
    age = props.age ;
  }
  return <div>

   <h1> Hello, {props.name}</h1>
   <h2>your age is {age}</h2>
  </div>
;
}
function App(){

  return <div>

      <Greeting name='John'></Greeting>
      <Greeting name='Ashik' age='55'/>
      <UserCard name='Sruthi' age='18' email='sruthi@yahoo.com'/>
      <Check name='ashik' age ='24'/>
      <br/>
      <CounterApp></CounterApp>
      <br/>
      <UserInputForm></UserInputForm>
      <ToggleButton></ToggleButton>
       
      {/* <Item items={itemsArr}/> */}
  </div>
}

export default App;
