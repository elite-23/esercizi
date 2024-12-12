import React, {useState} from 'react';
import Child from './Child2';

function Parent3 (){
    const [user, setUser]= useState({name:'',age:0});

    const handleUserChange= (userInfo) =>{
        setUser(userInfo);
    };

    return(
        <div>
            <h1>Nome:{user.name}, Età:{user.age}</h1>
            <Child onUserChange={handleUserChange}/>
        </div>
    );

};

export default Parent3;