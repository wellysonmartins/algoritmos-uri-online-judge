n1, n2, n3, n4 = map(float, input().split(" "))

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

def print_media(media):
   return print("Media: {:.1f}".format(media))

if media >= 7.0:
   print_media(media)
   print("Aluno aprovado.")
elif media < 5.0:
   print_media(media)
   print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
   n5 = float(input())
   media_final = (n5 + media) / 2

   print_media(media)
   print("Aluno em exame.")
   print("Nota do exame: {:.1f}".format(n5))
   
   if media_final >= 5.0:
      print("Aluno aprovado.")
   elif media_final <= 4.9:
      print("Aluno reprovado.")
   
   print("Media final: {:.1f}".format(media_final))