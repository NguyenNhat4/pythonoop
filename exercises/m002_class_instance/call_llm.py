from google import genai
from dotenv import load_dotenv
import os
load_dotenv

client = genai.Client(api_key="AIzaSyDbMWa2VOLfeI0Q3fnAWaQa9mR-YYpSRgQ")

def call_llm(prompt):

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    return response.text


def build_prompt(text):
    return f"""
    
    phân loại các sản phẩm trong List sau: 
    {text}
    này thành một danh sách tương ứng , thuộc các loại như sau:
    - VEGETABLES
    - FRUITS
    - GRAINS_LEGUMES
    - DAIRY_EGGS
    - MEAT_SEAFOOD
    Example:
    ```yaml
    types: [MEAT_SEAFOOD,MEAT_SEAFOODVEGETABLES,GRAINS_LEGUMES,GRAINS_LEGUMES ]
    ```
    
    
    trả về chinh xac câu trúc YML như trên:
    """
import yaml  
prompt = ""
with open('./orderitems.txt','r') as f:
    prompt = f.readlines()
prompt = build_prompt(prompt)



yaml_str = call_llm(prompt).split("```yaml")[1].split("```")[0].strip()

with open('result.txt','w') as f:
    f.write(yaml_str)