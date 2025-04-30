def query_llm(query, df):
    prompt = f"Dados: {df.head()} \nPergunta: {query}"
    return prompt


def initial_prompt(df):
    prompt = f"""
    Estes são os dados das primeiras linhas do meu CSV:
    {df}

    Com base nisso, me diga os principais padrões que você consegue identificar.
  """
    return prompt
