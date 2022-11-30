import React, { useState, useRef } from 'react';
import { Chart } from "react-google-charts";

const Estaciones =()=>{
  const Ref = useRef(this);
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
    { label: "sja", value: "sja" },
    { label: "Tláhuac", value: "tah" },
    { label: "Tlalnepantla", value: "tla" },
    { label: "Tultitlán", value: "tli" },
    { label: "UAM Xochimilco", value: "uax" },
    { label: "UAM Iztapalapa", value: "uiz" },
    { label: "Villa de las Flores", value: "vif" },
    { label: "Xalostoc", value: "xal" },
  ];
  const [fecha,setFecha] = useState("2015");
  const [selected, setSelected] = useState("aco");
  const [maxValues,setMaxValues]=useState([])
  const selection = () => {
    const url="http://127.0.0.1:8000/getImecaMaxValues/"+selected+"&"+fecha;
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
   // console.log(Ref.current.innerHTML);
    setMaxValues([
      ["fecha",e]]);
  }




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
        name="stations" id="stations" 
        style={{margin: "10px", width: "30%"}} 
        onChange={
        event => {
          empty(event.target.value);
          selection();
          setSelected(event.target.value);
        }
      }>
        {stations.map((e,index)=><option key={index} value={e.value} ref={Ref}>{e.label}</option> )}
      </select>
      <select
      name="fecha" id="fecha" 
      onChange={
        
        event => {
          setFecha(event.target.value);
          empty(event.target.value);
          selection();
        }
      }>
        <option value="2015">2015</option>
        <option value="2016">2016</option>
        <option value="2017">2017</option>
        <option value="2018">2018</option>
        <option value="2019">2019</option>
        <option value="2020">2020</option>
        <option value="2021">2021</option>
        <option value="2022">2022</option>
      </select>
      </>
  )
};

export default Estaciones;
