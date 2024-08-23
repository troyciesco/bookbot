def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        words = contents.split()

        chars = {}
        lowered = contents.lower()
        for c in lowered:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1

        list = []
        for c in chars:
            if c.isalpha():
                list.append({"char": c, "count": chars[c]})

        def sort_on(dict):
            return dict["count"]

        list.sort(reverse=True, key=sort_on)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} found in the document\n")
        for l in list:
            print(f"The '{l["char"]}' character was found {l['count']} times")
        print('--- End report ---')


main()
