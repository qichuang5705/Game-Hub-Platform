import os

a = "avatar\\ccc.pt"
aa, image_extension = os.path.splitext(a)

print(aa)
print(image_extension)