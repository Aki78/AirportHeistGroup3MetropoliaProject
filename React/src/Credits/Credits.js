import './credits.css'
import React from 'react'

const Credits = () => {
    return (
        <>
            <main>
                <h2 id='motto'>PREPARE FOR TROUBLE AND MAKE IT DOUBLE</h2>
                <section>
                    <div className="backend">
                        <h4>The team behind the backend:</h4>
                        <ul>
                            <li>Francesco Natanni</li>
                            <li>Eiaki V. Morooka</li>
                        </ul>
                    </div>

                    <div className="database">
                        <h4>Person who worked on the database:</h4>
                        <ul>
                            <li>Jenni Hallikas</li>
                        </ul>
                    </div>

                    <div className="frontend">
                        <h4>People who built the frontend:</h4>
                        <ul>
                            <li>Khai Cao</li>
                            <li>Kiana Aghajani</li>
                        </ul>
                    </div>
                </section>
                <div id='line'></div>
                <h2 id='how'>Our Contact Information</h2>
                <article>
                    <div className='back'>
                        <h4>The backend team:</h4>
                        <div className="frank">
                            <p>Frank</p>
                            <p>His e-mail:</p>
                            <a href="mailto: francesn@metropolia.fi">francesn@metropolia.fi</a>
                            <p>His github link:</p>
                            <a href='https://github.com/murphyslemon'>https://github.com/murphyslemon</a>
                            <br></br> <br></br>
                        </div>
                        <div className="aki">
                            <p>Aki</p>
                            <p>You can reach him at:</p>
                            <a href='mailto: eiakim@metropolia.fi'>eiakim@metropolia.fi</a>
                            <br></br> <br></br>
                        </div>
                    </div>
                    <div className="data">
                        <br></br> <br></br>
                        <h4>Database:</h4>
                        <div className="jenni">
                            <p>Jenni</p>
                            <p>Her e-mail address is:</p>
                            <a href='mailto: jenni.hallikas@metropolia.fi'>jenni.hallikas@metropolia.fi</a>
                            <br></br> <br></br>
                        </div>
                    </div>
                    <div className="front">
                        <br></br> <br></br>
                        <h4>The frontend team:</h4>
                        <div className="khai">
                            <p>Khai</p>
                            <p>His e-mail is:</p>
                            <a href='mailto: khai.caho@metropolia.fi'>khai.caho@metropolia.fi</a>
                            <p>His github link is:</p>
                            <a href='x'>https://github.com/khai2003</a>
                            <br></br> <br></br>
                        </div>
                        <div className="kia">
                            <p>Kiana</p>
                            <p>E-mail address is:</p>
                            <a href='mailto: kiana.aghajani@metropolia.fi'>kiana.aghajani@metropolia.fi</a>
                            <p>Contact on Discord with:</p>
                            <p>kiian#2547</p>
                        </div>
                    </div>
                </article>
            </main>
        </>

    )
}


export default Credits;



