# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824813.910934
_enable_loop = True
_template_filename = 'themes/carpet/templates/crumbs.tmpl'
_template_uri = 'crumbs.tmpl'
_source_encoding = 'utf-8'
_exports = ['bar']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bar(context,crumbs):
    __M_caller = context.caller_stack._push_frame()
    try:
        loop = __M_loop = runtime.LoopStack()
        index_file = context.get('index_file', UNDEFINED)
        carpet__breadcrumb_separator = context.get('carpet__breadcrumb_separator', UNDEFINED)
        carpet__breadcrumb_home = context.get('carpet__breadcrumb_home', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if crumbs:
            __M_writer('  <nav class="level breadcrumbs">\n    <div class="breadcrumb level-left">\n')
            loop = __M_loop._enter(crumbs)
            try:
                for link, text in loop:
                    if text != index_file:
                        if loop.first:
                            __M_writer('            <div class="level-item icon-group home">\n')
                            if carpet__breadcrumb_home:
                                __M_writer('                <span class="icon is-small">\n                  <i class="fa ')
                                __M_writer(filters.html_escape(str(carpet__breadcrumb_home)))
                                __M_writer('"\n                    aria-hidden="true"></i>\n                </span>\n')
                        else:
                            __M_writer('            <div class="level-item icon-group separator">\n')
                            if carpet__breadcrumb_separator:
                                __M_writer('                <span class="icon is-small">\n                  <i class="fa ')
                                __M_writer(filters.html_escape(str(carpet__breadcrumb_separator)))
                                __M_writer('"\n                    aria-hidden="true"></i>\n                </span>\n')
                        if link == '#':
                            __M_writer('            <span>')
                            __M_writer(str(text.rsplit('.html', 1)[0]))
                            __M_writer('</span>\n')
                        else:
                            __M_writer('            <a href="')
                            __M_writer(str(link))
                            __M_writer('">')
                            __M_writer(str(text))
                            __M_writer('</a>\n')
                        __M_writer('          </div>\n')
            finally:
                loop = __M_loop._exit()
            __M_writer('    </div>\n  </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "crumbs.tmpl", "line_map": {"64": 29, "65": 31, "68": 34, "74": 68, "16": 0, "21": 2, "22": 37, "28": 3, "36": 3, "37": 4, "38": 5, "39": 7, "42": 8, "43": 9, "44": 10, "45": 11, "46": 12, "47": 13, "48": 13, "49": 17, "50": 18, "51": 19, "52": 20, "53": 21, "54": 21, "55": 26, "56": 27, "57": 27, "58": 27, "59": 28, "60": 29, "61": 29, "62": 29, "63": 29}, "filename": "themes/carpet/templates/crumbs.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
