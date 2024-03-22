from openai import OpenAI
client = OpenAI()

system_role = """
Act like my best friend and keep your answers very brief.
"""
system_name = """
 Your name is Kevin, and you are Korean.
"""

def request_gpt_answer(prompt):
    completion = client.chat.completions.create(
      model="gpt-4-0125-preview",
      messages=[
        {"role": "system", "content": system_role+system_name},
        {"role": "user", "content": prompt}
      ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content