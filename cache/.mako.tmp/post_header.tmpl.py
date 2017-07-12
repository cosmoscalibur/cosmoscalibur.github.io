# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824005.560074
_enable_loop = True
_template_filename = 'themes/carpet/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_sourcelink', 'html_title', 'html_post_header', 'html_translations']


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


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
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


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_sourcelink():
            return render_html_sourcelink(context)
        _link = context.get('_link', UNDEFINED)
        def html_title():
            return render_html_title(context)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        post = context.get('post', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def html_translations(post):
            return render_html_translations(context,post)
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
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"filename": "themes/carpet/templates/post_header.tmpl", "source_encoding": "utf-8", "uri": "post_header.tmpl", "line_map": {"128": 72, "129": 73, "130": 75, "131": 75, "132": 75, "133": 75, "134": 79, "135": 80, "136": 80, "137": 80, "138": 82, "139": 84, "140": 84, "175": 169, "146": 13, "23": 2, "26": 3, "155": 13, "156": 14, "29": 0, "158": 16, "159": 16, "160": 17, "161": 18, "34": 2, "35": 3, "36": 11, "37": 24, "38": 34, "39": 86, "168": 19, "169": 22, "166": 19, "45": 26, "157": 15, "52": 26, "53": 27, "54": 28, "55": 30, "56": 30, "57": 30, "58": 30, "64": 5, "70": 5, "71": 6, "72": 7, "73": 8, "74": 8, "75": 8, "76": 8, "162": 19, "82": 36, "163": 19, "164": 19, "167": 19, "165": 19, "99": 36, "100": 38, "101": 38, "102": 45, "103": 46, "104": 46, "105": 46, "106": 46, "107": 46, "108": 47, "109": 48, "110": 48, "111": 48, "112": 50, "113": 58, "114": 58, "115": 59, "116": 59, "117": 59, "118": 59, "119": 59, "120": 59, "121": 64, "122": 65, "123": 66, "124": 66, "125": 69, "126": 70, "127": 70}}
__M_END_METADATA
"""
