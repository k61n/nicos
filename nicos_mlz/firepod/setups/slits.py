description = 'Sample Slit'

group = 'optional'

devices = dict(
    ss_l = device('nicos.devices.generic.Axis',
        visibility = (),
        precision = 0.1,
        backlash = -2.,
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-25, 20),
            speed = 1.0,
            unit = 'mm',
        ),
    ),
    ss_r = device('nicos.devices.generic.Axis',
        visibility = (),
        precision = 0.1,
        backlash = 2.,
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-20, 25),
            speed = 1.0,
            unit = 'mm',
        ),
    ),
    ss_b = device('nicos.devices.generic.Axis',
        visibility = (),
        precision = 0.1,
        backlash = -2.,
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-50, 20),
            speed = 1.0,
            unit = 'mm',
        ),
    ),
    ss_t = device('nicos.devices.generic.Axis',
        visibility = (),
        precision = 0.1,
        backlash = 2.,
        motor = device('nicos.devices.generic.VirtualMotor',
            abslimits = (-40, 50),
            speed = 1.0,
            unit = 'mm',
        ),
    ),
    slit = device('nicos.devices.generic.Slit',
        description = 'sample slit',
        left = 'ss_l',
        right = 'ss_r',
        bottom = 'ss_b',
        top = 'ss_t',
        opmode = 'centered',
        pollinterval = 5,
        maxage = 10,
    ),
)