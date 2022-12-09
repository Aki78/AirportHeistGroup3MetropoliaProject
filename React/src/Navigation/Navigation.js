import React from 'react'
import { Link } from "react-router-dom";

import './navigation.css'
import Logo from '../Images/title.png'



const Navigation = ({ checkSignedIn, usernameSignedin }) => {

    return (

        <nav className="nav_bar">
            <ul>
                <li><img src={Logo} alt="logo"></img></li>
                <li><Link to="home" >Home</Link></li>
                <li><Link to="Game" >Game</Link></li>
                <li><Link to="LeaderBoard" >Leaderboard</Link></li>
                <li><Link to="Tutorial">Tutorial</Link></li>
                <li><Link to="Weather">Weather</Link></li>
                {/*<li><Link to="Download">Download</Link></li>*/}

            </ul>

            <div className="account">
                <p><Link to="Account">Account</Link></p>
            </div>
        </nav>
    )
}


export default Navigation;
