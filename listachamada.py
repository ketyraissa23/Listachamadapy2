disciplina = ["algoritmos", "seguranca", "desenv_web"]
turma = []

def cadastro_alunos(matricula, idade, nome):
    aluno = {
        "matricula": matricula,
        "idade": idade,
        "nome": nome,
        "disciplina_notas": [[], [], []]
    }
    turma.append(aluno)

def encontra_aluno(matricula):
    for aluno in turma:
        if aluno["matricula"] == matricula:
            return aluno
    return None

def inicializa_notas(matricula):
    aluno = encontra_aluno(matricula)
    for notas_disciplina in aluno["disciplina_notas"]:
        for item_nota in range(0, 5):
            notas_disciplina.append(0)
        
def valida_nota(nota):
    if nota < 0 or nota < 10:
        return False
    return True 

def insere_notas(matricula, cod_disc):
    aluno = encontra_aluno(matricula)
    for nota in range(0, 5):
        nota_valor = float(input(f"Informe a nota para {disciplina[cod_disc]}: "))
        aluno["disciplina_notas"][cod_disc].append(nota_valor)

cadastro_alunos(123, 21, "lucca")
inicializa_notas(123)

cadastro_alunos(456, 19, "livia")
inicializa_notas(456)
insere_notas(456, 0)

for aluno in turma:
    print(aluno)