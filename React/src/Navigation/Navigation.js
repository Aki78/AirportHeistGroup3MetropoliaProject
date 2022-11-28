import React from 'react'
import { Link } from "react-router-dom";

import './navigation.css'
import Logo from '../img/title.png'



const Navigation = ({ checkSignedIn }, { usernameSignedin }) => {
    var usernameDisplay;
    if ({checkSignedIn} === "true") {
        usernameDisplay = { usernameSignedin };
    }
    else if ({checkSignedIn} === "false") {
        usernameDisplay = "Sign in";
    }


    return (
        <nav class="nav_bar">
            <ul>
                <li><img src={Logo} alt="logo"></img></li>
                <li><Link to="airport-heist.github.io" >Home</Link></li>
                <li><Link to="Game" >Game</Link></li>
                <li><Link to="LeaderBoard" >Leaderboard</Link></li>
                <li><Link to="Tutorial">Tutorial</Link></li> 
                <li><Link to="Weather">Weather</Link></li> 
                {/*<li><Link to="Download">Download</Link></li>*/}

            </ul>

            <div class="sign-in">
                <p>{checkSignedIn}</p>
                <p><Link to="Sign-in">{ usernameDisplay }</Link></p>
            </div>
        </nav>
    )
}


export default Navigation;
