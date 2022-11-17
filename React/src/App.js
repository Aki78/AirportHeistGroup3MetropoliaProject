import spinner from './img/spina.gif'
import background from './img/main_background.png'

import './App.css';

/*
const Hello = (passed) => {
    return (
      <div>
        <p>Hello {passed.name} and you are {passed.age}</p>
      </div>
    )
  }

const sqr = p => p * p

  
const App = () => {
    const a = [1, 2, 4];
    const asqr = a.map(p => sqr(p))

    return (
        <div>
        <h1>Greetings</h1>
        <Hello name="Ajkhg" age={21}/>
        <p>Result: {asqr}</p>
        </div>
    )
}
*/
/*
const Small_calc = (props) => {
    const name = props.username
    const age = props.userage

    const born_year = new Date().getFullYear() - age

    return (
        <div>
            <p>Hello {name}, you are {age} years old</p>
            <p>You are probably born in {born_year} </p>
        </div>
    )
}
*/

const Play = () => {

    return (
        <>
            
            <div id='folder-background'></div>
        </>
    )

}




const App = () => {
    return (
        /*
        <div id="logo">
            <img src={spinner} alt="spinner"></img>
        </div>
        */
        
        <>
            <img src={background} alt='background'></img>
            <div id='body-content'></div>
                
                
            

            
        </>
        
    )
}


export default App;
