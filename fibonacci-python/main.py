a = 1
b = 1
i = 1

n = int(input("insira o numero que deseja ver na sequencia de fibonacci: "))
print("1\n1")

for i in range(n - 2):
    fibo = a + b
    a = b
    b = fibo
    print(f"{fibo}")