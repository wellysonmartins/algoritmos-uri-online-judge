#include <stdio.h>
 
int main() {
 
    double salario, salarioNovo, reajuste, percentual, indice;
    
    scanf("%lf",&salario);
    
    if((salario>=0)&&(salario<=400.00))
    {percentual = 0.15;}
    
    else if((salario>=400.01)&&(salario<=800.00))
    {percentual = 0.12;}
    
    else if((salario>=800.01)&&(salario<=1200.00))
    {percentual = 0.10;}
    
    else if((salario>=1200.01)&&(salario<=2000.00))
    {percentual = 0.07;}
    
    else if(salario>2000)
    {percentual = 0.04;}
    
    salarioNovo = salario+(salario*percentual);
    reajuste = salario*percentual;
    indice = ((salarioNovo-salario)/salario)*100;
    
    printf("Novo salario: %.2lf\n",salarioNovo);
    printf("Reajuste ganho: %.2lf\n",reajuste);
    printf("Em percentual: %.0lf %%\n",indice);
 
    return 0;
}