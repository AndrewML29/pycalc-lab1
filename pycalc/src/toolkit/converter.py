from toolkit.errors import ConversionError

UNIT_COEFFICENTS = {
    'length':{
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
    },
    'mass':{
        'mg': 0.001,
        'g': 1.0,
        'kg': 1000.0,
    }
}
TEMPERATURE_UNITS = {'c','f','k'}

def convert (value,from_unit,to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    try:
        value = float(value)
    except (ValueError,TypeError):
        raise ConversionError(f"Неверное числовое значение: '{value}'")
    
    if from_unit in TEMPERATURE_UNITS and to_unit in TEMPERATURE_UNITS:
        if from_unit == 'c':
            celsius = value
        elif from_unit == 'f':
            celsius = (value - 32) * 5 / 9
        elif from_unit == 'k':
            celsius = value - 273.15
        if celsius < -273.15:
            raise ConversionError('Temperature below absolut zero is prohibited.')
        if to_unit == 'c':
            return celsius
        elif to_unit == 'f':
            return celsius * 9 / 5 + 32
        elif to_unit == 'k':
            return celsius + 273.15

    elif from_unit in UNIT_COEFFICENTS['length'] and to_unit in UNIT_COEFFICENTS['length']:
        units = UNIT_COEFFICENTS['length']
        return (value * units[from_unit] / units[to_unit])
    elif from_unit in UNIT_COEFFICENTS['mass'] and to_unit in UNIT_COEFFICENTS['mass']:
        units = UNIT_COEFFICENTS['mass']
        return (value * units[from_unit] / units[to_unit])
    else:
        raise ConversionError('Incompatible units.')