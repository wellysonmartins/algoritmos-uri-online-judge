#include <stdio.h>
 
int main() {
 
    double A, B, C, aux;
    
    scanf("%lf %lf %lf",&A, &B, &C);
    
    while((A<B)||(B<C))
    {   
         if(A<B)
         {  aux = A; A = B; B = aux;  }
         if(B<C)
         {  aux = B; B = C; C = aux;  }
    }
    
    if(A>=B+C)
    {printf("NAO FORMA TRIANGULO\n");}
    
    else
    {
         if(pow(A,2)==pow(B,2)+pow(C,2))  
         {printf("TRIANGULO RETANGULO\n");} 
    
         else if(pow(A,2)>pow(B,2)+pow(C,2))
         {printf("TRIANGULO OBTUSANGULO\n");}
    
         else if(pow(A,2)<pow(B,2)+pow(C,2))
         {printf("TRIANGULO ACUTANGULO\n");}
    }
    
    if((A==B)&&(B==C))
         {printf("TRIANGULO EQUILATERO\n");}
    
    else if((A==B)||(B==C)||(A==C))
         {printf("TRIANGULO ISOSCELES\n");}
 
    return 0;
}