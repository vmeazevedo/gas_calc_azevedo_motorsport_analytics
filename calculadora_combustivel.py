import tkinter as tk
from tkinter import messagebox
import logging
from PIL import Image, ImageTk


def limpar_campos():
    entry_consumo.delete(0, tk.END)
    entry_voltas.delete(0, tk.END)
    entry_tanque.delete(0, tk.END)
    entry_reserva.delete(0, tk.END)
    entry_tempo.delete(0, tk.END)
    resultado_text.delete("1.0", tk.END)


# Função de cálculo de combustível corrigida
def calcular_combustivel_porshce_911_gt3(consumo_medio_por_volta, num_voltas, capacidade_tanque, reserva_combustivel, tempo_por_volta):
    combustivel_necessario_por_volta = consumo_medio_por_volta
    combustivel_necessario_total = combustivel_necessario_por_volta * num_voltas

    if combustivel_necessario_total > capacidade_tanque - reserva_combustivel:
        combustivel_necessario_total = capacidade_tanque - reserva_combustivel

    tempo_total = tempo_por_volta * num_voltas
    return combustivel_necessario_total, tempo_total

def converter_segundos_para_minutos_segundos(segundos):
    minutos = int(segundos // 60)
    segundos_restantes = int(segundos % 60)
    return minutos, segundos_restantes

def calcular_combustivel():
    try:
        consumo_medio_por_volta = float(entry_consumo.get())
        num_voltas = int(entry_voltas.get())
        capacidade_tanque = float(entry_tanque.get())
        reserva_combustivel = float(entry_reserva.get())
        tempo_por_volta = float(entry_tempo.get())

        # Cálculo do combustível necessário e tempo total
        combustivel_necessario, tempo_total = calcular_combustivel_porshce_911_gt3(consumo_medio_por_volta, num_voltas, capacidade_tanque, reserva_combustivel, tempo_por_volta)

        minutos_total, segundos_total = converter_segundos_para_minutos_segundos(tempo_total)

        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, f"Para {num_voltas} volta(s), serão necessários aproximadamente: {combustivel_necessario:.2f} litros de combustível.\n", "left")
        resultado_text.insert(tk.END, f"Tempo total estimado: {minutos_total:02d} minutos e {segundos_total:02d} segundos.", "left")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida. Certifique-se de digitar valores numéricos corretos.")

# Interface Gráfica
root = tk.Tk()
root.title("Calculadora de Combustível - Azevedo Motorsport Analytics")

# Define o tamanho fixo da janela (largura x altura)
root.geometry("790x400")

# Estilo dos elementos
bg_color = "#f0f0f0"  # Cor de fundo
font_label = ("Helvetica", 12, "bold")  # Fonte dos labels
font_entry = ("Helvetica", 12)  # Fonte das caixas de entrada
font_button = ("Helvetica", 12, "bold")  # Fonte do botão "Calcular"
font_resultado = ("Helvetica", 12)  # Fonte do resultado

frame = tk.Frame(root, bg=bg_color)
frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Redimensiona a imagem do logotipo
logo_image = Image.open("banner.png")  # Substitua pelo caminho do logotipo desejado
logo_image = logo_image.resize((265, 165), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(frame, image=logo_image, bg=bg_color)
logo_label.grid(row=0, column=3, rowspan=5, padx=10, pady=5)

label_consumo = tk.Label(frame, text="Consumo médio por volta (L):", font=font_label, bg=bg_color, anchor="w", justify="left")
label_consumo.grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_consumo = tk.Entry(frame, font=font_entry)
entry_consumo.grid(row=0, column=1, padx=10, pady=5, sticky="w")

label_voltas = tk.Label(frame, text="Número de voltas desejadas:", font=font_label, bg=bg_color, anchor="w", justify="left")
label_voltas.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_voltas = tk.Entry(frame, font=font_entry)
entry_voltas.grid(row=1, column=1, padx=10, pady=5, sticky="w")

label_tanque = tk.Label(frame, text="Capacidade do tanque (L):", font=font_label, bg=bg_color, anchor="w", justify="left")
label_tanque.grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_tanque = tk.Entry(frame, font=font_entry)
entry_tanque.grid(row=2, column=1, padx=10, pady=5, sticky="w")

label_reserva = tk.Label(frame, text="Reserva de combustível (L):", font=font_label, bg=bg_color, anchor="w", justify="left")
label_reserva.grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_reserva = tk.Entry(frame, font=font_entry)
entry_reserva.grid(row=3, column=1, padx=10, pady=5, sticky="w")

label_tempo = tk.Label(frame, text="Tempo de volta estimado (s):", font=font_label, bg=bg_color, anchor="w", justify="left")
label_tempo.grid(row=4, column=0, sticky="w", padx=10, pady=5)
entry_tempo = tk.Entry(frame, font=font_entry)
entry_tempo.grid(row=4, column=1, padx=10, pady=5, sticky="w")

calcular_button = tk.Button(frame, text="Calcular", font=font_button, command=calcular_combustivel, bg="#333333", fg="white", activebackground="#45a049")
calcular_button.grid(row=5, columnspan=4, pady=10, padx=100, sticky="w")

limpar_button = tk.Button(frame, text="Limpar", font=font_button, command=limpar_campos, bg="#333333", fg="white", activebackground="#45a049")
limpar_button.grid(row=5, columnspan=4, pady=10, padx=10, sticky="w")

resultado_text = tk.Text(frame, height=5, width=50, font=font_resultado, bd=2, relief=tk.SOLID)
resultado_text.grid(row=6, column=0, columnspan=4, pady=10, padx=10, sticky="ew")

rodape_label = tk.Label(root, text="Desenvolvido por Vinícius Azevedo", font=("Helvetica", 10), bg=bg_color)
rodape_label.pack(side=tk.BOTTOM, pady=5)

root.mainloop()
