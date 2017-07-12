# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824593.8910227
_enable_loop = True
_template_filename = 'themes/carpet/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_post_header', 'html_translations', 'html_title', 'html_sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

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


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def html_translations(post):
            return render_html_translations(context,post)
        _link = context.get('_link', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        date_format = context.get('date_format', UNDEFINED)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def html_title():
            return render_html_title(context)
        def html_sourcelink():
            return render_html_sourcelink(context)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<header class="heading">\n  ')
        __M_writer(str(html_title()))
        __M_writer('\n  <div class="level metadata">\n    \n    <div class="level-left">\n      <div class="level-item">\n        <p class="byline author vcard">\n          <span class="byline-name fn">\n')
        if author_pages_generated:
            __M_writer('              <a href="')
            __M_writer(str(_link('author', post.author())))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('</a>\n')
        else:
            __M_writer('              ')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('\n')
        __M_writer('          </span>\n        </p>\n      </div>\n    </div>\n    \n    <div class="level-right">\n      <div class="level-item">\n        <p class="dateline">\n          <a href="')
        __M_writer(str(post.permalink()))
        __M_writer('" rel="bookmark">\n            <time class="published dt-published" datetime="')
        __M_writer(str(post.formatted_date('webiso')))
        __M_writer('" itemprop="datePublished" title="')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('">')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('</time>\n          </a>\n        </p>\n      </div>\n      \n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('        <div class="level-item">\n          <p class="commentline">')
            __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
            __M_writer('</p>\n        </div>\n')
        __M_writer('      \n      ')
        __M_writer(str(html_sourcelink()))
        __M_writer('\n      \n')
        if post.meta('link'):
            __M_writer('        <div class="level-item">\n          <p class="linkline">\n            <a href="')
            __M_writer(str(post.meta('link')))
            __M_writer('">')
            __M_writer(str(messages("Original site")))
            __M_writer('</a>\n          </p>\n        </div>\n')
        if post.description():
            __M_writer('        <meta name="description" itemprop="description" content="')
            __M_writer(filters.html_escape(str(post.description())))
            __M_writer('">\n')
        __M_writer('    </div>\n  </div>\n  ')
        __M_writer(str(html_translations(post)))
        __M_writer('\n</header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        sorted = context.get('sorted', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(post.translated_to) > 1:
            __M_writer('  <div class="metadata posttranslations translations">\n    <h2 class="subtitle is-2 posttranslations-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h2>\n')
            for langname in sorted(translations):
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('        <p><a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a></p>\n')
            __M_writer('  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('  <h1 class="title is-1 p-name entry-title" itemprop="headline name">\n    <a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a>\n  </h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('  <div class="level-item">\n    <p class="sourceline">\n      <a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n    </p>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 19, "129": 19, "130": 19, "131": 19, "132": 22, "138": 5, "144": 5, "145": 6, "146": 7, "147": 8, "148": 8, "149": 8, "150": 8, "23": 2, "26": 3, "175": 169, "156": 26, "29": 0, "34": 2, "35": 3, "36": 11, "37": 24, "38": 34, "39": 86, "168": 30, "169": 30, "165": 28, "45": 36, "164": 27, "166": 30, "163": 26, "62": 36, "63": 38, "64": 38, "65": 45, "66": 46, "67": 46, "68": 46, "69": 46, "70": 46, "71": 47, "72": 48, "73": 48, "74": 48, "75": 50, "76": 58, "77": 58, "78": 59, "79": 59, "80": 59, "81": 59, "82": 59, "83": 59, "84": 64, "85": 65, "86": 66, "87": 66, "88": 69, "89": 70, "90": 70, "91": 72, "92": 73, "93": 75, "94": 75, "95": 75, "96": 75, "97": 79, "98": 80, "99": 80, "100": 80, "101": 82, "102": 84, "103": 84, "167": 30, "109": 13, "118": 13, "119": 14, "120": 15, "121": 16, "122": 16, "123": 17, "124": 18, "125": 19, "126": 19, "127": 19}, "filename": "themes/carpet/templates/post_header.tmpl", "uri": "post_header.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
