import sqlite3
import os

def create():
    if not os.path.exists("c.db"):
        conn = sqlite3.connect("c.db")
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS credenciais (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user TEXT,
                            password TEXT,
                            key INT
        )''')

        conn.commit()
        conn.close()
    else:
        pass

def add(loginwd, passwd, keywd):
    conn = sqlite3.connect("c.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO credenciais (user, password, key) VALUES (?, ?, ?)",
                   (loginwd, passwd, keywd))

    conn.commit()
    conn.close()
    print(f"User cadastrado, key: {keywd}")

def remove(keywd):
    conn = sqlite3.connect("c.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM credenciais WHERE key = ?", (keywd,))

    conn.commit()
    conn.close()
    print(f"User com key {keywd} removido.")

def change_password(keywd, new_passwd):
    conn = sqlite3.connect("c.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE credenciais SET password = ? WHERE key = ?", (new_passwd, keywd))

    conn.commit()
    conn.close()
    print(f"Senha atualizada para key {keywd}.")

def search(keywd):
    with sqlite3.connect("c.db") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT user, password, key FROM credenciais WHERE key = ?", (keywd,))

        resultado = cursor.fetchone()

        if resultado:
            user, password, key = resultado
            resposta = f"""
User: {user}
Pass: {password}
Key: {key}"""
            print(resposta)
        else:
            print("Usuário não encontrado.")

def main():
    create()
    opt = input("Digite 1 para cadastro, 2 para busca, 3 para remoção, ou 4 para mudar senha: ")
    if opt == "1":
        add(loginwd=input("Insira o login: "), passwd=input("Insira a senha: "), keywd=int(input("Insira a key de consulta/recuperação (números): ")))
    elif opt == "2":
        search(keywd=int(input("Insira a key da conta (números): ")))
    elif opt == "3":
        remove(keywd=int(input("Insira a key da conta a ser removida (números): ")))
    elif opt == "4":
        change_password(keywd=int(input("Insira a key da conta cuja senha será alterada (números): ")), new_passwd=input("Insira a nova senha: "))
    else:
        print("Opção inválida. Escolha 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()
