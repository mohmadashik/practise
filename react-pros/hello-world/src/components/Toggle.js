import React, { useState} from 'react';

function ToggleButton(){
    const [isOn,setIsOn] = useState(false);
    return (
    
     <div>
    <br></br>
    <button onClick={()=>setIsOn(!isOn)} 
    style={{backgroundColor : isOn? 'green':'red'}}
    >
        {isOn?'On':'Off'}
    </button>
    <br></br>

    </div>
    );

}

export default ToggleButton;