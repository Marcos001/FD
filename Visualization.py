
import cv2

from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.patches import Rectangle


plt.style.use('seaborn')



class MyMplCanvas(FigureCanvas):
    """
     Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.).
    """

    def __init__(self, parent=None, width=8, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        self.axes.cla()
        pass


class Visualization(QWidget):

    def __init__(self,):
        super(QWidget, self).__init__()

        self.layout = QVBoxLayout()

        self.grafico_canvas = MyMplCanvas(self, width=8, height=3, dpi=100)

        self.layout.addWidget(self.grafico_canvas)
        self.setLayout(self.layout)



    def plot_image(self, array_numpy, title=None):
        self.grafico_canvas.axes.cla()
        self.grafico_canvas.axes.axis('off')
        if title:
            self.grafico_canvas.axes.set_title(title)
        self.grafico_canvas.axes.imshow(cv2.cvtColor(array_numpy, cv2.COLOR_BGR2RGB))

        self.grafico_canvas.draw()

    def plot_face_image(self, array_numpy, faces):

        self.grafico_canvas.axes.cla()
        self.grafico_canvas.axes.axis('off')
        self.grafico_canvas.axes.imshow(cv2.cvtColor(array_numpy, cv2.COLOR_BGR2RGB))

        # for each face, draw a rectangle based on coordinates
        for face in faces:
            x, y, width, height = face['box']
            face_border = Rectangle((x, y), width, height,
                                    linewidth=3,
                                    fill=False,
                                    color='red')

            self.grafico_canvas.axes.add_patch(face_border)
        self.grafico_canvas.draw()



def highlight_faces(image_path, faces):
  # display image
    image = plt.imread(image_path)
    plt.axis('off')
    plt.grid(False)
    plt.imshow(image)

    ax = plt.gca()

    # for each face, draw a rectangle based on coordinates
    for face in faces:
        x, y, width, height = face['box']
        face_border = Rectangle((x, y), width, height,
                          fill=False, color='red')
        ax.add_patch(face_border)
    plt.show()