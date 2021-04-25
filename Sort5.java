import java.util.*;

public class Sort5 {
    public static void main (String [] args){

        Scanner sc=new Scanner(System.in);
        int [] a=new int [5];
        for (int i=0;i<a.length;i++){
            a[i]=sc.nextInt();
        }
        for (int i=0;i<a.length-1;i++){
            int min=a[i];
            int pos=i;
            for(int j=i+1;j<a.length;j++){
                if (a[j]<min){
                    min=a[j];
                    pos=j;
                }
            }
            int temp=a[i];
            a[i]=min;
            a[pos]=temp;
        }
        for (int i=0;i<a.length;i++){
            System.out.print(a[i]+" ");
        }
        System.out.println("Sorted");
    }
    
}