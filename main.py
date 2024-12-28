def main():
  book_path = "books/frankenstein.txt"  
  text = get_text(book_path)
  word_count = count_words(text)
  chars = count_char(text)
  chars_list = [{"key":key, "value":value} for key, value in chars.items()]

  print(f"{word_count} words found in the document")
  chars_list.sort(reverse=True, key=return_num)
  for dict in chars_list:
    if dict["key"].isalpha():
      print(f"The '{dict["key"]}' character was found {dict["value"]} times")


def get_text(path):
  with open(path) as f:
    return f.read()
   
def count_words(text):
  words = text.split()
  return len(words)

def count_char(text):
  lower_text = text.lower()
  characters = {}
  for char in lower_text:
    if char in characters:
      characters[char] += 1
    else:
      characters[char] = 1
  return characters

def return_num(dict):
  return dict["value"]

main()