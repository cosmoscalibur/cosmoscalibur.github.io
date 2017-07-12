# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824593.6295028
_enable_loop = True
_template_filename = 'themes/carpet/templates/tag.tmpl'
_template_uri = 'tag.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head']


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
        title = context.get('title', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        date_format = context.get('date_format', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        description = context.get('description', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        len = context.get('len', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context)
        date_format = context.get('date_format', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        description = context.get('description', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
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


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        parent = context.get('parent', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"line_map": {"128": 55, "129": 55, "130": 55, "131": 55, "132": 58, "133": 58, "134": 58, "135": 58, "136": 62, "137": 64, "143": 4, "178": 11, "27": 0, "157": 4, "158": 5, "159": 5, "160": 6, "161": 7, "162": 8, "163": 8, "164": 8, "165": 8, "166": 8, "167": 8, "168": 8, "169": 8, "170": 8, "171": 10, "172": 11, "173": 11, "174": 11, "175": 11, "176": 11, "177": 11, "50": 2, "55": 13, "184": 178, "60": 65, "66": 15, "85": 15, "86": 18, "87": 18, "88": 19, "89": 20, "90": 20, "91": 20, "92": 22, "93": 23, "94": 23, "95": 23, "96": 25, "97": 26, "98": 26, "99": 26, "100": 26, "101": 26, "102": 28, "103": 30, "104": 32, "105": 33, "106": 34, "107": 36, "108": 36, "109": 36, "110": 36, "111": 36, "112": 36, "113": 36, "114": 36, "115": 40, "116": 41, "117": 43, "118": 43, "119": 43, "120": 43, "121": 47, "122": 50, "123": 51, "124": 52, "125": 53, "126": 55, "127": 55}, "filename": "themes/carpet/templates/tag.tmpl", "uri": "tag.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
