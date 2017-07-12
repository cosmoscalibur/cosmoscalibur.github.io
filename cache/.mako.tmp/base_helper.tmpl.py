# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824719.7624214
_enable_loop = True
_template_filename = 'themes/carpet/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_css', 'html_headstart', 'html_feedlinks', 'preload_stylesheets', 'html_stylesheets', 'late_load_js', 'html_translations']


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
        def preload_stylesheets():
            return render_preload_stylesheets(context)
        def html_stylesheets():
            return render_html_stylesheets(context)
        __M_writer = context.writer()
        __M_writer('\n  ')
        __M_writer(str(preload_stylesheets()))
        __M_writer('\n  <noscript id="deferred-styles">\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n  </noscript>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        url_type = context.get('url_type', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        def late_load_css():
            return render_late_load_css(context)
        abs_link = context.get('abs_link', UNDEFINED)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        nextlink = context.get('nextlink', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        carpet__late_load_css = context.get('carpet__late_load_css', UNDEFINED)
        description = context.get('description', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        lang = context.get('lang', UNDEFINED)
        title = context.get('title', UNDEFINED)
        carpet__head_prefix = context.get('carpet__head_prefix', UNDEFINED)
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
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        len = context.get('len', UNDEFINED)
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


def render_preload_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
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


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
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


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        carpet__late_load_css = context.get('carpet__late_load_css', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
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
        sorted = context.get('sorted', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 82, "23": 89, "24": 120, "25": 142, "26": 165, "27": 177, "28": 184, "34": 84, "42": 84, "43": 85, "44": 85, "45": 87, "46": 87, "52": 3, "85": 3, "86": 6, "87": 7, "88": 8, "89": 10, "90": 11, "91": 13, "92": 14, "93": 15, "94": 17, "95": 18, "96": 21, "97": 21, "98": 21, "99": 23, "100": 24, "101": 24, "102": 24, "103": 26, "104": 28, "105": 29, "106": 29, "107": 29, "108": 31, "109": 32, "110": 33, "111": 33, "112": 33, "113": 35, "114": 38, "115": 39, "116": 39, "117": 39, "118": 40, "119": 41, "120": 41, "121": 41, "122": 41, "123": 41, "124": 43, "125": 44, "126": 44, "127": 46, "128": 46, "129": 47, "130": 47, "131": 49, "132": 50, "133": 51, "134": 51, "135": 51, "136": 51, "137": 51, "138": 51, "139": 51, "140": 54, "141": 55, "142": 56, "143": 56, "144": 56, "145": 58, "146": 59, "147": 60, "148": 60, "149": 60, "150": 62, "151": 63, "152": 64, "153": 64, "154": 64, "155": 66, "156": 67, "157": 68, "158": 68, "159": 68, "160": 70, "161": 71, "162": 71, "163": 72, "164": 73, "165": 74, "166": 75, "167": 75, "168": 75, "169": 77, "170": 78, "171": 78, "172": 79, "173": 80, "174": 80, "175": 80, "181": 144, "192": 144, "193": 145, "194": 146, "195": 146, "196": 146, "197": 147, "198": 148, "199": 149, "200": 150, "201": 150, "202": 150, "203": 150, "204": 150, "205": 152, "206": 153, "207": 153, "208": 153, "209": 156, "210": 157, "211": 158, "212": 159, "213": 159, "214": 159, "215": 159, "216": 159, "217": 161, "218": 162, "219": 162, "220": 162, "226": 91, "234": 91, "235": 92, "236": 93, "237": 94, "238": 96, "239": 97, "240": 100, "241": 101, "242": 109, "243": 110, "244": 114, "245": 115, "251": 122, "259": 122, "260": 123, "261": 124, "262": 125, "263": 126, "264": 127, "265": 129, "266": 130, "267": 134, "268": 135, "269": 138, "270": 139, "276": 179, "282": 179, "283": 180, "284": 181, "285": 183, "286": 183, "287": 183, "293": 167, "303": 167, "304": 169, "305": 170, "306": 171, "307": 172, "308": 172, "309": 172, "310": 172, "311": 172, "312": 172, "313": 176, "319": 313}, "filename": "themes/carpet/templates/base_helper.tmpl", "uri": "base_helper.tmpl"}
__M_END_METADATA
"""
