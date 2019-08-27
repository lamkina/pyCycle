import numpy as np

from pycycle.maps.map_data import MapData

"""Python version of lpt2269.map Turbine map from NPSS"""

LPT2269 = MapData()


# Map design point values
LPT2269.defaults = {}
LPT2269.defaults['alphaMap'] = 1.0
LPT2269.defaults['NpMap'] = 100.0
LPT2269.defaults['PRmap'] = 6.0          # Design Pressure Ratio
#effMapDes = 0.9276   # = effMap for no scaling

LPT2269.alphaMap = np.array([1.0, 2.0])
LPT2269.NpMap = np.array([60., 70.0, 80.0, 90.0, 100., 110., 120.])
LPT2269.PRmap = np.array([ 3.00, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25, 7.5, 8.0])

LPT2269.effMap = np.array([[[0.8388,  0.8309,  0.8234,  0.8159,  0.8091,  0.8030,  0.7975, 0.7924,  0.7876,  0.7832,  0.7791,  0.7753,  0.7717,  0.7684, 0.7652,  0.7623,  0.7595,  0.7568,  0.7542,  0.7495],
                    [0.8878,  0.8813,  0.8745,  0.8685,  0.8629,  0.8577,  0.8528, 0.8484,  0.8443,  0.8404,  0.8368,  0.8334,  0.8302,  0.8272, 0.8242,  0.8210,  0.8179,  0.8150,  0.8122,  0.8071],
                    [0.9201,  0.9152,  0.9105,  0.9061,  0.9018,  0.8978,  0.8940, 0.8905,  0.8872,  0.8840,  0.8810,  0.8776,  0.8741,  0.8707, 0.8676,  0.8646,  0.8618,  0.8590,  0.8565,  0.8516],
                    [0.9381,  0.9360,  0.9336,  0.9310,  0.9283,  0.9257,  0.9231, 0.9206,  0.9182,  0.9153,  0.9119,  0.9087,  0.9056,  0.9027, 0.8999,  0.8973,  0.8948,  0.8924,  0.8901,  0.8858],
                    [0.9447,  0.9455,  0.9456,  0.9450,  0.9440,  0.9429,  0.9417, 0.9404,  0.9383,  0.9355,  0.9327,  0.9301,  0.9276,  0.9252, 0.9229,  0.9207,  0.9186,  0.9165,  0.9146,  0.9099],
                    [0.9415,  0.9454,  0.9479,  0.9495,  0.9504,  0.9510,  0.9512, 0.9511,  0.9492,  0.9472,  0.9452,  0.9433,  0.9414,  0.9396, 0.9378,  0.9361,  0.9344,  0.9326,  0.9304,  0.9262],
                    [0.9295,  0.9366,  0.9419,  0.9458,  0.9487,  0.9509,  0.9526, 0.9538,  0.9528,  0.9517,  0.9505,  0.9493,  0.9481,  0.9468, 0.9456,  0.9444,  0.9432,  0.9413,  0.9395,  0.9360]],
                    [[0.8388,  0.8309,  0.8234,  0.8159,  0.8091,  0.8030,  0.7975, 0.7924,  0.7876,  0.7832,  0.7791,  0.7753,  0.7717,  0.7684, 0.7652,  0.7623,  0.7595,  0.7568,  0.7542,  0.7495],
                    [0.8878,  0.8813,  0.8745,  0.8685,  0.8629,  0.8577,  0.8528, 0.8484,  0.8443,  0.8404,  0.8368,  0.8334,  0.8302,  0.8272, 0.8242,  0.8210,  0.8179,  0.8150,  0.8122,  0.8071],
                    [0.9201,  0.9152,  0.9105,  0.9061,  0.9018,  0.8978,  0.8940, 0.8905,  0.8872,  0.8840,  0.8810,  0.8776,  0.8741,  0.8707, 0.8676,  0.8646,  0.8618,  0.8590,  0.8565,  0.8516],
                    [0.9381,  0.9360,  0.9336,  0.9310,  0.9283,  0.9257,  0.9231, 0.9206,  0.9182,  0.9153,  0.9119,  0.9087,  0.9056,  0.9027, 0.8999,  0.8973,  0.8948,  0.8924,  0.8901,  0.8858],
                    [0.9447,  0.9455,  0.9456,  0.9450,  0.9440,  0.9429,  0.9417, 0.9404,  0.9383,  0.9355,  0.9327,  0.9301,  0.9276,  0.9252, 0.9229,  0.9207,  0.9186,  0.9165,  0.9146,  0.9099],
                    [0.9415,  0.9454,  0.9479,  0.9495,  0.9504,  0.9510,  0.9512, 0.9511,  0.9492,  0.9472,  0.9452,  0.9433,  0.9414,  0.9396, 0.9378,  0.9361,  0.9344,  0.9326,  0.9304,  0.9262],
                    [0.9295,  0.9366,  0.9419,  0.9458,  0.9487,  0.9509,  0.9526, 0.9538,  0.9528,  0.9517,  0.9505,  0.9493,  0.9481,  0.9468, 0.9456,  0.9444,  0.9432,  0.9413,  0.9395,  0.9360],
                    ]])

