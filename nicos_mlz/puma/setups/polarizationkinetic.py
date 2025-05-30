description = 'Kinetic polarization analysis measurements'

group = 'basic'

includes = [
    'pumabase', 'seccoll', 'collimation', 'ios', 'hv', 'notifiers', 'multidet',
    'multiana', 'rdcad', 'opticalbench', 'detector', 'ana_alias', 'pollengths',
    'slits',
]

sysconfig = {
    'datasinks': ['Listmode']
}

tango_base = 'tango://mesydaq.puma.frm2.tum.de:10000/qm/qmesydaq/'

devices = dict(
    Listmode = device('nicos_mlz.puma.datasinks.ListmodeSink',
        description = 'Listmode data written via QMesyDAQ',
        image = 'image',
        subdir = 'list',
        filenametemplate = ['%(pointcounter)07d.mdat'],
        detectors = ['det'],
    ),
    channels = device('nicos.devices.vendor.qmesydaq.tango.MultiCounter',
        tangodevice = tango_base + 'image',
        visibility = (),
        channels = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    ),
    cycles = device('nicos_mlz.puma.devices.tango.CycleCounter',
        description = 'QMesyDAQ cycle channel',
        tangodevice = tango_base + 'counter4',
        type = 'counter',
        visibility = (),
        fmtstr = '%d',
    ),
    det = device('nicos_mlz.puma.devices.KineticDetector',
        description = 'Puma detector QMesydaq device (11 counters)',
        timers = ['timer'],
        monitors = ['mon1', 'cycles'],
        counters = ['channels'],
        images = [],
        maxage = 86400,
        pollinterval = None,
    ),
)

startupcode = '''
med.opmode = 'pa'
SetDetectors(det)
set('image', 'listmode', True)
'''
