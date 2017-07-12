# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824719.7885537
_enable_loop = True
_template_filename = 'themes/carpet/templates/listing.tmpl'
_template_uri = 'listing.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        def content():
            return render_content(context)
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\n\n')
        if folders or files:
            __M_writer('<ul>\n\n')
            for name in folders:
                __M_writer('  <li><a href="')
                __M_writer(filters.url_escape(str(name)))
                __M_writer('"><i class="icon-folder-open"></i> ')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a>\n')
            __M_writer('\n')
            for name in files:
                __M_writer('  <li><a href="')
                __M_writer(filters.url_escape(str(name)))
                __M_writer('.html"><i class="icon-file"></i> ')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a>\n')
            __M_writer('\n</ul>\n')
        __M_writer('\n')
        if code:
            __M_writer('  <h1 class="title is-1">')
            __M_writer(str(title))
            __M_writer('</h1>\n')
            if source_link:
                __M_writer('    <p class="subtitle is-2">\n      <a href="')
                __M_writer(str(source_link))
                __M_writer('">(')
                __M_writer(str(messages("Source")))
                __M_writer(')</a>\n    </p>\n')
            __M_writer('  <div class="content">\n    ')
            __M_writer(str(code))
            __M_writer('\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"74": 4, "75": 5, "76": 5, "77": 7, "78": 8, "79": 10, "80": 11, "81": 11, "82": 11, "83": 11, "84": 11, "85": 13, "86": 14, "87": 15, "88": 15, "89": 15, "90": 15, "91": 15, "92": 17, "29": 0, "94": 21, "95": 22, "96": 22, "97": 22, "98": 23, "99": 24, "100": 25, "101": 25, "102": 25, "93": 20, "104": 28, "105": 29, "106": 29, "103": 25, "46": 2, "47": 3, "112": 106, "52": 32, "23": 3, "58": 4}, "filename": "themes/carpet/templates/listing.tmpl", "uri": "listing.tmpl"}
__M_END_METADATA
"""
