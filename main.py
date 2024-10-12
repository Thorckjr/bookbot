def get_word_count(str):
    return len(str.split())

def get_unique_letter_count(str):
    ltr_result = set()
    dict_result = {}
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for l in str:
        if l in alpha:
            ltr_result.add(l)

    for l2 in ltr_result:
        l2_cnt = str.count(l2)
        dict_result.update({ l2: l2_cnt })
    
    return dict_result

    

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        dict = get_unique_letter_count(file_contents.lower());
        print("--- Begin report of books/frankenstein.txt ---")
        
        wrd_count = get_word_count(file_contents)
        print(f"{wrd_count} words found in the document")
        print("")
        
        for kv in dict:
            print(f"The'{kv}' character was found '{dict[kv]}' times.")
        print("--- End report ---")

main()