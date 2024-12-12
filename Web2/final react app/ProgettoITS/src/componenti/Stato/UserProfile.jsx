import React, {useState} from 'react';

function UserProfile() {
    const [name, setName]=useState('');
    const [email, setEmail]=useState('');

    const handleNameChange = (e)=>{
        setName(e.target.value);
    };

    const handleEmailChange = (e)=>{
        setEmail(e.target.value);
    };

    return(
        <div>
            <h2>Profilo Utente</h2>
            <label>
                Nome:
                <input type="text" value={name} onChange={handleNameChange}/>
            </label>
            <br/>
            <label>
                Email:
                <input type="email" value={email} onChange={handleEmailChange}/>
            </label>
            <h3>Dati inseriti:</h3>
            <p>Nome:{name}</p>
            <p>Email:{email}</p>
        </div>
    );
};

export default UserProfile;