import './account.css'
import React, { useRef } from 'react';
import { useState } from 'react';
import { useNavigate } from "react-router-dom";


import Home from '../Home/Home';

const Account = ({ callbackUsername ,  callbackPassword ,  callbackSignedIn} ) => {
    
    //const nametest = document.getElementsByTagName("input[type='text']")[0].value;
    const usernameInputRef = useRef(null);
    const passwordInputRef = useRef(null);
    var checkSignInInputRef = useRef(null);

    let navigate = useNavigate();

    const [info, setInfo] = useState();

    function checkCredentials(usernameInputRef, passwordInputRef) {
        console.log("Log check", usernameInputRef)

        async function retrieveInfo(usernameInputRef) {
            await fetch('http://127.0.0.1:5000/Account/' + usernameInputRef)
                .then(response => response.json())
                .then(response => {
                    console.log("???", response)
                    setInfo(response);
                    console.log(response);
                })
                .catch(err => console.error(err));
        }

        retrieveInfo(usernameInputRef);
        
        let checkUser = info.username;
        //let checkPass = info[1];    
        console.log("After fetch", checkUser);
        if (checkUser === usernameInputRef) { // && checkPass === passwordInputRef) {
            console.log("Match");
            return true;
        }
        else {
            console.log("Incorrect credentials");
            return false;
        }
    }


    function handleUSername(username) {
        callbackUsername(username);
    }

    function handlePassword(password) {
        callbackPassword(password);
    }

    function handleSignedIn(signedin) {
        callbackSignedIn(signedin);
    }

    function handleClick() {
        handleUSername(usernameInputRef.current.value);
        handlePassword(passwordInputRef.current.value);
        
        if (checkCredentials(usernameInputRef.current.value, passwordInputRef.current.value)) {
            handleSignedIn(checkSignInInputRef.current = true);
            const routeChange = () => {
                let path = '/airport-heist.github.io';
                navigate(path);
            }
            console.log("User logged in");
            routeChange();

        }
        else {
            handleSignedIn(checkSignInInputRef.current = false);
        }


    }

    return (
        <>
            <h1>Sign in</h1>
            <div className="sign-in-form">
                <div className="username">
                    <input 
                        id="username"
                        type="text"
                        placeholder='Username'
                        ref={usernameInputRef}
                    />
                </div>
                
                <div className="password">
                    <input
                        id="password"
                        type="password"
                        placeholder='Password'
                        ref={passwordInputRef}
                    />
                </div>
                <button onClick={handleClick}>Sign in</button>
                <br/>
            </div>

            <div className="line"></div>


{/*
            <h4>Or</h4>
            <h3>Sign up</h3>

            <div class="sign-up-form">
                <div class="username">
                    <input 
                        placeholder='Username'
                        onChange={e => setUsername(e.target.value)}
                    />
                </div>
                
                <div class="password">
                    <input
                        type="password"
                        placeholder='Password'
                        onChange={e => setPassword(e.target.value)}
                    />
                </div>

                <div class="password-confirm">
                    <input
                        type="password"
                        placeholder='Confirm password'
                        onChange={e => setPasswordconfirm(e.target.value)}
                    />
                </div>

                <button onClick={() => setText("Signed up")}>
                    <Link to="../airport-heist.github.io">Sign up</Link>
                </button>
            </div>
*/}
        </>

    )
}


export default Account;



