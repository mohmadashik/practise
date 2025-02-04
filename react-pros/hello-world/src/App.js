

import logo from './logo.svg';
import './App.css';
import UserCard  from './components/User';
import Item from './components/Item';

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
      {
          const itemsArr = ['giri','hero','vali'];

      }
      <Item items={itemsArr}/>
  </div>
}

export default App;
