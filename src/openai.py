from openai import OpenAI
from src.config import OPENAI_API_KEY, MODEL_NAME, MAX_TOKENS
from src.functions import count_tokens


client = OpenAI(api_key=OPENAI_API_KEY)


def get_response(messages: list[dict]) -> tuple[str, int]:
    sliced = 0

    while count_tokens(messages) > MAX_TOKENS:
        messages = messages[2:]
        sliced += 1

    response = client.responses.create(model=MODEL_NAME, input=messages)

    return response.output_text, sliced
