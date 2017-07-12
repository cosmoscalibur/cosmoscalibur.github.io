# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824173.0059383
_enable_loop = True
_template_filename = 'themes/carpet/templates/pagination_helper.tmpl'
_template_uri = 'pagination_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['page_navigation']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_navigation(context,current_page,page_links,prevlink,nextlink,prev_next_links_reversed,surrounding=5):
    __M_caller = context.caller_stack._push_frame()
    try:
        abs = context.get('abs', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<nav class="pagination is-centered">\n  <ul class="pagination-list page-navigation">\n')
        for i, link in enumerate(page_links):
            if abs(i - current_page) <= surrounding or i == 0 or i == len(page_links) - 1:
                if i == current_page:
                    __M_writer('          <li><a class="pagination-link is-current current-page">')
                    __M_writer(str(i+1))
                    __M_writer('</a></li>\n')
                else:
                    __M_writer('          <li><a class="pagination-link" href="')
                    __M_writer(str(page_links[i]))
                    __M_writer('">')
                    __M_writer(str(i+1))
                    __M_writer('</a></li>\n')
            elif i == current_page - surrounding - 1 or i == current_page + surrounding + 1:
                __M_writer('        <li><span class="pagination-ellipsis ellipsis">&hellip;</span></li>\n')
        __M_writer('  </ul>\n</nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/carpet/templates/pagination_helper.tmpl", "source_encoding": "utf-8", "uri": "pagination_helper.tmpl", "line_map": {"48": 13, "34": 2, "35": 5, "36": 6, "37": 7, "38": 8, "39": 8, "40": 8, "41": 9, "42": 10, "43": 10, "44": 10, "45": 10, "46": 10, "47": 12, "16": 0, "49": 16, "21": 18, "55": 49, "27": 2}}
__M_END_METADATA
"""
