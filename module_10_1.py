import threading
import time

def write_words(word_count, file_name):
    """Тело функции для записи в файл и его создания."""
    file_new = f"{file_name}.txt"
    with open(file_new, 'w', encoding='utf-8') as file:
        for w in range(word_count+1):
            file.write(f'Какое-то слово № {w}\n')
            time.sleep(0.1)
    return print(f"Завершилась запись в файл {file_new}")

start_time = time.time()
# Запуск потоков
write_in_file = write_words(10, 'example1')
write_in_file = write_words(30, "example2")
write_in_file = write_words(200, "example3")
write_in_file = write_words(100, "example4")

end_time = time.time()
# Форматирование и захват времени выполнения потоков
execution_time = end_time - start_time
formatted_time = f"{execution_time:02.6f}"
print(f"Работа потоков: {formatted_time}")

start_time2 = time.time()
# Создание потоков
thread1 = threading.Thread(target=write_words, args=(10, "example5" ))
thread2 = threading.Thread(target=write_words, args=(30, "example6" ))
thread3 = threading.Thread(target=write_words, args=(200, "example7" ))
thread4 = threading.Thread(target=write_words, args=(100, "example8" ))
# Запуск потоков
thread1.start()
thread2.start()
thread3.start()
thread4.start()
# Остановка потоков
thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time2 = time.time()
# Форматирование и захват разницы времени выполнения потоков
execution_time2 = end_time2 - start_time2
formatted_time2 = f"{execution_time2:02.6f}"
print(f"Работа потоков: {formatted_time2} ")
