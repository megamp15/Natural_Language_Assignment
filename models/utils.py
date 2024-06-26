import os

def save_response(model_name, hyperparams, response):
    os.makedirs('logs', exist_ok=True)
    with open(f'../logs/{model_name}_log.txt', 'a',encoding='utf-8') as f:
        hyphen_line = '-'*50
        log_entry = (
        f"{hyphen_line}\n"
        f"Model Name: {model_name}\n"
        f"Hyperparameters: {hyperparams}\n"
        f"Response:\n {response}\n"
        f"{hyphen_line}\n\n\n"
        )
        f.write(log_entry)