import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Dicionário de itens disponíveis para venda
itens_disponiveis = {
    'Maçã': 2.50,
    'Banana': 1.50,
    'Laranja': 2.00,
    'Pera': 2.00,
    'Abacaxi': 4.50
}

def calcular_total():
    total = 0.0

    for item in carrinho_listbox.get(0, tk.END):
        quantidade, nome = item.split(' x ')
        valor_unitario = itens_disponiveis.get(nome, 0.0)
        total += float(quantidade) * valor_unitario

    total_label.config(text='Total: R$ {:.2f}'.format(total))

def adicionar_item():
    quantidade = quantidade_entry.get()
    item_selecionado = itens_combobox.get()
    valor_manual = valor_entry.get()

    if quantidade.isdigit() and quantidade != '' and (item_selecionado in itens_disponiveis or item_selecionado.strip() != ''):
        if item_selecionado not in itens_disponiveis:
            if valor_manual.replace('.', '').isdigit():
                valor_unitario = float(valor_manual)
                itens_disponiveis[item_selecionado] = valor_unitario
            else:
                messagebox.showerror('Erro', 'Insira um valor válido para o item.')

        carrinho_listbox.insert(tk.END, '{} x {}'.format(quantidade, item_selecionado))
        quantidade_entry.delete(0, tk.END)
        valor_entry.delete(0, tk.END)
        calcular_total()
    else:
        messagebox.showerror('Erro', 'Insira uma quantidade válida e um item válido.')

# Criação da janela principal
window = tk.Tk()
window.title('Ponto de Venda')

# Componentes da interface
itens_combobox = ttk.Combobox(window, values=list(itens_disponiveis.keys()))
itens_combobox.pack()

valor_label = tk.Label(window, text='Valor (opcional):')
valor_label.pack()

valor_entry = tk.Entry(window)
valor_entry.pack()

quantidade_label = tk.Label(window, text='Quantidade:')
quantidade_label.pack()

quantidade_entry = tk.Entry(window)
quantidade_entry.pack()

adicionar_button = tk.Button(window, text='Adicionar Item', command=adicionar_item)
adicionar_button.pack()

carrinho_listbox = tk.Listbox(window)
carrinho_listbox.pack()

total_label = tk.Label(window, text='Total: R$ 0.00')
total_label.pack()

window.mainloop()
