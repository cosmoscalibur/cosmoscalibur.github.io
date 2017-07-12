# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824005.3636963
_enable_loop = True
_template_filename = 'themes/carpet/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_site_title', 'html_site_header', 'html_translation_header', 'html_header', 'html_search', 'html_navigation_links']


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
        def html_site_header():
            return render_html_site_header(context)
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        carpet__unlink_blog_brand = _import_ns.get('carpet__unlink_blog_brand', context.get('carpet__unlink_blog_brand', UNDEFINED))
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


def render_html_site_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
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


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
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


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        def html_site_title():
            return render_html_site_title(context)
        def html_navigation_links():
            return render_html_navigation_links(context)
        def html_translation_header():
            return render_html_translation_header(context)
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
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


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
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


"""
__M_BEGIN_METADATA
{"filename": "themes/carpet/templates/base_header.tmpl", "source_encoding": "utf-8", "uri": "base_header.tmpl", "line_map": {"23": 2, "26": 0, "33": 2, "34": 19, "35": 33, "36": 55, "37": 69, "38": 113, "39": 122, "45": 57, "58": 57, "59": 60, "60": 61, "61": 61, "62": 61, "63": 62, "64": 63, "65": 63, "66": 63, "67": 63, "68": 63, "69": 64, "70": 64, "71": 67, "77": 35, "86": 35, "87": 36, "88": 37, "89": 39, "90": 40, "91": 41, "92": 42, "93": 42, "94": 42, "95": 42, "96": 45, "97": 46, "98": 47, "99": 47, "100": 47, "101": 48, "102": 49, "103": 49, "104": 49, "105": 51, "106": 52, "107": 53, "113": 115, "123": 115, "124": 116, "125": 117, "126": 118, "127": 118, "128": 119, "129": 119, "135": 4, "152": 4, "153": 8, "154": 9, "155": 10, "156": 10, "157": 11, "158": 11, "159": 14, "160": 14, "161": 14, "162": 15, "163": 15, "169": 21, "176": 21, "177": 22, "178": 23, "179": 27, "180": 27, "186": 71, "200": 71, "201": 80, "202": 81, "203": 82, "204": 82, "205": 82, "206": 83, "207": 84, "208": 85, "209": 85, "210": 85, "211": 85, "212": 85, "213": 85, "214": 85, "215": 85, "216": 85, "217": 86, "218": 87, "219": 87, "220": 87, "221": 87, "222": 87, "223": 87, "224": 87, "225": 90, "226": 91, "227": 92, "228": 92, "229": 92, "230": 92, "231": 92, "232": 92, "233": 92, "234": 92, "235": 92, "236": 93, "237": 94, "238": 94, "239": 94, "240": 94, "241": 94, "242": 94, "243": 94, "244": 98, "245": 98, "246": 99, "247": 99, "253": 247}}
__M_END_METADATA
"""
