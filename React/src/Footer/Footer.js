import './footer.css'
import React from 'react'
import { Link } from "react-router-dom";

const Footer = () => {
    return (
        <>  
            <div class="footer">
                <div class="copyright">
                    <p>© 2022 Metropolia-ITG3</p>
                </div>

                <div class="about-us">
                    <p><Link to="Credits">About us</Link></p>
                </div>

            </div>
            
        </>
        
    )
}


export default Footer;



