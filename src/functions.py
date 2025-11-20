def form_message(user, new_message):
    return [
        {"role": msg.author, "content": msg.content} for msg in user.message_history
    ] + [{"role": "user", "content": new_message}]
