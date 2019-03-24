#include <stdio.h>
 
int main() {
 
    int tempo, velocidade; 
    float result, distancia;

    scanf("%d %d",&tempo,&velocidade);

    distancia = (tempo*velocidade);
    result = distancia/12;

    printf("%.3f\n",result);
 
    return 0;
}