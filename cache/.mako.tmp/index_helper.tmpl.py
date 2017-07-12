# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824719.8497474
_enable_loop = True
_template_filename = 'themes/carpet/templates/index_helper.tmpl'
_template_uri = 'index_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_pager', 'mathjax_script']


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


def render_html_pager(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        nextlink = context.get('nextlink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"64": 19, "65": 20, "66": 21, "67": 22, "68": 24, "69": 25, "70": 28, "71": 28, "72": 32, "73": 33, "74": 37, "75": 38, "76": 40, "77": 41, "78": 41, "79": 41, "16": 0, "81": 43, "21": 17, "22": 49, "87": 81, "28": 2, "80": 42, "35": 2, "36": 3, "37": 4, "38": 7, "39": 8, "40": 8, "41": 8, "42": 8, "43": 8, "44": 10, "45": 11, "46": 11, "47": 11, "48": 11, "49": 11, "50": 13, "56": 19}, "filename": "themes/carpet/templates/index_helper.tmpl", "uri": "index_helper.tmpl"}
__M_END_METADATA
"""
