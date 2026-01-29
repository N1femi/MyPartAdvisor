import time
from advisor import basic_results

def main():
    gathering_info = True
    
    query_params: dict[str, str | None] = {
        "part_number": "Part Number?", 
        "part_name": "Part Name?",
        "part_brand": "Part Brand?",
        "compat_model": "Compatible Model?",
        "manu_year": "Manafactuar Year?"
    }
    
    print("Welcome to MyPartAdvisor \n")
    print(f"Skip unknown info or quit program ('quit') \n{'-' * 100} \n")
    
    for key in query_params:
        currentInput = input(f"{'-'*5}\n{query_params[key]} Enter: ") # Consistent Input Request
        currentInput = currentInput.strip()
        
        if currentInput == "":
            currentInput = None
            
        query_params[key] = currentInput
    
    initial_results = basic_results(query_params)
    
    print(initial_results)
    
    affirmed_advancement = input("\n Would you like to further filter? (Yes / No): ")
    
    if affirmed_advancement.lower().strip() == 'yes':
        print("No")
    
    
    
    
if __name__ == "__main__":
    main()

