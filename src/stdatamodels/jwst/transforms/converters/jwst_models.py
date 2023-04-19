# Licensed under a 3-clause BSD style license - see LICENSE.rst

from asdf_astropy.converters.transform.core import TransformConverterBase


__all__ = ['Gwa2SlitConverter', 'Slit2MsaConverter', 'LogicalConverter', 'NirissSOSSConverter',
           'RefractionIndexConverter', 'MIRI_AB2SliceConverter', 'NIRCAMGrismDispersionConverter',
           'NIRISSGrismDispersionConverter', 'Rotation3DToGWAConverter', 'GratingEquationConverter',
           'V23ToSkyConverter', 'SnellConverter', 'CoordsConverter', 'Rotation3DToGWAConverter']


class NIRCAMGrismDispersionConverter(TransformConverterBase):

    tags = ["tag:stsci.edu:jwst_pipeline/nircam_grism_dispersion-*"]

    types = ["stdatamodels.jwst.transforms.models.NIRCAMForwardRowGrismDispersion",
             "stdatamodels.jwst.transforms.models.NIRCAMForwardColumnGrismDispersion",
             "stdatamodels.jwst.transforms.models.NIRCAMBackwardGrismDispersion"]

    def from_yaml_tree_transform(self, node, tag, ctx):
        from stdatamodels.jwst.transforms import models

        _fname = getattr(models, node["model_type"])
        return _fname(list(node['orders']),
                      list(node['lmodels']),
                      list(node['xmodels']),
                      list(node['ymodels']),
                      list(node['inv_lmodels']),
                      list(node['inv_xmodels']),
                      list(node['inv_ymodels']),
                      )

    def to_yaml_tree_transform(self, model, tag, ctx):
        xll = [list(m) for m in model.xmodels]
        yll = [list(m) for m in model.ymodels]
        lll = [list(m) for m in model.lmodels]
        inv_xll = [list(m) for m in model.inv_xmodels]
        inv_yll = [list(m) for m in model.inv_ymodels]
        inv_lll = [list(m) for m in model.inv_lmodels]
        node = {'orders': list(model.orders),
                'xmodels': xll,
                'ymodels': yll,
                'lmodels': lll,
                'inv_xmodels': inv_xll,
                'inv_ymodels': inv_yll,
                'inv_lmodels': inv_lll,
                'model_type': type(model).name
                }
        return node


class NIRISSGrismDispersionConverter(TransformConverterBase):

    tags = ["tag:stsci.edu:jwst_pipeline/niriss_grism_dispersion-*"]

    types = ["stdatamodels.jwst.transforms.models.NIRISSForwardRowGrismDispersion",
             "stdatamodels.jwst.transforms.models.NIRISSForwardColumnGrismDispersion",
             "stdatamodels.jwst.transforms.models.NIRISSBackwardGrismDispersion"]

    def from_yaml_tree_transform(self, node, tag, ctx):
        from stdatamodels.jwst.transforms import models

        _fname = getattr(models, node["model_type"])
        return _fname(list(node['orders']),
                      list(node['lmodels']),
                      list(node['xmodels']),
                      list(node['ymodels']),
                      node['theta'],
                      )

    def to_yaml_tree_transform(self, model, tag, ctx):
        xll = [list(m) for m in model.xmodels]
        yll = [list(m) for m in model.ymodels]
        node = {'orders': list(model.orders),
                'xmodels': xll,
                'ymodels': yll,
                'lmodels': list(model.lmodels),
                'theta': model.theta,
                'model_type': type(model).name
                }
        return node


class Gwa2SlitConverter(TransformConverterBase):

    tags = ["tag:stsci.edu:jwst_pipeline/gwa_to_slit-*"]

    types = ["stdatamodels.jwst.transforms.models.Gwa2Slit"]

    def from_yaml_tree_transform(self, node, tag, ctx):

        from stdatamodels.jwst.transforms.models import Gwa2Slit

        return Gwa2Slit(node['slits'], node['models'])

    def to_yaml_tree_transform(self, model, tag, ctx):
        node = {'slits': model._slits,
                'models': model.models}
        return node


