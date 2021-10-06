import os 

base_dir = os.path.dirname(os.path.realpath(__file__))
target_dir = os.path.join(base_dir, 'algorithms')

modules = [x.split('.')[0] for x in os.listdir(target_dir) if x.endswith('.py') and not x.startswith('_')]

for module in modules:
    eval(f"exec('from algorithms.{module} import *')")
