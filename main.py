from PyPDF2 import PdfReader
import pandas as pd
import re

pdf_path = './_OceanofPDF.com_The_Way_of_Kings_-_Brandon_Sanderson.pdf'

# Create an empty DataFrame to store all mentions
all_mentions_df = pd.DataFrame(columns=['page', 'Spren'])

reader = PdfReader(pdf_path)
number_of_pages = len(reader.pages)

for page_num in range(number_of_pages):
    page = reader.pages[page_num]
    text = page.extract_text()
    search_pattern = r'\w*spren'

    # Find all matches using re.findall()
    matches = re.findall(search_pattern, text)

    # Create a Pandas DataFrame from the matches on this page
    page_df = pd.DataFrame({'page': [page_num + 1] * len(matches), 'Spren': matches})

    # Concatenate the DataFrame for this page to the all_mentions_df
    all_mentions_df = pd.concat([all_mentions_df, page_df], ignore_index=True)

# Group by 'Spren' and aggregate 'page' into a list
grouped_df = all_mentions_df.groupby('Spren')['page'].agg(list).reset_index()

# Add a column 'Count' to count the number of times each 'Spren' appears
grouped_df['Count'] = grouped_df['page'].transform(len)

# Print the DataFrame with all mentions, their corresponding pages, and the count
print(grouped_df)