class Slit2MsaConverter(TransformConverterBase):

    tags = ["tag:stsci.edu:jwst_pipeline/slit_to_msa-*"]

    types = ["stdatamodels.jwst.transforms.models.Slit2Msa"]

    def from_yaml_tree_transform(self, node, tag, ctx):

        from stdatamodels.jwst.transforms.models import Slit2Msa

        return Slit2Msa(node['slits'], node['models'])

    def to_yaml_tree_transform(self, model, tag, ctx):
        node = {'slits': model._slits,
                'models': model.models}
        return node


class LogicalConverter(TransformConverterBase):

    tags = ["tag:stsci.edu:jwst_pipeline/logical-*"]
    types = ["stdatamodels.jwst.transforms.models.Logical"]

    def from_yaml_tree_transform(self, node, tag, ctx):
        from stdatamodels.jwst.transforms.models import Logical

        return Logical(node['condition'], node['compareto'], node['value'])

    def to_yaml_tree_transform(self, model, tag, ctx):

        node = {'condition': model.condition,
                'compareto': model.compareto,
                'value': model.value}
        return node


class NirissSOSSConverter(TransformConverterBase):
    tags = ["tag:stsci.edu:jwst_pipeline/niriss-soss-*",
            "tag:stsci.edu:jwst_pipeline/niriss_soss-*"]
    types = ["stdatamodels.jwst.transforms.models.NirissSOSSModel"]

    def from_yaml_tree_transform(self, node, tag, ctx):

        from stdatamodels.jwst.transforms.models import NirissSOSSModel

        return NirissSOSSModel(node['spectral_orders'], node['models'])

    def to_yaml_tree_transform(self, model, tag, ctx):
        node = {'spectral_orders': list(model.models.keys()),
                'models': list(model.models.values())
                }
        return node


class RefractionIndexConverter(TransformConverterBase):
    tags = ["tag:stsci.edu:jwst_pipeline/refraction_index_from_prism-*"]
    types = ["stdatamodels.jwst.transforms.models.RefractionIndexFromPrism"]

    def from_yaml_tree_transform(self, node, tag, ctx):

        from stdatamodels.jwst.transforms.models import RefractionIndexFromPrism

        return RefractionIndexFromPrism(node['prism_angle'])

    def to_yaml_tree_transform(self, model, tag, ctx):
        node = {'prism_angle': model.prism_angle.value
                }
        return node


class MIRI_AB2SliceConverter(TransformConverterBase):
    tags = ["tag:stsci.edu:jwst_pipeline/miri_ab2slice-*"]
    types = ["stdatamodels.jwst.transforms.models.MIRI_AB2Slice"]

    def from_yaml_tree_transform(self, node, tag, ctx):
        from stdatamodels.jwst.transforms.models import MIRI_AB2Slice
        return MIRI_AB2Slice(node['beta_zero'], node['beta_del'], node['channel'])

    def to_yaml_tree_transform(self, model, tag, ctx):
        node = {'beta_zero': model.beta_zero.value,
                'beta_del': model.beta_del.value,
                'channel': model.channel.value
                }
        return node


class Rotation3DToGWAConverter(TransformConverterBase):

    tags = ["tag:stsci.edu:jwst_pipeline/rotation_sequence-*"]

    types = ["stdatamodels.jwst.transforms.models.Rotation3DToGWA"]

    def from_yaml_tree_transform(self, node, tag, ctx):
        from stdatamodels.jwst.transforms.models import Rotation3DToGWA

        angles = node['angles']
        axes_order = node['axes_order']
        return Rotation3DToGWA(angles, axes_order)

    def to_yaml_tree_transform(self, model, tag, ctx):
        node = {'angles': list(model.angles.value)}
        node['axes_order'] = model.axes_order
        return node


