import numpy as np

INPUT_SCHEMA = {
    "prompt": {
        'datatype': str,
        'required': True,
        'shape': [1],
        'example': ["There is a fine house in the forest"]
    },
    'negative_prompt': {
        'datatype': str,
        'required': False,
        'example': ["test"],
        'shape': [1]
    },
    'width': {
        'datatype': np.int8,
        'required': False,
        'example': [ 768 ,  512 ],
        'shape': [2]
    },
}
