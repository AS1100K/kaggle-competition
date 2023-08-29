def pd_to_csv(data, file_path):
    with open(file_path, "w") as f:
        f.write(data.to_csv())

    return 'DONE'

def transform_csv(df, save_path):
    import json

    with open("object_mapping.json", "r") as f:
        obj_mapping = json.loads(f.read())

    # Replacing
    for column, mapping in obj_mapping.items():
        df[column].replace(mapping, inplace=True)
    
    # Replacing all empty values with 0
    df.fillna(0, inplace=True)

    # Save the data
    with open(save_path, "w") as f:
        f.write(df.to_csv())