class GratingEquationConverter(TransformConverterBase):

    tags = ["tag:stsci.edu:jwst_pipeline/grating_equation-*"]

    types = ["stdatamodels.jwst.transforms.models.WavelengthFromGratingEquation",
             "stdatamodels.jwst.transforms.models.AngleFromGratingEquation"
             ]

    def from_yaml_tree_transform(self, node, tag, ctx):
        from stdatamodels.jwst.transforms.models import WavelengthFromGratingEquation, AngleFromGratingEquation

        groove_density = node['groove_density']
        order = node['order']
        output = node['output']
        if output == "wavelength":
            model = WavelengthFromGratingEquation(groove_density, order)
        elif output == "angle":
            model = AngleFromGratingEquation(groove_density, order)
        else:
            raise ValueError("Can't create a GratingEquation model with"
                             "output {0}".format(output))
        return model

    def to_yaml_tree_transform(self, model, tag, ctx):
        from stdatamodels.jwst.transforms.models import WavelengthFromGratingEquation, AngleFromGratingEquation

        node = {'order': model.order.value,
                'groove_density': model.groove_density.value
                }
        if isinstance(model, AngleFromGratingEquation):
            node['output'] = 'angle'
        elif isinstance(model, WavelengthFromGratingEquation):
            node['output'] = 'wavelength'
        else:
            raise TypeError("Can't serialize an instance of {0}"
                            .format(model.__class__.__name__))
        return node


class V23ToSkyConverter(TransformConverterBase):

    tags = ["tag:stsci.edu:jwst_pipeline/v23tosky-*"]

    types = ["stdatamodels.jwst.transforms.models.V23ToSky"]

    def from_yaml_tree_transform(self, node, tag, ctx):
        from stdatamodels.jwst.transforms.models import V23ToSky
        angles = node['angles']
        axes_order = node['axes_order']
        return V23ToSky(angles, axes_order=axes_order)

    def to_yaml_tree_transform(self, model, tag, ctx):
        node = {'angles': list(model.angles.value)}
        node['axes_order'] = model.axes_order
        return node


class SnellConverter(TransformConverterBase):

    tags = ["tag:stsci.edu:jwst_pipeline/snell-*"]

    types = ["stdatamodels.jwst.transforms.models.Snell"]

    def from_yaml_tree_transform(self, node, tag, ctx):
        from stdatamodels.jwst.transforms.models import Snell
        return Snell(node['prism_angle'], node['kcoef'], node['lcoef'], node['tcoef'],
                     node['ref_temp'], node['ref_pressure'], node['temp'], node['pressure'])

    def to_yaml_tree_transform(self, model, tag, ctx):
        node = {'prism_angle': model.prism_angle,
                'kcoef': model.kcoef.tolist(),
                'lcoef': model.lcoef.tolist(),
                'tcoef': model.tcoef.tolist(),
                'ref_temp': model.tref,
                'ref_pressure': model.pref,
                'temp': model.temp,
                'pressure': model.pressure
                }
        return node


class CoordsConverter(TransformConverterBase):

    tags = ["tag:stsci.edu:jwst_pipeline/coords-*"]

    types = ["stdatamodels.jwst.transforms.models.Unitless2DirCos",
             "stdatamodels.jwst.transforms.models.DirCos2Unitless"]

    def from_yaml_tree_transform(self, node, tag, ctx):
        from stdatamodels.jwst.transforms.models import Unitless2DirCos, DirCos2Unitless

        model_type = node['model_type']
        if model_type in ('to_dircos', 'unitless2directional'):
            return Unitless2DirCos()
        elif model_type in ('from_dircos', 'directional2unitless'):
            return DirCos2Unitless()
        else:
            raise TypeError("Unknown model_type")

    def to_yaml_tree_transform(self, model, tag, ctx):
        from stdatamodels.jwst.transforms.models import Unitless2DirCos, DirCos2Unitless

        if isinstance(model, DirCos2Unitless):
            model_type = 'directional2unitless'
        elif isinstance(model, Unitless2DirCos):
            model_type = 'unitless2directional'
        else:
            raise TypeError("Model of type {0} i snot supported."
                            .format(model.__class__))
        node = {'model_type': model_type}
        return node
