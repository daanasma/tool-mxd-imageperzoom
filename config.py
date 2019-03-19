import os

maindir = os.getcwd()
mapdir = os.path.join(maindir, 'maps')

src_map = os.path.join(mapdir, 'map.mxd')
output_folder_name = 'output'

scales = [
    '1128',
    '2257',
    '4515',
    '9028',
    '18056',
    '36112',
    '72224',
    '144448'
]

locations = [
    {
        'name': 'Mechelen',
        'location': {
            'x': '157780',
            'y': '190836'
        }
    },
    {
        'name': 'Antwerpen',
        'location': {
            'x': '153361',
            'y': '212578'
        }
    },
]