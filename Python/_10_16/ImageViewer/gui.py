import tkinter
import _10_16.ImageViewer.paths as path
import _10_16.ImageViewer.imager as imager


class ViewWindow(tkinter.Canvas):
    def __init__(self, *args, **kwargs):
        tkinter.Canvas.__init__(self, *args, **kwargs)
        self.imageLeft = path.get_paths()
        self.imageRight = []
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.bg = "black"

    def show_image(self, path):
        img = imager.tk_image(path)
        self.ready = self.create_image(self.winfo_screenwidth() / 2, self.winfo_screenheight() / 2,
                                       image=img, anchor='center')
        self.image = img
        self.master.title(f'Image Viewer by MBkkt ({path})')

    def previous_image(self):
        if self.imageRight:
            try:
                img = self.imageRight.pop()
                self.show_image(img)
                self.imageLeft.append(img)
            except EOFError:
                self.previous_image()

    def next_image(self):
        if self.imageLeft:
            try:
                img = self.imageLeft.pop()
                self.show_image(img)
                self.imageRight.append(img)
            except EOFError:
                self.next_image()

    def create_buttons(self):
        tkinter.Button(self, text="<", command=self.previous_image).place(x=10, y=10)
        tkinter.Button(self, text=">", command=self.next_image).place(x=30, y=10)
