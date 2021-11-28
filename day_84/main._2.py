import wx
from PIL import Image, ImageDraw


# from helpers import wx2PIL, PIL2wx


class WatermarkApp(wx.Frame):
    """"""

    def __init__(self):
        super().__init__(parent=None, title="Watermark")

        self.panel = wx.Panel(self)
        # self.create_widgets()

        self.max_img_size = 600

        # Image Widget
        img = wx.Image(600, 375)
        img_control_flags = wx.ID_ANY | wx.FD_FILE_MUST_EXIST
        self.img_control = wx.StaticBitmap(
            self.panel, img_control_flags,
            wx.Bitmap(img)
        )

        # Buttons
        self.browse_button = wx.Button(self.panel, label="Browse Images")
        self.browse_button.Bind(wx.EVT_BUTTON, self.browse_images)

        self.add_watermark_button = wx.Button(self.panel, label="Add Watermark")
        self.add_watermark_button.Bind(wx.EVT_BUTTON, self.add_watermark)

        self.save_button = wx.Button(self.panel, label="Save as New Image")
        self.save_button.Bind(wx.EVT_BUTTON, self.save_watermarked_image)

        # Sizers / Placing widgets on sizers
        self.vertical_sizer = wx.BoxSizer(wx.VERTICAL)
        self.horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.horizontal_sizer.Add(self.browse_button, 0, wx.ALL, 5)
        self.horizontal_sizer.Add(self.add_watermark_button, 0, wx.ALL, 5)
        self.horizontal_sizer.Add(self.save_button, 0, wx.ALL, 5)
        self.vertical_sizer.Add(self.horizontal_sizer, 0, wx.ALL | wx.CENTRE, 5)
        self.vertical_sizer.Add(self.img_control, 0, wx.ALL, 5)

        # Setting Main Sizer / Fitting Sizers onto Frame
        self.panel.SetSizer(self.vertical_sizer)
        self.vertical_sizer.Fit(self)

        # Showing Widgets
        self.Show()

    def browse_images(self, *args):
        """
        Opens FileDialog box, user to select image to watermark. jpg,
        png and bmp file formats only.
        """

        # Contains the file formats that the following FileDialog accepts
        wildcard = "JPEG files (*.jpg)|*.jpg|" \
                   "PNG files (*.png)|*.png|" \
                   "BMP files (*.bmp)|*.bmp"

        with wx.FileDialog(
                self, "Select a file to watermark",
                wildcard=wildcard, style=wx.FD_OPEN
        ) as open_dialog:
            if open_dialog.ShowModal() == wx.ID_OK:
                # IDEA: If going to use _wx_to_pil(), change self.path to
                #       self.watermarked_img ? or better name and use throughout
                self.path = open_dialog.GetPath()
                self.view_image(self.path)
            else:
                return

    def view_image(self, img, *args):
        """
        Called in self.browse_images(). Shows image in self.image_control.
        """
        # If Image is watermarked image or image opened from FileDialog
        if isinstance(img, wx.Bitmap):
            img = wx.Bitmap.ConvertToImage(img)
        else:
            img = wx.Image(img, wx.BITMAP_TYPE_ANY)

        # Scaling the image, preserving the aspect ratio
        width = img.GetWidth()
        height = img.GetHeight()
        if width > height:
            new_width = self.max_img_size
            new_height = int(self.max_img_size * height / width)
        else:
            new_width = self.max_img_size
            new_height = int(self.max_img_size * height / width)
        img = img.Scale(new_width, new_height)

        self.img_control.SetBitmap(wx.Bitmap(img))
        # self.panel.Refresh()
        # self.panel.Refresh()

    def add_watermark(self, *args):
        """
        Uses Python Image Library (PIL / pillow) to place a watermark on a user
        selected image.
        """
        img = Image.open(self.path).convert("RGB")

        copied_img = img.copy()

        draw = ImageDraw.Draw(copied_img)
        # TODO: If keeping text watermark, work on font type and size.
        # TODO: If not keeping text watermark, find appropriate image
        draw.text(
            (copied_img.size[0] - 100, copied_img.size[1] - 70), "hello",
            font=None
        )

        # WORKS
        self.watermarked_img = self._pil_to_wx(copied_img)

        self.view_image(self.watermarked_img)
        # self.img_control.SetBitmap(wx.Bitmap(self.watermarked_img))
        # self.panel.Refresh()
        # self.panel.Refresh()

    def _pil_to_wx(self, image):
        """Helper method. Convert PIL Image() into wx.Bitmap()."""
        width, height = image.size
        return wx.Bitmap.FromBuffer(width, height, image.tobytes())

    def _wx_to_pil(self, bitmap):
        """Helper method. Convert wx.Bitmap() to PIL Image()."""
        size = tuple(bitmap.GetSize())
        # try:
        # NOTICE: Code in function / method came in try/except with no
        #         specific Exceptions in except block
        # TODO: Test for errors. If exceptions occur, do try/except block
        #       with actual Exceptions in except block
        buf = size[0] * size[1] * 3 * "\x00"
        # POSSIBLE PROBLEM: .CopyToBuffer() may be deprecated
        bitmap.CopyToBuffer(buf)
        # except:
        del buf
        buf = bitmap.CopyToImage().GetData()
        return Image.frombuffer("RGB", size, buf, "raw", "RGB", 0, 1)

    def save_watermarked_image(self, *args):
        """
        After image has been watermarked, user can save image to a selected
        directory
        """
        pass


if __name__ == "__main__":
    app = wx.App()
    frame = WatermarkApp()
    app.MainLoop()
