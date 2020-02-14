
import sys, os, cv2, json
import numpy as np

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, \
    QApplication, QWidget, \
    QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QLabel, QCheckBox, QDesktopWidget, QSpacerItem, QSizePolicy, \
    QFileDialog


#from validate_matches import fix_bounds
from mtcnn import MTCNN

from Visualization import Visualization as view



class JanelaPrincipal(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        '''
        Construtor
        '''

        self.initUI()



    def initUI(self):
        '''
        configurar os elementos da janela principal
        '''
        self.resize(1200, 700)
        self.setWindowTitle('Face Detection')
        self.add_Widgets()
        self.center()
        self.show()



    def add_Widgets(self):

        # painel com a imagem
        self.lb_image = QLabel('Face Detection')
        self.lb_image.setAlignment(Qt.AlignHCenter)

        self.view_image = view()

        self.bt_open_image = QPushButton('Open Image')

        # painel com as opções
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.lb_image)
        self.main_layout.addWidget(self.view_image)
        self.main_layout.addItem(QSpacerItem(5, 10, QSizePolicy.Minimum, QSizePolicy.Minimum))
        self.main_layout.addWidget(self.bt_open_image)

        self.bt_open_image.clicked.connect(self.select_path_image)


        self.main_panel = QWidget()
        self.main_panel.setLayout(self.main_layout)
        self.setCentralWidget(self.main_panel)

        print('-' * 30)
        print('Loading model')
        self.model = MTCNN()


    def select_path_image(self):

        self.path_image = self.open_image()
        print('PATH image:', self.path_image)

        # load image
        image = cv2.imread(self.path_image)

        # detectar a face com o modelo

        faces = self.model.detect_faces(image)

        self.view_image.plot_face_image(image, faces)

        # print('results > ', faces)
        #
        # for face in faces:
        #     x, y, width, height = face['box']
        #
        #     cv2.rectangle(image, (x, y), (width, height),
        #               (0, 0, 255), 1)
        #
        # self.view_image.plot_image(image)
        # print('-'*50)


    def open_image(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        nome, _ = QFileDialog.getOpenFileName(self, "Open Image", "/home/nigom/Imagens/",
                                              "Image files (*.jpg *.png *.jpeg)", options=options)

        if nome:
            print('Read image : ', nome)

        return nome


    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()))




class App:

    def __init__(self):
        print('-' * 30)
        print(' init application')
        print('-' * 30)

    def start(self):

        app = QApplication(sys.argv)
        ex = JanelaPrincipal()
        sys.exit(app.exec_())


if __name__ == '__main__':
    ##########
    # App.py #
    ##########
    app = App()
    app.start()