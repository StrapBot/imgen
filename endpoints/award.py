from io import BytesIO

from PIL import Image, ImageDraw
from flask import send_file

from utils import http
from utils.endpoint import Endpoint, setup
from utils.textutils import auto_text_size, render_text_with_emoji


@setup
class Award(Endpoint):
    params = ['avatar0', 'username0']

    def generate(self, avatars, text, usernames, kwargs):
        username = usernames[0]
        base = Image.open(self.assets.get('assets/award/award.png'))
        avatar = http.get_image(avatars[0]).resize((315, 315)).convert('RGBA')
        font = self.assets.get_font('assets/fonts/arimobold.ttf', size=60)
        base.paste(avatar, (520, 5), avatar)
        base.paste(avatar, (145, 130), avatar)
        base = base.convert('RGBA')

        canv = ImageDraw.Draw(base)
        render_text_with_emoji(base, canv, (540, 320), username, font=font, fill='White')
        render_text_with_emoji(base, canv, (175, 450), username, font=font, fill='White')

        b = BytesIO()
        base.save(b, format='png')
        b.seek(0)
        return send_file(b, mimetype='image/png')
