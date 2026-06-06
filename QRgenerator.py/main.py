import qrcode

url = input("Enter the URL of the image: ")
file_name = input("Enter the name of the file to save it as: ")

if not (file_name.endswith(".png") ):
    file_name = file_name + ".png"
else:
    file_name = file_name + ".png"

img = qrcode.make(url)
img.save(file_name)