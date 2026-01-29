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
    
    print("Retrieving Results.")
    time.sleep(0.75)
    print("Retrieving Results..")
    time.sleep(0.75)
    print("Retrieving Results...\n")
    time.sleep(0.75)
    
    print(basic_results(query_params))
    
    
    
if __name__ == "__main__":
    main()



