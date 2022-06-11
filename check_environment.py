import importlib

packages = [
    "causal_curve",
    "causalgraphicalmodels",
    "doubleml",
    "matplotlib",
    "numpy",
    "pandas",
    "sklearn",
    "scipy",
    "seaborn",
    "statsmodels"
]

    
bad = []
for package in packages:
    try:
        importlib.import_module(package)
    except ImportError:
        bad.append("Can't import %s" % package)

if len(bad) > 0:
    print('\n'.join(bad))
else:
    print("Looks like you're all set!")