from flask_assets import Bundle, Environment, Filter
from flask import Flask

class ConcatFilter(Filter):
    def concat(self, out, hunks, **kw):
        out.write(';'.join([h.data() for h, info in hunks]))

scss_main = Bundle(
    '../assets/sass/main.scss',
    filters=('libsass', 'cssmin'),
    output='css/main.css'
)

scss_ns = Bundle(
    '../assets/sass/noscript.scss',
    filters=('libsass', 'cssmin'),
    output='css/noscript.css'
)

css = Bundle(
    '../../node_modules/font-awesome/css/font-awesome.css',
    filters=('cssmin'),
    output='css/packed.css'
)

assets = Environment()
assets.register('scss_main', scss_main)
assets.register('scss_ns', scss_ns)
assets.register('css_all', css)
