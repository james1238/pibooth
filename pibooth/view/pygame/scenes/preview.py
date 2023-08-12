# -*- coding: utf-8 -*-

from pibooth.view.pygame.sprites import BasePygameScene, ImageSprite, CapturesCounterSprite


class PreviewScene(BasePygameScene):

    def __init__(self):
        super().__init__()
        self.left_image = ImageSprite(self, 'capture_left.png')
        self.right_image = ImageSprite(self, 'capture_right.png')
        self.captures_counter = CapturesCounterSprite(self, 4)

    def resize(self, size):
        # Hide status bar
        self.status_bar.hide()

        # Preview capture
        self.image.set_rect(0, -200,
                            self.rect.width, self.rect.height)

        # Left image
        height = self.rect.height // 4
        size = (height, height)
        self.left_image.set_rect(10, self.rect.bottom - size[1], size[0] * 1.5, size[1])

        # Right image
        self.right_image.set_rect(self.rect.right - size[0] - 10, self.rect.bottom - size[1], size[0], size[1])

        # Dots
        self.captures_counter.set_rect(self.rect.width // 6, self.rect.bottom - self.rect.height // 8 + 10,
                                       self.rect.width * 2 // 3, self.rect.height // 8 - 10)

    def set_capture_number(self, current, total):
        self.captures_counter.set_status(current, total)
