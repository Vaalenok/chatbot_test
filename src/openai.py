from openai import OpenAI
from src.config import OPENAI_API_KEY, MODEL_NAME, MAX_TOKENS
import tiktoken

client = OpenAI(api_key=OPENAI_API_KEY)


def get_response(messages: list[dict]) -> tuple[str, int]:
    sliced = 0

    while count_tokens(messages) > MAX_TOKENS:
        messages = messages[2:]
        sliced += 1

    response = client.responses.create(model=MODEL_NAME, input=messages)

    return response.output_text, sliced


def count_tokens(messages: list[dict]) -> int:
    encoding = tiktoken.encoding_for_model(MODEL_NAME)
    num_tokens = len(encoding.encode("".join([msg["content"] for msg in messages])))
    return num_tokens
