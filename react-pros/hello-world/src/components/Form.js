import React, {useState} from 'react';
function UserInputForm(){
    const [inputValue,setInputValue] = useState('');
    const handleSubmit = (e)  =>{
        e.preventDefault();
        alert(`you have entered ${inputValue}`);
    };
    

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    Enter Something: 
                <input type = 'text' value = {inputValue} onChange={(e) =>setInputValue(e.target.value)}/>
                </label>
                <br></br>
                <button type='submit'>Submit</button>
            </form>
            <p>Current Input : {inputValue}</p>
        </div>
    )
}
export default UserInputForm;