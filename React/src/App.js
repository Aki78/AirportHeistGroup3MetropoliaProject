import ReactDOM from "react-dom/client";
import { 
  Routes,
  Route,
} from "react-router-dom";

import Home from './Home/Home'
import LeaderBoard from './LeaderBoard/LeaderBoard'
import Tutorial from './Tutorial/Tutorial'
import Game from './Game/Game'
import Download from './Download/Download'
import Credits from './Credits/Credits'
import Weather from './Weather/Weather'

import './App.css';

import Navigation from './Navigation/Navigation';
import Footer from './Footer/Footer';


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
                <Route path="Credits" element={<Credits />} />
                <Route path="Download" element={<Download />} />
                <Route path="Weather" element={<Weather />} />
            </Routes>
        </div>
        
        <Footer />

    </>

  )
}


export default App;
