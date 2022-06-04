
class ExtensionManager():
    def __init__(self):
        self.wrapper = []
        self.pre_render = []
        self.post_render = []

    def register_root_wrapper(self, ext):
        self.wrapper.append(ext)

    def register_pre_render(self, func):
        self.pre_render.append(func)

    def register_post_render(self, func):
        self.post_render.append(func)

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

default_extension_manager = ExtensionManager()

