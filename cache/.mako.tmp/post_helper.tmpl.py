# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824813.9793646
_enable_loop = True
_template_filename = 'themes/carpet/templates/post_helper.tmpl'
_template_uri = 'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['mathjax_script', 'html_pager', 'html_tags', 'open_graph_metadata', 'meta_translations', 'twitter_card_information']


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
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        katex_auto_render = context.get('katex_auto_render', UNDEFINED)
        use_katex = context.get('use_katex', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.is_mathjax:
            if use_katex:
                __M_writer('    <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.js"></script>\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/contrib/auto-render.min.js"></script>\n')
                if katex_auto_render:
                    __M_writer('      <script>\n        renderMathInElement(document.body,\n          {\n            ')
                    __M_writer(str(katex_auto_render))
                    __M_writer('\n          }\n        );\n      </script>\n')
                else:
                    __M_writer('      <script>\n        renderMathInElement(document.body);\n      </script>\n')
            else:
                __M_writer('    <script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"> </script>\n    \n')
                if mathjax_config:
                    __M_writer('      ')
                    __M_writer(str(mathjax_config))
                    __M_writer('\n')
                else:
                    __M_writer('      <script type="text/x-mathjax-config">\n        MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});\n      </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.prev_post or post.next_post:
            __M_writer('  <div class="columns">\n    <div class="column">\n      <nav class="pagination pager hidden-print">\n')
            if post.prev_post:
                __M_writer('          <a class="pagination-previous previous" href="')
                __M_writer(str(post.prev_post.permalink()))
                __M_writer('" rel="prev" title="')
                __M_writer(filters.html_escape(str(post.prev_post.title())))
                __M_writer('">')
                __M_writer(str(messages("Previous post")))
                __M_writer('</a>\n')
            if post.next_post:
                __M_writer('          <a class="pagination-next next" href="')
                __M_writer(str(post.next_post.permalink()))
                __M_writer('" rel="next" title="')
                __M_writer(filters.html_escape(str(post.next_post.title())))
                __M_writer('">')
                __M_writer(str(messages("Next post")))
                __M_writer('</a>\n')
            __M_writer('      </nav>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.tags:
            __M_writer('  <div class="columns tags" itemprop="keywords">\n')
            for tag in post.tags:
                if tag not in hidden_tags:
                    __M_writer('        <div class="column has-text-centered">\n          <a class="tag is-primary is-medium p-category" href="')
                    __M_writer(str(_link('tag', tag)))
                    __M_writer('" rel="tag">')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('</a>\n        </div>\n')
            __M_writer('  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_open_graph:
            __M_writer('  <meta property="og:site_name" content="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('">\n  <meta property="og:title" content="')
            __M_writer(filters.html_escape(str(post.title()[:70])))
            __M_writer('">\n  <meta property="og:url" content="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n  \n')
            if post.description():
                __M_writer('    <meta property="og:description" content="')
                __M_writer(filters.html_escape(str(post.description()[:200])))
                __M_writer('">\n')
            else:
                __M_writer('    <meta property="og:description" content="')
                __M_writer(filters.html_escape(str(post.text(strip_html=True)[:200])))
                __M_writer('">\n')
            __M_writer('  \n')
            if post.previewimage:
                __M_writer('    <meta property="og:image" content="')
                __M_writer(str(url_replacer(permalink, post.previewimage, lang, 'absolute')))
                __M_writer('">\n')
            __M_writer('  \n  <meta property="og:type" content="article">\n\n')
            __M_writer('  \n')
            if post.date.isoformat():
                __M_writer('    <meta property="article:published_time" content="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('">\n')
            __M_writer('  \n')
            if post.tags:
                for tag in post.tags:
                    __M_writer('      <meta property="article:tag" content="')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for langname in sorted(translations):
                if langname != lang and ((not post.skip_untranslated) or post.is_translation_available(langname)):
                    __M_writer('      <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if twitter_card and twitter_card['use_twitter_cards']:
            __M_writer('  <meta name="twitter:card" content="')
            __M_writer(filters.html_escape(str(twitter_card.get('card', 'summary'))))
            __M_writer('">\n  \n')
            if 'site:id' in twitter_card:
                __M_writer('    <meta name="twitter:site:id" content="')
                __M_writer(str(twitter_card['site:id']))
                __M_writer('">\n')
            elif 'site' in twitter_card:
                __M_writer('    <meta name="twitter:site" content="')
                __M_writer(str(twitter_card['site']))
                __M_writer('">\n')
            __M_writer('  \n')
            if 'creator:id' in twitter_card:
                __M_writer('    <meta name="twitter:creator:id" content="')
                __M_writer(str(twitter_card['creator:id']))
                __M_writer('">\n')
            elif 'creator' in twitter_card:
                __M_writer('    <meta name="twitter:creator" content="')
                __M_writer(str(twitter_card['creator']))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "post_helper.tmpl", "line_map": {"16": 0, "21": 2, "22": 11, "23": 25, "24": 42, "25": 77, "26": 95, "27": 127, "33": 97, "40": 97, "41": 98, "42": 99, "43": 100, "44": 102, "45": 103, "46": 106, "47": 106, "48": 110, "49": 111, "50": 115, "51": 116, "52": 118, "53": 119, "54": 119, "55": 119, "56": 120, "57": 121, "63": 27, "68": 27, "69": 28, "70": 29, "71": 32, "72": 33, "73": 33, "74": 33, "75": 33, "76": 33, "77": 33, "78": 33, "79": 35, "80": 36, "81": 36, "82": 36, "83": 36, "84": 36, "85": 36, "86": 36, "87": 38, "93": 13, "99": 13, "100": 14, "101": 15, "102": 16, "103": 17, "104": 18, "105": 19, "106": 19, "107": 19, "108": 19, "109": 23, "115": 44, "125": 44, "126": 45, "127": 46, "128": 46, "129": 46, "130": 47, "131": 47, "132": 48, "133": 48, "134": 50, "135": 51, "136": 51, "137": 51, "138": 52, "139": 53, "140": 53, "141": 53, "142": 55, "143": 56, "144": 57, "145": 57, "146": 57, "147": 59, "148": 66, "149": 67, "150": 68, "151": 68, "152": 68, "153": 70, "154": 71, "155": 72, "156": 73, "157": 73, "158": 73, "164": 3, "172": 3, "173": 4, "174": 5, "175": 6, "176": 7, "177": 7, "178": 7, "179": 7, "180": 7, "186": 79, "191": 79, "192": 80, "193": 81, "194": 81, "195": 81, "196": 83, "197": 84, "198": 84, "199": 84, "200": 85, "201": 86, "202": 86, "203": 86, "204": 88, "205": 89, "206": 90, "207": 90, "208": 90, "209": 91, "210": 92, "211": 92, "212": 92, "218": 212}, "filename": "themes/carpet/templates/post_helper.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
