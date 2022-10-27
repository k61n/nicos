description = 'Devices from Motor Rack 09'

pvprefix = 'SQ:SANS-LLB:rack09:'

devices = dict(
    sl1yp = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Slit1 down',
        motorpv = pvprefix + 'sl1yp',
        errormsgpv = pvprefix + 'sl1yp-MsgTxt',
        precision = 0.01,
    ),
    sl1yn = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Slit1 up',
        motorpv = pvprefix + 'sl1yn',
        errormsgpv = pvprefix + 'sl1yn-MsgTxt',
        precision = 0.01,
    ),
    sl1xp = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Slit1 left',
        motorpv = pvprefix + 'sl1xp',
        errormsgpv = pvprefix + 'sl1xp-MsgTxt',
        precision = 0.01,
    ),
    sl1xn = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Slit1 right',
        motorpv = pvprefix + 'sl1xn',
        errormsgpv = pvprefix + 'sl1xn-MsgTxt',
        precision = 0.01,
    ),
    guide1pos = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Guide 1  translation',
        motorpv = pvprefix + 'guide1',
        errormsgpv = pvprefix + 'guide1-MsgTxt',
        precision = 0.01,
    ),
    guide1 = device('nicos.devices.generic.switcher.Switcher',
        description = 'Guide 1 choice',
        moveable = 'guide1pos',
        mapping = {
            'out': 10,
            'in': 100,
        },
        precision = .1,
        blockingmove = True,
    ),
    slit1 = device('nicos.devices.generic.slit.Slit',
        description = 'Slit 1 with left, right, bottom and top motors',
        opmode = '4blades',
        coordinates = 'opposite',
        left = 'sl1xp',
        right = 'sl1xn',
        top = 'sl1yp',
        bottom = 'sl1yn',
        visibility = (),
    ),
    sl1xw = device('nicos.core.device.DeviceAlias',
        description = 'slit  1 width',
        alias = 'slit1.width',
        devclass = 'nicos.devices.generic.slit.WidthSlitAxis'
    ),
    sl1xc = device('nicos_sinq.sans-llb.devices.slit.InvertedXSlitAxis',
        description = 'slit 1 x center position',
        slit = 'slit1',
        unit = 'mm',
    ),
    sl1yw = device('nicos.core.device.DeviceAlias',
        description = 'slit 1 height',
        alias = 'slit1.height',
        devclass = 'nicos.devices.generic.slit.HeightSlitAxis'
    ),
    sl1yc = device('nicos.core.device.DeviceAlias',
        description = 'slit 1 y center position',
        alias = 'slit1.centery',
        devclass = 'nicos.devices.generic.slit.CenterYSlitAxis'
    ),
    sl2yp = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Slit 2 down',
        motorpv = pvprefix + 'sl2yp',
        errormsgpv = pvprefix + 'sl2yp-MsgTxt',
        precision = 0.01,
    ),
    sl2yn = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Slit 2 up',
        motorpv = pvprefix + 'sl2yn',
        errormsgpv = pvprefix + 'sl2yn-MsgTxt',
        precision = 0.01,
    ),
    sl2xp = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Slit 2 left',
        motorpv = pvprefix + 'sl2xp',
        errormsgpv = pvprefix + 'sl2xp-MsgTxt',
        precision = 0.01,
    ),
    sl2xn = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Slit 2 right',
        motorpv = pvprefix + 'sl2xn',
        errormsgpv = pvprefix + 'sl2xn-MsgTxt',
        precision = 0.01,
    ),
    guide2pos = device('nicos_ess.devices.epics.motor.HomingProtectedEpicsMotor',
        epicstimeout = 3.0,
        description = 'Guide 2  translation',
        motorpv = pvprefix + 'guide2',
        errormsgpv = pvprefix + 'guide2-MsgTxt',
        precision = 0.01,
    ),
    guide2 = device('nicos.devices.generic.switcher.Switcher',
        description = 'Guide 2 choice',
        moveable = 'guide2pos',
        mapping = {
            'out': 10,
            'in': 100,
        },
        precision = .1,
        blockingmove = True,
    ),
    slit2 = device('nicos.devices.generic.slit.Slit',
        description = 'Slit 2 with left, right, bottom and top motors',
        opmode = '4blades',
        coordinates = 'opposite',
        left = 'sl2xp',
        right = 'sl2xn',
        top = 'sl2yp',
        bottom = 'sl2yn',
        visibility = (),
    ),
    sl2xw = device('nicos.core.device.DeviceAlias',
        description = 'slit  2 width',
        alias = 'slit2.width',
        devclass = 'nicos.devices.generic.slit.WidthSlitAxis'
    ),
    sl2xc = device('nicos_sinq.sans-llb.devices.slit.InvertedXSlitAxis',
        description = 'slit 2 x center position',
        slit = 'slit2',
        unit = 'mm',
    ),
    sl2yw = device('nicos.core.device.DeviceAlias',
        description = 'slit 2 height',
        alias = 'slit2.height',
        devclass = 'nicos.devices.generic.slit.HeightSlitAxis'
    ),
    sl2yc = device('nicos.core.device.DeviceAlias',
        description = 'slit 2 y center position',
        alias = 'slit2.centery',
        devclass = 'nicos.devices.generic.slit.CenterYSlitAxis'
    ),
)

startupcode = """
sl1xw.alias='slit1.width'
sl1yw.alias='slit1.height'
sl1yc.alias='slit1.centery'
sl2xw.alias='slit2.width'
sl2yw.alias='slit2.height'
sl2yc.alias='slit2.centery'
"""