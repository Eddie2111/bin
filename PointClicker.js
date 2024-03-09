// setting default branch using this,
git config --global init.defaultBranch main
// edit all configs
git config --global --edit
// set up a proxy for git
git config --global http.proxy proxy-url
// git help
git config -h



import {React, useState} from 'react';
import "./styles.css";

function Score(x){
  const [highest, setHighest] = useState(0);
  const [lowest, setLowest] = useState(0);
    if (x>highest){
      setHighest(x);
    }
    if (x<lowest){
      setLowest(x);
    }
  return (
    <>
    <div className ='score-card'>
      <p> highest point = {highest}</p>
      <p> lowest point = {lowest}</p>
      </div>
    </>
  )
}

function Main(){
  const [variable , setVariable] = useState(0);
  const [constrain, setConstrain] = useState(1);
  const style = {
    fontFamily: 'sans-serif',
    textAlign: 'center'
    }
  return (
    <>
    <div style = {style}>
    <h1>Point Clicker</h1>
    <p> Current Constrain = {constrain}</p>
    <button onClick = {()=> setVariable(variable+constrain)}> + </button>
    <br/>
    <h5>{variable}</h5>
    
    <button onClick = {()=> setVariable(variable-constrain)}> - </button>
    <h1>{ Score(variable) }</h1>
    <button onClick = {()=> 
      setConstrain(constrain+1)}>Increase Constrain</button>
    
    <button onClick = {()=> setConstrain(constrain-1)}>Decrease Constrain</button>
    </div>
    
    </>
  )
}
export default Main;
