def caesar_encrypt(plaintext, k):
    ciphertext = ""
    for char in plaintext:
        # 处理大写字母
        if 'A' <= char <= 'Z':
            ciphertext += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        # 处理小写字母
        elif 'a' <= char <= 'z':
            ciphertext += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        # 非字母字符直接保留
        else:
            ciphertext += char
    return ciphertext

# 测试：k=3，明文为"I love information security"
k = 3
plaintext = "I love information security"
ciphertext = caesar_encrypt(plaintext, k)
print(f"加密后密文：{ciphertext}")

def caesar_decrypt(ciphertext, k):
    plaintext = ""
    for char in ciphertext:
        # 处理大写字母
        if 'A' <= char <= 'Z':
            plaintext += chr((ord(char) - ord('A') - k) % 26 + ord('A'))
        # 处理小写字母
        elif 'a' <= char <= 'z':
            plaintext += chr((ord(char) - ord('a') - k) % 26 + ord('a'))
        # 非字母字符直接保留
        else:
            plaintext += char
    return plaintext

def brute_force_caesar(ciphertext):
    print("暴力破解结果（k=1到25）：")
    for k in range(1, 26):
        candidate = caesar_decrypt(ciphertext, k)
        print(f"k={k}：{candidate}")

# 测试：使用上述加密生成的密文
brute_force_caesar(ciphertext)