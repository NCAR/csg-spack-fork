# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class LroseCore(CMakePackage):
    """The overall goal of the project is to provide high-quality, open source
    software to the community of scientists, researchers, educators, and
    operational organizations using atmospheric lidars, radars, and
    profilers."""

    homepage = "https://www.eol.ucar.edu/content/lidar-radar-open-software-environment"
    url = "https://github.com/NCAR/lrose-core/archive/lrose-core-20250105.tar.gz"
    git = "https://github.com/NCAR/lrose-core.git"

    #maintainers("jedwards4b")

    license("Apache-2.0")

    version("20250105", sha256="c91938a1fa022359d2cd3c447a1ea777c70d456344967db768b3b0d2a08bd53b")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    #variant("pnetcdf", default=False, description="enable pnetcdf")

    depends_on("cmake@3.7:", type="build")
    depends_on("libx11")
    depends_on("netcdf-c")
    depends_on("qt@5:")
    depends_on("fftw@3:")

    root_cmakelists_dir = "codebase"

    resource(
        name="lrose-displays",
        git="https://github.com/NCAR/lrose-displays",
        branch="master"
    )

    # The CMake install does not install these components, and the color_scales needed by
    # HawkEye do not come with the source code at all!
    @run_after("install")
    def add_extra_components(self):
        prefix = self.prefix
        install_tree("docs", "{}/docs".format(prefix))
        install_tree("release_notes", "{}/release_notes".format(prefix))
        install_tree("lrose-displays/color_scales", "{}/share/color_scales".format(prefix))
