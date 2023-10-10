from torchvision import transforms
from PIL import Image

Img_path=("Pics/pic1.png")
img=Image.open (Img_path)

tensor_trans=transforms.ToTensor()
tensor_img=tensor_trans(img)\

print(tensor_img)
