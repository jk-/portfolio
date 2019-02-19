from flask_assets import Bundle, Environment, Filter
from flask import Flask


class ConcatFilter(Filter):
    def concat(self, out, hunks, **kw):
        out.write(';'.join([h.data() for h, info in hunks]))

scss_material = Bundle(
    '../assets/sass/materialize/main.scss',
    filters=('libsass', 'cssmin'),
    output='css/materialize.css'
)

scss_main = Bundle(
    '../assets/sass/index.scss',
    '../assets/sass/main.scss',
    filters=('libsass', 'cssmin'),
    output='css/main.css'
)

js = Bundle(
    '../assets/js/materialize.js',
    '../assets/js/blazy.js',
    filters=(ConcatFilter, 'jsmin'),
    output='js/packed.js'
)

assets = Environment()
assets.register('scss_material', scss_material)
assets.register('scss_main', scss_main)
assets.register('js_all', js)