LPT2269.WpMap = np.array([[[153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812],
                    [153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511],
                    [152.799, 152.982, 153.052, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061],
                    [150.995, 151.316, 151.518, 151.647, 151.729, 151.781, 151.814, 151.834, 151.846, 151.852, 151.856, 151.858, 151.859, 151.859, 151.859, 151.859, 151.859, 151.859, 151.859, 151.859],
                    [148.751, 149.107, 149.349, 149.517, 149.635, 149.719, 149.779, 149.822, 149.852, 149.872, 149.885, 149.894, 149.898, 149.899, 149.899, 149.899, 149.899, 149.899, 149.899, 149.899],
                    [145.352, 145.680, 145.905, 146.061, 146.169, 146.244, 146.293, 146.324, 146.339, 146.344, 146.344, 146.344, 146.344, 146.344, 146.344, 146.344, 146.344, 146.344, 146.344, 146.344],
                    [140.863, 141.131, 141.310, 141.428, 141.503, 141.547, 141.567, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569]],
                    [[153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812, 153.812],
                    [153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511, 153.511],
                    [152.799, 152.982, 153.052, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061, 153.061],
                    [150.995, 151.316, 151.518, 151.647, 151.729, 151.781, 151.814, 151.834, 151.846, 151.852, 151.856, 151.858, 151.859, 151.859, 151.859, 151.859, 151.859, 151.859, 151.859, 151.859],
                    [148.751, 149.107, 149.349, 149.517, 149.635, 149.719, 149.779, 149.822, 149.852, 149.872, 149.885, 149.894, 149.898, 149.899, 149.899, 149.899, 149.899, 149.899, 149.899, 149.899],
                    [145.352, 145.680, 145.905, 146.061, 146.169, 146.244, 146.293, 146.324, 146.339, 146.344, 146.344, 146.344, 146.344, 146.344, 146.344, 146.344, 146.344, 146.344, 146.344, 146.344],
                    [140.863, 141.131, 141.310, 141.428, 141.503, 141.547, 141.567, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569, 141.569]]])

#LPT2269.Np_data, LPT2269.alpha_data, LPT2269.PR_data = np.meshgrid(LPT2269.Nc_vals, LPT2269.alpha_vals, LPT2269.PR_vals, sparse=False)
LPT2269.Npts = LPT2269.NpMap.size
LPT2269.units = {}
LPT2269.units['NpMap'] = 'rpm'
LPT2269.units['WpMap'] = 'lbm/s'

# format for new regular grid interpolator:

LPT2269.param_data = []
LPT2269.output_data = []

LPT2269.param_data.append({'name': 'alphaMap', 'values': LPT2269.alphaMap,
                          'default': 1.0, 'units': None})
LPT2269.param_data.append({'name': 'NpMap', 'values': LPT2269.NpMap,
                          'default': 100.0, 'units': 'rpm'})
LPT2269.param_data.append({'name': 'PRmap', 'values': LPT2269.PRmap,
                          'default': 6.0, 'units': None})

LPT2269.output_data.append({'name': 'WpMap', 'values': LPT2269.WpMap,
                           'default': np.mean(LPT2269.WpMap), 'units': 'lbm/s'})
LPT2269.output_data.append({'name': 'effMap', 'values': LPT2269.effMap,
                           'default': np.mean(LPT2269.effMap), 'units': None})