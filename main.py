from lista import ListaUsuarios 
from gerenciar_usuario import GerenciadorUsuariosApp # Mude AppGUI para GerenciadorUsuariosApp


def main():
    storage = ListaUsuarios("usuarios.txt") 
    app = GerenciadorUsuariosApp(storage) 
    app.mainloop()


if __name__ == "__main__":
    main()