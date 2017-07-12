# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824593.9049115
_enable_loop = True
_template_filename = 'themes/carpet/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_hero_body', 'content', 'extra_head']



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
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        enable_comments = context.get('enable_comments', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        def html_hero_body():
            return render_html_hero_body(context._locals(__M_locals))
        messages = context.get('messages', UNDEFINED)
        carpet__hero_post_title = context.get('carpet__hero_post_title', UNDEFINED)
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


def render_html_hero_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_hero_body():
            return render_html_hero_body(context)
        carpet__hero_post_title = context.get('carpet__hero_post_title', UNDEFINED)
        title = context.get('title', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        post = context.get('post', UNDEFINED)
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
        enable_comments = context.get('enable_comments', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
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


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        helper = _mako_get_namespace(context, 'helper')
        def extra_head():
            return render_extra_head(context)
        parent = context.get('parent', UNDEFINED)
        post = context.get('post', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"line_map": {"16": 6, "32": 2, "35": 4, "38": 3, "44": 0, "65": 2, "66": 3, "67": 4, "68": 5, "69": 13, "74": 42, "79": 82, "84": 103, "90": 44, "100": 44, "101": 45, "102": 46, "103": 46, "104": 46, "105": 47, "106": 48, "107": 49, "108": 49, "109": 49, "110": 50, "111": 51, "112": 51, "113": 51, "114": 51, "115": 51, "116": 53, "117": 54, "118": 55, "119": 56, "120": 56, "121": 56, "122": 58, "123": 59, "124": 59, "125": 59, "126": 61, "127": 63, "128": 64, "129": 65, "130": 66, "131": 66, "132": 66, "133": 67, "134": 68, "135": 68, "136": 68, "137": 68, "138": 68, "139": 70, "140": 71, "141": 72, "142": 73, "143": 73, "144": 73, "145": 75, "146": 76, "147": 76, "148": 76, "149": 78, "150": 80, "156": 84, "169": 84, "170": 85, "171": 85, "172": 86, "173": 86, "174": 88, "175": 88, "176": 91, "177": 91, "178": 92, "179": 92, "180": 94, "181": 95, "182": 96, "183": 96, "184": 97, "185": 97, "186": 100, "187": 100, "188": 100, "189": 102, "190": 102, "196": 14, "205": 14, "206": 15, "207": 15, "208": 17, "209": 18, "210": 18, "211": 18, "212": 20, "213": 21, "214": 22, "215": 22, "216": 22, "217": 24, "218": 25, "219": 25, "220": 27, "221": 28, "222": 28, "223": 28, "224": 28, "225": 28, "226": 30, "227": 31, "228": 32, "229": 32, "230": 32, "231": 32, "232": 32, "233": 34, "234": 35, "235": 36, "236": 38, "237": 39, "238": 39, "239": 40, "240": 40, "241": 41, "242": 41, "248": 242}, "filename": "themes/carpet/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
