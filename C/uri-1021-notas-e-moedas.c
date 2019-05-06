#include <stdio.h>
 
int main() {
 
    int cem , cinquenta , vinte , dez , cinco , dois , um;
    int cinquentaCent, vinteCent, dezCent, cincoCent, umCent;
    double N; 
    
    scanf("%lf",&N);
     
    cem = N / 100;
    N = N - (cem * 100);
 
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
    N = N - (um / 1);
    
    cinquentaCent = N / 0.50;
    N = N - (cinquentaCent * 0.50);
    
    vinteCent = N / 0.25;
    N = N - (vinteCent * 0.25);
    
    dezCent = N / 0.10; 
    N = N - (dezCent * 0.10);
    
    cincoCent = N / 0.05;
    N = N - (cincoCent * 0.05);
    
    umCent = N / 0.01;
        
    printf("NOTAS:\n");
    printf("%d nota(s) de R$ 100.00\n",cem);
    printf("%d nota(s) de R$ 50.00\n",cinquenta);
    printf("%d nota(s) de R$ 20.00\n",vinte);
    printf("%d nota(s) de R$ 10.00\n",dez);
    printf("%d nota(s) de R$ 5.00\n",cinco);
    printf("%d nota(s) de R$ 2.00\n",dois);
    printf("MOEDAS:\n");
    printf("%d moeda(s) de R$ 1.00\n",um);
    printf("%d moeda(s) de R$ 0.50\n",cinquentaCent);
    printf("%d moeda(s) de R$ 0.25\n",vinteCent);
    printf("%d moeda(s) de R$ 0.10\n",dezCent);
    printf("%d moeda(s) de R$ 0.05\n",cincoCent);
    printf("%d moeda(s) de R$ 0.01\n",umCent);
 
    return 0;
}