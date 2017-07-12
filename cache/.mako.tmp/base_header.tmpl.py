# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824719.776548
_enable_loop = True
_template_filename = 'themes/carpet/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_search', 'html_header', 'html_site_header', 'html_navigation_links', 'html_translation_header', 'html_site_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_search(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if search_form:
            __M_writer('  <section class="hero is-primary">\n    <div class="hero-body">\n      <div class="container">\n        <div class="content searchform" role="search">  \n          ')
            __M_writer(str(search_form))
            __M_writer('\n        </div>\n      </div>\n    </div>\n  </section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        def html_navigation_links():
            return render_html_navigation_links(context)
        def html_translation_header():
            return render_html_translation_header(context)
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        def html_site_title():
            return render_html_site_title(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="hero-head">\n  <header  id="header" class="nav">\n    <div class="container">\n')
        if logo_url or show_blog_title or len(translations) > 1:
            __M_writer('      <div class="nav-left">\n        ')
            __M_writer(str(html_site_title()))
            __M_writer('\n        ')
            __M_writer(str(html_translation_header()))
            __M_writer('\n      </div>\n')
        __M_writer('      ')
        __M_writer(str(html_navigation_links()))
        __M_writer('\n      ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n    </div>\n  </header>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if logo_url or show_blog_title:
            __M_writer('  <span class="level is-mobile">\n')
        __M_writer('\n')
        if logo_url:
            __M_writer('  <span class="level-item image is-24x24 site-image">\n    <img id="logo" class="site-logo" src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('">\n  </span>\n')
        __M_writer('\n')
        if show_blog_title:
            __M_writer('  <span id="blog-title" class="level-item site-title">')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</span>\n')
        elif logo_url:
            __M_writer('  <span id="blog-title" class="level-item site-title visuallyhidden">')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</span>\n')
        __M_writer('\n')
        if logo_url or show_blog_title:
            __M_writer('  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<!-- This "nav-toggle" hamburger menu is only visible on mobile -->\n<!-- You need JavaScript to toggle the "is-active" class on "nav-menu" -->\n<span id="nav-toggle-burger" class="nav-toggle">\n  <span></span>\n  <span></span>\n  <span></span>\n</span>\n<div id="menu" class="nav-right nav-menu">\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('    <span class="nav-item is-active">')
                __M_writer(str(text))
                __M_writer('</span>\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('        <a class="nav-item has-text-right is-active" title="')
                        __M_writer(str(text))
                        __M_writer('" href="')
                        __M_writer(str(permalink))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer(' <span class="sr-only">')
                        __M_writer(str(messages("(active)", lang)))
                        __M_writer('</span></a>\n')
                    else:
                        __M_writer('        <a class="nav-item has-text-right" title="')
                        __M_writer(str(text))
                        __M_writer('" href="')
                        __M_writer(str(suburl))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('      <a class="nav-item is-active" title="')
                    __M_writer(str(text))
                    __M_writer('" href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer(' <span class="sr-only">')
                    __M_writer(str(messages("(active)", lang)))
                    __M_writer('</span></a>\n')
                else:
                    __M_writer('      <a class="nav-item" title="')
                    __M_writer(str(text))
                    __M_writer('" href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n</div>\n<script type="text/javascript">\ndocument.getElementById(\'nav-toggle-burger\').onclick = function() {\n  var myMenu = document.getElementById(\'menu\');\n  var className = \' \' + myMenu.className + \' \';\n  var IS_ACTIVE_CLASS = \'is-active\';\n  if ( ~className.indexOf(\' \' + IS_ACTIVE_CLASS + \' \') ) {\n    myMenu.className = className.replace(\' \' + IS_ACTIVE_CLASS + \' \', \' \');\n  } else {\n    myMenu.className += \' \' + IS_ACTIVE_CLASS;\n  }\n}\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        base = _mako_get_namespace(context, 'base')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('  <div id="toptranslations" class="nav-item">\n    <h2>')
            __M_writer(str(messages("Languages:")))
            __M_writer('</h2>\n    ')
            __M_writer(str(base.html_translations()))
            __M_writer('\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        carpet__unlink_blog_brand = _import_ns.get('carpet__unlink_blog_brand', context.get('carpet__unlink_blog_brand', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        def html_site_header():
            return render_html_site_header(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="nav-item is-brand">\n  <h1 id="brand" class="site-header">\n')
        if carpet__unlink_blog_brand:
            __M_writer('      ')
            __M_writer(str(html_site_header()))
            __M_writer('\n')
        else:
            __M_writer('      <a href="')
            __M_writer(str(abs_link(_link("root", None, lang))))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('" rel="home">\n        ')
            __M_writer(str(html_site_header()))
            __M_writer('\n      </a>\n')
        __M_writer('  </h1>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 19, "35": 33, "36": 55, "37": 69, "38": 113, "39": 122, "45": 21, "52": 21, "53": 22, "54": 23, "55": 27, "56": 27, "62": 4, "79": 4, "80": 8, "81": 9, "82": 10, "83": 10, "84": 11, "85": 11, "86": 14, "87": 14, "88": 14, "89": 15, "90": 15, "96": 35, "105": 35, "106": 36, "107": 37, "108": 39, "109": 40, "110": 41, "111": 42, "112": 42, "113": 42, "114": 42, "115": 45, "116": 46, "117": 47, "118": 47, "119": 47, "120": 48, "121": 49, "122": 49, "123": 49, "124": 51, "125": 52, "126": 53, "132": 71, "146": 71, "147": 80, "148": 81, "149": 82, "150": 82, "151": 82, "152": 83, "153": 84, "154": 85, "155": 85, "156": 85, "157": 85, "158": 85, "159": 85, "160": 85, "161": 85, "162": 85, "163": 86, "164": 87, "165": 87, "166": 87, "167": 87, "168": 87, "169": 87, "170": 87, "171": 90, "172": 91, "173": 92, "174": 92, "175": 92, "176": 92, "177": 92, "178": 92, "179": 92, "180": 92, "181": 92, "182": 93, "183": 94, "184": 94, "185": 94, "186": 94, "187": 94, "188": 94, "189": 94, "190": 98, "191": 98, "192": 99, "193": 99, "199": 115, "209": 115, "210": 116, "211": 117, "212": 118, "213": 118, "214": 119, "215": 119, "221": 57, "234": 57, "235": 60, "236": 61, "237": 61, "238": 61, "239": 62, "240": 63, "241": 63, "242": 63, "243": 63, "244": 63, "245": 64, "246": 64, "247": 67, "253": 247}, "filename": "themes/carpet/templates/base_header.tmpl", "uri": "base_header.tmpl"}
__M_END_METADATA
"""
