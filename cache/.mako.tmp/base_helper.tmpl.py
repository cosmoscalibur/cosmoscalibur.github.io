# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824593.7562644
_enable_loop = True
_template_filename = 'themes/carpet/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_css', 'late_load_js', 'html_translations', 'preload_stylesheets', 'html_headstart', 'html_feedlinks', 'html_stylesheets']


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
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_css(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_stylesheets():
            return render_html_stylesheets(context)
        def preload_stylesheets():
            return render_preload_stylesheets(context)
        __M_writer = context.writer()
        __M_writer('\n  ')
        __M_writer(str(preload_stylesheets()))
        __M_writer('\n  <noscript id="deferred-styles">\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n  </noscript>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        carpet__late_load_css = context.get('carpet__late_load_css', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if carpet__late_load_css:
            __M_writer('    <script>!function(e){"use strict";var t=function(t,n,r){function o(e){return i.body?e():void setTimeout(function(){o(e)})}function a(){d.addEventListener&&d.removeEventListener("load",a),d.media=r||"all"}var l,i=e.document,d=i.createElement("link");if(n)l=n;else{var s=(i.body||i.getElementsByTagName("head")[0]).childNodes;l=s[s.length-1]}var u=i.styleSheets;d.rel="stylesheet",d.href=t,d.media="only x",o(function(){l.parentNode.insertBefore(d,n?l:l.nextSibling)});var f=function(e){for(var t=d.href,n=u.length;n--;)if(u[n].href===t)return e();setTimeout(function(){f(e)})};return d.addEventListener&&d.addEventListener("load",a),d.onloadcssdefined=f,f(a),d};"undefined"!=typeof exports?exports.loadCSS=t:e.loadCSS=t}("undefined"!=typeof global?global:this),function(e){if(e.loadCSS){var t=loadCSS.relpreload={};if(t.support=function(){try{return e.document.createElement("link").relList.supports("preload")}catch(e){return!1}},t.poly=function(){for(var t=e.document.getElementsByTagName("link"),n=0;n<t.length;n++){var r=t[n];"preload"===r.rel&&"style"===r.getAttribute("as")&&(e.loadCSS(r.href,r),r.rel=null)}},!t.support()){t.poly();var n=e.setInterval(t.poly,300);e.addEventListener&&e.addEventListener("load",function(){t.poly(),e.clearInterval(n)}),e.attachEvent&&e.attachEvent("onload",function(){e.clearInterval(n)})}}}(this);</script>\n')
        __M_writer('  ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="level translations">\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('      <div class="level-item has-text-centered">\n        <a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a>\n      </div>\n')
        __M_writer('</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_preload_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('    <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n      href="/assets/css/all.css">\n')
            else:
                __M_writer('    <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n      href="/assets/css/all-nocdn.css">\n')
        else:
            __M_writer('  <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n    href="/assets/css/rst.css">\n  <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n    href="/assets/css/code.css">\n  <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n    href="/assets/css/font-awesome.css">\n  <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n    href="/assets/css/styles.css">\n')
            if has_custom_css:
                __M_writer('    <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n      href="/assets/css/custom.css">\n')
        if needs_ipython_css:
            __M_writer('  <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n    href="/assets/css/ipython.min.css">\n  <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n    href="/assets/css/nikola_ipython.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_feedlinks():
            return render_html_feedlinks(context)
        comment_system = context.get('comment_system', UNDEFINED)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        use_cdn = context.get('use_cdn', UNDEFINED)
        url_type = context.get('url_type', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        carpet__head_prefix = context.get('carpet__head_prefix', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        def late_load_css():
            return render_late_load_css(context)
        title = context.get('title', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        description = context.get('description', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        carpet__late_load_css = context.get('carpet__late_load_css', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
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
        __M_writer('">\n<head>\n')
        if carpet__head_prefix:
            __M_writer('    ')
            __M_writer(str(carpet__head_prefix))
            __M_writer('\n')
        __M_writer('  <meta charset="utf-8">\n  \n')
        if use_base_tag:
            __M_writer('    <base href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        __M_writer('  \n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('  \n  <meta name="viewport" content="width=device-width">\n  \n')
        if title == blog_title:
            __M_writer('    <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('    <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n  <meta name="theme-color" content="')
        __M_writer(str(theme_color))
        __M_writer('">\n  <meta name="generator" content="Nikola (getnikola.com)">\n  ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n  <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('      <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('    <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('    <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        __M_writer('  \n')
        if nextlink:
            __M_writer('    <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('  \n')
        if not carpet__late_load_css:
            __M_writer('    ')
            __M_writer(str(html_stylesheets()))
            __M_writer('\n')
        __M_writer('\n  ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('    <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('    <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang, url_type)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n  ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        if carpet__late_load_css:
            __M_writer('    ')
            __M_writer(str(late_load_css()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('  ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('      <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('    <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('      <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('    <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('    <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('    <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer('  <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n  <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n  <link href="/assets/css/font-awesome.css" rel="stylesheet" type="text/css">\n  <link href="/assets/css/styles.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('    <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('  <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n  <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "21": 2, "22": 82, "23": 89, "24": 120, "25": 142, "26": 165, "27": 177, "28": 184, "34": 84, "42": 84, "43": 85, "44": 85, "45": 87, "46": 87, "52": 179, "58": 179, "59": 180, "60": 181, "61": 183, "62": 183, "63": 183, "69": 167, "79": 167, "80": 169, "81": 170, "82": 171, "83": 172, "84": 172, "85": 172, "86": 172, "87": 172, "88": 172, "89": 176, "95": 91, "103": 91, "104": 92, "105": 93, "106": 94, "107": 96, "108": 97, "109": 100, "110": 101, "111": 109, "112": 110, "113": 114, "114": 115, "120": 3, "153": 3, "154": 6, "155": 7, "156": 8, "157": 10, "158": 11, "159": 13, "160": 14, "161": 15, "162": 17, "163": 18, "164": 21, "165": 21, "166": 21, "167": 23, "168": 24, "169": 24, "170": 24, "171": 26, "172": 28, "173": 29, "174": 29, "175": 29, "176": 31, "177": 32, "178": 33, "179": 33, "180": 33, "181": 35, "182": 38, "183": 39, "184": 39, "185": 39, "186": 40, "187": 41, "188": 41, "189": 41, "190": 41, "191": 41, "192": 43, "193": 44, "194": 44, "195": 46, "196": 46, "197": 47, "198": 47, "199": 49, "200": 50, "201": 51, "202": 51, "203": 51, "204": 51, "205": 51, "206": 51, "207": 51, "208": 54, "209": 55, "210": 56, "211": 56, "212": 56, "213": 58, "214": 59, "215": 60, "216": 60, "217": 60, "218": 62, "219": 63, "220": 64, "221": 64, "222": 64, "223": 66, "224": 67, "225": 68, "226": 68, "227": 68, "228": 70, "229": 71, "230": 71, "231": 72, "232": 73, "233": 74, "234": 75, "235": 75, "236": 75, "237": 77, "238": 78, "239": 78, "240": 79, "241": 80, "242": 80, "243": 80, "249": 144, "260": 144, "261": 145, "262": 146, "263": 146, "264": 146, "265": 147, "266": 148, "267": 149, "268": 150, "269": 150, "270": 150, "271": 150, "272": 150, "273": 152, "274": 153, "275": 153, "276": 153, "277": 156, "278": 157, "279": 158, "280": 159, "281": 159, "282": 159, "283": 159, "284": 159, "285": 161, "286": 162, "287": 162, "288": 162, "294": 122, "302": 122, "303": 123, "304": 124, "305": 125, "306": 126, "307": 127, "308": 129, "309": 130, "310": 134, "311": 135, "312": 138, "313": 139, "319": 313}, "filename": "themes/carpet/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
