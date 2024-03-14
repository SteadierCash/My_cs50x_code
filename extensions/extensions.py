a = input("File name: ")

b = a.strip().split(".")
if len(b) > 1:
    b = b[-1].lower()
else:
    b = b[0].lower()

if b in ["gif", "png"]:
    print(f"image/{b}")

elif b in ["jpg", "jpeg"]:
    print("image/jpeg")

elif b in ["pdf", "zip"]:
    print(f"application/{b}")

elif b == "txt":
    print("text/plain")

else:
    print("application/octet-stream")

