import re

class URL:

    def __init__(self, url, template_dir):
        split_url = url.split('/')
        view_kwargs = {}
        for string in split_url:
            if string.startswith('!') and string.endswith('!'):
                kwarg = re.search('[(.*)]', string).group(1)
                view_kwargs.update({kwarg : ''})
                view(view_kwargs, template_dir)

