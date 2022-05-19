import pydoc

def create_object_from_dict(d, **default_kwargs):
    '''Create an object from a dictionary.
    
    Inspired by `iglovikov_helper_functions.config_parsing.utils`. [1]_

    Parameters
    ----------
    d : dict
        Dictionary to create the object from. Must have a key "type" which specifies the class of the object.
        Any additional key-value pairs will be passed to the constructor when creating the object.
    **default_kwargs : additional arguments
        Default parameters to be passed to the constructor, if they do not exist in `d`.

    Returns
    -------
    object
        The initialized object.
    
    References
    ----------
    .. [1] https://github.com/ternaus/iglovikov_helper_functions/
    '''
    if not isinstance(d, dict):
        raise TypeError("'d' should be of type 'dict'.")
    if not 'type' in d:
        raise KeyError("'d' should have a key 'type'.")
    kwargs = d.copy()
    class_type = kwargs.pop('type')
    for name, value in default_kwargs.items():
        kwargs.setdefault(name, value)
    return pydoc.locate(class_type)(**kwargs)

def get_class_from_str(s):
    '''Get the uninitialized class `s`.

    Parameters
    ----------
    s : str
        The name of the class.
    
    Returns
    -------
    class
        The uninitialized class `s`.
    '''
    return pydoc.locate(s)