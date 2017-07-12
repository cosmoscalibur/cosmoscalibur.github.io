# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824719.6998343
_enable_loop = True
_template_filename = 'themes/carpet/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'html_hero_body', 'content', 'extra_js']



import re
def lower(text):
  # remove all non-alphabet chars from string
  regex = re.compile('[^a-zA-Z0-9]')
  result = regex.sub('', text)
  return result.lower()


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('header', context._clean_inheritance_tokens(), templateuri='base_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'header')] = ns

    ns = runtime.TemplateNamespace('annotations', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'annotations')] = ns

    ns = runtime.TemplateNamespace('footer', context._clean_inheritance_tokens(), templateuri='base_footer.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'footer')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        blog_description = _import_ns.get('blog_description', context.get('blog_description', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        carpet__show_hero = _import_ns.get('carpet__show_hero', context.get('carpet__show_hero', UNDEFINED))
        carpet__body_prefix = _import_ns.get('carpet__body_prefix', context.get('carpet__body_prefix', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        carpet__cookie_expiry = _import_ns.get('carpet__cookie_expiry', context.get('carpet__cookie_expiry', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        carpet__hero_footer = _import_ns.get('carpet__hero_footer', context.get('carpet__hero_footer', UNDEFINED))
        carpet__content_prefix = _import_ns.get('carpet__content_prefix', context.get('carpet__content_prefix', UNDEFINED))
        carpet__cookie_path = _import_ns.get('carpet__cookie_path', context.get('carpet__cookie_path', UNDEFINED))
        carpet__cookie_message = _import_ns.get('carpet__cookie_message', context.get('carpet__cookie_message', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        header = _mako_get_namespace(context, 'header')
        footer = _mako_get_namespace(context, 'footer')
        carpet__hero_size = _import_ns.get('carpet__hero_size', context.get('carpet__hero_size', UNDEFINED))
        carpet__show_hero_title = _import_ns.get('carpet__show_hero_title', context.get('carpet__show_hero_title', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        def html_hero_body():
            return render_html_hero_body(context._locals(__M_locals))
        carpet__content_suffix = _import_ns.get('carpet__content_suffix', context.get('carpet__content_suffix', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body>\n')
        if carpet__body_prefix:
            __M_writer('  ')
            __M_writer(str(carpet__body_prefix))
            __M_writer('\n')
        __M_writer('<script type="text/javascript">\n  // Detect JS support\n  document.body.className = document.body.className + " js_enabled";\n</script>\n<a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(str(messages("Skip to main content")))
        __M_writer('</a>\n<div id="container">\n')
        if carpet__hero_size:
            __M_writer('    <section class="hero is-primary ')
            __M_writer(str(carpet__hero_size))
            __M_writer('">\n')
        else:
            __M_writer('    <section class="hero is-primary">\n')
        __M_writer('    <!-- Hero header: will stick at the top -->\n    ')
        __M_writer(str(header.html_header()))
        __M_writer('\n    <!-- Hero content: will be in the middle -->\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'html_hero_body'):
            context['self'].html_hero_body(**pageargs)
        

        __M_writer('\n    <!-- Hero footer: will stick at the bottom -->\n')
        if carpet__hero_footer:
            __M_writer('      ')
            __M_writer(str(carpet__hero_footer))
            __M_writer('\n')
        __M_writer('  </section>\n')
        if carpet__cookie_message:
            __M_writer('  <div id="cookie-message" class="section section-cookie"\n')
            if carpet__cookie_path:
                __M_writer('      data-cookie-path="')
                __M_writer(filters.html_escape(str(carpet__cookie_path)))
                __M_writer('"\n')
            if carpet__cookie_expiry:
                __M_writer('      data-cookie-expiry="')
                __M_writer(filters.html_escape(str(carpet__cookie_expiry)))
                __M_writer('"\n')
            __M_writer('  >\n    <div class="notification">\n      <button id="cookie-close" class="delete"></button>\n      ')
            __M_writer(str(carpet__cookie_message))
            __M_writer('\n    </div>\n  </div>\n')
        if carpet__content_prefix:
            __M_writer('    ')
            __M_writer(str(carpet__content_prefix))
            __M_writer('\n')
        __M_writer('  <main id="content" class="section section-main">\n    <div class="container">\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n    </div>\n  </main>\n')
        if carpet__content_suffix:
            __M_writer('    ')
            __M_writer(str(carpet__content_suffix))
            __M_writer('\n')
        __M_writer('  ')
        __M_writer(str(header.html_search()))
        __M_writer('\n  ')
        __M_writer(str(footer.html_footer()))
        __M_writer('\n</div>\n')
        if carpet__cookie_message:
            __M_writer('<script async src="/assets/js/cookie-message.js"></script>\n')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(body_end))
        __M_writer('\n')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_hero_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        blog_description = _import_ns.get('blog_description', context.get('blog_description', UNDEFINED))
        def html_hero_body():
            return render_html_hero_body(context)
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        carpet__show_hero_title = _import_ns.get('carpet__show_hero_title', context.get('carpet__show_hero_title', UNDEFINED))
        carpet__show_hero = _import_ns.get('carpet__show_hero', context.get('carpet__show_hero', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if carpet__show_hero:
            if title:
                __M_writer('          <div class="hero-body hero-')
                __M_writer(filters.trim(filters.html_escape(lower(str(title)))))
                __M_writer('">\n')
            else:
                __M_writer('          <div class="hero-body">\n')
            if carpet__show_hero_title:
                __M_writer('          <div class="container has-text-centered">\n')
                if blog_title:
                    __M_writer('              <p class="title">')
                    __M_writer(filters.html_escape(str(blog_title)))
                    __M_writer('</p>\n')
                if blog_description:
                    __M_writer('              <p class="subtitle">')
                    __M_writer(filters.html_escape(str(blog_description)))
                    __M_writer('</p>\n')
                __M_writer('          </div>\n')
            __M_writer('        </div>\n')
        __M_writer('    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"261": 246, "16": 6, "32": 2, "35": 3, "38": 5, "41": 4, "44": 0, "82": 2, "83": 3, "84": 4, "85": 5, "86": 13, "87": 14, "88": 14, "89": 15, "90": 15, "95": 18, "96": 19, "97": 19, "98": 22, "99": 23, "100": 23, "101": 23, "102": 25, "103": 29, "104": 29, "105": 31, "106": 32, "107": 32, "108": 32, "109": 33, "110": 34, "111": 36, "112": 37, "113": 37, "118": 58, "119": 60, "120": 61, "121": 61, "122": 61, "123": 63, "124": 64, "125": 65, "126": 66, "127": 67, "128": 67, "129": 67, "130": 69, "131": 70, "132": 70, "133": 70, "134": 72, "135": 75, "136": 75, "137": 79, "138": 80, "139": 80, "140": 80, "141": 82, "146": 84, "147": 87, "148": 88, "149": 88, "150": 88, "151": 90, "152": 90, "153": 90, "154": 91, "155": 91, "156": 93, "157": 94, "158": 96, "159": 96, "164": 97, "165": 98, "166": 98, "167": 99, "168": 99, "174": 16, "184": 16, "190": 39, "205": 39, "206": 40, "207": 41, "208": 42, "209": 42, "210": 42, "211": 43, "212": 44, "213": 46, "214": 47, "215": 48, "216": 49, "217": 49, "218": 49, "219": 51, "220": 52, "221": 52, "222": 52, "223": 54, "224": 56, "225": 58, "231": 84, "246": 97}, "filename": "themes/carpet/templates/base.tmpl", "uri": "base.tmpl"}
__M_END_METADATA
"""
