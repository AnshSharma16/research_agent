import google.generativeai as genai

genai.configure(api_key="AIzaSyAA0YNMWXi0aarPTkNP1bwTUWIhg0DnA4s")

for model in genai.list_models():
    print(model.name)