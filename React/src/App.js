import ReactDOM from "react-dom/client";
import { 
  Routes,
  Route,
} from "react-router-dom";
//import CookieConsent from "react-cookie-consent";

import Home from './Home/Home'
import LeaderBoard from './LeaderBoard/LeaderBoard'
import Tutorial from './Tutorial/Tutorial'
import Game from './Game/Game'
import Download from './Download/Download'
import Credits from './Credits/Credits'
import Weather from './Weather/Weather'
import Account from './Account/Account'
import AccountManagement from './Account/AccountManagement'

import './App.css';

import Navigation from './Navigation/Navigation';
import Footer from './Footer/Footer';

import { useState } from 'react';



const App = () => {
  const [username, setUsername] = useState("");
  const [signedin, setSignedin] = useState(false);


  const callbackUsernameFunction = (username) => {
    setUsername(username);
  }

  const callbackSignedInFunction = (signedin) => {
    setSignedin(signedin);
  }


  return (
    <>  
        <Navigation checkSignIn={signedin} usernameSignedin={username}/>
        {/*<p>{signedin.toString()}</p>*/}
        <div className="container">
            <Routes>
                <Route path="airport-heist.github.io" element={<Home />} />
                <Route path="LeaderBoard" element={<LeaderBoard />} />
                <Route path="Game" element={<Game />} />
                <Route path="Tutorial" element={<Tutorial />} />
                <Route path="Credits" element={<Credits />} />
                <Route path="Download" element={<Download />} />
                <Route path="Weather" element={<Weather />} />
                {/* <Route path="Account" element={signedin ? <Account /> :  username }/> */}
                <Route path="Account"  element={signedin ? <AccountManagement username={username} /> : <Account callbackUsername={callbackUsernameFunction} callbackSignedIn={callbackSignedInFunction}/> } />
            </Routes>
        </div>
      {/*<CookieConsent
    location="top"
    buttonText="Okay!"
    cookieName="mywmeookieName2"
    style={{ background: "#2B373B" }}
    buttonStyle={{ color: "#4e503b", fontSize: "33px" }}
>
    This website uses cookies to enhance the user experience.{" "}
  </CookieConsent>*/}
        <Footer />

    </>

  )
}


export default App;
