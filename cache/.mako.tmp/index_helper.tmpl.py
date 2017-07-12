# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824814.1857655
_enable_loop = True
_template_filename = 'themes/carpet/templates/index_helper.tmpl'
_template_uri = 'index_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['mathjax_script', 'html_pager']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        katex_auto_render = context.get('katex_auto_render', UNDEFINED)
        use_katex = context.get('use_katex', UNDEFINED)
        any = context.get('any', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if any(post.is_mathjax for post in posts):
            if use_katex:
                __M_writer('    <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.js"></script>\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/contrib/auto-render.min.js"></script>\n')
                if katex_auto_render:
                    __M_writer('      <script>\n        renderMathInElement(document.body,\n          {\n            ')
                    __M_writer(str(katex_auto_render))
                    __M_writer('\n          }\n        );\n      </script>\n')
                else:
                    __M_writer('      <script>\n        renderMathInElement(document.body);\n      </script>\n')
            else:
                __M_writer('    <script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"> </script>\n    \n')
                if mathjax_config:
                    __M_writer('      ')
                    __M_writer(str(mathjax_config))
                    __M_writer('\n')
                else:
                    __M_writer('      <script type="text/x-mathjax-config">\n        MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});\n      </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        prevlink = context.get('prevlink', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if prevlink or nextlink:
            __M_writer('  <div class="columns">\n    <div class="column">\n      <nav class="pagination postindexpager pager">\n')
            if prevlink:
                __M_writer('          <a class="pagination-previous previous"href="')
                __M_writer(str(prevlink))
                __M_writer('" rel="prev">')
                __M_writer(str(messages("Newer posts")))
                __M_writer('</a>\n')
            if nextlink:
                __M_writer('          <a class="pagination-next next" href="')
                __M_writer(str(nextlink))
                __M_writer('" rel="next">')
                __M_writer(str(messages("Older posts")))
                __M_writer('</a>\n')
            __M_writer('      </nav>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index_helper.tmpl", "line_map": {"66": 2, "67": 3, "68": 4, "69": 7, "70": 8, "71": 8, "72": 8, "73": 8, "74": 8, "75": 10, "76": 11, "77": 11, "78": 11, "79": 11, "16": 0, "81": 13, "21": 17, "22": 49, "87": 81, "28": 19, "80": 11, "36": 19, "37": 20, "38": 21, "39": 22, "40": 24, "41": 25, "42": 28, "43": 28, "44": 32, "45": 33, "46": 37, "47": 38, "48": 40, "49": 41, "50": 41, "51": 41, "52": 42, "53": 43, "59": 2}, "filename": "themes/carpet/templates/index_helper.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
