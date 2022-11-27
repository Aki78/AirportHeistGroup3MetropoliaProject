import './account.css'
import React from 'react'
import { useState } from 'react'
import Form from 'react'
import Button from 'react'

const Account = () => {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [password_confirm, setPasswordconfirm] = useState("")

    const [text, setText] = useState("")

    function validateForm() {
        return username.length > 0 && password.length > 0;
    }

    function handleSubmit(event) {
        event.preventDefault();
    }




    return (
        <>
            <h1>Sign in</h1>
            <div class="sign-in-form">
                <div class="username">
                    <input 
                        placeholder='Username'
                        onChange={event => setUsername(event.target.value)}
                    />
                </div>
                
                <div class="password">
                    <input
                        type="password"
                        placeholder='Password'
                        onChange={event => setPassword(event.target.value)}
                    />
                </div>

                <button onClick={() => setText("Signed in")}>
                    Sign in
                </button>
            </div>

            <div class="line"></div>

            <h4>Or</h4>
            <h3>Sign up</h3>

            <div class="sign-up-form">
                <div class="username">
                    <input 
                        placeholder='Username'
                        onChange={event => setUsername(event.target.value)}
                    />
                </div>
                
                <div class="password">
                    <input
                        type="password"
                        placeholder='Password'
                        onChange={event => setPassword(event.target.value)}
                    />
                </div>

                <div class="password-confirm">
                    <input
                        type="password"
                        placeholder='Confirm password'
                        onChange={event => setPasswordconfirm(event.target.value)}
                    />
                </div>

                <button onClick={() => setText("Signed up")}>
                    Sign up
                </button>

            </div>
        </>

    )
}


export default Account;



