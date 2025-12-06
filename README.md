## **📋 Sobre o Projeto**

O **Gerenciador de Usuários** é uma aplicação desktop simples desenvolvida em **Python** que utiliza a biblioteca gráfica **Tkinter** para a interface do usuário (GUI) e armazena os dados de cadastro em um arquivo JSON (```usuarios.txt```) para persistência.

O projeto foi estruturado em camadas para separar a lógica de negócio (gerenciamento de dados) da interface gráfica, facilitando a manutenção e a expansão.

### 🗂️ Estrutura de Arquivos
```bash
/
├── main.py               # Ponto de entrada da aplicação.
├── gerenciar_usuario.py  # Contém a classe GerenciadorUsuariosApp (a GUI em Tkinter).
├── lista.py              # Contém a classe ListaUsuarios (camada de persistência/Storage).
├── usuario.py            # Contém a classe Usuario (modelo de dados/objeto).
└── usuarios.txt          # Arquivo JSON onde os dados são salvos.
```

---
## **✨ Funcionalidades**

O sistema permite realizar as principais operações de um CRUD (Create, Read, Update, Delete):

- **Adicionar (Create):** Cadastrar novos usuários.
- **Listar (Read):** Exibir todos os usuários em uma tabela (```Treeview```).
- **Buscar (Search):** Filtrar usuários por nome ou email em tempo real.
- **Editar (Update):** Carregar dados de um usuário selecionado para edição.
- **Atualizar (Update):** Salvar as alterações de um usuário.
- **Excluir (Delete):** Remover um usuário selecionado.

---
## **🛠️ Tecnologias Utilizadas**

- **Python 3.x**
- **Tkinter:** Biblioteca padrão do Python para criação de GUIs.
- **```tkinter.ttk```:** Módulo para widgets temáticos (usado para a tabela ```Treeview```).
- **JSON:** Formato de arquivo usado para armazenamento de dados (```usuarios.txt```).

---
## **⚙️ Como Rodar o Projeto**

### **1. Pré-requisitos**
Certifique-se de ter o **Python 3.x** instalado em seu sistema. Nenhuma biblioteca externa (como ```pip install``` ) é necessária, pois ```tkinter```, ```json``` e ```os``` são módulos padrão do Python.

### **2. Clonar o Repositório**
```bash
git clone https://github.com/seu-usuario/seu-projeto.git
```

### **3. Execução**
Execute o arquivo principal ```main.py``` diretamente:
```bash
python main.py
```

A janela do **Gerenciador de Usuários** será aberta.
