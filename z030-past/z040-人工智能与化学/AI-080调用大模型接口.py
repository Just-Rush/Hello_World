from openai import OpenAI

client = OpenAI(
    api_key="sk-e1zbmGbnIkoH2FCIsekNZwb55Pt64PIOBHTxlLqonb8Y1oq9",  # 在这里将 MOONSHOT_API_KEY 替换为你从 Kimi 开放平台申请的 API Key
    base_url="https://api.moonshot.cn/v1",
)

messages = [
    {"role": "system",
     "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
]


def chat(input: str) -> str:
    """
    chat 函数支持多轮对话，每次调用 chat 函数与 Kimi 大模型对话时，Kimi 大模型都会”看到“此前已经
    产生的历史对话消息，换句话说，Kimi 大模型拥有了记忆。
    """

    messages.append({
        "role": "user",
        "content": input,
    })

    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=messages,
        temperature=0.3,
    )

    assistant_message = completion.choices[0].message

    messages.append(assistant_message)

    return assistant_message.content

print(chat("你好，我是一名计算化学方向的在读研究生。"))
print(chat("你可以为我拟定一个学习或共工作计划吗？"))
print(chat("比如我现在正在学习如何使用python代码来与大模型进行交互，你能给我什么意见吗"))