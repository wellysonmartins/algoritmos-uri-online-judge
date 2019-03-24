#include <stdio.h>
 
int main() {
 
    int inicioHora, finalHora, inicioMinuto, finalMinuto, resultHora, resultMinuto;
    
    scanf("%d %d %d %d",&inicioHora,&inicioMinuto,&finalHora,&finalMinuto);
    
    if (inicioHora>=finalHora)
    {resultHora = (24-inicioHora)+finalHora;}
    else
    {resultHora = finalHora-inicioHora;}
     
    if (inicioMinuto<=finalMinuto)
    { 
       resultMinuto = finalMinuto-inicioMinuto;
       printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n",resultHora,resultMinuto);
    }
    else
    {
       resultMinuto = 60-(inicioMinuto-finalMinuto);
       printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n",resultHora-1,resultMinuto);
    } 
 
    return 0;
}