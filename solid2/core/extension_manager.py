
class ExtensionManager():
    def __init__(self):
        self.wrapper = []
        self.pre_render = []
        self.post_render = []
        self.access_syntax = {}

    def register_root_wrapper(self, ext):
        self.wrapper.append(ext)

    def register_pre_render(self, func):
        self.pre_render.append(func)

    def register_post_render(self, func):
        self.post_render.append(func)

    def register_access_syntax(self, fn):
        import inspect
        if fn.__name__ in self.access_syntax:
            raise Exception(f'Unable to register "{fn.__name__}" plugin, it '
                             'would overwrite an existing plugin or method.')

        if inspect.isclass(fn):
            self.access_syntax[fn.__name__] = \
                lambda y, *args, **kwargs: fn(*args, **kwargs)(y)
        else:
            self.access_syntax[fn.__name__] = fn

    def wrap_root_node(self, root):
        new_root_node = root
        for w in self.wrapper:
            new_root_node = w(new_root_node)

        return new_root_node

    def call_pre_render(self, root):
        pre_render_str = ''

        for f in self.pre_render:
            pre_render_str += f(root)

        return pre_render_str

    def call_post_render(self, root):
        post_render_str = ''

        for f in self.post_render:
            post_render_str += f(root)

        return post_render_str

    def access_syntax_lookup(self, key):
        return self.access_syntax.get(key, None)

default_extension_manager = ExtensionManager()

# expose register functions as decorators / global functions
def register_access_syntax(fn):
    default_extension_manager.register_access_syntax(fn)
    return fn

def register_pre_render(fn):
    default_extension_manager.register_pre_render(fn)
    return fn

def register_post_render(fn):
    default_extension_manager.register_post_render(fn)
    return fn

def register_root_wrapper(fn):
    default_extension_manager.register_root_wrapper(fn)
    return fn

