# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824719.8371973
_enable_loop = True
_template_filename = 'themes/carpet/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        comments = _mako_get_namespace(context, 'comments')
        _link = context.get('_link', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        index_teasers = context.get('index_teasers', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        nextlink = context.get('nextlink', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        carpet__post_type = context.get('carpet__post_type', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

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
        parent = context.get('parent', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        index_file = context.get('index_file', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('  <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        comments = _mako_get_namespace(context, 'comments')
        _link = context.get('_link', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        def content_header():
            return render_content_header(context)
        nextlink = context.get('nextlink', UNDEFINED)
        def content():
            return render_content(context)
        helper = _mako_get_namespace(context, 'helper')
        carpet__post_type = context.get('carpet__post_type', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('  ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        if page_links:
            __M_writer('  ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        __M_writer('<div class="postindex">\n')
        for post in posts:
            __M_writer('    <div class="columns">\n      <div class="column">\n        <div class="card post-card">\n          <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('">\n            <div class="card-content">\n              <div class="media metadata">\n                <div class="media-content">\n                  <p class="title is-2 p-name entry-title">\n                    <a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a>\n                  </p>\n                </div>\n')
            if carpet__post_type:
                __M_writer('                  <div class="media-right">\n                    <span class="icon">\n                      <i class="fa ')
                __M_writer(str(carpet__post_type[post.meta('type')]))
                __M_writer('"\n                        aria-hidden="true"></i>\n                    </span>\n                    <span class="visuallyhidden">')
                __M_writer(str(post.meta('type')))
                __M_writer('</span>\n                  </div>\n')
            __M_writer('              </div>\n')
            if index_teasers:
                __M_writer('                <div class="content p-summary entry-summary">\n                  ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n                </div>\n')
            else:
                __M_writer('                <div class="content e-content entry-content">\n                  ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n                </div>\n')
            __M_writer('            </div>\n\n            <footer class="card-footer">\n              <p class="card-footer-item byline author vcard">\n                <span class="byline-name fn">\n')
            if author_pages_generated:
                __M_writer('                    <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                    ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('                </span>\n              </p>\n              <p class="card-footer-item dateline">\n                <a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark">\n                  <time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time>\n                </a>\n              </p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="card-footer-item commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('</p>\n')
            __M_writer('            </footer>\n          </article>\n        </div>\n      </div>\n    </div>\n')
        __M_writer('</div>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"23": 4, "26": 3, "29": 2, "35": 0, "66": 2, "67": 3, "68": 4, "69": 5, "74": 12, "79": 84, "85": 7, "95": 7, "96": 8, "97": 8, "98": 9, "99": 10, "100": 10, "101": 10, "107": 14, "132": 14, "137": 15, "138": 16, "139": 17, "140": 17, "141": 17, "142": 19, "143": 20, "144": 20, "145": 20, "146": 22, "147": 23, "148": 24, "149": 27, "150": 27, "151": 32, "152": 32, "153": 32, "154": 32, "155": 35, "156": 36, "157": 38, "158": 38, "159": 41, "160": 41, "161": 44, "162": 45, "163": 46, "164": 47, "165": 47, "166": 49, "167": 50, "168": 51, "169": 51, "170": 54, "171": 59, "172": 60, "173": 60, "174": 60, "175": 60, "176": 60, "177": 61, "178": 62, "179": 62, "180": 62, "181": 64, "182": 67, "183": 67, "184": 68, "185": 68, "186": 68, "187": 68, "188": 68, "189": 68, "190": 71, "191": 72, "192": 72, "193": 72, "194": 74, "195": 80, "196": 81, "197": 81, "198": 82, "199": 82, "200": 83, "201": 83, "207": 15, "218": 207}, "filename": "themes/carpet/templates/index.tmpl", "uri": "index.tmpl"}
__M_END_METADATA
"""
