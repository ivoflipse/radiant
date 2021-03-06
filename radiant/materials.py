from functools import lru_cache
import os

__all__ = ('Material', 'MeshBasicMaterial', 'MeshPhongMaterial')


@lru_cache(maxsize=None)
def load_shader_sources(key):
    """
    Load all built-in shaders from filesystem.

    Returns
    -------
    dict of dict
        Mapping of shader key to mapping of shader type to shader source.
    """
    shader_sources = {}
    shader_path = os.path.join(os.path.dirname(__file__), 'shaders')
    for filename in filter(lambda fn: fn.startswith(f"{key}."), os.listdir(shader_path)):
        _, ext = os.path.splitext(filename)
        with open(os.path.join(shader_path, filename)) as fh:
            shader_sources[ext[1:]] = fh.read()
    return shader_sources


class Material:
    def __init__(self, shaders=None, uniforms=None):
        self.shaders = shaders or {}
        self.uniforms = uniforms or {}


class MeshBasicMaterial(Material):
    def __init__(self, color=(1.0, 0.0, 0.0, 1.0)):
        super().__init__(shaders=load_shader_sources('meshbasic'), uniforms={
            'color': color
        })


class MeshPhongMaterial(Material):
    def __init__(self, color=(1.0, 0.0, 0.0, 1.0), shininess=4.0):
        super().__init__(shaders=load_shader_sources('meshphong'), uniforms={
            'color': color,
            'shininess': shininess
        })
