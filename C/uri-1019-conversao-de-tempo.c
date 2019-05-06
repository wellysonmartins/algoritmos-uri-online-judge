#include <stdio.h>
 
int main() {
 
    int tempo, horas, horasSegundo, minutos, segundos;
    
    horasSegundo=3600;
    
    scanf("%d", &tempo);
    
    horas = tempo/horasSegundo;
    minutos = (tempo -(horasSegundo*horas))/60;
    segundos = (tempo -(horasSegundo*horas)-(minutos*60));
    
    printf("%d:%d:%d\n",horas,minutos,segundos);
 
    return 0;
}