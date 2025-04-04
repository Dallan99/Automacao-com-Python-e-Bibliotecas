from transformers import AutoModelForCausalLM, AutoTokenizer

# Definir o modelo em português
model_name = "pierreguillou/gpt2-small-portuguese"

# Carregar o tokenizer e o modelo
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Texto de entrada
input_text = "Era uma vez um aventureiro chamado João que"

# Tokenizar o texto
input_ids = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=50)

# Gerar texto
output = model.generate(
    input_ids,
    max_length=150,
    temperature=0.8,
    top_p=0.9,
    num_beams=5,  # Beam Search ativado
    num_return_sequences=3,  # Agora pode gerar 3 textos diferentes
    pad_token_id=tokenizer.eos_token_id
)
# Decodificar e exibir resultado
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
