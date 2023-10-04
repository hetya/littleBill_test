import React, { useEffect, useState } from 'react';
import axios from 'axios';
const Connection = () => {
    const [connectionLogin, setConnectionLogin] = useState('');
    const [connectionPassword, setConnectionPassword] = useState('');
    const [error, setError] = useState('');

    const handleLoginChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setConnectionLogin(event.target.value);
    }

    const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setConnectionPassword(event.target.value);
    }

    const handleLogin = () => {
        axios.post(process.env.REACT_APP_IP_BACK + '/user/auth/login', {
            "login" : connectionLogin,
            "password" : connectionPassword
        })
            .then(response => {
                console.log(response);
            })
            .catch(error => {
                console.log(error?.response?.data?.detail);
                setError(error?.response?.data?.detail);
            });
        setConnectionLogin('')
        setConnectionPassword('')
    }

    const handleSignup = () => {
        axios.post(process.env.REACT_APP_IP_BACK + '/user/auth/signup', {
            "login" : connectionLogin,
            "password" : connectionPassword
        })
            .then(response => {
                console.log(response);
            })
            .catch(error => {
                console.log(error.data);
                console.log(error?.response?.data?.detail);
                setError(error?.response?.data?.detail);
            });
        setConnectionLogin('')
        setConnectionPassword('')
    }

    return (
        <div>
            <h3>Connection</h3>
            <input type="text" placeholder="login" value={connectionLogin} onChange={handleLoginChange}/>
            <input type="password" placeholder="password" value={connectionPassword} onChange={handlePasswordChange}/>
            <button onClick={handleLogin}>login</button>
            <button onClick={handleSignup}>signup</button>
        </div>
    );
}
export default Connection;