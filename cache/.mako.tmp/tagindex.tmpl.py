# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500351778.1160202
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/tagindex.tmpl'
_template_uri = 'tagindex.tmpl'
_source_encoding = 'utf-8'
_exports = ['content_header', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'index.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        subcategories = _import_ns.get('subcategories', context.get('subcategories', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        tag = _import_ns.get('tag', context.get('tag', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        subcategories = _import_ns.get('subcategories', context.get('subcategories', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def content_header():
            return render_content_header(context)
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.content_header()))
        __M_writer('\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n')
        if description:
            __M_writer('        <p>')
            __M_writer(str(description))
            __M_writer('</p>\n')
        if subcategories:
            __M_writer('        ')
            __M_writer(str(messages('Subcategories:')))
            __M_writer('\n        <ul>\n')
            for name, link in subcategories:
                __M_writer('            <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        tag = _import_ns.get('tag', context.get('tag', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(tag)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 5, "23": 3, "77": 5, "78": 6, "79": 6, "80": 8, "81": 8, "82": 9, "83": 10, "84": 10, "85": 10, "86": 12, "87": 13, "88": 13, "89": 13, "90": 15, "91": 16, "92": 16, "29": 0, "94": 16, "95": 16, "96": 18, "97": 20, "103": 23, "93": 16, "47": 2, "48": 3, "114": 23, "115": 24, "116": 24, "53": 21, "118": 25, "58": 26, "124": 118, "117": 25}, "source_encoding": "utf-8", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/tagindex.tmpl", "uri": "tagindex.tmpl"}
__M_END_METADATA
"""
