import ReactDOM from "react-dom/client";
import { 
  Routes,
  Route,
} from "react-router-dom";

import Home from './Home/Home'
import LeaderBoard from './LeaderBoard/LeaderBoard'
import Tutorial from './Tutorial/Tutorial'
import Game from './Game/Game'

import './App.css';

import Navigation from './Navigation/Navigation';


const App = () => {

  return (
    <>  
        <Navigation />
        <div class="container">
            <Routes>
                <Route path="airport-heist.github.io" element={<Home />} />
                <Route path="LeaderBoard" element={<LeaderBoard />} />
                <Route path="Game" element={<Game />} />
                <Route path="Tutorial" element={<Tutorial />} />
            </Routes>
        </div>

    </>

  )
}


export default App;


