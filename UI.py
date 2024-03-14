import tkinter as tk
from tkinter import filedialog
checkbuttons = []
def select_folder(caixa_texto):
    def inner():
        pasta = filedialog.askdirectory()
        if pasta:
            caixa_texto.delete(1.0, tk.END)  # Limpa o conteúdo atual da caixa de texto
            caixa_texto.insert(tk.END, pasta)
    return inner
def teste():
   global created_folders
   global checkbuttons
   created_folders.append(checkbuttons)
   print(checkbuttons)

def criar_janela_organizacao():
    #a logica ta toda errada.
    #que merda
    nova_janela = tk.Toplevel(root)
    nova_janela.geometry("500x500")
    nova_janela.title("Create Folder Organization")
    nova_janela.resizable(False, False)  # Impede o redimensionamento da janela

    # Cria um frame para conter os widgets
    frame = tk.Frame(nova_janela)
    frame.pack(fill=tk.BOTH, expand=True)

    # Cria um canvas dentro do frame
    canvas = tk.Canvas(frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Adiciona uma barra de rolagem vertical
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configura o canvas para rolar verticalmente com a barra de rolagem
    canvas.configure(yscrollcommand=scrollbar.set)

    # Cria outro frame dentro do canvas para colocar os widgets
    inner_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    FolderName = tk.Label(inner_frame, text="Folder Name: ", font=('Arial', 15), padx=10, pady=20)
    FolderName.grid(row=0, column=0)

    caixa_texto = tk.Text(inner_frame, height=1, width=40)
    caixa_texto.grid(row=0, column=1, sticky=tk.W)

    # Lista de extensões de arquivos desejadas
    extensoes = [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".tiff", ".svg", ".pdf", ".docx", ".xlsx", ".pptx", ".txt"]
    global created_folders
    checkbuttons = []
    # Cria uma matriz de Checkbuttons para as extensões de arquivo
    for i, extensao in enumerate(extensoes):
        var = tk.BooleanVar()  # Cria uma variável booleana para armazenar o estado do Checkbutton
        checkbutton = tk.Checkbutton(inner_frame, text=extensao, variable=var)
        checkbutton.grid(row=i + 1, column=1, sticky=tk.W)
        checkbuttons.append(var)


    # Botão para confirmar seleção
    botao_confirmar = tk.Button(inner_frame, text="Confirmar",command = teste)
    botao_confirmar.grid(row=len(extensoes) + 1, column=1, pady=10,sticky=tk.W)

    # Atualiza o tamanho do canvas
    inner_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    return checkbuttons

root = tk.Tk()
root.geometry("600x500")
root.title("Minha primeira Interface!")

# Cria um rótulo com o texto "DownloadManager"
label = tk.Label(root, text="DownloadManager", font=('Arial', 18))
label.pack(pady=25)

frame = tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

# Cria um rótulo com o texto fixo
info_label = tk.Label(frame, text="Downloads Folder: ", font=('Arial', 13), padx=10, pady=10)
info_label.grid(row=0, column=0, sticky=tk.E)

# Cria uma caixa de texto para exibir o caminho da pasta selecionada
caixa_texto = tk.Text(frame, height=1, width=40)
caixa_texto.grid(row=0, column=1, sticky=tk.W)

# Botão para selecionar a pasta
botao_selecionar = tk.Button(frame, text="Select Folder", command=select_folder(caixa_texto))
botao_selecionar.grid(row=0, column=2, sticky=tk.W, padx=10)

# Segundo conjunto de rótulo, caixa de texto e botão
info_label2 = tk.Label(frame, text="Folder Wanted: ", font=('Arial', 13))
info_label2.grid(row=1, column=0, sticky=tk.E)

caixa_texto2 = tk.Text(frame, height=1, width=40)
caixa_texto2.grid(row=1, column=1, sticky=tk.W)

botao_selecionar2 = tk.Button(frame, text="Select Folder", command=select_folder(caixa_texto2))
botao_selecionar2.grid(row=1, column=2, sticky=tk.W, padx=10)

created_folders = []
# Botão para criar a organização de pastas
botao_criar_organizacao = tk.Button(frame, text="Create Folder\n Organization", command= criar_janela_organizacao)
botao_criar_organizacao.grid(row=2, column=2, sticky=tk.W, padx=10)

# Lista de pastas selecionadas
lista_pastas = tk.Listbox(frame, height=5, width=50)
lista_pastas.grid(row=2, column=1, columnspan=2, pady=10, sticky=tk.W)


frame.pack()

root.mainloop()
