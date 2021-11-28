from PIL import Image, ImageFont, ImageDraw
import wx


class WatermarkFrame(wx.Frame):
    """"""
    def __init__(self):
        super().__init__(parent=None, title="Watermark!")

        self.panel = wx.Panel(self)

        self.PhotoMaxSize = 600

        self.create_widgets()
        self.Show()
        # self.Maximize(True)
    
    def create_widgets(self):
        """Creates all of the widgets to be used and arranges them on the Frame."""
        instructions = "Browse for an image"
        
        img = wx.Image(600, 600)
        self.image_control = wx.StaticBitmap(self.panel, 
                                             wx.ID_ANY | wx.FD_FILE_MUST_EXIST | wx.FD_SHOW_HIDDEN, 
                                             wx.Bitmap(img))

        instructions_label = wx.StaticText(self.panel, label=instructions)
        self.photo_text = wx.TextCtrl(self.panel, size=(200, -1))
        
        browse_button = wx.Button(self.panel, label="Browse Images")
        browse_button.Bind(wx.EVT_BUTTON, self.browse_images)
        
        add_watermark_button = wx.Button(self.panel, label="Add Watermark")
        add_watermark_button.Bind(wx.EVT_BUTTON, self.add_watermark)
        
        save_image_button = wx.Button(self.panel, label="Save As New Image")
        save_image_button.Bind(wx.EVT_BUTTON, self.save_watermarked_image)

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # self.main_sizer.Add(wx.StaticLine(self.panel, wx.ID_ANY), 0,
        #                     wx.ALL | wx.EXPAND, 5)
        self.main_sizer.Add(instructions_label, 0, wx.ALL, 5)
        self.main_sizer.Add(self.image_control, 0, wx.ALL, 5)
        self.sizer.Add(self.photo_text, 0, wx.ALL, 5)
        self.sizer.Add(browse_button, 0, wx.ALL, 5)
        self.sizer.Add(add_watermark_button, 0, wx.ALL, 5)
        self.sizer.Add(save_image_button, 0, wx.ALL, 5)
        self.main_sizer.Add(self.sizer, 0, wx.ALL, 5)

        self.panel.SetSizer(self.main_sizer)
        self.main_sizer.Fit(self)

    def browse_images(self, *args):
        """"""
        wildcard = "JPEG files (*.jpg)|*.jpg|" \
                   "PNG files (*.png)|*.png|" \
                   "BMP files (*.bmp)|*.bmp"

        with wx.FileDialog(self, "Select a file to watermark",
                           wildcard=wildcard, style=wx.FD_OPEN) as open_dialog:
            if open_dialog.ShowModal() == wx.ID_OK:
                self.photo_text.SetValue(open_dialog.GetPath())
            else:
                return

        self.view_image()

    def view_image(self, img=None):
        """"""
        if img is None:
            filepath = self.photo_text.GetValue()
            img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)

        # Scale the image, preserving the aspect ratio
        width = img.GetWidth()
        height = img.GetHeight()
        if width > height:
            new_width = self.PhotoMaxSize
            new_height = int(self.PhotoMaxSize * height / width)
        else:
            new_width = self.PhotoMaxSize
            new_height = int(self.PhotoMaxSize * height / width)
        img = img.Scale(new_width, new_height)

        self.image_control.SetBitmap(wx.Bitmap(img))
        self.panel.Refresh()
    
    def add_watermark(self, *args):
        """"""
        try:
            img = Image.open(self.photo_text.GetValue())
        except AttributeError:
            error_message = "You must open an image before you can use this feature."
            styles = wx.OK | wx.CENTRE | wx.ICON_ERROR
            error_message_box = wx.MessageBox(error_message, caption="Error",
                                              style=styles)
        else:
            # if no errors occurred
            print(img.format, img.size, img.mode)

            # A copy of the above image
            self.watermarked_img = img.copy()

            draw = ImageDraw.Draw(self.watermarked_img)
            # TODO: Below works. Work on coordinate positioning, watermark,
            #                    font style/size,
            draw.text((img.size[0] - 50, img.size[1] - 50), "hello", font=None)

            # FIX THIS: Causes -> TypeError: Expected a list of bytes objects.
            self.watermarked_img = wx.Bitmap.ConvertToImage(
                wx.Bitmap(self.watermarked_img))

            self.view_image(self.watermarked_img)

            # self.image_control.SetBitmap(wx.Bitmap(self.watermarked_img))
            # self.panel.Refresh()

            # self.view_image()  # TODO: get this to work with an unsaved
            #                            watermarked image, if possible with
            #                            wxPython. If not, use .show()
            #self.watermarked_img.save("test_img.jpg")

    def save_watermarked_image(self, *args):
        """"""
        # TODO: Find a way to use wx.FileDialog() to save image after it has been watermarked
        # IDEA:
        to_save_message = "Would you like to save as a new image?"
        styles = wx.YES_NO | wx.CENTRE | wx.ICON_QUESTION
        to_save = wx.MessageDialog(self, to_save_message, caption="Save",
                                   style=styles)
        result = to_save.ShowModal()

        if result == wx.ID_YES:
            print(result)
        else:
            print(result)


if __name__ == "__main__":
    app = wx.App()
    frame = WatermarkFrame()
    app.MainLoop()
