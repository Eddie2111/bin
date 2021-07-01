#include<stdio.h>
#include<stdlib.h>
#include<time.h>


int randomgen(int lower, int upper,int count)
{
    for (int i = 0; i < count; i++) 
    {
        int num = (rand() % (upper - lower + 1)) + lower;
        printf(" %d", num);
    }
}

int main()
{
    int l = -5, u = 5, c = 1;
    //srand(time(0));
    int xb=0,yb=0; //for bot
    int xu=0,yu=0;
    char loc[90] = "a"; //for user
    for (int i=0;i<14;i++)
    {
        printf("Bot is moving.\nLocation:");xb+=randomgen(l,u,c),yb+=randomgen(l,u,c);
        printf("\n");
        if ( (xb==1 && yb==0) || (xb==0 && yb==4) || (xb==4 && yb==0) || (xb==5 && yb==2) || (xb==4 && yb==4) || (xb==4 && yb==5) || (xb==5 && yb==4) || (xb==5 && yb==5) || (xb==1 && yb==5) || (xb==0 && yb==9) || (xb==4 && yb==9) || (xb==8 && yb==6) )
        {
            xb=xb-1;
            yb=yb-1;
            printf("\n Faced wall..!\n");
        }
        else if ( (xb==1 && yb==2) || (xb==7 && yb==0) || (xb==9 && yb==2) || (xb==3 && yb==3) || (xb==7 && yb==4) || (xb==3 && yb==6) || (xb==0 && yb==7) || (xb==6 && yb==7) || (xb==7 && yb==9) )
        {
            printf("BOMBED..!\nGame Over for BOT.");
            break;
        }
        else if (xb==9 && yb==9)
        {
            printf("\nBot won the game");
        }
        printf("Enter any of these buttons to navigate your position:[u,d,l,r]\nu=up\nd=down\nl=left\nr=right.\nKey:");
        scanf("%ch",loc);
        if(loc[0]=='u')
        {
            yu+=-1;
        }
        if(loc[0]=='d')
        {
            yu+=1;
        }
        if(loc[0]=='l')
        {
            xu+=-1;
        }
        if(loc[0]=='r')
        {
            xu+=1;
        }
         if ( (xu==1 && yu==0) || (xu==0 && yu==4) || (xu==4 && yu==0) || (xu==5 && yu==2) || (xu==4 && yu==4) || (xu==4 && yu==5) || (xu==5 && yu==4) || (xu==5 && yu==5) || (xu==1 && yu==5) || (xu==0 && yu==9) || (xu==4 && yu==9) || (xu==8 && yu==6) )
        {
            xu=xu-1;
            yu=yu-1;
            printf("\n Faced wall..!\n");
        }
        else if ( (xu==1 && yu==2) || (xu==7 && yu==0) || (xu==9 && yu==2) || (xu==3 && yu==3) || (xu==7 && yu==4) || (xu==3 && yu==6) || (xu==0 && yu==7) || (xu==6 && yu==7) || (xu==7 && yu==9) )
        {
            printf("BOMBED..!\nGame Over.");
            break;
            
        }
        else if (xu==9 && yu==9)
        {
            printf("\nBot won the game");
        }
        printf("\n%d,%d\n",xu,yu);
        
    }
    return 0;
}
