#include <stdio.h>
 
int main() {
 
    int raio; 
    double volume; 
    
    scanf("%d", &raio); 
    
    volume = (4/3.0) * 3.14159 * pow(raio,3); 
    
    printf("VOLUME = %.3f\n", volume);
 
    return 0;
}