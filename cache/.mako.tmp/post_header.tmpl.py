# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824173.0904071
_enable_loop = True
_template_filename = 'themes/carpet/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translations', 'html_sourcelink', 'html_post_header', 'html_title']


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


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        len = context.get('len', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
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


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
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
        messages = context.get('messages', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def html_sourcelink():
            return render_html_sourcelink(context)
        _link = context.get('_link', UNDEFINED)
        def html_title():
            return render_html_title(context)
        comments = _mako_get_namespace(context, 'comments')
        date_format = context.get('date_format', UNDEFINED)
        def html_translations(post):
            return render_html_translations(context,post)
        post = context.get('post', UNDEFINED)
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
{"filename": "themes/carpet/templates/post_header.tmpl", "source_encoding": "utf-8", "uri": "post_header.tmpl", "line_map": {"128": 59, "129": 59, "130": 59, "131": 59, "132": 64, "133": 65, "134": 66, "135": 66, "136": 69, "137": 70, "138": 70, "139": 72, "140": 73, "141": 75, "142": 75, "143": 75, "144": 75, "145": 79, "146": 80, "147": 80, "148": 80, "149": 82, "150": 84, "23": 3, "26": 2, "175": 169, "29": 0, "34": 2, "35": 3, "36": 11, "37": 24, "38": 34, "39": 86, "168": 8, "169": 8, "45": 13, "157": 5, "163": 5, "54": 13, "55": 14, "56": 15, "57": 16, "58": 16, "59": 17, "60": 18, "61": 19, "62": 19, "63": 19, "64": 19, "65": 19, "66": 19, "67": 19, "68": 22, "74": 26, "81": 26, "82": 27, "83": 28, "84": 30, "85": 30, "86": 30, "87": 30, "164": 6, "93": 36, "165": 7, "151": 84, "166": 8, "167": 8, "110": 36, "111": 38, "112": 38, "113": 45, "114": 46, "115": 46, "116": 46, "117": 46, "118": 46, "119": 47, "120": 48, "121": 48, "122": 48, "123": 50, "124": 58, "125": 58, "126": 59, "127": 59}}
__M_END_METADATA
"""
