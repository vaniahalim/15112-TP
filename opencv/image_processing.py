# scoring of your drink vs customer's desired drink
from PIL import Image, ImageChops

img1 = Image.open('../images/latte1.png')
# img1.show()

img2 = Image.open('../images/latte2.png')
diff = ImageChops.difference(img1,img2)


diff.show()

