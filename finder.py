import pandas as pd

def find_in_csv(a, search_term):
    try:
        a = input("Enter CSV file path:")
        data = pd.read_csv(a)
        
        results = data[data.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
        
        if not results.empty:
            print(f"Found {len(results)} matching rows:")
            print(results)
        else:
            print(f"No matches found for '{search_term}'.")
    except Exception as e:
        print(f"Error: {e}")

file_path = input("Enter CSV file path: ")
search_term = input("Enter search term: ")
find_in_csv(file_path, search_term)
#write the path of your file twice and write the name which you want to search
