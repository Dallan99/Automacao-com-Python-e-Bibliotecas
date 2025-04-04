from transformers import pipeline

# Carregar pipeline de perguntas e respostas com um modelo atualizado
qa_pipeline = pipeline("question-answering", model="pierreguillou/bert-base-cased-squad-v1.1-portuguese")

# Definir contexto e pergunta
contexto = "O Brasil é o maior país da América do Sul e tem uma população de mais de 200 milhões de habitantes."
pergunta = "Qual é a população do Brasil?"

# Obter resposta
resposta = qa_pipeline(question=pergunta, context=contexto)

# Exibir resposta
print("Resposta:", resposta["answer"])
