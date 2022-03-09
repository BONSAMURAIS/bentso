COUNTRIES = [
    'AT', 'BA', 'BE', 'BG', 'CH', 'CZ', 'DE', 'DK',
    'EE', 'ES', 'FI', 'FR', 'GB', 'GR', 'HR', 'HU',
    'IE', 'IT', 'LU', 'LV', 'ME', 'MK', 'MT', 'NL',
    'NO', 'PL', 'PT', 'RO', 'RS', 'SE', 'SI', 'SK'
]

RENEWABLES = {
    'Solar',
    'Wind Onshore',
    'Wind Offshore',
    'Hydro Water Reservoir',
    'Hydro Run-of-river and poundage',
    'Marine',
    'Geothermal',
    'Biomass',
}

# Not all countries actually present, even if they should be
ENTSO_COUNTRIES = set(COUNTRIES).difference({"CY", "IS", "NI"})

TRADE_PAIRS = {
    'AT': {'CH', 'CZ', 'DE', 'HU', 'IT', 'SI'},
    'BA': {'HR', 'ME', 'RS'},
    'BE': {'FR', 'GB', 'LU', 'NL'},
    'BG': {'GR', 'MK', 'RO', 'RS', 'TR'},
    'CH': {'AT', 'DE', 'FR', 'IT'},
    'CZ': {'AT', 'DE', 'PL', 'SK'},
    'DE': {'AT', 'CH', 'CZ', 'DK', 'FR', 'LU', 'NL', 'PL', 'SE'},
    'DK': {'DE', 'NO', 'SE'},
    'EE': {'FI', 'LV'},
    'FI': {'EE', 'NO', 'RU', 'SE'},
    'FR': {'BE', 'CH', 'DE', 'ES', 'GB', 'IT'},
    'GR': {'AL', 'BG', 'IT', 'MK', 'TR'},
    'HR': {'BA', 'HU', 'RS', 'SI'},
    'HU': {'AT', 'HR', 'RO', 'RS', 'SK', 'UA'},
    'IT': {'AT', 'CH', 'FR', 'GR', 'MT', 'SI'},
    'LU': {'BE', 'DE'},
    'LV': {'EE', 'LT', 'RU'},
    'ME': {'BA', 'RS'},
    'MK': {'BG', 'GR', 'RS'},
    'NL': {'BE', 'DE', 'GB', 'NO'},
    'NO': {'DK', 'FI', 'NL', 'RU', 'SE'},
    'PL': {'CZ', 'DE', 'LT', 'SE', 'SK', 'UA'},
    'RO': {'BG', 'HU', 'RS', 'UA'},
    'RS': {'AL', 'BA', 'BG', 'HR', 'HU', 'ME', 'MK', 'RO'},
    'SE': {'DE', 'DK', 'FI', 'LT', 'NO', 'PL'},
    'SI': {'AT', 'HR', 'IT'},
    'SK': {'CZ', 'HU', 'PL', 'UA'},
    'ES': {'FR', 'MA', 'PT'},
    'PT': {'ES'},
    'IE': {'GB'}
}
