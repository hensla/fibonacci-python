🌀 fibonacci-sequence
Ferramenta simples em Python que exibe os primeiros N termos da sequência de Fibonacci diretamente no terminal.
📋 Descrição
fibonacci-sequence solicita ao usuário a quantidade de termos desejados e imprime a sequência de Fibonacci correspondente, um número por linha.
🚀 Como usar
bashpython main.py
Exemplo de execução:
insira o numero que deseja ver na sequencia de fibonacci: 7
1
1
2
3
5
8
13
🐛 Código
pythona = 1
b = 1
i = 1

n = int(input("insira o numero que deseja ver na sequencia de fibonacci: "))
print("1\n1")

for i in range(n - 2):
    fibo = a + b
    a = b
    b = fibo
    print(f"{fibo}")
💡 Como funciona

Define os dois primeiros termos da sequência: a = 1 e b = 1.
Imprime os dois primeiros valores fixos (1 e 1).
Percorre um laço for calculando os próximos termos com fibo = a + b.
A cada iteração, desloca os valores: a recebe b e b recebe o novo termo.
Repete até atingir o total de termos desejado.

📁 Estrutura do projeto
fibonacci-sequence/
└── main.py   # Script principal
🛠️ Requisitos

Python 3.x
Nenhuma biblioteca externa necessária

📄 Licença MIT
