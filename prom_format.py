import mistune

class PromFormat(mistune.HTMLRenderer):
    def __init__(self):
        super().__init__()

    def heading(self, text, level, **attrs):
        return f"\n{'#' * level} {text.upper()}\n"

    def emphasis(self, text, **attrs):
        return f"*{text}*"

    def strong(self, text, **attrs):
        return f"**{text}**"

    def block_code(self, code, lang=None, **attrs):
        return f"\n```{lang or ''}\n{code}\n```\n"

    def link(self, link, text=None, title=None):
        return ""

    def image(self, src, alt="", title=None):
        return ""

    def paragraph(self, text, **attrs):
        return f"\n{text}\n"

    def parse(self, content):
        parser = mistune.create_markdown(renderer=self)
        return parser(content)

def load_prom_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    return PromFormat().parse(content)
