# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824005.3469973
_enable_loop = True
_template_filename = 'themes/carpet/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_stylesheets', 'html_headstart', 'html_feedlinks', 'late_load_js', 'late_load_css', 'preload_stylesheets', 'html_translations']


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


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
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


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        permalink = context.get('permalink', UNDEFINED)
        carpet__head_prefix = context.get('carpet__head_prefix', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        carpet__late_load_css = context.get('carpet__late_load_css', UNDEFINED)
        description = context.get('description', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def late_load_css():
            return render_late_load_css(context)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        is_rtl = context.get('is_rtl', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
        url_type = context.get('url_type', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
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
        rss_link = context.get('rss_link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
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


def render_preload_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
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


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        abs_link = context.get('abs_link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
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
{"filename": "themes/carpet/templates/base_helper.tmpl", "source_encoding": "utf-8", "uri": "base_helper.tmpl", "line_map": {"16": 0, "21": 2, "22": 82, "23": 89, "24": 120, "25": 142, "26": 165, "27": 177, "28": 184, "34": 122, "42": 122, "43": 123, "44": 124, "45": 125, "46": 126, "47": 127, "48": 129, "49": 130, "50": 134, "51": 135, "52": 138, "53": 139, "59": 3, "92": 3, "93": 6, "94": 7, "95": 8, "96": 10, "97": 11, "98": 13, "99": 14, "100": 15, "101": 17, "102": 18, "103": 21, "104": 21, "105": 21, "106": 23, "107": 24, "108": 24, "109": 24, "110": 26, "111": 28, "112": 29, "113": 29, "114": 29, "115": 31, "116": 32, "117": 33, "118": 33, "119": 33, "120": 35, "121": 38, "122": 39, "123": 39, "124": 39, "125": 40, "126": 41, "127": 41, "128": 41, "129": 41, "130": 41, "131": 43, "132": 44, "133": 44, "134": 46, "135": 46, "136": 47, "137": 47, "138": 49, "139": 50, "140": 51, "141": 51, "142": 51, "143": 51, "144": 51, "145": 51, "146": 51, "147": 54, "148": 55, "149": 56, "150": 56, "151": 56, "152": 58, "153": 59, "154": 60, "155": 60, "156": 60, "157": 62, "158": 63, "159": 64, "160": 64, "161": 64, "162": 66, "163": 67, "164": 68, "165": 68, "166": 68, "167": 70, "168": 71, "169": 71, "170": 72, "171": 73, "172": 74, "173": 75, "174": 75, "175": 75, "176": 77, "177": 78, "178": 78, "179": 79, "180": 80, "181": 80, "182": 80, "188": 144, "199": 144, "200": 145, "201": 146, "202": 146, "203": 146, "204": 147, "205": 148, "206": 149, "207": 150, "208": 150, "209": 150, "210": 150, "211": 150, "212": 152, "213": 153, "214": 153, "215": 153, "216": 156, "217": 157, "218": 158, "219": 159, "220": 159, "221": 159, "222": 159, "223": 159, "224": 161, "225": 162, "226": 162, "227": 162, "233": 179, "239": 179, "240": 180, "241": 181, "242": 183, "243": 183, "244": 183, "250": 84, "258": 84, "259": 85, "260": 85, "261": 87, "262": 87, "268": 91, "276": 91, "277": 92, "278": 93, "279": 94, "280": 96, "281": 97, "282": 100, "283": 101, "284": 109, "285": 110, "286": 114, "287": 115, "293": 167, "303": 167, "304": 169, "305": 170, "306": 171, "307": 172, "308": 172, "309": 172, "310": 172, "311": 172, "312": 172, "313": 176, "319": 313}}
__M_END_METADATA
"""
