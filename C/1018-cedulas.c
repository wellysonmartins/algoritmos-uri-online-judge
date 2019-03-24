#include <stdio.h>
 
int main() {
 
    int N,valor, cem , cinquenta , vinte , dez , cinco , dois , um;

    scanf("%d",&valor);
    
    N = valor;

    cem = N / 100;
    N = N - (cem *100);

    cinquenta = N / 50;
    N = N - (cinquenta * 50);

    vinte = N / 20;
    N = N - (vinte * 20);

    dez = N /10;
    N = N -(dez * 10);

    cinco = N / 5;
    N = N - (cinco * 5);

    dois = N / 2;
    N = N - (dois * 2);
    
    um = N;

    printf("%d\n",valor);
    printf("%d nota(s) de R$ 100,00\n",cem);
    printf("%d nota(s) de R$ 50,00\n",cinquenta);
    printf("%d nota(s) de R$ 20,00\n",vinte);
    printf("%d nota(s) de R$ 10,00\n",dez);
    printf("%d nota(s) de R$ 5,00\n",cinco);
    printf("%d nota(s) de R$ 2,00\n",dois);
    printf("%d nota(s) de R$ 1,00\n",um);
 
    return 0;
}