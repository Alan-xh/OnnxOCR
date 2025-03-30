<<<<<<< HEAD
from .operators import *


def transform(data, ops=None):
    """transform"""
=======
from onnxocr.operators import *

def transform(data, ops=None):
    """ transform """
>>>>>>> 74123dc (renew)
    if ops is None:
        ops = []
    for op in ops:
        data = op(data)
        if data is None:
            return None
    return data


def create_operators(op_param_list, global_config=None):
    """
    create operators based on the config

    Args:
        params(list): a dict list, used to create some operators
    """
<<<<<<< HEAD
    assert isinstance(op_param_list, list), "operator config should be a list"
    ops = []
    for operator in op_param_list:
        assert isinstance(operator, dict) and len(operator) == 1, "yaml format error"
=======
    assert isinstance(op_param_list, list), ('operator config should be a list')
    ops = []
    for operator in op_param_list:
        assert isinstance(operator,
                          dict) and len(operator) == 1, "yaml format error"
>>>>>>> 74123dc (renew)
        op_name = list(operator)[0]
        param = {} if operator[op_name] is None else operator[op_name]
        if global_config is not None:
            param.update(global_config)
        op = eval(op_name)(**param)
        ops.append(op)
<<<<<<< HEAD
    return ops
=======
    return ops
>>>>>>> 74123dc (renew)
