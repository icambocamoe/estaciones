import React from 'react'
import {  Link  } from "react-router-dom";

function Home() {
  return (
    <div style={{
      display: "flex",
      background: 'black',
      opacity: 0.8,
      padding: '5px 0 5px 5px',
      fontSize: '20px'
  }}>
    <div><nav>  
    <ul>  
    <li>  
    <Link to="/Home" > Limpieza de datos </Link>
    </li>  
    <li>  
    <Link to="/Home" >  Carga datos  </Link>
    </li>  
    <li>  
    <Link to="/App" >Prediccion del dia </Link>
    </li>  

    </ul>  
    </nav> </div>
    </div>
  )
}

export default Home