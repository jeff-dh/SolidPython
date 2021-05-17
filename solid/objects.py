"""
Classes for OpenSCAD builtins
"""
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, Optional, Sequence, Tuple, Union, List

from .solidpython import IncludedOpenSCADObject, OpenSCADObject

PathStr = Union[Path, str]

P2 = Tuple[float, float]
P3 = Tuple[float, float, float]
P4 = Tuple[float, float, float, float]
Vec3 = P3
Vec4 = P4
Vec34 = Union[Vec3, Vec4]
P3s = Sequence[P3]
P23 = Union[P2, P3]
Points = Sequence[P23]
Indexes = Union[Sequence[int], Sequence[Sequence[int]]]
ScadSize = Union[int, Sequence[float]]
OpenSCADObjectPlus = Union[OpenSCADObject, Sequence[OpenSCADObject]]


# ================================
# = Modifier Convenience Methods =
# ================================
def debug(openscad_obj: OpenSCADObject) -> OpenSCADObject:
    openscad_obj.set_modifier("#")
    return openscad_obj


def background(openscad_obj: OpenSCADObject) -> OpenSCADObject:
    openscad_obj.set_modifier("%")
    return openscad_obj


def root(openscad_obj: OpenSCADObject) -> OpenSCADObject:
    openscad_obj.set_modifier("!")
    return openscad_obj


def disable(openscad_obj: OpenSCADObject) -> OpenSCADObject:
    openscad_obj.set_modifier("*")
    return openscad_obj


# ===========================
# = IMPORTING OPENSCAD CODE =
# ===========================
def import_scad(scad_file_or_dir: PathStr) -> SimpleNamespace:
    '''
    Recursively look in current directory & OpenSCAD library directories for
        OpenSCAD files. Create Python mappings for all OpenSCAD modules & functions
    Return a namespace or raise ValueError if no scad files found
    '''
    scad = Path(scad_file_or_dir)
    candidates: List[Path] = [scad]
    if not scad.is_absolute():
        candidates = [d/scad for d in _openscad_library_paths()]

    for candidate_path in candidates:
        namespace = _import_scad(candidate_path)
        if namespace is not None:
            return namespace
    raise ValueError(f'Could not find .scad files at or under {scad}. \nLocations searched were: {candidates}')

def _import_scad(scad: Path) -> Optional[SimpleNamespace]:
    '''
    cases:
        single scad file:
            return a namespace populated with `use()`
        directory
            recurse into all subdirectories and *.scad files
            return namespace if scad files are underneath, otherwise None
        non-scad file:
            return None            
    '''
    namespace: Optional[SimpleNamespace] = None
    if scad.is_file() and scad.suffix == '.scad':
        namespace = SimpleNamespace()
        use(scad.absolute(), dest_namespace_dict=namespace.__dict__)
    elif scad.is_dir():
        subspaces = [(f, _import_scad(f)) for f in scad.iterdir() if f.is_dir() or f.suffix == '.scad']
        for f, subspace in subspaces:
            if subspace:
                if namespace is None:
                    namespace = SimpleNamespace()
                # Add a subspace to namespace named by the file/dir it represents
                setattr(namespace, f.stem, subspace)

    return namespace
   
def _openscad_library_paths() -> List[Path]:
    """
    Return system-dependent OpenSCAD library paths or paths defined in os.environ['OPENSCADPATH']
    """
    import platform
    import os
    import re

    paths = [Path('.')]

    user_path = os.environ.get('OPENSCADPATH')
    if user_path:
        for s in re.split(r'\s*[;:]\s*', user_path):
            paths.append(Path(s))

    default_paths = {
        'Linux':   Path.home() / '.local/share/OpenSCAD/libraries',
        'Darwin':  Path.home() / 'Documents/OpenSCAD/libraries',
        'Windows': Path('My Documents\OpenSCAD\libraries')
    }

    paths.append(default_paths[platform.system()])
    return paths

def _find_library(library_name: PathStr) -> Path:
    result = Path(library_name)

    if not result.is_absolute():
        paths = _openscad_library_paths()
        for p in paths:
            f = p / result
            # print(f'Checking {f} -> {f.exists()}')
            if f.exists():
                result = f

    return result
 
# use() & include() mimic OpenSCAD's use/include mechanics.
# -- use() makes methods in scad_file_path.scad available to be called.
# --include() makes those methods available AND executes all code in
#   scad_file_path.scad, which may have side effects.
#   Unless you have a specific need, call use().
def use(scad_file_path: PathStr, use_not_include: bool = True, dest_namespace_dict: Dict = None, builtins=False):
    """
    Opens scad_file_path, parses it for all usable calls,
    and adds them to caller's namespace.
    """
    # These functions in solidpython are used here and only here; don't pollute
    # the global namespace with them
    from .solidpython import parse_scad_callables
    from .solidpython import new_openscad_class_str
    from .solidpython import calling_module

    scad_file_path = _find_library(scad_file_path) 

    symbols_dicts = parse_scad_callables(scad_file_path)

    for sd in symbols_dicts:
        class_str = new_openscad_class_str(sd['name'], sd['args'], sd['kwargs'],
                                           scad_file_path.as_posix() if not builtins else None,
                                           use_not_include)
        # If this is called from 'include', we have to look deeper in the stack
        # to find the right module to add the new class to.
        if dest_namespace_dict is None:
            stack_depth = 2 if use_not_include else 3
            dest_namespace_dict = calling_module(stack_depth).__dict__
        try:
            exec(class_str, dest_namespace_dict)
        except Exception as e:
            classname = sd['name']
            msg = f"Unable to import SCAD module: `{classname}` from `{scad_file_path.name}`, with error: {e}"
            print(msg)

    return True

def include(scad_file_path: PathStr) -> bool:
    return use(scad_file_path, use_not_include=False)

# ====================
# = dynamic builtins =
# ====================
"""
    This block loads all the built in OpenSCAD functions (like circle, square,
    color, translate.....) from builtins.openscad file.
    I intentionally didn't use a *.scad file because it would be ignore through
    .gitignore und would be a pain to maintain (unless we remove *.scad from
    .gitignore, but that would cause a lot of generated files to show up while
    developing...). The only drawback is, that you have to setup your editor to
    also use OpenScad syntax highlighting for *.openscad files.
"""
OPENSCAD_BUILTINS_FILE = Path(__file__).absolute().parent / "builtins.openscad"

use(OPENSCAD_BUILTINS_FILE, builtins=True)

