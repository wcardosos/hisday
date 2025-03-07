import torch
from transformers import pipeline

def fetch_historical_event(date: str):
    pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16,
                    device_map="auto")

    # We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
    messages = [
        {
            "role": "system",
            "content": "Você é um professor acadêmico de história com doutorado",
        },
        {"role": "user", "content": f"Me dê um evento histórico que tenha acontecido na data de {date}. O texto deve estar em Português Brasil"},
    ]
    prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)

    return outputs[0]["generated_text"]