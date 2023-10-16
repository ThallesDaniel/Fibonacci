import tkinter as tk


def fibonacci():
    result_label.config(text="Sequência de Fibonacci:")
    fib_sequence = [0, 1]
    for i in range(2, 20):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)
    output_text.set(', '.join(map(str, fib_sequence)))

def tribonacci():
    result_label.config(text="Sequência de Tribonacci:")
    trib_sequence = [0, 0, 1]
    for i in range(3, 20):
        next_number = trib_sequence[i - 1] + trib_sequence[i - 2] + trib_sequence[i - 3]
        trib_sequence.append(next_number)
    output_text.set(', '.join(map(str, trib_sequence)))

# Configuração da janela

window = tk.Tk()
window.title("Sequências Matemáticas")

 

# Rótulo para exibir o resultado

result_label = tk.Label(window, text="", font=("Helvetica", 12))
result_label.pack()


# Texto de saída

output_text = tk.StringVar()
output_label = tk.Label(window, textvariable=output_text, font=("Helvetica", 12))
output_label.pack()

# Botões

fib_button = tk.Button(window, text="Fibonacci", command=fibonacci)
trib_button = tk.Button(window, text="Tribonacci", command=tribonacci)
fib_button.pack()
trib_button.pack()

 
window.mainloop()
