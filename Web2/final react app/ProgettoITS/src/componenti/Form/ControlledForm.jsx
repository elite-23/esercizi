import React,{useState} from 'react';

function ControlledForm(){
    const [name,setName]=useState('');

    const handleChange=(event)=>{
        setName(event.target.value);        
    };

    const handleSubmit=(event)=>{
        event.preventDefault();
        alert(`Nome inviato: ${name}`);
    };
    return(
        <form onSubmit={handleSubmit}>
            <label>
                Nome:
                <input
                    type="text"
                    value={name}
                    onChange={handleChange}
                />
            </label>
        </form>
    );
};

export default ControlledForm;