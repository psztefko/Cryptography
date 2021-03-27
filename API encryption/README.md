Ćwiczenie 4: FastAPI

Zapoznaj się z biblioteką Cryptography powtarzając przykłady z wykładu (szyfrowanie symetryczne, generowanie klucza publicznego i prywatnego, serializacja kluczy, itp.)

Stwórz prosty serwis z API za pomocą https://fastapi.tiangolo.com/ z endpointami:

a) symetric:

GET symetric/key -> zwraca losowo wygenerowany klucz symetryczny w postaci HEXów (może być JSON)

POST symetric/key -> ustawia na serwerze klucz symetryczny podany w postaci HEX w request

POST symetric/encode -> wysyłamy wiadomość, w wyniku dostajemy ją zaszyfrowaną

POST symetric/decode -> wysyłamy wiadomość, w wyniku dostajemy ją odszyfrowaną

b) asymetric:

GET asymetric/key -> zwraca nowy klucz publiczny i prywatny w postaci HEX (w JSON jako dict) i ustawia go na serwerze

GET asymetric/key/ssh -> zwraca klucz publiczny i prywatny w postaci HEX zapisany w formacie OpenSSH

POST asymetric/key -> ustawia na serwerze klucz publiczny i prywatny w postaci HEX (w JSON jako dict)

POST asymetric/verify -> korzystając z aktualnie ustawionego klucza prywatnego, podpisuje wiadomość i zwracaą ją podpisaną

POST asymetric/sign -> korzystając z aktualnie ustawionego klucza publicznego, weryfikuję czy wiadomość była zaszyfrowana przy jego użyciu

POST asymetric/encode -> wysyłamy wiadomość, w wyniku dostajemy ją zaszyfrowaną

POST asymetric/decode -> wysyłamy wiadomość, w wyniku dostajemy ją odszyfrowaną

Zadbaj o:

Przejrzystość
Docstringi
Jakość kodu i modularność
Obsługę błędów (np. ktoś poda złą wartość dla klucza, to należy zwrócić informacje user-friendly o wyjątku)
Zweryfikuj jakość dokumentacji (generuje się automatycznie jak dobrze zrobisz docstringi)
Dla chętnych:

Dodaj testy jednostkowe do projektu
Użyj jinja2 i zrób prosty Frontend do tego.