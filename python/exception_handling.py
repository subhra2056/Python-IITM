

try:
    f = open(r"C:\Users\Encry\Desktop\My files\PDSA-IITM\python\test_file.txt", "r")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally...")