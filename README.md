# hisday

Projeto criado para a mentoria de Python na ZRP buscando mostrar como adicionar IA em uma aplicação Python. A aplicação consiste em uma API REST feita em FastAPI que retorna dados históricos de uma determinada data fornecida pelo usuário.

## Como utilizar

Com a sua venv já criada, instale as dependências do projeto com:

```sh
pip install -r requirement.txt
```

### OpenAI API
Para utilizar a OpenAI é necessário ter uma conta na plataforma da OpenAI, créditos válidos na plataforma e uma API key. Para utilizar a API key é necessário que a variável ambiente esteja disponível. Para isso você pode rodar o comando abaixo:

```sh
export OPENAI_API_KEY=sua_api_key
```

### Deepseek
Para utilizar o DeepSeek é necessário ter instalado o [Ollama](https://ollama.com). No nosso exemplo estamos utilizando o modelo `deepseek-r1:7b` que pode ser baixado para sua máquina com o seguinte comando

```sh
ollama run deepseek-r1:7b
```

Com o Deepseek baixado, podemos rodar o servidor do Ollama:

```sh
ollama serve
```

### Hugging Face
Para utilizar modelos presentes no [Hugging Face](https://huggingface.co) precisamos apenas ter as libs `transformers` e `torch` instaladas no nosso projeto.

## Como rodar
Com a venv criada e as dependências instaladas, basta rodar o comando abaixo:

```sh
fastapi dev main.py
```
