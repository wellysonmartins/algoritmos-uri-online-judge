#include <stdio.h>
 
int main() {
 
    int distancia;
    float combustivel, result;
    
    scanf("%d %f", &distancia, &combustivel);
    
    result = distancia/combustivel;
    
    printf("%.3f km/l\n",result);
 
    return 0;
}