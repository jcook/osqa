import markdown
from django.utils.safestring import mark_safe
from django.utils.html import strip_tags
from forum.utils.html import sanitize_html

class LimitedSyntaxExtension(markdown.extensions.Extension):
    def extendMarkdown(self, md, md_globals):
        del md.inlinePatterns["image_reference"]

def makeExtension(configs=None) :
    if configs is None: configs = {}
    return LimitedSyntaxExtension(configs=configs)
