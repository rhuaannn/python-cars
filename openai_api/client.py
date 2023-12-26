import openai

def get_car_ai_bio(model, brand, year):
    prompt = ''''
    Me mostra uma descrção de venda para o carro {} {} {} em apenas 200 caracteres. Fale coisa especifica 
    do carro.
    '''
    openai.api_key = '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'
    prompt = prompt.format(brand, model, year)
    response = openai.completions.create(
        model = 'text-davinci-003',   
        prompt = '',
        max_tokens=1000,
        
    )
    return response['choices'][0]['text']