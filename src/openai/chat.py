from src.utils.config import client


def chat(system, user_assistant, language):
    assert isinstance(system, str), "`system` should be a string"
    assert isinstance(user_assistant, list), "`user_assistant` should be a list"
    system_msg = [{"role": "system", "content": f"{system} Respond in language: {language}."}]
    user_assistant_msgs = [
        {"role": "assistant", "content": user_assistant[i]} if i % 2 else {"role": "user", "content": user_assistant[i]}
        for i in range(len(user_assistant))]

    msgs = system_msg + user_assistant_msgs
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=msgs)
    status_code = response.choices[0].finish_reason
    assert status_code == "stop", f"The status code was {status_code}."
    return response.choices[0].message.content