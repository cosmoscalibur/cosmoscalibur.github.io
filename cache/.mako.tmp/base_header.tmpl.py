# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824172.8833647
_enable_loop = True
_template_filename = 'themes/carpet/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_navigation_links', 'html_site_title', 'html_header', 'html_search', 'html_translation_header', 'html_site_header']


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


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
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


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        carpet__unlink_blog_brand = _import_ns.get('carpet__unlink_blog_brand', context.get('carpet__unlink_blog_brand', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        def html_site_header():
            return render_html_site_header(context)
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
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


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def html_site_title():
            return render_html_site_title(context)
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        def html_navigation_links():
            return render_html_navigation_links(context)
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        def html_translation_header():
            return render_html_translation_header(context)
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
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
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
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
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
{"filename": "themes/carpet/templates/base_header.tmpl", "source_encoding": "utf-8", "uri": "base_header.tmpl", "line_map": {"23": 2, "26": 0, "33": 2, "34": 19, "35": 33, "36": 55, "37": 69, "38": 113, "39": 122, "45": 71, "59": 71, "60": 80, "61": 81, "62": 82, "63": 82, "64": 82, "65": 83, "66": 84, "67": 85, "68": 85, "69": 85, "70": 85, "71": 85, "72": 85, "73": 85, "74": 85, "75": 85, "76": 86, "77": 87, "78": 87, "79": 87, "80": 87, "81": 87, "82": 87, "83": 87, "84": 90, "85": 91, "86": 92, "87": 92, "88": 92, "89": 92, "90": 92, "91": 92, "92": 92, "93": 92, "94": 92, "95": 93, "96": 94, "97": 94, "98": 94, "99": 94, "100": 94, "101": 94, "102": 94, "103": 98, "104": 98, "105": 99, "106": 99, "112": 57, "125": 57, "126": 60, "127": 61, "128": 61, "129": 61, "130": 62, "131": 63, "132": 63, "133": 63, "134": 63, "135": 63, "136": 64, "137": 64, "138": 67, "144": 4, "161": 4, "162": 8, "163": 9, "164": 10, "165": 10, "166": 11, "167": 11, "168": 14, "169": 14, "170": 14, "171": 15, "172": 15, "178": 21, "185": 21, "186": 22, "187": 23, "188": 27, "189": 27, "195": 115, "205": 115, "206": 116, "207": 117, "208": 118, "209": 118, "210": 119, "211": 119, "217": 35, "226": 35, "227": 36, "228": 37, "229": 39, "230": 40, "231": 41, "232": 42, "233": 42, "234": 42, "235": 42, "236": 45, "237": 46, "238": 47, "239": 47, "240": 47, "241": 48, "242": 49, "243": 49, "244": 49, "245": 51, "246": 52, "247": 53, "253": 247}}
__M_END_METADATA
"""
