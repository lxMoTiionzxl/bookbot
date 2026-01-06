from stats import get_num_words, get_letters_count, sort_dict_value
import sys

def get_book_text (book_path):
    """
    Input: book path, str
    Output: book content, str
    """

    with open(book_path) as f:
        book_content = f.read()
    return book_content


def main ():

    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        book = get_book_text(book_path)
        num_words = get_num_words(book)
        letters_count = get_letters_count(book)
        letters_sorted = sort_dict_value(letters_count)

        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {book_path}...')
        print('----------- Word Count ----------')
        print('Found',num_words, 'total words')
        print('--------- Character Count -------')
        for dic in letters_sorted:
            if dic['char'].isalpha():
                print(f'{dic['char']}: {dic['num']}')
    else:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

main()