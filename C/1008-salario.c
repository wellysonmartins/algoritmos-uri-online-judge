#include <stdio.h>
 
int main() {
 
    int num, horas;
    double valor, SALARY;
    
        scanf("%d %d", &num, &horas);
        scanf("%lf", &valor);
        
        SALARY = horas * valor;
        
        printf("NUMBER = %d", num);
        printf("\nSALARY = U$ %.2lf\n", SALARY);
 
    return 0;
}