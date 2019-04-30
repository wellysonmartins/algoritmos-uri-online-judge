#include <stdio.h>
 
int main() {
 
    int peca1, peca2, quant1, quant2;
    double valor1, valor2, result;
               
        scanf("%d %d %lf", &peca1, &quant1, &valor1);
        scanf("%d %d %lf", &peca2, &quant2, &valor2);
                
        result = (quant1 * valor1) + (quant2 * valor2);

        printf("VALOR A PAGAR: R$ %.2lf\n", result);
        
    return 0;
}