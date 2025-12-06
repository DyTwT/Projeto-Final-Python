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

##
