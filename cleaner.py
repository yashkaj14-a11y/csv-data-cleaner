import pandas as pd

def clean_csv_data(input_file):
    """
    Cleans a CSV file by removing duplicate rows, 
    handling missing values, and exporting a clean copy.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Remove duplicate rows
        df = df.drop_duplicates()
        
        # Fill missing values with 'N/A'
        df = df.fillna('N/A')
        
        # Save to a new clean file
        output_file = "cleaned_output.csv"
        df.to_csv(output_file, index=False)
        print(f"Data cleaned successfully! Saved as {output_file}")
        
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    # Example function call (you can pass any csv file name here)
    print("CSV Data Automation Tool is ready.")
