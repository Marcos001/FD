

from mtcnn.mtcnn import MTCNN
import cv2

from Visualization import  highlight_faces

path_root = '/home/nigom/Imagens/Webcam/'
imagem = '2020-02-14-084947.jpg'

image = cv2.imread(path_root+imagem)

detector = MTCNN()

faces = detector.detect_faces(image)

print(faces)

highlight_faces(path_root+imagem, faces)



# plt.axis('off')
# plt.grid(False)
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.show()