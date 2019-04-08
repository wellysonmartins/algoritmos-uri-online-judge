palavras = []
for i in range(3): palavras.append(input())

animal = {
   "vertebrado":{ "ave":{ "carnivoro":"aguia", "onivoro":"pomba" },
                  "mamifero":{ "onivoro":"homem", "herbivoro":"vaca" }},
   "invertebrado":{ "inseto":{ "hematofago":"pulga", "herbivoro":"lagarta" },
                    "anelideo":{ "hematofago":"sanguessuga", "onivoro":"minhoca" }}
}

print(animal[palavras[0]][palavras[1]][palavras[2]])