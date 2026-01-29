import pandas as pd

def retrieve_data():
    return pd.read_csv("./data/parts.csv")

def filter_parts(df, query_params):
    filtered = df.copy()

    if query_params["part_number"]:
        filtered = filtered[filtered["part_number"].str.contains(query_params["part_number"], case=False, na=False)]
    if query_params["part_name"]:
        filtered = filtered[filtered["part_name"].str.contains(query_params["part_name"], case=False, na=False)]
    if query_params["part_brand"]:
        filtered = filtered[filtered["brand"].str.contains(query_params["part_brand"], case=False, na=False)]
    if query_params["compat_model"]:
        filtered = filtered[filtered["compatible_model"].str.contains(query_params["compat_model"], case=False, na=False)]
    if query_params["manu_year"]:
        year = int(query_params["manu_year"])
        filtered = filtered[(filtered["year_start"] <= year) & (filtered["year_end"] >= year)]

    return filtered.sort_values("price")

def basic_results(query_params):
    raw = retrieve_data()
    filtered_data = filter_parts(raw, query_params)
    
    if filtered_data.empty:
        return "No results."
    else:
        return filtered_data.to_string(index=False, header=False)