class Usuario:
    def __init__(self, id: int, nome: str, email: str, senha: str, idade: int):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.idade = idade

    # Método para converter o objeto Usuario em um dicionário (JSON) para salvar.
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "idade": self.idade
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        # A função cls() chama o construtor __init__ da classe Usuario
        return cls(
            id=data['id'],
            nome=data['nome'],
            email=data['email'],
            senha=data['senha'],
            idade=data['idade']
        )
    
    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Email: {self.email}"
