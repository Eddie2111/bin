import java.util.*;
class prac2 {

  
  // method with no parameter
  public int throwcoin() {
    Random rnd=new Random();
    int c1=rnd.nextInt(2);
    return c1;
  }

  // method with single parameter
  public int throwdice() {
    Random rnd= new Random();
    int d1=rnd.nextInt(7);
    return d1;
  }

  public static void main(String[] args) {
    
    // create an object of Main
    Main obj = new Main();
    int a=obj.throwdice();
    int b=obj.throwcoin();
    int g=1;
    while (g<5)
    {
        System.out.println("Dice: "+obj.throwdice());
        System.out.println("Coin: "+obj.throwcoin());
        int sum=a+b;
        if (sum==7)
        {
            System.out.println("You won..!");
            break;
        }
        if(sum<7)
        {
            System.out.println("Your point: "+sum);
            sum+=sum;
        }
        if (sum==0)
        {
            System.out.println("Lost..!");
            break;
        }
    }

  }
}
