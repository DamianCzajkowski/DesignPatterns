from .image import Image, ProxyImage


my_image = Image("C:\\image.img")
my_image = ProxyImage(my_image)
my_image.display_image()
