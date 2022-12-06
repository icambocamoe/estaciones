import React, { useState} from 'react';

const Regression = () => {
    const stations = [
        { label: "Acolman", value: "aco" },
        { label: "Ajusco Medio", value: "ajm" },
        { label: "Atizapán", value: "ati" },
        { label: "Camarones", value: "cam" },
        { label: "Centro de Ciencias de la Atmósfera", value: "cca" },
        { label: "Chalco", value: "cho" },
        { label: "Cuajimalpa", value: "cua" },
        { label: "FES Acatlán", value: "fac" },
        { label: "Hospital General de México", value: "hgm" },
        { label: "Camarones", value: "inn" },
        { label: "Centro de Ciencias de la Atmósfera", value: "izt" },
        { label: "Laboratorio de Análisis Ambiental", value: "lla" },    
        { label: "La Presa", value: "lpr" },
        { label: "Merced", value: "mer" },
        { label: "Miguel Hidalgo", value: "mgh" },
        { label: "Montecillo", value: "mon" },
        { label: "Nezahualcóyotl", value: "nez" },
        { label: "Pedregal", value: "ped" }, 
        { label: "San Agustín", value: "sag" },
        { label: "Santa Fe", value: "sfe" },
        { label: "San Juan de Aragón", value: "sja" },
        { label: "Tláhuac", value: "tah" },
        { label: "Tlalnepantla", value: "tla" },
        { label: "Tultitlán", value: "tli" },
        { label: "UAM Xochimilco", value: "uax" },
        { label: "UAM Iztapalapa", value: "uiz" },
        { label: "Villa de las Flores", value: "vif" },
        { label: "Xalostoc", value: "xal" },
    ];

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
        
        setYhat(((beta0+(beta1*(regressionValues.length+1)))/5.5).toFixed(2));
        setRegressionValues([]);
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
            
        }
        
    }>
        {stations.map((e,index)=><option key={index} value={e.value} >{e.label}</option> )}
    </select>
    Prediccion del dia de hoy: {yhat}
  </>
  )
}

export default Regression