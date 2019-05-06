#include <stdio.h>
 
int main() {
 
    char nome;
    double salarioFixo, vendas, salarioFinal;
    
        scanf("%s", &nome);
        scanf("%lf %lf", &salarioFixo, &vendas);
        
        salarioFinal = (vendas*0.15) + salarioFixo;
        
        printf("TOTAL = R$ %.2lf\n", salarioFinal);
        
    return 0;
}