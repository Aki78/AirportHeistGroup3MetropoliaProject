import './weather.css'
import React from 'react'
import Iframe from 'react-iframe';

const Weather = () => {
    return (
        <>     
            <h3>OpenWeather</h3>      
            <div className="weather-screen">
                <Iframe className="porting" frameborder="0" src="https://openweathermap.org/weathermap?basemap=map&cities=true&layer=temperature&lat=60&lon=25&zoom=9" width="1366" height="768">
                    <a href="https://openweathermap.org/weathermap?basemap=map&cities=true&layer=temperature&lat=60&lon=25&zoom=9">openweathermap</a>
                </Iframe>
            </div>
        </>
        
    )
}


export default Weather;



