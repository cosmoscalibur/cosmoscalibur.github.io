# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824593.6451187
_enable_loop = True
_template_filename = 'themes/carpet/templates/list_post.tmpl'
_template_uri = 'list_post.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('archive_nav', context._clean_inheritance_tokens(), templateuri='archive_navigation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'archive_nav')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        archive_nav = _mako_get_namespace(context, 'archive_nav')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        def content():
            return render_content(context)
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        archive_nav = _mako_get_namespace(context, 'archive_nav')
        __M_writer = context.writer()
        __M_writer('\n<article class="listpage">\n  <header class="heading">\n    <h1 class="title is-1">')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n  </header>\n  ')
        __M_writer(str(archive_nav.archive_navigation()))
        __M_writer('\n')
        if posts:
            __M_writer('    <div class="postlist">\n')
            for post in posts:
                __M_writer('        <div class="columns">\n          <div class="column is-2">\n            <time class="listdate" datetime="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('" title="')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('</time>\n          </div>\n          <div class="column">\n            <a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('</a>\n          </div>\n        </div>\n')
            __M_writer('    </div>\n')
        else:
            __M_writer('  <p>')
            __M_writer(str(messages("No posts found.")))
            __M_writer('</p>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"68": 5, "69": 8, "70": 8, "71": 10, "72": 10, "73": 11, "74": 12, "75": 13, "76": 14, "77": 16, "78": 16, "79": 16, "80": 16, "81": 16, "82": 16, "83": 19, "84": 19, "85": 19, "86": 19, "23": 3, "88": 24, "89": 25, "90": 25, "91": 25, "92": 27, "29": 0, "98": 92, "43": 2, "44": 3, "49": 28, "55": 5, "87": 23}, "filename": "themes/carpet/templates/list_post.tmpl", "uri": "list_post.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
