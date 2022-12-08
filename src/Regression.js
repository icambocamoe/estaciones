import React, { useState} from 'react';
import stations from './Stations';
const Regression = () => {
    

    const current = new Date();
    const month = current.getMonth()+1;
    const day = current.getDate();

    const [yhat, setYhat] = useState();

    const [selected, setSelected] = useState("aco");
    const [regressionValues,setRegressionValues]=useState([])
    const selection = (e) => {
        const url="http://127.0.0.1:8000/getRegressionValues/"+selected+"&"+month+"&"+day;
        const request=fetch(url);
        request
        .then(datos=>datos.json())
        .then(read=>{
          read.RegressionValues.map((station)=>{//after read gets to be the name of the json defiened in the api
            setRegressionValues((e)=>
              [...e,
                [parseInt(station.row),
                  parseFloat(station.estacion)],
              ]
            )
            setDatos((e)=>
              [...e,
                  <tr key={station.row}>
                    <td>{station.fecha} </td>
                    <td>{station.estacion}</td>
                  </tr>
            ])
          })
        })
        .catch(()=>console.log(url))
        
        setSelected(e);
        
        handleRegression();
      };

      const handleRegression=()=>{
        var sigmax =0;
        var sigmax2 =0;
        var sigmaxy =0;
        var sigmay =0;
        for (let value in regressionValues){
            sigmax += regressionValues[value][0];
            sigmax2 += regressionValues[value][0] * regressionValues[value][0];
            sigmaxy += regressionValues[value][0] * regressionValues[value][1];
            sigmay += regressionValues[value][1];
            
        }
        var beta0 = 0;
        var beta1 = 0;
        beta1 = (regressionValues.length * sigmaxy - sigmax * sigmay) / (regressionValues.length * sigmax2 - sigmax * sigmax);
        beta0 = (sigmay - beta1 * sigmax) / regressionValues.length;
        
        setYhat(((beta0+(beta1*(8)))).toFixed(2));
        setRegressionValues([]);
       }
       
       const [datos,setDatos]=useState([
        <tr>
          <th>fecha</th>
          <th>medida mas alta</th>
        </tr>
        ])
        const empty = (e) =>{
          setDatos([
            <tr>
              <th>año</th>
              <th>medida</th>
            </tr>
          ]);
        }
      
  return (
    <>
        <select 
        name="stations" id="stations" 
        style={{margin: "10px", width: "30%"}} 
        onClick={
        event => {
            
            setSelected(event.target.value);
            selection(event.target.value);
            empty();
        }
        
    }>
        {stations.map((e,index)=><option key={index} value={e.value} >{e.label}</option> )}
    </select>
    Prediccion del dia de hoy: {yhat}
    <table style={{backgroundColor: 'DarkTurquoise', opacity: 0.7}}>
      {datos}
    </table>
  </>
  )
}

export default Regression