import './credits.css'
import React from 'react'

const Credits = () => {
    return (
        <>
            <main>
                <section>
                    <div class="backend">
                        <h4>People behind the backend part:</h4>
                        <ul>
                            <li>Francesco Natanni</li>
                            <li>Eiaki V. Morooka</li>
                        </ul>
                    </div>

                    <div class="database">
                        <h4>The person who made the database work:</h4>
                        <ul>
                            <li>Jenni Hallikas</li>
                        </ul>
                    </div>

                    <div class="frontend">
                        <h4>People who built the frontend:</h4>
                        <ul>
                            <li>Khai Cao</li>
                            <li class="front">Kiana Aghajani</li>
                        </ul>
                    </div>

                    <div class="info">
                    </div>
                </section>
            </main>
        </>

    )
}


export default Credits;



