from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectLabel import DirectLabel
from panda3d.core import TextNode

class PlayerHUD():
    def __init__(self):
        #
        # Player status section
        #
        heartscale = (0.1, 1, 0.1)
        self.heart1 = OnscreenImage(
            image = "HeartIcon.png",
            scale = heartscale,
            pos = (0.2, 0, -0.15))
        self.heart1.setTransparency(True)
        self.heart1.reparentTo(base.a2dTopLeft)
        self.heart2 = OnscreenImage(
            image = "HeartIcon.png",
            scale = heartscale,
            pos = (0.45, 0, -0.15))
        self.heart2.setTransparency(True)
        self.heart2.reparentTo(base.a2dTopLeft)
        self.heart3 = OnscreenImage(
            image = "HeartIcon.png",
            scale = heartscale,
            pos = (0.7, 0, -0.15))
        self.heart3.setTransparency(True)
        self.heart3.reparentTo(base.a2dTopLeft)

        self.keys = DirectLabel(
            text = "x0",
            frameColor = (0, 0, 0, 0),
            text_fg = (1, 1, 1, 1),
            text_scale = 1.8,
            text_pos = (1, -0.25, 0),
            text_align = TextNode.ALeft,
            image = "Keys.png",
            pos = (0.2, 0, -0.4))
        self.keys.setScale(0.085)
        self.keys.setTransparency(True)
        self.keys.reparentTo(base.a2dTopLeft)

        self.actionKey = DirectLabel(
            frameColor = (0, 0, 0, 0),
            text_fg = (1, 1, 1, 1),
            scale = 0.15,
            pos = (0, 0, 0.15),
            text = _("Action: E/Enter"))
        self.actionKey.setTransparency(True)
        self.actionKey.reparentTo(base.a2dBottomCenter)
        self.actionKey.hide()

    def show(self):
        self.keys.show()

    def hide(self):
        self.heart1.hide()
        self.heart2.hide()
        self.heart3.hide()
        self.keys.hide()
        self.hideActionKey()

    def setHealthStatus(self, value):
        """this function will set the health image in the top righthand corner
        according to the given value, where value is a integer between 0 and 100
        """
        if value >= 1: self.heart1.show()
        else: self.heart1.hide()
        if value >= 2: self.heart2.show()
        else: self.heart2.hide()
        if value >= 3: self.heart3.show()
        else: self.heart3.hide()

    def showActionKey(self):
        self.actionKey.show()

    def hideActionKey(self):
        self.actionKey.hide()

    def updateKeyCount(self, numKeys):
        self.keys["text"] = "x%d" % numKeys
