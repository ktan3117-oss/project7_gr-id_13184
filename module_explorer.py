import math
import random
import datetime
import uuid


def explore_module():
    module_name = input(
        "Enter module name (math/random/datetime/uuid): "
    )

    modules = {
        "math": math,
        "random": random,
        "datetime": datetime,
        "uuid": uuid
    }

    if module_name in modules:
        print(dir(modules[module_name]))
    else:
        print("Module not found.")