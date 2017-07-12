# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824173.1030781
_enable_loop = True
_template_filename = 'themes/carpet/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head', 'html_hero_body']



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
    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        messages = context.get('messages', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        parent = context.get('parent', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def html_hero_body():
            return render_html_hero_body(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        title = context.get('title', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        carpet__hero_post_title = context.get('carpet__hero_post_title', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = context.get('enable_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = context.get('enable_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
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
        post = context.get('post', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
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
        title = context.get('title', UNDEFINED)
        carpet__hero_post_title = context.get('carpet__hero_post_title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        def html_hero_body():
            return render_html_hero_body(context)
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


"""
__M_BEGIN_METADATA
{"filename": "themes/carpet/templates/post.tmpl", "source_encoding": "utf-8", "uri": "post.tmpl", "line_map": {"16": 6, "32": 3, "35": 4, "38": 2, "44": 0, "65": 2, "66": 3, "67": 4, "68": 5, "69": 13, "74": 42, "79": 82, "84": 103, "90": 84, "103": 84, "104": 85, "105": 85, "106": 86, "107": 86, "108": 88, "109": 88, "110": 91, "111": 91, "112": 92, "113": 92, "114": 94, "115": 95, "116": 96, "117": 96, "118": 97, "119": 97, "120": 100, "121": 100, "122": 100, "123": 102, "124": 102, "130": 14, "139": 14, "140": 15, "141": 15, "142": 17, "143": 18, "144": 18, "145": 18, "146": 20, "147": 21, "148": 22, "149": 22, "150": 22, "151": 24, "152": 25, "153": 25, "154": 27, "155": 28, "156": 28, "157": 28, "158": 28, "159": 28, "160": 30, "161": 31, "162": 32, "163": 32, "164": 32, "165": 32, "166": 32, "167": 34, "168": 35, "169": 36, "170": 38, "171": 39, "172": 39, "173": 40, "174": 40, "175": 41, "176": 41, "182": 44, "192": 44, "193": 45, "194": 46, "195": 46, "196": 46, "197": 47, "198": 48, "199": 49, "200": 49, "201": 49, "202": 50, "203": 51, "204": 51, "205": 51, "206": 51, "207": 51, "208": 53, "209": 54, "210": 55, "211": 56, "212": 56, "213": 56, "214": 58, "215": 59, "216": 59, "217": 59, "218": 61, "219": 63, "220": 64, "221": 65, "222": 66, "223": 66, "224": 66, "225": 67, "226": 68, "227": 68, "228": 68, "229": 68, "230": 68, "231": 70, "232": 71, "233": 72, "234": 73, "235": 73, "236": 73, "237": 75, "238": 76, "239": 76, "240": 76, "241": 78, "242": 80, "248": 242}}
__M_END_METADATA
"""
