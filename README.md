
# qa_python

## Список реализованных тестов

1. Проверяем добавление новой книги без жанра

    def test_add_new_book_add_book_no_genre(self, collector):
    
2. Проверяем, что книга с названием длиной более 40 символов не добавляется в коллекцию

    def test_add_new_book_len_name_more_40(self, collector):
 
3. Проверяем, что книга с названием длиной 0 символов не добавляется в коллекцию

   def test_add_new_book_len_name_0(self, collector):

5. Проверяем добавление жанра книге

   def test_set_book_genre_new_add_new_genre(self, collector):
        
7. Проверяем вывод жанра книги по её имени

   def test_get_book_genre_get_genre(self, collector):
        
9. Проверяем, что метод возвращает книги с указанным жанром

   def test_get_books_with_specific_genre_get_books_with_new_genre(self, collector):
        
11. Проверяем метод вывода текущего словаря

    def test_get_books_genre_get_current_dictionaryv(self, collector):
        
13. Проверяем, что книги без возрастных ограничений - подходят детям

    def test_get_books_for_children_not_age_limit(self, collector):
        
15. Проверяем, что книги с возрастным ограничением - не подходят детям

    def test_get_books_for_children_with_age_limit(self, collector):
        
17. Проверяем, что книга добавлена в избранное

    def test_add_book_in_favorites_add_favorites_book(self, collector):
      
19. Проверяем, что книга удалена из избранного

    def test_delete_book_from_favorites_delete_favorites_book(self, collector):
      
21. Проверяем, получение списка книг, добавленных в избранное

    def test_get_list_of_favorites_books_list_books(self, collector):
        
