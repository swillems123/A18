def write_anime_tuples_to_py():
    input_file_path = r"C:\A18\toprankedanime.csv"
    output_file_path = r"C:\A18\output.py"
    
    with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
        outfile.write("anime_tuples = [\n")
        
        for line in infile:
            line = line.strip()
            if not line:
                continue
            
            # Split the line by commas, but handle the lists properly
            fields = []
            current_field = ""
            inside_quotes = False
            
            for char in line:
                if char == ',' and not inside_quotes:
                    fields.append(current_field)
                    current_field = ""
                else:
                    if char == '"':
                        inside_quotes = not inside_quotes
                    current_field += char
            
            fields.append(current_field)  # Add the last field
            
            if len(fields) > 11:  # Ensure there are enough fields
                name = fields[0].strip("[]'\"")
                genre = fields[11].strip('[]"')  # Only remove brackets and double quotes, keep single quotes
                outfile.write(f"    ('{name}', {genre}),\n")
        
        outfile.write("]\n")

# Call the function to execute the script
write_anime_tuples_to_py()