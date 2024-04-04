import yaml

def load_config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config()
    rail_choice = input("What rail do you wish to use? Agent Assist or Customer Assist? ").lower()
    
    if rail_choice == "agent":
        print("All following queries will be submitted to the Agent Assist Rails.")
        # Simulate sending queries to Agent Assist Rails based on config
        model = config['rails']['agent_assist']['model']
        print(f"Using model: {model}")
    elif rail_choice == "customer":
        print("All following queries will be submitted to the Customer Assist Rails.")
        # Simulate sending queries to Customer Assist Rails based on config
        model = config['rails']['customer_assist']['model']
        print(f"Using model: {model}")
    else:
        print("Invalid choice. Please start over.")

if __name__ == "__main__":
    main()


