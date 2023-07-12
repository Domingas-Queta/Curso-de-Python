identidade = input("Qual é o seu número de B.I?")
resultado = identidade.strip()
base_de_dados = {"00590786LA045":
                 {
                 "Nome":"Domingas Queta",
                 "Cursos":["Python", "Desenvolvimento web"],
                 "Computador": "Mediateca"
                 },
                 "005835741LA048":
                 {
                 "Nome":"Tatiana Gomes",
                 "Cursos":["Python", "Desenvolvimento web"],
                 "Computador": "Code Academy: Girls"
                 }
                  }
        
aluna = base_de_dados.get(resultado)
if aluna:
    print("Aluna encontrada com sucesso!")
    print("Hora de entrada 9h00")
else:
     print("O B.I não corresponde a nenhuma aluna.")
    
