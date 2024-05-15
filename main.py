# main.py
import yaml
from mymodule import greet, add, subtract

def load_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

if __name__ == "__main__":
    config = load_config('config.yaml')
    user_name = config.get('user', 'Guest')

    print(greet(user_name))

    a = 10
    b = 5
    print(f"The sum of {a} and {b} is {add(a, b)}.")
    print(f"The difference between {a} and {b} is {subtract(a, b)}.")
