def units(input_dict, **kwargs):
    """
    Defines default input/output units if needed.
    
    The input_dict keys used by this function (which can be renamed using the 
    function's keyword arguments):
    length_unit -- the unit of length to use. Default is angstrom.
    energy_unit -- the unit of energy to use. Default is eV.
    pressure_unit -- the unit of pressure to use. Default is GPa.
    force_unit -- the unit of force to use. Default is eV/angstrom.
    
    Argument:
    input_dict -- dictionary containing input parameter key-value pairs
    
    Keyword Arguments:
    length_unit -- replacement parameter key name for 'length_unit'
    energy_unit -- replacement parameter key name for 'energy_unit'
    pressure_unit -- replacement parameter key name for 'pressure_unit'
    force_unit -- replacement parameter key name for 'force_unit'
    """
    
    #Set default keynames
    keynames = ['length_unit', 'energy_unit', 'pressure_unit', 'force_unit']
    for keyname in keynames:
        kwargs[keyname] = kwargs.get(keyname, keyname)
    
    #Set default unit styles to any terms not given
    input_dict[kwargs['length_unit']] =   input_dict.get(kwargs['length_unit'],   'angstrom')
    input_dict[kwargs['energy_unit']] =   input_dict.get(kwargs['energy_unit'],   'eV')
    input_dict[kwargs['pressure_unit']] = input_dict.get(kwargs['pressure_unit'], 'GPa')
    input_dict[kwargs['force_unit']] =    input_dict.get(kwargs['force_unit'],    'eV/angstrom')