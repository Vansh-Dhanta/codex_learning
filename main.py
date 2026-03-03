from calc import calculate_sum
from openai import OpenAI


def query_groq_model(system_message: str, user_message: str) -> str:
    # Replace this with your real Groq API key.
    groq_api = "your_groq_api_key_here"

    client = OpenAI(
        api_key=groq_api,
        base_url="https://api.groq.com/openai/v1",
    )

    response = client.responses.create(
        model="llama-3.3-70b-versatile",
        input=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
    )

    return response.output_text


if __name__ == "__main__":
    system = "You are a helpful assistant."
    user = "Explain recursion in one short paragraph."

    result = query_groq_model(system, user)
    print(result)

    total = calculate_sum(10, 20)
    print(f"Sum from calc.py: {total}")
