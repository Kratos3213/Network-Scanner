# -*- coding: utf-8 -*-
import os
import sys
import hashlib
import hmac
import binascii
import base64

target_host = "192.168.1.33"
target_port = 6666
target_path = "C:\\Users\\vg541\\OneDrive\\Desktop\\network scanner\\file.txt"  # Path to the file you want to scan

target_file = os.path.basename(target_path)
target_dir = os.path.dirname(target_path)
target_file_path = os.path.join(target_dir, target_file)

if not os.path.exists(target_file_path):
    print(f"File {target_file_path} does not exist.")
    sys.exit(1)

def scan_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    return data

def compute_hashes(data):
    file_hash = hashlib.sha256(data).hexdigest()
    file_hash_base64 = base64.b64encode(file_hash.encode()).decode()
    file_hash_hmac = hmac.new(b'secret_key', data, hashlib.sha256).hexdigest()
    file_hash_hmac_base64 = base64.b64encode(file_hash_hmac.encode()).decode()
    file_hash_hmac_hex = binascii.hexlify(file_hash_hmac.encode()).decode()
    return file_hash, file_hash_base64, file_hash_hmac, file_hash_hmac_base64, file_hash_hmac_hex

if __name__ == "__main__":
    file_data = scan_file(target_file_path)
    file_hash, file_hash_base64, file_hash_hmac, file_hash_hmac_base64, file_hash_hmac_hex = compute_hashes(file_data)

    print(f"File hash: {file_hash}")
    print(f"File hash base64: {file_hash_base64}")
    print(f"File hash hmac: {file_hash_hmac}")
    print(f"File hash hmac base64: {file_hash_hmac_base64}")
    print(f"File hash hmac hex: {file_hash_hmac_hex}")
