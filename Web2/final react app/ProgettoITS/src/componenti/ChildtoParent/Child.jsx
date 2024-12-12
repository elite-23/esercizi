import React from 'react';

function Child({onMessage}){
    const sendMessageToParent=()=>{
        onMessage('Ciao dal componente Child');
    };

    return(
        <div>
            <button onClick={sendMessageToParent}>Invia messaggio al Parent</button>
        </div>
    );

};

export default Child;