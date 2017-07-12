# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824719.8754404
_enable_loop = True
_template_filename = 'themes/carpet/templates/tag.tmpl'
_template_uri = 'tag.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        sorted = context.get('sorted', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        subcategories = context.get('subcategories', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        posts = context.get('posts', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        description = context.get('description', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        title = context.get('title', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        sorted = context.get('sorted', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        generate_rss = context.get('generate_rss', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if len(translations) > 1 and generate_rss:
            for language in sorted(translations):
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS for ')
                __M_writer(str(kind))
                __M_writer(' ')
                __M_writer(filters.html_escape(str(tag)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')" href="')
                __M_writer(str(_link(kind + "_rss", tag, language)))
                __M_writer('">\n')
        elif generate_rss:
            __M_writer('        <link rel="alternate" type="application/rss+xml" title="RSS for ')
            __M_writer(str(kind))
            __M_writer(' ')
            __M_writer(filters.html_escape(str(tag)))
            __M_writer('" href="')
            __M_writer(str(_link(kind + "_rss", tag)))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        sorted = context.get('sorted', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context)
        _link = context.get('_link', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        description = context.get('description', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        title = context.get('title', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="tagpage">\n  <header class="heading">\n    <h1 class="title is-1">')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n')
        if description:
            __M_writer('    <p>')
            __M_writer(str(description))
            __M_writer('</p>\n')
        if subcategories:
            __M_writer('    ')
            __M_writer(str(messages('Subcategories:')))
            __M_writer('\n    <ul>\n')
            for name, link in subcategories:
                __M_writer('      <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
        __M_writer('    <div class="metadata level">\n      <div class="level-left">\n')
        if len(translations) > 1 and generate_rss:
            for language in sorted(translations):
                __M_writer('          <div class="level-item">\n            <p class="feedlink">\n              <a href="')
                __M_writer(str(_link(kind + "_rss", tag, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="application/rss+xml">')
                __M_writer(str(messages('RSS feed', language)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')</a>&nbsp;\n            </p>\n          </div>\n')
        elif generate_rss:
            __M_writer('          <div class="level-item">\n            <p class="feedlink">\n              <a href="')
            __M_writer(str(_link(kind + "_rss", tag)))
            __M_writer('" type="application/rss+xml">')
            __M_writer(str(messages('RSS feed')))
            __M_writer('</a>\n            </p>\n          </div>\n')
        __M_writer('      </div>\n    </div>\n  </header>\n')
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
                __M_writer('<a>\n          </div>\n        </div>\n')
            __M_writer('    </div>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 18, "129": 19, "130": 20, "131": 20, "132": 20, "133": 22, "134": 23, "135": 23, "136": 23, "137": 25, "138": 26, "139": 26, "140": 26, "141": 26, "142": 26, "143": 28, "144": 30, "145": 32, "146": 33, "147": 34, "148": 36, "149": 36, "150": 36, "151": 36, "152": 36, "153": 36, "154": 36, "27": 0, "156": 40, "157": 41, "158": 43, "159": 43, "160": 43, "161": 43, "162": 47, "155": 36, "164": 51, "163": 50, "166": 53, "167": 55, "168": 55, "169": 55, "170": 55, "171": 55, "172": 55, "173": 58, "174": 58, "175": 58, "176": 58, "177": 62, "50": 2, "55": 13, "184": 178, "60": 65, "66": 4, "80": 4, "81": 5, "82": 5, "83": 6, "84": 7, "85": 8, "86": 8, "87": 8, "88": 8, "89": 8, "90": 8, "91": 8, "92": 8, "93": 8, "94": 10, "95": 11, "96": 11, "97": 11, "98": 11, "99": 11, "100": 11, "101": 11, "165": 52, "178": 64, "107": 15, "126": 15, "127": 18}, "filename": "themes/carpet/templates/tag.tmpl", "uri": "tag.tmpl"}
__M_END_METADATA
"""
