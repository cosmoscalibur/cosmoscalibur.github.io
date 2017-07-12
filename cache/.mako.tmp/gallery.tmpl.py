# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824172.816931
_enable_loop = True
_template_filename = 'themes/carpet/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head', 'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        loop = __M_loop = runtime.LoopStack()
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        loop = __M_loop = runtime.LoopStack()
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        def content():
            return render_content(context)
        ui = _mako_get_namespace(context, 'ui')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\n\n')
        if title:
            __M_writer('  <h1 class="title is-1">')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        if post:
            __M_writer('  <div class="columns">\n    <div class="column content gallery-post">\n      ')
            __M_writer(str(post.text()))
            __M_writer('\n    </div>\n  </div>\n')
        if folders:
            __M_writer('<div class="columns is-multiline gallery-folders">\n')
            for folder, ftitle in folders:
                __M_writer('    <div class="column is-2 gallery-folder">\n      <div class="card">\n        <div class="card-image">\n          <figure class="image is-square gallery-folder-image"></figure>\n        </div>\n        <div class="card-content">\n          <a title="')
                __M_writer(filters.html_escape(str(ftitle)))
                __M_writer('" href="')
                __M_writer(str(folder))
                __M_writer('">')
                __M_writer(filters.html_escape(str(ftitle)))
                __M_writer('</a>\n        </div>\n      </div>\n    </div>\n')
            __M_writer('</div>\n')
        if photo_array:
            __M_writer('<div class="columns is-multiline gallery-photos">\n')
            loop = __M_loop._enter(photo_array)
            try:
                for image in loop:
                    __M_writer('    <div class="column is-2 gallery-photo">\n      <div class="card gallery-card">\n        <div class="card-image">\n          <figure class="image">\n            <img src="')
                    __M_writer(str(image['url_thumb']))
                    __M_writer('" alt="')
                    __M_writer(filters.html_escape(str(image['title'])))
                    __M_writer('" />\n          </figure>\n        </div>\n        <div class="card-content">\n          <p class="title is-4">')
                    __M_writer(filters.html_escape(str(image['title'])))
                    __M_writer('</p>\n        </div>\n        <footer class="card-footer">\n          <a class="card-footer-item image-button" data-target="photo-array-')
                    __M_writer(str(loop.index))
                    __M_writer('">View</a>\n        </footer>\n      </div>\n      <div id="photo-array-')
                    __M_writer(str(loop.index))
                    __M_writer('" class="modal">\n        <div class="modal-background"></div>\n        <div class="modal-content">\n          <p class="image">\n            <img src="')
                    __M_writer(str(image['url']))
                    __M_writer('">\n          </p>\n        </div>\n        <button class="modal-close image-close" data-target="photo-array-')
                    __M_writer(str(loop.index))
                    __M_writer('"></button>\n      </div>\n    </div>\n')
            finally:
                loop = __M_loop._exit()
            __M_writer('</div>\n<script type="text/javascript">\nvar handleClick = function(event) {\n  var attribute = this.getAttribute(\'data-target\');\n  var myModal = document.getElementById(attribute);\n  var className = \' \' + myModal.className + \' \';\n  var IS_ACTIVE_CLASS = \'is-active\';\n  if ( ~className.indexOf(\' \' + IS_ACTIVE_CLASS + \' \') ) {\n    myModal.className = className.replace(\' \' + IS_ACTIVE_CLASS + \' \', \' \');\n  } else {\n    myModal.className += \' \' + IS_ACTIVE_CLASS;\n  }\n};\nfunction addEventListenerByClass(className, event, fn) {\n  var list = document.getElementsByClassName(className);\n  for (var i = 0, len = list.length; i < len; i++) {\n      list[i].addEventListener(event, fn, false);\n  }\n}\naddEventListenerByClass(\'image-button\', \'click\', handleClick);\naddEventListenerByClass(\'image-close\', \'click\', handleClick); \n</script>\n')
        __M_writer('\n')
        if site_has_comments and enable_comments:
            __M_writer('<section class="comments">\n  <h2 class="title is-2">')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\n  ')
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/carpet/templates/gallery.tmpl", "source_encoding": "utf-8", "uri": "gallery.tmpl", "line_map": {"128": 39, "129": 43, "130": 43, "131": 43, "132": 43, "133": 47, "134": 47, "135": 50, "136": 50, "137": 53, "138": 53, "139": 57, "140": 57, "141": 60, "142": 60, "145": 64, "146": 87, "147": 88, "148": 89, "149": 90, "150": 90, "23": 4, "152": 91, "26": 3, "158": 95, "32": 0, "167": 95, "168": 96, "169": 96, "151": 91, "175": 5, "58": 2, "59": 3, "60": 4, "65": 5, "70": 93, "75": 98, "81": 7, "188": 175, "101": 7, "102": 8, "103": 8, "104": 10, "105": 11, "106": 11, "107": 11, "108": 13, "109": 14, "110": 16, "111": 16, "112": 20, "113": 21, "114": 22, "115": 23, "116": 29, "117": 29, "118": 29, "119": 29, "120": 29, "121": 29, "122": 34, "123": 36, "124": 37, "125": 38}}
__M_END_METADATA
"""
