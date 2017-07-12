from __future__ import unicode_literals
from mezzanine import template
from bs4 import BeautifulSoup
from PIL import Image
import requests

register = template.Library()


@register.filter
def to_amp_html(html):
    """
    Markdown HTML to AMP HTML
    """
    soup = BeautifulSoup(html)
    for elem in soup.find_all(True, id=lambda x: x and 'amp' in x):
        elem["id"] = elem.get("id").replace("amp", "accelerated-mobile-pages")

    for img in soup.find_all('img'):
        amp_img = soup.new_tag("amp-img")
        for attr in img.attrs:
            if "style" != attr:
                amp_img[attr] = img[attr]
        src = str(img.get("src"))
        if src.startswith("//"):
            src = src.replace("//", "https://")
        im = Image.open(requests.get(src, stream=True).raw)
        amp_img["width"] = im.size[0]
        amp_img["height"] = im.size[1]
        amp_img["layout"] = "responsive"
        img.replace_with(amp_img)
    soup.body.hidden = True
    return str(soup.body)
