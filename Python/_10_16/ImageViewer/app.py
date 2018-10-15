import tkinter
import time
from _10_16.ImageViewer.gui import ViewWindow


def loop(mod='free', t=3):
    if mod == 'free':
        x.create_buttons()
        root.mainloop()
    else:
        while True:
            root.update()
            x.next_image()
            time.sleep(t)
            if not x.imageLeft:
                return


if __name__ == '__main__':
    root = tkinter.Tk(className="Image Viewer")
    root.wm_minsize(width=1280, height=720)
    x = ViewWindow(root)
    x.pack(expand="yes", fill="both")
    x.next_image()
    loop()
