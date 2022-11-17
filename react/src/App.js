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

const App = () => {
    return (
        <>
        <p>test</p>
      <Router>
    <div class="container">
        <div class="nav__bar">
            <ul>
                <li><Link to="Home" >Home</Link></li>
                <li><Link to="Home" >Home</Link></li>
                <li><Link to="Home" >Home</Link></li>
                <li><Link to="Home" >Home</Link></li>
            </ul>
        </div>
    </div>
          <div>

            <Routes>
              <Route path="Home" element={<Home/>}/>
            </Routes>
            <Routes>
              <Route path="Home" element={<Home/>}/>
            </Routes>
          </div>
    </Router> 
        </>
        
    )
}

            //<img src={background} alt='background'></img>
            //<div id='body-content'></div>

export default App;


