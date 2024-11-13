# TODO Найдите количество книг, которое можно разместить на дискете
quantity_disc_bt = 1.44 * 1024 * 1024
count_of_book_pages = 100
count_of_str_on_page = 50
count_of_chars_in_str = 25
memory_of_one_char_bt = 4

memory_of_one_book = count_of_book_pages * count_of_str_on_page * count_of_chars_in_str * memory_of_one_char_bt
count_of_books = round((quantity_disc_bt / memory_of_one_book))

print("Количество книг, помещающихся на дискету:", count_of_books)
