import wx
from PIL import Image


class WatermarkApp(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title="Watermark")

        self.panel = wx.Panel(self)
        self.max_img_size = 600

        # Image Widget - for viewing images
        img = wx.Image(600, 375)
        img_control_flags = wx.ID_ANY | wx.FD_FILE_MUST_EXIST
        self.img_control = wx.StaticBitmap(
            self.panel, img_control_flags,
            wx.Bitmap(img)
        )

        # Browse Image Button
        self.browse_button = wx.Button(self.panel, label="Browse Images")
        self.browse_button.Bind(wx.EVT_BUTTON, self.browse_images)

        # Add Watermark Button
        self.add_watermark_button = wx.Button(self.panel, label="Add Watermark")
        self.add_watermark_button.Bind(wx.EVT_BUTTON, self.add_watermark)

        # Save as New Image Button
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
        open_wildcard = "JPEG files (*.jpg)|*.jpg|" \
                        "PNG files (*.png)|*.png"

        with wx.FileDialog(
                self, "Select a file to watermark",
                wildcard=open_wildcard, style=wx.FD_OPEN
        ) as open_dialog:
            if open_dialog.ShowModal() == wx.ID_OK:
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
        self.panel.Refresh()

    def add_watermark(self, *args):
        """
        Uses Python Image Library (PIL / pillow) to place a watermark on a user
        selected image.
        """
        try:
            if self.path.endswith(".png"):
                img = Image.open(self.path).convert("RGBA")
            else:
                img = Image.open(self.path).convert("RGB")

            self.copied_img = img.copy()  # .convert("RGBA")

            # For PNG images, setting mask to white (regarding background
            # transparency)
            self.logo = Image.open("sm_logo.png").convert("RGBA")
            logo_size = (20, 20)
            self.logo.resize(logo_size)

            watermark_position = (self.copied_img.size[0] - 100,
                                  self.copied_img.size[1] - 130)
            self.copied_img.paste(self.logo, watermark_position, self.logo)

            self.watermarked_img = self._pil_to_wx(self.copied_img)

        except AttributeError:
            message = "You need to open an image before then watermark " \
                      "feature can be used"
            styles = wx.OK | wx.ICON_ERROR
            no_image_selected = wx.MessageBox(
                message=message, caption="Warning",
                style=styles
            )
        else:
            self.view_image(self.watermarked_img)
            self.panel.Refresh()

    def save_watermarked_image(self, *args):
        """
        After image has been watermarked, user can save image to a selected
        directory
        """
        try:
            save_wildcard = "All files (*.*)|*.*"
            style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT

            # image = self._wx_to_pil(self.watermarked_img)
            image = self.copied_img

            with wx.FileDialog(
                    self, "Save image:", ".", "", wildcard=save_wildcard,
                    style=style
            ) as save_dialog:
                if save_dialog.ShowModal() == wx.ID_OK:
                    filename = save_dialog.GetFilename()
                    # directory_name = save_dialog.GetDirectory()
                    image.save(filename)
                else:
                    return
        except AttributeError:
            message = "You need to open an image before you can save an image"
            styles = wx.OK | wx.ICON_ERROR
            no_image_selected = wx.MessageBox(
                message=message, caption="Warning", style=styles
            )
        except ValueError:
            message = "Incorrect File Extension. Please make sure you enter " \
                      "the correct file extension."
            styles = wx.OK | wx.ICON_ERROR
            no_image_selected = wx.MessageBox(
                message=message, caption="Warning", style=styles
            )

    def _pil_to_wx(self, image):
        """Helper method. Convert PIL Image() into wx.Bitmap()."""
        width, height = image.size
        return wx.Bitmap.FromBuffer(width, height, image.tobytes())


if __name__ == "__main__":
    app = wx.App()
    frame = WatermarkApp()
    app.MainLoop()
