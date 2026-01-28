import time

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
    
    print("Done!", query_params)
        
    
    #part_number = input("\nPart Number? Enter: ")
        
        
        
        
    
    
if __name__ == "__main__":
    main()



