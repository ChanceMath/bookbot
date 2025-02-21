def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    # Get character counts
    char_counts = count_characters(text)
    
    # Generate the sorted report
    chars_list = get_char_report(char_counts)
    
    # Print the report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()  # Empty line for spacing
    
    # Loop through each character's data to print it
    for char_data in chars_list:
        char = char_data["char"]
        count = char_data["count"]
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_characters(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def get_char_report(chars_dict):
    chars_list = []
    for char, count in chars_dict.items():
        char_data = {"char": char, "count": count}
        chars_list.append(char_data)

    def sort_on(char_data):
        return char_data["count"]
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
main()

