# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824005.249204
_enable_loop = True
_template_filename = 'themes/carpet/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        permalink = context.get('permalink', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        page_links = context.get('page_links', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        pagekind = context.get('pagekind', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        prevlink = context.get('prevlink', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        parent = context.get('parent', UNDEFINED)
        carpet__post_type = context.get('carpet__post_type', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        def content_header():
            return render_content_header(context)
        page_links = context.get('page_links', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        pagekind = context.get('pagekind', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        def content():
            return render_content(context)
        prevlink = context.get('prevlink', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        carpet__post_type = context.get('carpet__post_type', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
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


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        posts = context.get('posts', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        permalink = context.get('permalink', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
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
{"filename": "themes/carpet/templates/index.tmpl", "source_encoding": "utf-8", "uri": "index.tmpl", "line_map": {"23": 2, "26": 3, "29": 4, "35": 0, "66": 2, "67": 3, "68": 4, "69": 5, "74": 12, "79": 84, "85": 14, "110": 14, "115": 15, "116": 16, "117": 17, "118": 17, "119": 17, "120": 19, "121": 20, "122": 20, "123": 20, "124": 22, "125": 23, "126": 24, "127": 27, "128": 27, "129": 32, "130": 32, "131": 32, "132": 32, "133": 35, "134": 36, "135": 38, "136": 38, "137": 41, "138": 41, "139": 44, "140": 45, "141": 46, "142": 47, "143": 47, "144": 49, "145": 50, "146": 51, "147": 51, "148": 54, "149": 59, "150": 60, "151": 60, "152": 60, "153": 60, "154": 60, "155": 61, "156": 62, "157": 62, "158": 62, "159": 64, "160": 67, "161": 67, "162": 68, "163": 68, "164": 68, "165": 68, "166": 68, "167": 68, "168": 71, "169": 72, "170": 72, "171": 72, "172": 74, "173": 80, "174": 81, "175": 81, "176": 82, "177": 82, "178": 83, "179": 83, "185": 7, "195": 7, "196": 8, "197": 8, "198": 9, "199": 10, "200": 10, "201": 10, "207": 15, "218": 207}}
__M_END_METADATA
"""
