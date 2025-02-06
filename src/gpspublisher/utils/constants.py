DICT_DEFAULT_PORTS = {
    'Serial': '/dev/ttyAMA0',
}

DICT_NMEA = [
    {'GGA': [
        {'timestamp': {'name': 'Data_hora_UTC'}},
        {'latitude': {'name': 'Latitude'}},
        {'longitude': {'name': 'Longitude'}},
        {'altitude': {'name': 'Altitude'}},
        {'gps_qual': {'name': 'Indicador_qualidade_GPS'}},
        {'num_sats': {'name': 'Numero_Satelites_Utilizado'}}
    ]
    },
    {'RMC': [
        {'datestamp': {'name': 'Data'}},
        {'spd_over_grnd': {'name': 'Velocidade'}},
        {'true_track': {'name': 'Direcao_deslocamento_graus_norte'}},
        {'latitude': {'name': 'Latitude'}},
        {'longitude': {'name': 'Longitude'}},
    ]
    },
    {'VTG': [
        {'spd_over_grnd_kmph': {'name': 'Velocidade'}},
        {'true_track': {'name': 'Direcao_deslocamento_graus_norte'}}
    ]
    },
]

SOG_CONST = 1.852
