#include <stdio.h>
 
int main() {
 
    int inicio, final, result;
    
    scanf("%d %d",&inicio,&final);
    
    if (inicio>=final)
    {
       result = (24-inicio)+final;
       printf("O JOGO DUROU %d HORA(S)\n",result);
    }
    else
    {
       result = final-inicio;
       printf("O JOGO DUROU %d HORA(S)\n",result);
    }
 
    return 0;
}