import pandas as pd
import json
import hashlib
from openai import OpenAI

# =========================
# CONFIG
# =========================
client = OpenAI(api_key="Key_chatgpt")

# =========================
# CARREGA CSV
# =========================
try:
    df = pd.read_csv('Data.csv', dtype=str)  # força tudo como string
except FileNotFoundError:
    print("Erro: arquivo Data.csv não encontrado.")
    exit()

# =========================
# NORMALIZA COLUNAS
# =========================
df.columns = df.columns.str.strip().str.lower()

# =========================
# GARANTE UM ID
# =========================
if 'id' not in df.columns:
    print("Coluna 'id' não encontrada. Gerando IDs automaticamente...")

    def gerar_id(row):
        base = ''.join([str(v).strip() for v in row.values])
        return hashlib.md5(base.encode()).hexdigest()

    df['id'] = df.apply(gerar_id, axis=1)

# limpa espaços do id
df['id'] = df['id'].astype(str).str.strip()

# DEBUG (IMPORTANTE)
print("\nIDs disponíveis no CSV:")
print(df['id'].head(10).tolist())

# =========================
# ENTRADA DO USUÁRIO
# =========================
entrada = input("\nDigite os IDs separados por vírgula: ")

users_ids = [i.strip() for i in entrada.split(',')]

# DEBUG
print("\nIDs digitados:")
print(users_ids)

# =========================
# FILTRO
# =========================
users = df[df['id'].isin(users_ids)]

if users.empty:
    print("\n❌ Nenhum usuário encontrado.")
    print("Verifique se os IDs existem e estão no formato correto.")
    exit()

# =========================
# CONVERTE PARA DICT
# =========================
resultado = users.to_dict(orient='records')

print("\nUsuários encontrados:")
print(json.dumps(resultado, indent=2, ensure_ascii=False))

# =========================
# FUNÇÃO IA
# =========================
def generate_ai_news(user, max_retries=3):
    for attempt in range(max_retries):
        try:
            print(f"Gerando notícia para: {user.get('name')} (tentativa {attempt+1})")

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "Você é um especialista em marketing bancário."},
                    {"role": "user", "content": f"Crie uma notícia para {user.get('name')} (máx 100 caracteres)"}
                ]
            )

            news = response.choices[0].message.content.strip()[:100]
            return news

        except Exception as e:
            print(f"[ERRO] tentativa {attempt+1}: {e}")

            if attempt == max_retries - 1:
                print("[FALHA FINAL] seguindo sem IA...")
                return f"{user.get('name')}: novidades de investimento disponíveis."

            time.sleep(2)
