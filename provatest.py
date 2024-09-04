aluno = 0
media = 0
print("digite as notas do aluno separadas por espaco")
notas=input().split()
for nota in notas:
    media += int(notas [aluno])
    aluno += 1
    media = media/aluno
print(f"a media é {media}")