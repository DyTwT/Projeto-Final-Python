import json
import os
from usuario import Usuario
from typing import List

DEFAULT_FILE = "usuarios.txt"

class ListaUsuarios:
    def __init__(self, arquivo: str = DEFAULT_FILE):
        self.path = arquivo 
        
        # Isso aq vai garantir q o arquivo existe e contém um JSON vazio se ñ existir.
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False)
    
    def _read_all(self) -> List[Usuario]:
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Usuario.from_dict(d) for d in data]
     
    def _write_all(self, usuarios: List[Usuario]):  
        with open(self.path, "w", encoding="utf-8") as f:      
            json.dump([u.to_dict() for u in usuarios], f, indent=4, ensure_ascii=False)
    
    def list_usuarios(self) -> List[Usuario]:
        return self._read_all()
        
    def _next_id(self) -> int:
        usuarios = self._read_all()
        if not usuarios:
            return 1
        return max(u.id for u in usuarios) + 1
        
    def add_usuario(self, nome: str, email: str, senha: str, idade: int) -> Usuario:
        usuarios = self._read_all()
        
        # Verifica se email já foi cadastrado
        if any(u.email.lower() == email.lower() for u in usuarios):
            raise ValueError("Email já cadastrado.")
            
        # Cadastro de novo usuário
        new_id = self._next_id()
        novo_usuario = Usuario(id=new_id, nome=nome, email=email, senha=senha, idade=idade)
        usuarios.append(novo_usuario)
        self._write_all(usuarios)
        return novo_usuario
            
    def find_by_id(self, id: int) -> Usuario:
        usuarios = self._read_all()
        for u in usuarios:
            if u.id == id:
                return u 
        
        # Função de busca
        try:
            return next(u for u in usuarios if u.id == id)
        except StopIteration:
            return None
        

    def find_by_term(self, term: str) -> List[Usuario]:
        term = term.strip().lower()
        usuarios = self._read_all()
        return [u for u in usuarios if term in u.nome.lower() or term in u.email.lower()]
    
    def update_usuario(self, id: int, nome: str = None, email: str = None, senha: str = None, idade: int = None) -> Usuario:
        usuarios = self._read_all()
        updated = None
        for u in usuarios:
            if u.id == id:
                if nome:
                    u.nome = nome
                if email:
                    # Novamente faz a verificação de email único
                    if any(x.email.lower() == email.lower() and x.id != id for x in usuarios):
                        raise ValueError("Email já cadastrado por outro usuário")
                    u.email = email
                if senha: 
                    u.senha = senha
                if idade is not None:
                    u.idade = idade
                updated = u
                break
        if updated is None:
            raise ValueError("Usuário não encontrado.") 
        self._write_all(usuarios)
        return updated
    
    def delete_usuario(self, id: int) -> bool:
        usuarios = self._read_all()
        new = [u for u in usuarios if u.id != id]
        if len(new) == len(usuarios):
            return False  # Nenhum usuário foi deletado
        self._write_all(new)
        return True