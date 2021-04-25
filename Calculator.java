/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.edwardgit.javacalculator;

/**
 *
 * @author Zephyr
 */
import java.util.Scanner;
import java.lang.Math;
public class Calculator 
{
    public static void main (String[]args)
    {
    Scanner input=new Scanner(System.in);
    int sum=0, mul=1, b;
      for(int a=1;a<=1;a--)
         {
             System.out.println("****************************");
             System.out.println("It's a full form calculator.");
             System.out.println("Select the number of operation you want to perform:");
             System.out.println("1)Summation");
             System.out.println("2)Substraction");
             System.out.println("3)Multiplication");
             System.out.println("4)Division");
             System.out.println("5)Absolute difference");
             System.out.println("6)To find root");
             System.out.println("7)To use power");
             System.out.println("8)Interpret a number in words");
             
             System.out.println("to exit enter 0");
             b=input.nextInt();
             if(b==0)
             {
              System.out.println("********Good bye***********");
              break;
             }
             if(b==1)
             {
               System.out.print("how many numbers do you want to add ? =");
               int c=input.nextInt();
               for(int d=1;d<=c;d++)
                {
                 System.out.println("Enter number ("+d+") =");
                 int e=input.nextInt();
                 sum=sum+e;
                 System.out.println("Current Summation= "+sum); 
               }
                 System.out.println("Total summation= "+sum);
                 System.out.println("***********************");
             }
             
             if(b==2)
             {
                 System.out.println("Enter first number = ");
                 int j=input.nextInt();
                 System.out.println("Enter second number = ");
                 int k=input.nextInt();                 
                 int sub=j-k;
                 System.out.println("Result= "+sub);
                 System.out.println("***********************");
             }

             if(b==3)
             {
               System.out.print("how many numbers do you want to multiply ? =");
               int cd=input.nextInt();
               for(int dd=1;dd<=cd;dd++)
                {
                 System.out.println("Enter number ("+dd+") =");
                 int ed=input.nextInt();
                 mul=mul*ed;
                 System.out.println("Current Multiplication= "+mul); 
               }
                 System.out.println("Total Mutliplication= "+mul);
                 System.out.println("***********************");
             }
             
             
               if(b==4)
             {
               System.out.println("Enter dividend: ");
               int f=input.nextInt();
               System.out.println("Enter divisor: ");
               int g=input.nextInt();
               int h=f/g;
               int i=f%g;
               System.out.println("Result="+h+"  "+"Remainder="+i);
               System.out.println("***********************");
             }

             if(b==5)
             {
                 System.out.println("Enter first number = ");
                 int ja=input.nextInt();
                 System.out.println("Enter second number = ");
                 int ka=input.nextInt();
                 if(ja>=ka)
                 {
                 int asub=ja-ka;
                 System.out.println("Absolute Result= "+asub);
                 System.out.println("***********************");
                 }
                 else if(ka>=ja)
                 {
                   int asub=ka-ja;
                   System.out.println("Absolute Result= "+asub);
                   System.out.println("***********************");
                 }
             }
             if(b==6)
             {
                 System.out.print("Enter a your number:");
                 double bk=input.nextInt();
                 System.out.println("Enter the square root value:");
                 double ck=input.nextInt();
                 double ab=Math.pow(bk,(1/ck));
                 System.out.println("Answer="+ab);
             }
             if(b==7)
             {
                 System.out.print("Enter a number:");
                 int cd=input.nextInt();
                 System.out.print("Enter the power:");
                 double de=input.nextInt();
                 double dr=1/de;
                 double gf=Math.pow(cd,dr);
                 System.out.println("Answer: "+gf);
                 
             }
             if(b==8)
             {
                 System.out.print("Enter a number to interpret");
                 int x=input.nextInt();
                 int digit=x,count=0;
                 while(digit>0)
                 {
                 digit/=10;
                 count++;
                }
                 double pow=Math.pow(10,count-1);
                 int pw=(int)pow;
                 String s;
                 while(pw>0)
             {
                int n=x/pw;
                if(n==1) s="one";
            else if(n==2) s="two";
            else if(n==3) s="three";
            else if(n==4) s="four";
            else if(n==5) s="five";
            else if(n==6) s="six";
            else if(n==7) s="seven";
            else if(n==8) s="eight";
            else if(n==9) s="nine";
            else s="zero";
            System.out.print(s+" ");
            
            x%=pw;
            pw/=10;
       }
             }
             else
             {
               System.out.println("*********************************************");
               System.out.println("INVALID INPUT..!");
               System.out.println("Only operational numbers [1-6] are eligible as input.");
               System.out.println("***********************************************");
             }
    }
        
    }
    
}
