import React, { useState } from 'react';
import { Chart } from "react-google-charts";
import stations from './Stations';

const Estaciones =()=>{
  const [query,setQuery] = useState({
    date: "2015",
    point: "aco",
  })
  const [maxValues,setMaxValues]=useState([["fecha","point"]])
  const selection = () => {
    console.log(query)
    const url="http://127.0.0.1:8000/getImecaMaxValues/"+query.point+"&"+query.date;
    const request=fetch(url);
    request
    .then(datos=>datos.json())
    .then(read=>{
      read.MaxValues.map((station)=>{//after read gets to be the name of the json defiened in the api
        setMaxValues((e)=>
          [...e,
            [station.fecha,
              parseInt(station.estacion*50/5.5)/50],
          ]
        )
      })
    })
    .catch(()=>console.log(url))
    };

  const empty = (e) =>{
    setMaxValues([
      ["fecha","point"]]);
  }

  const onChange = e => {
    const value = e.target.value  
    const name = e.target.name  
    setQuery(prevState => ({
        ...prevState,
        [name] : value
    }))
    selection();
    empty();
  };




  return (
      <>
      <Chart
        chartType="ScatterChart"
        data={maxValues}
        width="100%"
        height="400px"
        legendToggle
      />
      <select 
        name="point" id="stations" 
        style={{margin: "10px", width: "30%"}} 
        onChange={onChange}>
        {stations.map((e,index)=><option key={index} value={e.value} >{e.label}</option> )}
      </select>
      <select
      name="date" id="fecha" 
      onChange={onChange}>
        <option  value="2015">2015</option>
        <option  value="2016">2016</option>
        <option  value="2017">2017</option>
        <option  value="2018">2018</option>
        <option  value="2019">2019</option>
        <option  value="2020">2020</option>
        <option  value="2021">2021</option>
      </select>
      </>
  )
};

export default Estaciones;
