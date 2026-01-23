import pandas as pd

def main():
    data_path = "./data"
    target_name = input("What is the part you're looking for? ")
    
    dataset = pd.read_csv(f"{data_path}/parts.csv")
    results = 0
    
    for index, row in dataset.iterrows():
        if target_name in row["part_name"]:
            print(row["part_number"])
            results += 1
        
    if results == 0:
        print("No results found..")
    else:
        print(f"Found {results} Results.")
        
        
    
    
    
if __name__ == "__main__":
    main()



