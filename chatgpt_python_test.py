import openai
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--prompt", type=str, default="cake")
args = parser.parse_args()

def chat(prompt):
    suffix = "The end of the story."
    response = openai.Completion.create(
        model="davinci:ft-personal-2023-04-25-09-12-07",
        prompt=prompt,
        max_tokens = 10,
        n = 1,
        stop = None,
        temperature = 0.3)#     response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "user", "content":prompt}
#     ]

# )
    # answer = response.choices[0].message.content
    answer = response.choices[0].text
    return answer
# 设置API密钥

def image_genaration(prompt):
    response = openai.Image.create(
    prompt=prompt,
    n=2,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

if __name__=='__main__':
    prompt=args.prompt
    result = image_genaration(prompt)
    # result = chat(prompt)

    print(result)
    # openai.Model.delete("ada")
