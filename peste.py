import tkinter as tk
from tkinter import messagebox, simpledialog

# Lista de sorteios da Mega-Sena
sorteiosMegaSena = [
    [13, 25, 27, 30, 37, 53],
    [2, 11, 25, 32, 37, 57],
    [1, 33, 35, 39, 42, 56],
    [13, 16, 17, 34, 41, 47],
    [19, 25, 37, 45, 47, 53],
    [2, 19, 25, 44, 46, 60]
]

# Números escolhidos pelo usuário
numerosEscolhidos = []

# Função para contar a frequência dos números nos sorteios
def contarFrequencia(sorteados):
    frequencia = {}
    for sorteio in sorteados:
        for numero in sorteio:
            if numero in frequencia:
                frequencia[numero] += 1
            else:
                frequencia[numero] = 1
    return frequencia

# Função para verificar se um jogo contém as 6 dezenas já sorteadas
def jogoContemDezenasSorteadas(jogo, sorteados):
    for sorteio in sorteados:
        if all(numero in sorteio for numero in jogo):
            return True
    return False

# Função para verificar se há pelo menos 3 sequências de 3 dezenas já sorteadas
def verificarSequenciasSorteadas(jogo, sorteados):
    if len(jogo) < 6:
        messagebox.showwarning("Verificar Sequências", "Você precisa escolher exatamente 6 números.")
        return
    
    sequencias_sorteadas = 0
    for i in range(len(jogo) - 2):
        sequencia = jogo[i:i + 3]
        for sorteio in sorteados:
            for j in range(len(sorteio) - 2):
                if sequencia == sorteio[j:j + 3]:
                    sequencias_sorteadas += 1
                    break
            if sequencias_sorteadas >= 3:
                messagebox.showinfo("Verificar Sequências", "Há pelo menos 3 sequências de 3 dezenas já sorteadas.")
                return
    messagebox.showinfo("Verificar Sequências", "Não há pelo menos 3 sequências de 3 dezenas já sorteadas.")

# Função para adicionar números escolhidos pelo usuário
def adicionarNumerosEscolhidos():
    sequenciaDigitada = simpledialog.askstring("Adicionar Números", "Digite a sequência de números escolhidos separados por espaço:")
    if sequenciaDigitada:
        numeros = list(map(int, sequenciaDigitada.split()))
        if len(numeros) != 6:
            messagebox.showwarning("Adicionar Números", "Você precisa escolher exatamente 6 números.")
            return
        elif any(num < 1 or num > 60 for num in numeros):
            messagebox.showwarning("Adicionar Números", "Os números devem estar entre 1 e 60.")
            return
        elif jogoContemDezenasSorteadas(numeros, sorteiosMegaSena):
            messagebox.showinfo("Adicionar Números", "Este jogo contém as 6 dezenas já sorteadas.")
        else:
            numerosEscolhidos.append(numeros)
            verificarSequenciasSorteadas(numeros, sorteiosMegaSena)
            messagebox.showinfo("Adicionar Números", "Números adicionados com sucesso!")

# Função para mostrar os números mais frequentes
def mostrarNumerosMaisFrequentes():
    frequencia = contarFrequencia(sorteiosMegaSena)
    numeros_ordenados = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)
    
    mensagem = ""
    for numero, freq in numeros_ordenados[:12]:
        mensagem += f"Número: {numero} - Frequência: {freq}\n"
    
    messagebox.showinfo("Números Mais Frequentes", mensagem)

# Função para contar a ocorrência de ternos, quadras, quinas e senas nos sorteios
def contarOcorrenciasTernosQuadrasQuinasSenas(sorteados):
    ocorrencias = {
        'Sena': 0,
        'Quina': 0,
        'Quadra': 0,
        'Terno': 0
    }

    for sorteio in sorteados:
        acertos = len(set(sorteio).intersection(numerosEscolhidos[-1]))
        if acertos == 6:
            ocorrencias['Sena'] += 1
        elif acertos == 5:
            ocorrencias['Quina'] += 1
        elif acertos == 4:
            ocorrencias['Quadra'] += 1
        elif acertos == 3:
            ocorrencias['Terno'] += 1

    return ocorrencias

# Configuração da janela principal
root = tk.Tk()
root.title("Mega-Sena - Consulta de Resultados")
root.geometry("400x300")

# Botões
btnAdicionar = tk.Button(root, text="Adicionar Números", command=adicionarNumerosEscolhidos)
btnAdicionar.pack(pady=10)

btnNumerosMaisFrequentes = tk.Button(root, text="Números Mais Frequentes", command=mostrarNumerosMaisFrequentes)
btnNumerosMaisFrequentes.pack(pady=10)

btnVerificarSequencias = tk.Button(root, text="Verificar Sequências", command=lambda: verificarSequenciasSorteadas(numerosEscolhidos[-1], sorteiosMegaSena) if numerosEscolhidos else messagebox.showwarning("Verificar Sequências", "Você precisa escolher pelo menos um jogo."))
btnVerificarSequencias.pack(pady=10)

btnContarOcorrencias = tk.Button(root, text="Contar Ocorrências", command=lambda: messagebox.showinfo("Contar Ocorrências", contarOcorrenciasTernosQuadrasQuinasSenas(sorteiosMegaSena)))
btnContarOcorrencias.pack(pady=10)

btnSair = tk.Button(root, text="Sair", command=root.quit)
btnSair.pack(pady=10)

# Rodar o loop principal do tkinter
root.mainloop()






