from openai import OpenAI
import openai

def get_car_ai_bio(model, brand, year):
    prompt = ''''
    Me mostra uma descrção de venda para o carro {} {} {} em apenas 200 caracteres. Fale coisa especifica 
    do carro.
    '''
    openai.api_key = ''
    client = OpenAI(
        organization = '',
    )
    prompt = prompt.format(brand, model, year)
    response = client.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
    )
    return response['choices'][0]['text']