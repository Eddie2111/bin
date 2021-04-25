import java.util.*;
public class Alph {
    public static void main (String [] args){

        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        if (s.length()%2==0){
            System.out.println("Even");
        }else {
            System.out.println("Odd");
        }

    }
    
}