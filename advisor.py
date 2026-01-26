import pandas as pd
import time

# // VARIABLES \\ #
default_params = {"part_number": "", "part_name": "", "manu_year": "", "part_brand": "Honda", "compat_car": ""}

# // FUNCTIONS \\ #
def retrieve_data():
    return pd.read_csv("./data/parts.csv")

def initiate_search() -> dict:
    part_number = input("Part Number? ")
    part_name = input("Part Name? ")
    manu_year = input("Year Manufactured? ")
    part_brand = input("Brand? ")
    compat_car = input("Compatible Car? ")
    
    
    return {
        "part_number": part_number,
        "part_name": part_name,
        "manu_year": manu_year,
        "part_brand": part_brand,
        "compat_car": compat_car
    }

def process_query(query_params= default_params):
    data = retrieve_data()
    print("Processing work: 99/100")
    
    time.sleep(1)
    
    print("Processing work: WE SHALL EAT TODAY")
    
    time.sleep(1)
    
    print(data.to_string())
    
process_query()