# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499824719.9458945
_enable_loop = True
_template_filename = 'themes/carpet/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'sourcelink']


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
        comments = _mako_get_namespace(context, 'comments')
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        ui = _mako_get_namespace(context, 'ui')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
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


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def extra_head():
            return render_extra_head(context)
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        loop = __M_loop = runtime.LoopStack()
        comments = _mako_get_namespace(context, 'comments')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def content():
            return render_content(context)
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
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
{"source_encoding": "utf-8", "line_map": {"128": 16, "129": 20, "130": 21, "131": 22, "132": 23, "133": 29, "134": 29, "135": 29, "136": 29, "137": 29, "138": 29, "139": 34, "140": 36, "141": 37, "142": 38, "145": 39, "146": 43, "147": 43, "148": 43, "149": 43, "150": 47, "23": 4, "152": 50, "153": 50, "26": 3, "155": 53, "156": 57, "154": 53, "158": 60, "159": 60, "32": 0, "162": 64, "163": 87, "164": 88, "165": 89, "166": 90, "167": 90, "168": 91, "169": 91, "151": 47, "157": 57, "58": 2, "59": 3, "60": 4, "65": 5, "175": 5, "70": 93, "75": 98, "81": 95, "90": 95, "91": 96, "92": 96, "98": 7, "188": 175, "118": 7, "119": 8, "120": 8, "121": 10, "122": 11, "123": 11, "124": 11, "125": 13, "126": 14, "127": 16}, "filename": "themes/carpet/templates/gallery.tmpl", "uri": "gallery.tmpl"}
__M_END_METADATA
"""
