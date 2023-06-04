# Варіант 4

У ході роботи були імплементовані криптосистема Рабіна та алгоритм ElGamal. Для перевірки алгоритмів можна запустити файли rabin.py і elgamal.py відповідно.

У ході виконання обох завдань були імплементовані методи encrypt(...) та decrypt(...), які відповідно зашифровують та розшифровують певне задане повідомлення.

Криптосистема Рабіна використовує високу складність факторизації чисел. На етапі генерації ключій ми беремо два великих простих числа p та q, що задовольняються певні додаткові умови і рахуємо n = p * q. n - публічний ключ, p та q - приватні. Процес шифрування є простим і полягає у знаходженні c = m^2 mod n, а ось зворотній процес полягає у знаходженні повідомлення m на основі c, p та q. У файлі rabin.py описано окремі деталі того, як це реалізовано. Також цю інформацію можна знайти тут: https://en.wikipedia.org/wiki/Rabin_cryptosystem

Алгоритм ElGamal складається з генерації ключів, алгоритм шифрування та розшифрування. Під час його роботи генерується пара приватного та публічного ключа; зашифрований текст розповсюджується разом з публічним ключем. У файлі elgamal.py можна побачити коментарії щодо того, як працюють окремі фрагменти цього алгоритму. Також цю інформацію можна знайти тут: https://en.wikipedia.org/wiki/ElGamal_encryption
