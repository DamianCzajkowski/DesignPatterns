from abc import ABC, abstractmethod


class AbstractImage(ABC):
    def __init__(self, filepath):
        self.filepath = filepath
    
    @abstractmethod
    def load_image(self):
        pass

    @abstractmethod
    def display_image(self):
        pass


class Image(AbstractImage):
    def load_image(self):
        print("Image loaded")
    
    def display_image(self):
        print("Image displayed")

class anotherImage(Image):
    pass
class ProxyImage(AbstractImage):
    def __init__(self, image):
        super().__init__(image.filepath)
        self.image_loaded = False
        self.image = image

    def load_image(self):
        self.image.load_image()
    
    def display_image(self):
        if not self.image_loaded:
            self.load_image()
        self.image.display_image()

if __name__ == "__main__":
    print(issubclass(anotherImage, AbstractImage))