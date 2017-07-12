# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824719.657321
_enable_loop = True
_template_filename = 'themes/carpet/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_sourcelink', 'html_post_header', 'html_translations', 'html_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

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


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        messages = context.get('messages', UNDEFINED)
        def html_title():
            return render_html_title(context)
        def html_translations(post):
            return render_html_translations(context,post)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def html_sourcelink():
            return render_html_sourcelink(context)
        date_format = context.get('date_format', UNDEFINED)
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
        len = context.get('len', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
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
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 13, "137": 13, "138": 14, "139": 15, "140": 16, "141": 16, "142": 17, "143": 18, "144": 19, "145": 19, "146": 19, "147": 19, "148": 19, "149": 19, "150": 19, "23": 3, "26": 2, "175": 169, "29": 0, "34": 2, "35": 3, "36": 11, "37": 24, "38": 34, "39": 86, "168": 8, "169": 8, "45": 26, "157": 5, "163": 5, "52": 26, "53": 27, "54": 28, "55": 30, "56": 30, "57": 30, "58": 30, "151": 22, "64": 36, "164": 6, "167": 8, "81": 36, "82": 38, "83": 38, "84": 45, "85": 46, "86": 46, "87": 46, "88": 46, "89": 46, "90": 47, "91": 48, "92": 48, "93": 48, "94": 50, "95": 58, "96": 58, "97": 59, "98": 59, "99": 59, "100": 59, "101": 59, "102": 59, "103": 64, "104": 65, "105": 66, "106": 66, "107": 69, "108": 70, "109": 70, "110": 72, "111": 73, "112": 75, "113": 75, "114": 75, "115": 75, "116": 79, "117": 80, "118": 80, "119": 80, "120": 82, "121": 84, "122": 84, "166": 8, "165": 7}, "filename": "themes/carpet/templates/post_header.tmpl", "uri": "post_header.tmpl"}
__M_END_METADATA
"""
