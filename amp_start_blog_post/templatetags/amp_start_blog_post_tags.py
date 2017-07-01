from __future__ import unicode_literals
from mezzanine import template
from bs4 import BeautifulSoup

register = template.Library()


@register.filter
def to_amp_html(html):
    """
    Markdown HTML to AMP HTML
    """
    soup = BeautifulSoup(html)
    for img in soup.find_all('img'):
        amp_img = soup.new_tag("amp-img")
        for attr in img.attrs:
            amp_img[attr] = img[attr]
        amp_img["layout"] = "fixed-height"
        amp_img["height"] = "300"
        img.replace_with(amp_img)
    return str(soup)
