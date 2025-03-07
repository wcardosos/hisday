from openai import OpenAI


client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="xxx"
)

def fetch_historical_event(date: str):
    completion = client.chat.completions.create(
        model="deepseek-r1:7b",
        messages=[
            {"role": "system", "content": "Você é um professor acadêmico de história com doutorado"},
            {
                "role": "user",
                "content": f"Me dê um evento histórico que tenha acontecido na data de {date}"
            }
        ]
    )

    return completion.choices[0].message.content