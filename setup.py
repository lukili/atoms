from setuptools import setup, Extension, Command
from setuptools import find_packages
import numpy
import sysconfig
from Cython.Build import cythonize
import mpi4py

# debug
from Cython.Compiler.Options import _directive_defaults

_directive_defaults['linetrace'] = True
_directive_defaults['binding'] = True

modules= {
    "btom.main.base_structure":["btom/main/base_structure.pyx"],\
    "btom.main.base_atom":["btom/main/base_atom.pyx"],\
    "btom.main.atoms_container":["btom/main/atoms_container.pyx"],\
    "btom.main.base_periodic_structure":["btom/main/base_periodic_structure.pyx"],\
    "btom.cell.base_cell":['btom/cell/base_cell.pyx'],\
    "btom.cell.grid_cell":['btom/cell/grid_cell.pyx'],\
    "btom.algebra.geometry_htree":["btom/algebra/geometry_htree.pyx"],\
    "btom.algebra.structure_htree":["btom/algebra/structure_htree.pyx"],\
    "btom.algebra.periodic_htree":["btom/algebra/periodic_htree.pyx"],\
    "btom.tb.tb_atom":["btom/tb/tb_atom.pyx"],\
    "btom.tb.tb_orbital":["btom/tb/tb_orbital.pyx"],\
    "btom.tb.tb_structure":["btom/tb/tb_structure.pyx"],\
    "btom.tb.orbitals_container":["btom/tb/orbitals_container.pyx"],\
    "btom.tb.tbmodel.base_tbmodel":["btom/tb/tbmodel/base_tbmodel.pyx"],\
    "btom.tb.tbmodel.planes_graphene_model":["btom/tb/tbmodel/planes_graphene_model.pyx"],\
    "btom.tb.tbmodel.planes_bilayer_graphene_model":\
            ["btom/tb/tbmodel/planes_bilayer_graphene_model.pyx"],\
    "btom.tb.tbmodel.graphene_model":["btom/tb/tbmodel/graphene_model.pyx"],\
    "btom.tb.tbmodel.small_to_large_model":["btom/tb/tbmodel/small_to_large_model.pyx"],\
    "btom.tb.tbmodel.strain_model":["btom/tb/tbmodel/strain_model.pyx"],\
    "btom.tb.tbmodel.base_slater_koster":["btom/tb/tbmodel/base_slater_koster.pyx"],\
    "btom.tb.tbmodel.cappelluti_model":["btom/tb/tbmodel/cappelluti_model.pyx"],\
    "btom.tb.tbmodel.koshino_model":["btom/tb/tbmodel/koshino_model.pyx"],\
    "btom.tb.tbmodel.threeband_model":["btom/tb/tbmodel/threeband_model.pyx"],\
    "btom.tb.tbmodel.simple_tb_model":["btom/tb/tbmodel/simple_tb_model.pyx"],\
    "btom.tb.tbmodel.hessian_model":["btom/tb/tbmodel/hessian_model.pyx"],\
    "btom.tb.tbmodel.dynamic_model":["btom/tb/tbmodel/dynamic_model.pyx"],\
    "btom.tb.nn_wrapper":["btom/tb/nn_wrapper.pyx"],\
    "btom.tb.n_wrapper":["btom/tb/n_wrapper.pyx"],\
    "btom.calc.coulomb.coulomb":["btom/calc/coulomb/coulomb.pyx"],\
    "btom.tb.decorator.magnetic_field_decorator":["btom/tb/decorator/magnetic_field_decorator.pyx"],\
    "btom.fileIO.baseIO":["btom/fileIO/baseIO.pyx"],\
    "btom.fileIO.base_constants":["btom/fileIO/base_constants.pyx"],\
    "btom.fileIO.greensIO":["btom/fileIO/greensIO.pyx"],\
    "btom.fileIO.wannierIO":["btom/fileIO/wannierIO.pyx"],\
    "btom.fileIO.phonopyIO":["btom/fileIO/phonopyIO.pyx"],\
    "btom.calc.base_calc":["btom/calc/base_calc.pyx"],\
    "btom.calc.corrugation.koshino_field":["btom/calc/corrugation/koshino_field.pyx"],\
    "btom.calc.corrugation.bilayer_field":["btom/calc/corrugation/bilayer_field.pyx"],\
    "btom.calc.BMD.BMD":["btom/calc/BMD/BMD.pyx"]
}

extensions = [Extension(k,v,language="c++",extra_complie_args=["-std=c++11"],define_macros=[('CYTHON_TRACE', '1')]) for k,v in modules.items()]

for e in extensions:
    e.cython_directives = {"embededsignature":True,\
                           "binding":True,
                           "language_level":3}

cmodules = {
    "btom.cmain.py_base_atom":["btom/cmain/py_base_atom.pyx",\
                                "btom/cmain/c_base_atom.cpp"]
}

cextensions = cythonize([Extension(k,v,language="c++",\
                                   include_dirs=["btom/cmain",numpy.get_include()],\
                                   extra_compile_args=["-std=c++11","-DPARALLEL"])\
                         for k,v in cmodules.items()])

import os
os.environ["CFLAGS"] = " ".join([u for u in sysconfig.get_config_var("CFLAGS").split(" ") if "xHost" not in u])
os.environ["CC"] = mpi4py.get_config()["mpicc"]

setup(name="btom",
        namespace_packages=["btom"],
        version='0.1',
        url='http://notset/jet',
        author="Lukas Linhart",
        author_email="lukas.linhart@tuwien.ac.at",
        license='None',
        ext_modules =cythonize(extensions)+cextensions, #+int_modules+cextensions,\
        packages=find_packages(),\
        zip_safe=False,\
        include_package_data=True)
