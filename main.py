import pandas as pd

def main():
    data_path = "./data"
    target_name = input("What is the part you're looking for? ")
    
    dataset = pd.read_csv(f"{data_path}/parts.csv")
    results = 0
    
    matches = dataset[dataset["part_name"].str.contains(target_name, case=False, na=False)]
    
    if matches.empty:
        print("No results found..")
    else:
        print(matches["part_number"].to_string(index=False))
        print(f"Found {len(matches)} Results.")
    
    exactMatches = matches["part_name"].str.lower()
    print(matches[["part_name", "part_number"]].to_string(index=False))
        
        
    
    
    
if __name__ == "__main__":
    main()



