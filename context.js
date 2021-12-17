import "./styles.css";
import {React, useState} from 'react';
function ASpp(x){
  if (x>15){
    setConstrain(constrain+15)
  }
  return(
    <button>hello world</button>
  )
}
export default function App() {
  const [variable,setVariable] = useState(0);
  const [constrain,setConstrain] = useState(1);
  const divStyle = {
    color:'red',
    display:'flex',
    justifiedContent:'center',
    margin: 'auto',
    width: '0%',
    border: '3px',
    padding: '-50px',
    wordSpacing:'30px'
  }  

  return (
    <div className="App">
      <h1>Hello CodeSandbox</h1>
      <h2>Start editing to see some magic happen!</h2>
      <div style= {divStyle}>
      <button onClick={()=>setVariable(variable+constrain)} >+</button>
      <div>{variable}</div>
      <button onClick={()=>setVariable(variable-constrain)} >-</button>
      </div>
      <ASpp/>

    </div>
  );
}
