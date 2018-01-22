from __future__ import unicode_literals
from mezzanine import template
from bs4 import BeautifulSoup
from PIL import Image
import six
try:
    from StringIO import StringIO
except ImportError:
    from io import BytesIO
    
import requests
import json
import logging

logger = logging.getLogger(__name__)
register = template.Library()


@register.filter
def to_amp_html(html):
    """
    Markdown HTML to AMP HTML
    """
    soup = BeautifulSoup(html, "html5lib")
    # ------------------------------------------------
    # romove style & script tags
    # ------------------------------------------------
    [s.decompose() for s in soup('style')]
    [s.decompose() for s in soup('script')]

    remove_attrs(soup, ("style","script",))
    
    # ------------------------------------------------
    # amp id replace to "accelerated-mobile-pages"
    # ------------------------------------------------
    for elem in soup.find_all(True, id=lambda x: x and 'amp' in x):
        elem["id"] = elem.get("id").replace("amp", "accelerated-mobile-pages")

    # h2
    for h2 in soup.find_all('h2'):
        h2['class'] = h2.get('class', []) + ['bold', 'mt2', 'mb2']
    # h3
    for h3 in soup.find_all('h3'):
        h3['class'] = h3.get('class', []) + ['bold', 'mt1', 'mb1']
    # h4
    for h4 in soup.find_all('h4'):
        h4['class'] = h4.get('class', []) + ['bold', 'mt1', 'mb1']
        
    # -----------------------------------------------
    # iframe replace to amp-iframe
    # -----------------------------------------------
    for iframe in soup.find_all('iframe'):
        iframe.name = "amp-iframe"

    # -----------------------------------------------
    # img replace to amp-img
    # -----------------------------------------------
    for img in soup.find_all('img'):
        try:
            amp_img = soup.new_tag("amp-img")
            for attr in img.attrs:
                if "style" != attr:
                    amp_img[attr] = img[attr]
            src = str(img.get("src"))
            if src.startswith("//"):
                src = src.replace("//", "https://")
            req = requests.get(src)
            if six.PY2:
                picture_IO = StringIO(req.content)
            else:
                picture_IO = BytesIO(req.content)
            picture_IO.seek(0)
            im = Image.open(picture_IO)
            amp_img["width"] = im.size[0]
            amp_img["height"] = im.size[1]
            amp_img["layout"] = "responsive"
            img.replace_with(amp_img)
        except IOError:
            logger.warning("something raised an exception: ", exc_info=True)
            amp_img["width"] = "4"
            amp_img["height"] = "3"
            amp_img["layout"] = "responsive"
            img.replace_with(amp_img)

    soup.body.hidden = True
    return str(soup.body)


def remove_attrs(soup, brack_list=tuple()):
    for tag in soup.findAll(True):
        for attr in [attr for attr in tag.attrs if attr in brack_list]:
            del tag[attr]
    return soup


@register.as_tag
def conv_blog_post_to_json_ld(blog=None):
    """
    Get blogpost JSON-LD
    """
    result_dict = {
        "@context": "http://schema.org",
        "@type": "BlogPosting",
        "headline": blog.title,
        "author": {"@type": "Person", "name": blog.user.first_name},
        "publisher": {"@type": "Organization",
                      "url": "https://www.monotalk.xyz",
                      "name": blog.user.first_name,
                      "logo": {"@type": "ImageObject", "url": "https://drive.google.com/uc?export=view&id=0By5O5w7iwOMOVE5pTEcyeE40WlE"}
                      },
        "image": {"@type": "ImageObject", "url": "https://drive.google.com/uc?export=view&id=0By5O5w7iwOMOMDdhaDhHdXBVTHc", "height": 450, "width": 800},
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": blog.get_absolute_url_with_host(),
        },
        "genre": ' '.join(map(lambda n: n.title, blog.categories.all())),
        "wordcount": str(len(blog.content)),
        "datePublished": str(blog.publish_date),
        "dateCreated": str(blog.created),
        "dateModified": str(blog.updated),
        "description": blog.description
    }
    json_o = json.dumps(result_dict, ensure_ascii=False)
    return json_o
