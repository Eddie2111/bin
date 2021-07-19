package main

import (  //fmt = format
	    "fmt"
)

  func main() { ///remember, it fails to compile if empty variable is found
    var foo int=42;
    var j int=21;
    var sum=foo+j; 
    var n bool=true;
    	  det :=21.8;  //detects variable type by given data;
    	  fmt.Println(sum,det) //prints line
	  fmt.Println("%v %T\n",n,n) //v→stored boolean value, →%T\n = data type of the recieved variable
	  
}

