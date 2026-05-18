from types import SimpleNamespace
from typing import NamedTuple
import inspect

from .utils import resolve_scad_filename, escape_openscad_identifier
from .parse_scad import get_scad_file_as_dict

# ===========================
# = IMPORTING OPENSCAD CODE =
# ===========================
module_cache_by_resolved_filename = {}
extra_scad_includes = []


class ScadImport(NamedTuple):
    resolved_scad: str
    original: str
    new_namespace_dict: dict
    use_not_include: bool
    skip_render: bool
    relative: str

def check_module_cache(resolved_scad, use_not_include):
    global module_cache_by_resolved_filename

    #check the module cache for the requested module
    if resolved_scad in module_cache_by_resolved_filename.keys():
        cache_entry = module_cache_by_resolved_filename[resolved_scad]

        #if this is a include call and the module was only used until now
        #set the "use/include" flag in the module cache
        if not use_not_include and cache_entry.use_not_include:
            cache_entry.use_not_include = False

        return cache_entry.new_namespace_dict

    return None

def update_module_cache(resolved_scad, original, new_namespace_dict, use_not_include, skip_render, relative):
    global module_cache_by_resolved_filename
    module_cache_by_resolved_filename[resolved_scad] = \
                                        ScadImport(resolved_scad, original, new_namespace_dict, use_not_include, skip_render, relative)

def load_scad_file_into_dict(resolved_scad, original, dest_namespace_dict, use_not_include, skip_render, relative):
    #check the cache
    cached_dict = check_module_cache(resolved_scad, use_not_include)
    if cached_dict:
        dest_namespace_dict.update(cached_dict)
        return

    #otherwise parse the file
    new_namespace_dict = get_scad_file_as_dict(resolved_scad)
    dest_namespace_dict.update(new_namespace_dict)

    #and update the cache
    update_module_cache(resolved_scad, original, new_namespace_dict, use_not_include, skip_render, relative)

def load_scad_dir_into_dict(resolved_scad, original, dest_namespace_dict, use_not_include, skip_render, relative):
    assert(resolved_scad.is_dir())

    #for each file in the dir
    for f in resolved_scad.iterdir():
        #skip non .scad files
        if f.is_file() and f.suffix != ".scad":
            continue

        #load it
        subspace = ExpSolidNamespace(f)
        load_scad_file_or_dir_into_dict(f, original, subspace.__dict__, use_not_include, skip_render)

        #and add it to the dest_namespace_dict
        identifier = escape_openscad_identifier(f.stem)
        dest_namespace_dict[identifier] = subspace

def load_scad_file_or_dir_into_dict(filename, dest_namespace_dict, use_not_include, skip_render, relative):
    assert(dest_namespace_dict != None)

    resolved_scad = resolve_scad_filename(filename)

    if not resolved_scad or not resolved_scad.exists():
        raise ValueError(f'Could not find .scad file {filename}.')

    if resolved_scad.is_file():
        load_scad_file_into_dict(resolved_scad,
                                 filename,
                                 dest_namespace_dict,
                                 use_not_include,
                                 skip_render,
                                 relative)
    elif resolved_scad.is_dir():
        load_scad_dir_into_dict(resolved_scad,
                                filename,
                                dest_namespace_dict,
                                use_not_include,
                                skip_render,
                                relative)

# use() & include() mimic OpenSCAD's use/include mechanics.
# -- use() makes methods in scad_file_path.scad available to be called.
# -- include() makes those methods available AND executes all code in
#    scad_file_path.scad, which may have side effects.
#    Unless you have a specific need, call use().
def get_callers_namespace_dict(depth=2):
    frame = inspect.currentframe()
    for _ in range(depth):
        assert(frame)
        frame = frame.f_back

    assert(frame)
    if frame.f_code.co_name == "<module>":
        return frame.f_locals
    else:
        raise Exception("use & include can not be used inside a function!\n" +\
              "they would polute the modules namespace and only if executed. This\n" +\
              "has strange side effects! Use them on module level.\n")

def use(filename, skip_render=False, render_relative=False):
    load_scad_file_or_dir_into_dict(filename, get_callers_namespace_dict(), True, skip_render, render_relative)

def include(filename, skip_render=False, render_relative=False):
    load_scad_file_or_dir_into_dict(filename, get_callers_namespace_dict(), False, skip_render, render_relative)

def import_scad(filename, dest_namespace=None, use_not_include=True, skip_render=False, render_relative=False):
    if dest_namespace == None:
        dest_namespace = ExpSolidNamespace(filename)

    load_scad_file_or_dir_into_dict(filename, dest_namespace.__dict__, use_not_include, skip_render, render_relative)

    return dest_namespace

def extra_scad_include(filename, use_not_include=True):
    global extra_scad_includes
    extra_scad_includes.append((filename, use_not_include))

# ========================
# = our helper namespace =
# ========================
class ExpSolidNamespace(SimpleNamespace):
    """
    we create our own namespace class for imported openscad modules to be able
    to overwrite the __repr__ func. This enables in a python shell

        s = import_scad("...")
        print(s)

    to list the "contents" of this namespace
    """
    def __init__(self, filename):
        super().__init__()
        self.__filename__ = filename

    def __repr__(self):
        node_strings = []
        for k in sorted(self.__dict__):
            if not k.startswith("__"):
                i = self.__dict__[k]
                if isinstance(i, ExpSolidNamespace):
                    node_strings += [f'\t{k}']
                else:
                    node_strings += [f'\t{i.__doc__}']

        return '\n'.join([f'{self.__filename__}:'] + node_strings)

