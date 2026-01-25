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


    
    