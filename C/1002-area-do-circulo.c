#include <stdio.h>
 
int main() {
 
    double raio, area;
               
        scanf("%lf", &raio);

        area  = 3.14159 * pow(raio,2);

        printf("A=%.4f\n", area);
 
    return 0;
}