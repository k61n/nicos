description = 'Monochromator CARESS HWB Devices'

group = 'lowlevel'

devices = dict(
    omgm_m = device('nicos.devices.generic.VirtualMotor',
        abslimits = (12, 63),
        unit = 'deg',
        fmtstr = '%.2f',
        lowlevel = True,
        speed = 1,
        curvalue = 39.4,
        # requires = {'level': 'admin'},
    ),
    omgm_c = device('nicos.devices.generic.VirtualCoder',
        motor = 'omgm_m',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    omgm = device('nicos.devices.generic.Axis',
        description = 'OMGM',
        motor = 'omgm_m',
        coder = 'omgm_c',
        precision = 0.005,
    ),
    transm_m = device('nicos.devices.generic.VirtualMotor',
        fmtstr = '%.3f',
        abslimits = (0, 60.5),
        lowlevel = True,
        # requires = {'level': 'admin'},
        unit = 'cm',
        curvalue = 60.292,
        speed = 3,
    ),
    transm_c = device('nicos.devices.generic.VirtualCoder',
        motor = 'transm_m',
        fmtstr = '%.3f',
        lowlevel = True,
    ),
    transm_a = device('nicos.devices.generic.Axis',
        description = 'HWB TRANSM',
        motor = 'transm_m',
        coder = 'transm_c',
        precision = 0.001,
        lowlevel = True,
    ),
    transm = device('nicos.devices.generic.Switcher',
        description = 'Monochromator changer',
        moveable = 'transm_a',
        mapping = {
            'Si': 0.292,
            'PG': 30.292,
            'Ge': 60.292,
        },
        precision = 0.01,
        unit = '',
        # requires = {'level': 'admin'},
    ),
    tthm_r = device('nicos_mlz.stressi.devices.wavelength.TransformedMoveable',
        description = 'Base hardware device',
        dev = 'tthm',
        informula = '1./0.956 * x - 11.5 / 0.956',
        outformula = '0.956 * x + 11.5',
        precision = 0.001,
        lowlevel = True,
    ),
    tthm = device('nicos.devices.generic.VirtualMotor',
        description = 'Take off angle',
        fmtstr = '%.2f',
        unit = 'deg',
        abslimits = (50, 100),
        curvalue = 84.,
        speed = 2,
    ),
    wav = device('nicos_mlz.stressi.devices.wavelength.Wavelength',
        description = 'The incoming wavelength',
        omgm = 'omgm',
        crystal = 'transm',
        plane = '311',  # '100',
        base = 'tthm_r',
        unit = 'AA',
        fmtstr = '%.2f',
        abslimits = (0.9, 2.5),
    ),
    chim_si_m = device('nicos.devices.generic.VirtualMotor',
        abslimits = (-5, 3),
        curvalue = 0,
        speed = 0.25,
        unit = 'deg',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    chim_si_c = device('nicos.devices.generic.VirtualCoder',
        motor = 'chim_si_m',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    chim_si = device('nicos.devices.generic.Axis',
        description = 'CHI Si monochromator',
        motor = 'chim_si_m',
        coder = 'chim_si_c',
        fmtstr = '%.2f',
        precision = 0.01,
    ),
    chim_pg_m = device('nicos.devices.generic.VirtualMotor',
        abslimits = (-5, 3),
        curvalue = 0,
        speed = 0.25,
        unit = 'deg',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    chim_pg_c = device('nicos.devices.generic.VirtualCoder',
        motor = 'chim_pg_m',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    chim_pg = device('nicos.devices.generic.Axis',
        description = 'CHI PG monochromator',
        motor = 'chim_pg_m',
        coder = 'chim_pg_c',
        fmtstr = '%.2f',
        precision = 0.01,
    ),
    chim_ge_m = device('nicos.devices.generic.VirtualMotor',
        abslimits = (-5, 3),
        curvalue = 0,
        speed = 0.25,
        unit = 'deg',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    chim_ge_c = device('nicos.devices.generic.VirtualCoder',
        motor = 'chim_ge_m',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    chim_ge = device('nicos.devices.generic.Axis',
        description = 'CHI Ge monochromator',
        motor = 'chim_ge_m',
        coder = 'chim_ge_c',
        fmtstr = '%.2f',
        precision = 0.01,
    ),
    foc_si_m = device('nicos.devices.generic.VirtualMotor',
        abslimits = (-75.85, 948.9),
        unit = 'a.u.',
        speed = 1,
        curvalue = 133,
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    foc_si = device('nicos.devices.generic.Axis',
        description = 'Horizontal focus Si monochromator',
        motor = 'foc_si_m',
        fmtstr = '%.1f',
        precision = 0.1,
    ),
    foc_pg_m = device('nicos.devices.generic.VirtualMotor',
        abslimits = (0, 2044),
        unit = 'steps',
        speed = 10,
        curvalue = 1500,
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    foc_pg = device('nicos.devices.generic.Axis',
        description = 'Vertical focus PG monochromator',
        motor = 'foc_pg_m',
        fmtstr = '%.1f',
        precision = 0.1,
    ),
    foc_ge_m = device('nicos.devices.generic.VirtualMotor',
        abslimits = (-100, 8000),
        unit = 'steps',
        speed = 10,
        curvalue = 0,
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    foc_ge_c = device('nicos.devices.generic.VirtualCoder',
        motor = 'foc_ge_m',
        fmtstr = '%.2f',
        lowlevel = True,
    ),
    foc_ge = device('nicos.devices.generic.Axis',
        description = 'Vertical focus Ge monochromator',
        motor = 'foc_ge_m',
        coder = 'foc_ge_c',
        fmtstr = '%.1f',
        precision = 0.1,
    ),
)