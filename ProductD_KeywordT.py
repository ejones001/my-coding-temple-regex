import re

descriptions = [
    "Smartphone with 6-inch screen and $300 memory",
    "Cotton t-shirt in medium size for $20.99",
    "Stainless steel kitchen knife set priced at $49"
]

# Define a function to standardize price formats
def standardize_price(description):
    # Regular expression to match price formats
    price_pattern = r'\$[\d,]+(?:\.\d{1,2})?'  # Matches $XXX.XX or $XXX,XXX.XX
    # Replace the matched price formats with 'USD XX.XX'
    standardized_description = re.sub(price_pattern, 'USD \\g<0>', description)
    return standardized_description

# Apply the standardize_price function to each description
standardized_descriptions = [standardize_price(desc) for desc in descriptions]

# Print the standardized descriptions
for i, desc in enumerate(standardized_descriptions, start=1):
    print(f"Product {i}: {desc}")
