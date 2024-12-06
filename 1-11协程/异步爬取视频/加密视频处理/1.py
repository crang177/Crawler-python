import requests
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

# res=requests.get("https://play.xluuss.com/play/Le3LZNRa/index.m3u8",headers=headers)
# res.encoding=res.apparent_encoding
# print(res.text)

##EXT-X-KEY:METHOD=AES-128,URI="enc.key",IV=0x00000000000000000000000000000000
# res=requests.get("https://play.xluuss.com/play/Le3LZNRa/enc.key",headers=headers)
# res.encoding=res.apparent_encoding
# print(res.text)




decryptor = Cipher(algorithms.AES("kA78eb8E7yneTnmr"), modes.CBC(b'0x00000000000000000000000000000000'), backend=default_backend()).decryptor()
decrypted_data = decryptor.update() + decryptor.finalize()