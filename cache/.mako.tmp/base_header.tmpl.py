# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824593.7724802
_enable_loop = True
_template_filename = 'themes/carpet/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_site_title', 'html_navigation_links', 'html_header', 'html_search', 'html_translation_header', 'html_site_header']


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


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def html_site_header():
            return render_html_site_header(context)
        carpet__unlink_blog_brand = _import_ns.get('carpet__unlink_blog_brand', context.get('carpet__unlink_blog_brand', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
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


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
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


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def html_site_title():
            return render_html_site_title(context)
        def html_navigation_links():
            return render_html_navigation_links(context)
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        def html_translation_header():
            return render_html_translation_header(context)
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
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


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
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


def render_html_site_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
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


"""
__M_BEGIN_METADATA
{"line_map": {"23": 2, "26": 0, "33": 2, "34": 19, "35": 33, "36": 55, "37": 69, "38": 113, "39": 122, "45": 57, "58": 57, "59": 60, "60": 61, "61": 61, "62": 61, "63": 62, "64": 63, "65": 63, "66": 63, "67": 63, "68": 63, "69": 64, "70": 64, "71": 67, "77": 71, "91": 71, "92": 80, "93": 81, "94": 82, "95": 82, "96": 82, "97": 83, "98": 84, "99": 85, "100": 85, "101": 85, "102": 85, "103": 85, "104": 85, "105": 85, "106": 85, "107": 85, "108": 86, "109": 87, "110": 87, "111": 87, "112": 87, "113": 87, "114": 87, "115": 87, "116": 90, "117": 91, "118": 92, "119": 92, "120": 92, "121": 92, "122": 92, "123": 92, "124": 92, "125": 92, "126": 92, "127": 93, "128": 94, "129": 94, "130": 94, "131": 94, "132": 94, "133": 94, "134": 94, "135": 98, "136": 98, "137": 99, "138": 99, "144": 4, "161": 4, "162": 8, "163": 9, "164": 10, "165": 10, "166": 11, "167": 11, "168": 14, "169": 14, "170": 14, "171": 15, "172": 15, "178": 21, "185": 21, "186": 22, "187": 23, "188": 27, "189": 27, "195": 115, "205": 115, "206": 116, "207": 117, "208": 118, "209": 118, "210": 119, "211": 119, "217": 35, "226": 35, "227": 36, "228": 37, "229": 39, "230": 40, "231": 41, "232": 42, "233": 42, "234": 42, "235": 42, "236": 45, "237": 46, "238": 47, "239": 47, "240": 47, "241": 48, "242": 49, "243": 49, "244": 49, "245": 51, "246": 52, "247": 53, "253": 247}, "filename": "themes/carpet/templates/base_header.tmpl", "uri": "base_header.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
