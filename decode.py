from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import sys
import time
import os

def read_file(i):
    try:
        file_in = open(i, 'rb')
        ciphered_data = file_in.read() # Read the rest of the data
        file_in.close()
        return ciphered_data
    except IOError:
        print("文件读取失败")
        sys.exit(0)

def decrypt_file(key,iv,ciphered_data):
    print("少女祈祷中...")
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # Setup cipher
        original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
        return original_data
    except:
        print("decrypt error")
        sys.exit(0)

def save_file(data,path,name,ext):
    try:
        fw = open(path+"\\"+name+"_decrypted."+ext,'w',encoding='utf8')
        fw.write(data)
        fw.close()
    except:
        print("save error")
        sys.exit(0)
    

while True:
    in_file = input("请将要解密的文件拖进来：") # Input file
    if in_file=="":
        print("未选择文件...")
        time.sleep(1)
        continue

    key = input("请输入key：").encode('utf-8')
    iv = input("请输入iv：").encode('utf-8')
    if key==b"" or iv==b"":
        print("未输入key和iv，将使用默认值")
        key = 'ds3KXwLJXS6pNKdhgh7cWnnDHCduy58K'.encode('utf-8')
        iv = "bHe28cVw22ey1KXz".encode('utf-8')
        # iv = file_in.read(16)
        break
    else:
        break

path = in_file.rsplit("\\",1)[0]
name = in_file.rsplit("\\",1)[1].split(".")[0]
ext = in_file.rsplit("\\",1)[1].split(".")[1]

f = read_file(in_file)
o = decrypt_file(key,iv,f)
save_file(o.decode('utf-8'),path,name,ext)

print("done")