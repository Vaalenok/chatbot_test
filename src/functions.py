import tiktoken
from src.config import MODEL_NAME


def form_message(user, new_message):
    return [
        {"role": msg.author, "content": msg.content} for msg in user.message_history
    ] + [{"role": "user", "content": new_message}]


def count_tokens(messages: list[dict]) -> int:
    encoding = tiktoken.encoding_for_model(MODEL_NAME)
    num_tokens = len(encoding.encode("".join([msg["content"] for msg in messages])))
    return num_tokens
