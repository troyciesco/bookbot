with open("books/frankenstein.txt") as f:
  file_contents = f.read()
  words = file_contents.split()

  char_dict = {}
  for word in words:
    lowercase_word = word.lower()
    for char in lowercase_word:
      if char in char_dict:
        char_dict[char] += 1
      else:
        char_dict[char] = 1

  def run_alpha_char_report(char_dict):
    list = []
    for char in char_dict:
      if char.isalpha():
        list.append((char, char_dict[char]))
    list.sort(reverse=True, key=lambda x: x[1])

    for item in list:
      print(f"The '{item[0]}' character was found {item[1]} times")


  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{len(words)} words found in the document")
  run_alpha_char_report(char_dict)
  print("--- End report ---")