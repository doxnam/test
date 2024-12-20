import requests
import sys
import os
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# command ="python craw.py folder"
lines = {
    0: "76c257a742a17b410526",
    1: "dfe72fb5e13aa14fb21d",
    3: "61dc117c680b1b2586d3",
    4: "288261fe18a12f42f318",
    5: "43f76f0a4f992231d996",
    6: "031f738593c2a5027be8",
    7: "a7d24df06d16d7d20912",
    8: "389a07d653d00fd6a062",
    9: "35ce167fd665fc4d8c43",
    10: "3e23dd0b5ad32416517b",
    11: "062f2c6e3cbb9cfe7f54",
    12: "043df042a72aa689c97c",
    13: "1dea22425b5d90649051",
    14: "1e49b4104b577838049b",
    15: "bacd21599f1d985c5b4b",
    16: "0693299ec3f1dec71858",
    17: "9ce38ac675776f6d61ad",
    18: "d646a800b769e546bdd6",
    19: "d9030f9081e0f31c1fa8",
    20: "266c947abbdfb9285460",
    21: "075d5f2e2ed1ae764bd2",
    22: "a611fe10beef25be88a3",
    23: "a5903399d18952a2998f",
    28: "3d226e348ac55fa178fe",
    29: "cc8e6356028db273ee03",
    30: "311ef8d82b02aff2c3a1",
    31: "817ba638b727854ad606",
    32: "49f6291a60f093fb02e2",
    33: "32150ca7b37f443865d5",
    34: "50784d34a1aeb1d08605",
    35: "4b80b7a4e9e3c92b24d3",
    36: "b7f7d1c07321035d049e",
    37: "2e18bfb501819720a7a0",
    38: "d5971a8592a8ca389230",
    39: "80be8d15c3c75604b0c7",
    40: "dbac1b28b97aeb2314cc",
    41: "38132fc09ed05728a0a8",
    42: "44006e37335308743e3f",
    43: "8c2cda154220245ac0f0",
    44: "0729cb616fd5f4833e2b",
    45: "bac3e33b45f0eb8911fb",
    46: "20bc023d01e1ab6d17cc",
    47: "847c96dc16cb09a81445",
    48: "39a847170ea8338dc9af",
    49: "3f88b77a4a894fdb4a74",
    50: "c131850a5cf7aebcc50c",
    51: "b4286d5fc17729b4d688",
    52: "cebe0fa87bddb2c6f456",
    53: "94b78968c171e7e19939",
    54: "df12439354d85e029307",
    55: "a5dc19320e72a0f8d329",
    56: "7418019630bce756ef64",
    57: "f36c0cba26fd8fc68b5d",
    58: "b9ac60a28009fd475f2a",
    59: "6acf0740e76e2538e5b7",
    60: "06ad478a48a5a6a14446",
    61: "1fcf5c61ddc0509302a6",
    62: "654e250d81b026ed146d",
    63: "1b47f0159e3b93f7a60c",
    64: "7c17f161cbf7675a04f1",
    65: "bdb5380bc23f2589083d",
    66: "f9448a276b36b654199b",
    67: "789f73b1566aaa8260a8",
    68: "5d64c14e8608b288dad4",
    69: "756dc476308d2907f1ea",
    70: "0ba50fe5b92afa3b2e0b",
    71: "c6ebc76ef487f0c8043a",
    72: "7dccb0afbda48a9ac766",
    73: "31345857e2fa1535d1db",
    74: "001050cf010a637563be",
    75: "b20358f043c24f03f5b4",
    76: "a3eb3099c050245b11a0",
    77: "d93d2cc64b97a3e1a9a4",
    78: "8fb2d0143dcae0ba377b",
    79: "f5799a77d941cb12c20c",
    80: "132bd619fda683f7c206",
}


http_proxy = "http://127.0.0.1:8080"
https_proxy = "http://127.0.0.1:8080"


proxies = {
    "http": http_proxy,
    "https": https_proxy,
}

burp0_url = "https://seanet.vn/canhan/"

burp0_headers = {
    "Sec-Ch-Ua": '"Not?A_Brand";v="8", "Chromium";v="108"',
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept": "*/*",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Dest": "script",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
}

number = 0
path = sys.argv[1] + "\js"
print(path)
if not os.path.exists(path):
    os.makedirs(path)

for i in lines:
    filename = str(i) + "." + lines[i] + ".js"
    print(filename)
    response = requests.get(burp0_url + filename, headers=burp0_headers, verify=False)
    f = open(os.path.join(path, filename), "w", encoding="utf-8")
    f.write(response.text)
    f.close()
