import './account.css'
import React from 'react'
import { useState } from 'react'
import { Link } from "react-router-dom";
import Form from 'react'

const Account = () => {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [password_confirm, setPasswordconfirm] = useState("")

    const [text, setText] = useState("")





    return (
        <>
            <h1>Sign in</h1>
            <div class="sign-in-form">
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

                <button onClick={() => setText("Signed in")}>
                    <Link to="../airport-heist.github.io">Sign in</Link>
                </button>
            </div>

            <div class="line"></div>

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
        </>

    )
}


export default Account;



