import React, {useState} from 'react';

function CounterApp(){
    const [count,setCount] = useState(0); /* why are using const and why 0 passed in useState? */
    return (
        <div>
            <h1>Counter : {count}</h1>
            <button onClick={()=>setCount(count+1)} disabled={count>=10}>Increment</button>
            <button onClick={()=>setCount(count-1)}disabled={count<-4}>Decrement</button>
            <button onClick={()=>setCount(0)}>Reset</button>
            {count===10 && <p>you've reached the max limit of 10!</p>}
            {count < -4 && <p>lessthan -5 is not allowed</p>}
        </div>
    );
};

export default CounterApp;