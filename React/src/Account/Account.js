import './account.css'
import React, { useEffect } from 'react'
import { useState } from 'react'
import { Link } from "react-router-dom";
import Form from 'react'

const Account = ({ callbackUsername }, { callbackPassword },  callbackSignedIn ) => {

    const [text, setText] = useState("")

    
    function handleUSername(username) {
        callbackUsername(username);
    }

    function handlePassword(password) {
        callbackPassword(password);
    }

    function handleSignedIn(signedin) {
        callbackSignedIn(signedin);
    }

    return (
        <>
            <h1>Sign in</h1>
            <div class="sign-in-form">
                <div class="username">
                    <input 
                        text="text"
                        placeholder='Username'
                        onChange={e => handleUSername(e.target.value)}
                    />
                </div>
                
                <div class="password">
                    <input
                        type="password"
                        placeholder='Password'
                        onChange={e => handlePassword(e.target.value)}
                    />
                </div>
                <button onClick={() => handleSignedIn("true")}>
                    <Link to="../airport-heist.github.io">Sign in</Link>
                </button>
            </div>

            <div class="line"></div>
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


