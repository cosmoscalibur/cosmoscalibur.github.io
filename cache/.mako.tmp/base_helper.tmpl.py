# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499823164.1727622
_enable_loop = True
_template_filename = 'themes/hack/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_feedlinks', 'html_stylesheets', 'late_load_js', 'html_translations', 'html_headstart']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        HACK_VARIANT = context.get('HACK_VARIANT', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n    <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n')
        if not HACK_VARIANT:
            __M_writer('        <link href="/assets/css/hack.css" rel="stylesheet" type="text/css">\n')
        elif HACK_VARIANT == 'dark':
            __M_writer('        <link href="/assets/css/dark.css" rel="stylesheet" type="text/css">\n')
        elif HACK_VARIANT == 'dark-grey':
            __M_writer('        <link href="/assets/css/dark-grey.css" rel="stylesheet" type="text/css">\n')
        elif HACK_VARIANT == 'solarized-dark':
            __M_writer('        <link href="/assets/css/solarized-dark.css" rel="stylesheet" type="text/css">\n')
        elif HACK_VARIANT == 'standard':
            __M_writer('        <link href="/assets/css/standard.css" rel="stylesheet" type="text/css">\n')
        __M_writer('    <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n    <link href="https://fonts.googleapis.com/css?family=Share+Tech+Mono" rel="stylesheet">\n')
        if has_custom_css:
            __M_writer('        <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <ul class="translations">\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        title = context.get('title', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        meta_generator_tag = context.get('meta_generator_tag', UNDEFINED)
        url_type = context.get('url_type', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        description = context.get('description', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<head>\n    <meta charset="utf-8">\n')
        if use_base_tag:
            __M_writer('    <base href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n')
        if title == blog_title:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    <meta name="theme-color" content="')
        __M_writer(str(theme_color))
        __M_writer('">\n')
        if meta_generator_tag:
            __M_writer('    <meta name="generator" content="Nikola (getnikola.com)">\n')
        __M_writer('    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang, url_type)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/hack/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "source_encoding": "utf-8", "line_map": {"256": 250, "16": 0, "21": 2, "22": 69, "23": 73, "24": 98, "25": 121, "26": 131, "32": 100, "43": 100, "44": 101, "45": 102, "46": 102, "47": 102, "48": 103, "49": 104, "50": 105, "51": 106, "52": 106, "53": 106, "54": 106, "55": 106, "56": 108, "57": 109, "58": 109, "59": 109, "60": 112, "61": 113, "62": 114, "63": 115, "64": 115, "65": 115, "66": 115, "67": 115, "68": 117, "69": 118, "70": 118, "71": 118, "77": 75, "84": 75, "85": 78, "86": 79, "87": 80, "88": 81, "89": 82, "90": 83, "91": 84, "92": 85, "93": 86, "94": 87, "95": 89, "96": 91, "97": 92, "98": 94, "99": 95, "105": 71, "110": 71, "111": 72, "112": 72, "118": 123, "128": 123, "129": 125, "130": 126, "131": 127, "132": 127, "133": 127, "134": 127, "135": 127, "136": 127, "137": 127, "138": 130, "144": 3, "173": 3, "174": 6, "175": 7, "176": 8, "177": 10, "178": 11, "179": 13, "180": 14, "181": 15, "182": 17, "183": 18, "184": 21, "185": 21, "186": 21, "187": 24, "188": 25, "189": 25, "190": 25, "191": 27, "192": 28, "193": 28, "194": 28, "195": 30, "196": 31, "197": 32, "198": 32, "199": 32, "200": 33, "201": 34, "202": 34, "203": 34, "204": 34, "205": 34, "206": 36, "207": 37, "208": 37, "209": 38, "210": 38, "211": 39, "212": 40, "213": 42, "214": 42, "215": 42, "216": 43, "217": 43, "218": 45, "219": 46, "220": 47, "221": 47, "222": 47, "223": 47, "224": 47, "225": 47, "226": 47, "227": 50, "228": 51, "229": 52, "230": 52, "231": 52, "232": 54, "233": 55, "234": 56, "235": 56, "236": 56, "237": 58, "238": 59, "239": 59, "240": 59, "241": 61, "242": 62, "243": 63, "244": 64, "245": 65, "246": 65, "247": 65, "248": 67, "249": 68, "250": 68}}
__M_END_METADATA
"""
