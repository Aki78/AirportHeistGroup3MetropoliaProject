import './account_management.css'
import React from 'react'
import { useNavigate } from "react-router-dom";

const AccountManagement = ({username, callbackUsername ,  callbackSignedIn}) => {
    let navigate = useNavigate();
    
    function handleSignOutEvent() {
        callbackUsername("")        
        callbackSignedIn(false);

        localStorage.clear();

        const routeChange = () => {
            let path = "/home";
            navigate(path);
        }
        routeChange();

    }
    

    return (
        <>
            <h1>Profile</h1>
            <p>Username: <strong>{username}</strong></p>

            <div className="change-password">
                <div className="cpw-old-password">
                    <input
                        type="password"
                        placeholder='Old password'
                        //onChange={e => setAccPassword(e.target.value)}
                    />
                </div>

                <div className="cpw-new-password">
                    <input
                        type="password"
                        placeholder='New password'
                        //onChange={e => setAccPassword(e.target.value)}
                    />
                </div>

                <div className="cpw-cfn-password">
                    <input
                        type="password"
                        placeholder='Confirm password'
                        //onChange={e => setPasswordConfirm(e.target.value)}
                    />
                </div>

                <button>Change password</button>
            </div>

            <div className="line"></div>

            <div className="sign-out">
                <button onClick={handleSignOutEvent}>Sign out</button>
            </div>
        </>

    )
}


export default AccountManagement;



