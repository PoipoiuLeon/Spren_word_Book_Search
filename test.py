from ebooklib import epub

# Define the path to your EPUB file
epub_path = 'El_camino_de_los_reyes_Brandon_Sanderson.epub'

# Read the EPUB file
book = epub.read_epub(epub_path)

# Specify the chapter number you want to access (e.g., Chapter 10)
target_chapter_number = 0

# Find and open the specified chapter
target_chapter = None

# Iterate through the items in the EPUB book
for item in book.items:
    if isinstance(item, epub.EpubHtml):
        # This is an HTML item (likely a chapter)
        # Check if the filename contains the chapter number
        if f"chapter{target_chapter_number}" in item.file_name.lower():
            target_chapter = item
            break  # Stop iterating after finding the target chapter

# Check if the target chapter was found
if target_chapter:
    # Access the content of the target chapter
    chapter_content = target_chapter.content.decode('utf-8')  # Convert bytes to a string

    # Print or process the content as needed
    print(chapter_content)
else:
    print(f"Chapter {target_chapter_number} not found in the EPUB.")
