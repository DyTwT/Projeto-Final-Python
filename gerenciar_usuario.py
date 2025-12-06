import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 

class GerenciadorUsuariosApp(tk.Tk):
    def __init__(self, storage):
        super().__init__()
        self.storage = storage 
        self.title("Gerenciador de Usuários")
        
        # Define as colunas do Treeview
        # Adicionei 'ID' aqui, mas o self.tree já tinha sido definido antes.
        columns = ("ID", "Nome", "Email", "Senha", "Idade")
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        
        # Configurações iniciais
        self.setup_ui()
        self.refresh_list() # Carrega os dados iniciais
    
    # --- CORREÇÃO DE LAYOUT: USANDO APENAS pack() OU AJUSTANDO O FLUXO DE pack() ---
    def setup_ui(self):
        # 1. Frame do Formulário (Entradas e Botões de Ação)
        form_frame = tk.Frame(self, padx=10, pady=10)
        form_frame.pack(side=tk.TOP, fill=tk.X) # Usa pack()

        # Usando grid() dentro do form_frame (isso é OK)
        tk.Label(form_frame, text="Nome:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.entry_nome = tk.Entry(form_frame, width=30)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(form_frame, text="Email:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.entry_email = tk.Entry(form_frame, width=30)
        self.entry_email.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(form_frame, text="Senha:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.entry_senha = tk.Entry(form_frame, width=30, show="*") # Oculta a senha
        self.entry_senha.grid(row=2, column=1, padx=5, pady=2)

        tk.Label(form_frame, text="Idade:").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.entry_idade = tk.Entry(form_frame, width=30)
        self.entry_idade.grid(row=3, column=1, padx=5, pady=2)
        
        # Frame dos Botões (dentro do form_frame)
        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(button_frame, text="Adicionar", command=self.on_add).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Editar", command=self.on_edit).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Atualizar", command=self.on_update).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Excluir", command=self.on_delete).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Limpar", command=self.clear_form).pack(side=tk.LEFT, padx=5)
        
        # 2. Frame de Busca (Pack SIDE=BOTTOM)
        search_frame = tk.Frame(self, padx=10, pady=5)
        search_frame.pack(side=tk.BOTTOM, fill=tk.X) 
        
        tk.Label(search_frame, text="Buscar:").pack(side=tk.LEFT)
        self.entry_search = tk.Entry(search_frame, width=50)
        self.entry_search.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.entry_search.bind("<KeyRelease>", self.on_search)
        
        # 3. Treeview e Barra de Rolagem (Pack FILL/EXPAND para ocupar o meio)
        # É crucial que o Treeview seja empacotado corretamente.
        
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Senha", text="Senha")
        self.tree.heading("Idade", text="Idade")
        
        self.tree.column("ID", width=50, stretch=tk.NO, anchor=tk.CENTER)
        self.tree.column("Nome", width=150, stretch=tk.YES)
        self.tree.column("Email", width=200, stretch=tk.YES)
        self.tree.column("Senha", width=100, stretch=tk.NO) 
        self.tree.column("Idade", width=70, stretch=tk.NO, anchor=tk.CENTER)

        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        
        # Empacotamento correto para Treeview e Scrollbar
        # Empacota a barra de rolagem primeiro (no lado RIGHT)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        # Empacota o Treeview no espaço restante (LEFT, FILL, EXPAND)
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)


    def on_add(self):
        nome, email, senha, idade = self._get_form_data()
        
        if not self.validate_form(nome, email, senha, idade):
            return
            
        try:
            idade = int(idade) 
            novo_usuario = self.storage.add_usuario(nome, email, senha, idade)
            
            messagebox.showinfo("Sucesso", f"Usuário {novo_usuario.nome} cadastrado com ID: {novo_usuario.id}")
            self.refresh_list()
            self.clear_form()
            
        except ValueError as e:
            messagebox.showerror("Erro de Cadastro", str(e))
    

    def on_search(self, event):
        term = self.entry_search.get()
        self.search_users(term)
    
    
    def _get_form_data(self):
        """Método auxiliar que deve retornar os dados atuais do formulário."""
        return self.entry_nome.get(), self.entry_email.get(), self.entry_senha.get(), self.entry_idade.get()

    def validate_form(self, nome, email, senha, idade):
        """Método auxiliar que deve validar os dados do formulário."""
        
        if not nome or not email or not senha or not idade:
            messagebox.showerror("Erro de Validação", "Todos os campos devem ser preenchidos.")
            return False
        
        try:
            if int(idade) <= 0:
                messagebox.showerror("Erro de Validação", "A idade deve ser um número positivo.")
                return False
        except ValueError:
            messagebox.showerror("Erro de Validação", "A idade deve ser um número inteiro válido.")
            return False
            
        return True

    def refresh_list(self):
        """Método auxiliar para recarregar a lista na Treeview."""
        self.tree.delete(*self.tree.get_children())
        usuarios = self.storage.list_usuarios()
        for u in usuarios:
            # Inserindo todos os campos, incluindo a Senha
            self.tree.insert("", tk.END, values=(u.id, u.nome, u.email, u.senha, u.idade))

    def clear_form(self):
        """Método auxiliar para limpar os campos do formulário."""
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)

    def search_users(self, term): 
        self.tree.delete(*self.tree.get_children()) 
        users = self.storage.find_by_term(term)
        for u in users:
            self.tree.insert("", tk.END, values=(u.id, u.nome, u.email, u.senha, u.idade))

    def _get_selected_id(self):
        sel = self.tree.selection()
        if not sel:
            return None
        item = self.tree.item(sel[0])
        return int(item["values"][0])

    def on_edit(self):
        id_sel = self._get_selected_id()
        if id_sel is None:
            messagebox.showwarning("Editar Usuário", "Nenhum usuário selecionado") 
            return
        user = self.storage.find_by_id(id_sel)
        if not user:
            messagebox.showerror("Erro", "Usuário não encontrado")
            return
        
        self.clear_form() # Limpa antes de preencher
        self.entry_nome.insert(0, user.nome)
        self.entry_email.insert(0, user.email)
        self.entry_senha.insert(0, user.senha)
        self.entry_idade.insert(0, str(user.idade))

    def on_update(self):
        id_sel = self._get_selected_id()
        if id_sel is None:
            messagebox.showwarning("Atualizar Usuário", "Selecione o usuário na lista antes de atualizar") 
            return
        nome, email, senha, idade_str = self._get_form_data()
        
        if not self.validate_form(nome, email, senha, idade_str):
            return
        
        try:
            idade = int(idade_str)
            updated = self.storage.update_usuario(id_sel, nome=nome, email=email, senha=senha, idade=idade)
            messagebox.showinfo("Atualizado", f"Usuário atualizado: {updated.nome}") 
            self.refresh_list()
            self.clear_form()
        except ValueError as e:
            messagebox.showerror("Erro de Atualização", str(e))

    def on_delete(self):
        id_sel = self._get_selected_id()
        if id_sel is None:
            messagebox.showwarning("Excluir Usuário", "Selecione um usuário para excluir") 
            return
        
        if not messagebox.askyesno("Confirmar Exclusão", "Deseja realmente excluir o usuário selecionado?"): 
            return
            
        ok = self.storage.delete_usuario(id_sel) 
        
        if ok:
            messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!") 
            self.refresh_list()
            self.clear_form()
        else:
            messagebox.showerror("Erro de Exclusão", "Usuário não pôde ser excluído ou não foi encontrado.")