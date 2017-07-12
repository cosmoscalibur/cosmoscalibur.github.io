# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824719.68044
_enable_loop = True
_template_filename = 'themes/carpet/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'html_hero_body', 'content']



import re
def lower(text):
  # remove all non-alphabet chars from string
  regex = re.compile('[^a-zA-Z0-9]')
  result = regex.sub('', text)
  return result.lower()


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

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        title = context.get('title', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        def content():
            return render_content(context._locals(__M_locals))
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        carpet__hero_post_title = context.get('carpet__hero_post_title', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        enable_comments = context.get('enable_comments', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        post = context.get('post', UNDEFINED)
        def html_hero_body():
            return render_html_hero_body(context._locals(__M_locals))
        pheader = _mako_get_namespace(context, 'pheader')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'html_hero_body'):
            context['self'].html_hero_body(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n  \n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        __M_writer('  \n')
        if post.description():
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(post.description())))
            __M_writer('">\n')
        __M_writer('  \n  <meta name="author" content="')
        __M_writer(filters.html_escape(str(post.author())))
        __M_writer('">\n  \n')
        if post.prev_post:
            __M_writer('    <link rel="prev" href="')
            __M_writer(str(post.prev_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('" type="text/html">\n')
        __M_writer('  \n')
        if post.next_post:
            __M_writer('    <link rel="next" href="')
            __M_writer(str(post.next_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('" type="text/html">\n')
        __M_writer('  \n')
        if post.is_draft:
            __M_writer('    <meta name="robots" content="noindex">\n')
        __M_writer('  \n  ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n  ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n  ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_hero_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_hero_body():
            return render_html_hero_body(context)
        carpet__hero_post_title = context.get('carpet__hero_post_title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if not carpet__hero_post_title:
            __M_writer('  ')
            __M_writer(str(parent.html_hero_body()))
            __M_writer('\n')
        elif post.meta('show-hero') == 'custom':
            if title:
                __M_writer('    <div class="hero-body hero-')
                __M_writer(filters.trim(filters.html_escape(lower(str(title)))))
                __M_writer('">\n')
            else:
                __M_writer('    <div class="hero-body hero-')
                __M_writer(filters.trim(filters.html_escape(lower(str(title)))))
                __M_writer(' ')
                __M_writer(str(post.meta('hero-class')))
                __M_writer('">\n')
            if post.meta('hero-title') or post.meta('hero-description'):
                __M_writer('  <div class="container has-text-centered">\n')
                if post.meta('hero-title'):
                    __M_writer('      <p class="title">')
                    __M_writer(filters.html_escape(str(post.meta('hero-title'))))
                    __M_writer('</p>\n')
                if post.meta('hero-description'):
                    __M_writer('      <p class="subtitle">')
                    __M_writer(filters.html_escape(str(post.meta('hero-description'))))
                    __M_writer('</p>\n')
                __M_writer('  </div>\n')
            __M_writer('  </div>\n')
        elif post.meta('show-hero'):
            if title:
                __M_writer('    <div class="hero-body hero-')
                __M_writer(filters.trim(filters.html_escape(lower(str(title)))))
                __M_writer('">\n')
            else:
                __M_writer('    <div class="hero-body hero-')
                __M_writer(filters.trim(filters.html_escape(lower(str(title)))))
                __M_writer(' ')
                __M_writer(str(post.meta('hero-class')))
                __M_writer('">\n')
            if post.meta('title') or post.meta('description'):
                __M_writer('  <div class="container has-text-centered">\n')
                if post.meta('title'):
                    __M_writer('      <p class="title">')
                    __M_writer(filters.html_escape(str(post.meta('title'))))
                    __M_writer('</p>\n')
                if post.meta('description'):
                    __M_writer('      <p class="subtitle">')
                    __M_writer(filters.html_escape(str(post.meta('description'))))
                    __M_writer('</p>\n')
                __M_writer('  </div>\n')
            __M_writer('  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context)
        helper = _mako_get_namespace(context, 'helper')
        comments = _mako_get_namespace(context, 'comments')
        pheader = _mako_get_namespace(context, 'pheader')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="post-')
        __M_writer(str(post.meta('type')))
        __M_writer(' h-entry hentry postpage" itemscope="itemscope" itemtype="http://schema.org/Article">\n  ')
        __M_writer(str(pheader.html_post_header()))
        __M_writer('\n  <div class="section content e-content entry-content" itemprop="articleBody text">\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n  </div>\n  <aside class="postpromonav">\n    ')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n  </aside>\n')
        if site_has_comments and enable_comments and not post.meta('nocomments'):
            __M_writer('    <section class="section comments hidden-print">\n      <h2 class="title is-2">')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\n      ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n    </section>\n')
        __M_writer('  ')
        __M_writer(str(helper.mathjax_script(post)))
        __M_writer('\n</article>\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 6, "32": 4, "35": 2, "38": 3, "44": 0, "65": 2, "66": 3, "67": 4, "68": 5, "69": 13, "74": 42, "79": 82, "84": 103, "90": 14, "99": 14, "100": 15, "101": 15, "102": 17, "103": 18, "104": 18, "105": 18, "106": 20, "107": 21, "108": 22, "109": 22, "110": 22, "111": 24, "112": 25, "113": 25, "114": 27, "115": 28, "116": 28, "117": 28, "118": 28, "119": 28, "120": 30, "121": 31, "122": 32, "123": 32, "124": 32, "125": 32, "126": 32, "127": 34, "128": 35, "129": 36, "130": 38, "131": 39, "132": 39, "133": 40, "134": 40, "135": 41, "136": 41, "142": 44, "152": 44, "153": 45, "154": 46, "155": 46, "156": 46, "157": 47, "158": 48, "159": 49, "160": 49, "161": 49, "162": 50, "163": 51, "164": 51, "165": 51, "166": 51, "167": 51, "168": 53, "169": 54, "170": 55, "171": 56, "172": 56, "173": 56, "174": 58, "175": 59, "176": 59, "177": 59, "178": 61, "179": 63, "180": 64, "181": 65, "182": 66, "183": 66, "184": 66, "185": 67, "186": 68, "187": 68, "188": 68, "189": 68, "190": 68, "191": 70, "192": 71, "193": 72, "194": 73, "195": 73, "196": 73, "197": 75, "198": 76, "199": 76, "200": 76, "201": 78, "202": 80, "208": 84, "221": 84, "222": 85, "223": 85, "224": 86, "225": 86, "226": 88, "227": 88, "228": 91, "229": 91, "230": 92, "231": 92, "232": 94, "233": 95, "234": 96, "235": 96, "236": 97, "237": 97, "238": 100, "239": 100, "240": 100, "241": 102, "242": 102, "248": 242}, "filename": "themes/carpet/templates/post.tmpl", "uri": "post.tmpl"}
__M_END_METADATA
"""
