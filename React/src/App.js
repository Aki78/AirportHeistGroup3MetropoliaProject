import background from './img/main_background.png'
import ReactDOM from "react-dom/client";

import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";

import './App.css';

import Home from './Home/Home' 
import LeaderBoard from './LeaderBoard/LeaderBoard' 
import Tutorial from './Tutorial/Tutorial' 
import Game from './Game/Game' 

const App = () => {
    return (
        <>
        <p>test</p>
      <Router>
    <div class="container">
        <div class="nav__bar">
            <ul>
                <li><Link to="Home" >Home</Link></li>
                <li><Link to="LeaderBoard" >LeaderBoard</Link></li>
                <li><Link to="Tutorial">Tutorial</Link></li>
                <li><Link to="Game" >Game</Link></li>
            </ul>
        </div>
    </div>
          <div>

            <Routes>
              <Route path="Home" element={<Home/>}/>
            </Routes>
            <Routes>
              <Route path="LeaderBoard" element={<LeaderBoard/>}/>
            </Routes>
            <Routes>
              <Route path="Tutorial" element={<Tutorial/>}/>
            </Routes>
            <Routes>
              <Route path="Game" element={<Game/>}/>
            </Routes>
          </div>
    </Router> 
        </>
        
    )
}

            //<img src={background} alt='background'></img>
            //<div id='body-content'></div>

export default App;


