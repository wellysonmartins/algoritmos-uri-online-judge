#include <stdio.h>
 
int main() {
 
    float N1, N2, N3, N4, MEDIA, notaExame, mediaFinal; 
        
         scanf("%f %f %f %f",&N1,&N2,&N3,&N4);
    
    MEDIA = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1) ) / 10;
    
         printf("Media: %.1f\n",MEDIA);
    
    if (MEDIA>=7.0)
    {
         printf("Aluno aprovado.\n");
    }
    else if (MEDIA<5.0)
    {
         printf("Aluno reprovado.\n");
    }
    else if ((MEDIA>=5.0)&&(MEDIA<=6.9))
    {
         printf("Aluno em exame.\n");
         scanf("%f",&notaExame);
         printf("Nota do exame: %.1f\n",notaExame);
         mediaFinal = (notaExame+MEDIA)/2;
         if (mediaFinal>=5.0)
         {
              printf("Aluno aprovado.\n");
              printf("Media final: %.1f\n",mediaFinal);
         }
         else if (mediaFinal<=4.9)
         {
              printf("Aluno reprovado.\n");
              printf("Media final: %.1f\n",mediaFinal);
         }
    }
 
    return 0;
}