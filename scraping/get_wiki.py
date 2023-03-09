
import openai
openai.api_key = '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'

prompt = "Get me the bio of Marie Curie"
model_engine = "text-davinci-002"
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

print(response.choices[0].text)