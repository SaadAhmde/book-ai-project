from openai import OpenAI

# Constants
system_prompt = """
You are a helpful book research assistant. Provide accurate book information.

For each book, provide:
- Book Title
- Author Name
- Publication Date
- Author's Country of Origin and city
- Summary
- Key Themes
- Genre

Format your response as a clean structured like a page heading is Book information and then give all information about books.
If you cannot find the information, say so clearly.
"""

def get_book_details(book_name):
    client = OpenAI()  

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Give me full details for this book: {book_name}"}
    ]

    response = client.chat.completions.create(
        model="gpt-5.4-mini",  
        messages=messages,
    )

    result = response.choices[0].message.content
    return result  


book_name = input("Enter a book name: ")
details = get_book_details(book_name)
print(details)