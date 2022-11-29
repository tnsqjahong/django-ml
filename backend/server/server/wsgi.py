# file backend/server/server/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.registry import MLRegistry, SDRegistry
from apps.ml.income_classifier.random_forest import RandomForestClassifier
from apps.ml.income_classifier.extra_trees import ExtraTreesClassifier
from apps.ml.image_creator.stable_diffusion import SDImageCreator

try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    rf = RandomForestClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="income_classifier",
                            algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Piotr",
                            algorithm_description="Random Forest with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier))
    
    et = ExtraTreesClassifier()
    
    registry.add_algorithm(endpoint_name="income_classifier",
                           algorithm_object=et,
                           algorithm_name="extra trees",
                           algorithm_status="testing",
                           algorithm_version="0.0.1",
                           owner="Piotr",
                           algorithm_description="Extra Trees with simple pre- and post- processing",
                           algorithm_code=inspect.getsource(RandomForestClassifier))

    sdRegistry = SDRegistry()

    sd = SDImageCreator()
    
    sdRegistry.add_algorithm(endpoint_name="image_creator",
                           algorithm_object=sd,
                           algorithm_name="stable diffusion",
                           algorithm_status="testing",
                           algorithm_version="0.0.1",
                           owner="beom",
                           algorithm_description="Image Create with stable diffusion",
                           algorithm_code=inspect.getsource(SDImageCreator))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))