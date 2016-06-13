# -*- python -*-
#
#       Copyright 2015 INRIA - CIRAD - INRA
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
# ==============================================================================
"""
===============
Segmentation 3D
===============

.. currentmodule:: alinea.phenomenal.segmentation_3d


Segmentation
============

.. automodule:: alinea.phenomenal.segmentation_3d.segmentation
.. currentmodule:: alinea.phenomenal.segmentation_3d

.. autosummary::
   :toctree: generated/

    maize_segmentation

Graph
=====

.. automodule:: alinea.phenomenal.segmentation_3d.graph
.. currentmodule:: alinea.phenomenal.segmentation_3d

.. autosummary::
   :toctree: generated/

    create_graph
    add_nodes

Peak Detect
===========
.. automodule:: alinea.phenomenal.segmentation_3d.peakdetect
.. currentmodule:: alinea.phenomenal.segmentation_3d

.. autosummary::
   :toctree: generated/

    peakdetect


Thinning
========

.. automodule:: alinea.phenomenal.segmentation_3d.thinning
.. currentmodule:: alinea.phenomenal.segmentation_3d

.. autosummary::
   :toctree: generated/

    thinning_3d

"""

from .graph import *
from .peakdetect import *
from .thinning import *
from .segmentation import *
