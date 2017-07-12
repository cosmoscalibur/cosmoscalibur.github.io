# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824593.878876
_enable_loop = True
_template_filename = 'themes/carpet/templates/post_helper.tmpl'
_template_uri = 'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['open_graph_metadata', 'meta_translations', 'html_pager', 'mathjax_script', 'html_tags', 'twitter_card_information']


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


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        permalink = context.get('permalink', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
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
        sorted = context.get('sorted', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
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
{"line_map": {"16": 0, "21": 2, "22": 11, "23": 25, "24": 42, "25": 77, "26": 95, "27": 127, "33": 44, "43": 44, "44": 45, "45": 46, "46": 46, "47": 46, "48": 47, "49": 47, "50": 48, "51": 48, "52": 50, "53": 51, "54": 51, "55": 51, "56": 52, "57": 53, "58": 53, "59": 53, "60": 55, "61": 56, "62": 57, "63": 57, "64": 57, "65": 59, "66": 66, "67": 67, "68": 68, "69": 68, "70": 68, "71": 70, "72": 71, "73": 72, "74": 73, "75": 73, "76": 73, "82": 3, "90": 3, "91": 4, "92": 5, "93": 6, "94": 7, "95": 7, "96": 7, "97": 7, "98": 7, "104": 27, "109": 27, "110": 28, "111": 29, "112": 32, "113": 33, "114": 33, "115": 33, "116": 33, "117": 33, "118": 33, "119": 33, "120": 35, "121": 36, "122": 36, "123": 36, "124": 36, "125": 36, "126": 36, "127": 36, "128": 38, "134": 97, "141": 97, "142": 98, "143": 99, "144": 100, "145": 102, "146": 103, "147": 106, "148": 106, "149": 110, "150": 111, "151": 115, "152": 116, "153": 118, "154": 119, "155": 119, "156": 119, "157": 120, "158": 121, "164": 13, "170": 13, "171": 14, "172": 15, "173": 16, "174": 17, "175": 18, "176": 19, "177": 19, "178": 19, "179": 19, "180": 23, "186": 79, "191": 79, "192": 80, "193": 81, "194": 81, "195": 81, "196": 83, "197": 84, "198": 84, "199": 84, "200": 85, "201": 86, "202": 86, "203": 86, "204": 88, "205": 89, "206": 90, "207": 90, "208": 90, "209": 91, "210": 92, "211": 92, "212": 92, "218": 212}, "filename": "themes/carpet/templates/post_helper.tmpl", "uri": "post_helper.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
