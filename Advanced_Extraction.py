import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

# Define the key to extract
key_to_extract = "Occupation"

# Construct the regular expression pattern
pattern = r"\b" + key_to_extract + r":\s*([^;]+)"

# Search for the value corresponding to the key
match = re.search(pattern, text)

if match:
    occupation = match.group(1).strip()
    print(f"The {key_to_extract} is: {occupation}")
else:
    print(f"No information found for the key '{key_to_extract}'")
