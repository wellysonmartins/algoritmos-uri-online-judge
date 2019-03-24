#include <stdio.h>
 
int main() {
 
    double A, B, C, delta, x, x1, x2;
    
    scanf("%lf %lf %lf",&A,&B,&C);
        
    delta = pow(B,2) - 4 * A * C;

    if (A==0)
       {
           printf("Impossivel calcular\n");
       }    
    else if (delta>0) 
       {
       x1 = ((-B)+sqrt(delta))/(2*A);
       x2 = ((-B)-sqrt(delta))/(2*A);
       printf("R1 = %.5lf\n",x1);
       printf("R2 = %.5lf\n",x2);
       }
    else if (delta<0)  
       {
           printf("Impossivel calcular\n");
       }
 
    return 0;
}