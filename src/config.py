ELKI_VERSION = "0.7.5"
ELKI_EXECUTABLE = f"elki-bundle-{ELKI_VERSION}.jar"
ELKI_DOWNLOAD_URL = f"https://elki-project.github.io/releases/release{ELKI_VERSION}/elki-bundle-{ELKI_VERSION}.jar"
INPUT_ROOT = "data/"
OUTPUT_ROOT = "output/"

# include input data in result
INCLUDE_RAW = True
# min-max normalize the computed OSF
NORMALIZE_OSF = True
# Range of k parameter for OSF
K_RANGE = [5] + list(range(10,110,10))

algorithms = {'LOF': {'name': 'outlier.lof.LOF', 'param': '-lof.k'},
              'kNN': {'name': 'outlier.distance.KNNOutlier', 'param': '-knno.k'},
              'kNN-weight': {'name': 'outlier.distance.KNNWeightOutlier', 'param': '-knnwod.k'},
              'ODIN': {'name': 'outlier.distance.ODIN', 'param': '-odin.k'},
              'simplifiedLOF': {'name': 'outlier.lof.SimplifiedLOF', 'param': '-lof.k'},
              'COF': {'name': 'outlier.lof.COF', 'param': '-cof.k'},
              'INFLO': {'name': 'outlier.lof.INFLO', 'param': '-inflo.k'},
              'LoOP': {'name': 'outlier.lof.LoOP', 'param': '-loop.kcomp'},
              'LDOF': {'name': 'outlier.lof.LDOF', 'param': '-ldof.k'},
              # 'LDF': {'name': 'outlier.lof.LDF', 'param': '-ldf.k'}, # needs a further parameter ldf.h
              # 'KDEOS': {'name': 'outlier.lof.KDEOSS', 'param': '-kdeos.k.min'}, # needs a further parameter kdeos.k.max
              'FastABOD': {'name': 'outlier.anglebased.FastABOD', 'param': '-fastabod.k'}
             }