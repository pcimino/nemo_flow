import yaml
import os
import random

model = None

def file_path(file_name):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   print(script_dir)
   print(file_name)
   print(os.path.join(script_dir, file_name))
   return os.path.join(script_dir, file_name)

def load_config():
    with open(file_path("config.yaml"), 'r') as file:
        return yaml.safe_load(file)

def get_user_choice():
    if model is None:
        return input("Input \"agent\" for Agent Assist, \"Customer\" for Customer Assist, \"quit\" to end program").lower()
    else:
        return input("> ")
    
def process_request(request, config):
    if request == "agent":
        print("All following queries will be submitted to the Agent Assist Rails.")
        model = config['rails']['agent_assist']['model']
    elif request == "customer":
        print("All following queries will be submitted to the Customer Assist Rails.")
        model = config['rails']['customer_assist']['model']
    
    print(f"Using model: {model}")

def get_user_choice():
    return input("What rail do you wish to use? Agent Assist or Customer Assist? Or type 'quit' to exit. ").lower()

def check_accuracy(response):
    # Placeholder for actual accuracy checking logic
    accuracy = random.uniform(0, 1)
    return accuracy

def call_model(model_name, input_data):
    """
    Simulate calling a model by name with some input data.

    Parameters:
    - model_name (str): The name of the model to call.
    - input_data (any): The input data for the model.

    Returns:
    str: A simulated response from the model.
    """
    # Placeholder for model calling logic. In a real application, this might involve:
    # - Sending an HTTP request to an API that hosts the model.
    # - Loading a machine learning model and passing the input data to it.
    print(f"Calling model '{model_name}' with input: {input_data}")
    
    # Simulated response
    return f"Response from {model_name}"

def process_request(request, config):
    if request == "agent":
        print("All following queries will be submitted to the Agent Assist Rails.")
        model = config['rails']['agent_assist']['model']
        print(f"Using model: {model}")
    elif request == "customer":
        print("All following queries will be submitted to the Customer Assist Rails.")
        model = config['rails']['customer_assist']['model']
        print(f"Using model: {model}")

    response = call_model(call_model, request)
    # Check accuracy of the response
    accuracy = check_accuracy("response")  # Simulated response
    if accuracy < 0.5:
        print("Accuracy is low. Sending request to the validate model.")
    else:
        return response

def main():
    config = load_config()
    
    while True:
        user_choice = get_user_choice()
        if user_choice == "quit":
            print("Exiting the program.")
            break
        process_request(user_choice, config)

if __name__ == "__main__":
    main()







##============================================
