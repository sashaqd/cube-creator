import pandas as pd

def delete_columns_from_csv(file_path, columns_to_delete):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Drop the columns by index
    df.drop(df.columns[columns_to_delete], axis=1, inplace=True)
    
    # Save the modified DataFrame back to a CSV file
    df.to_csv(file_path, index=False)
    print("Columns deleted and file saved.")

# Example usage:
file_path = 'file_generator/datasets/Aircrafts Movement By Emirate/AircraftsMovementByEmirate2014-2017.csv'  # Update this to your CSV file path
columns_to_delete = [5]  # List of column indices to delete (e.g., delete first and third columns)
delete_columns_from_csv(file_path, columns_to_delete)
