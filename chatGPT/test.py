
import os
import openai
openai.organization = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()




# import openai

# openai.api_key = "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" # API Key


# completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "라운드 숄더를 교정하기 가장 좋은 운동은?"}]
# )

# print(completion)