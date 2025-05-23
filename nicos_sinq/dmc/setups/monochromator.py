description = 'Monochromator devices for SINQ DMC.'

pvprefix = 'SQ:DMC:turboPmac1:'

devices = dict(
    a1 = device('nicos_sinq.devices.epics.motor.SinqMotor',
        description = 'Monochromator rotation (mth)',
        motorpv = f'{pvprefix}A1',
        errormsgpv = f'{pvprefix}A1-MsgTxt',
        can_disable = True,
    ),
    a2 = device('nicos_sinq.devices.epics.motor.SinqMotor',
        description = 'Monochromator takeoff angle (m2t)',
        motorpv = f'{pvprefix}A2',
        errormsgpv = f'{pvprefix}A2-MsgTxt',
        can_disable = True,
    ),
    mtl = device('nicos_sinq.devices.epics.motor.SinqMotor',
        description = 'Monochromator translation lower',
        motorpv = f'{pvprefix}MTL',
        errormsgpv = f'{pvprefix}MTL-MsgTxt',
        can_disable = True,
    ),
    mtu = device('nicos_sinq.devices.epics.motor.SinqMotor',
        description = 'Monochromator translation upper',
        motorpv = f'{pvprefix}MTU',
        errormsgpv = f'{pvprefix}MTU-MsgTxt',
        can_disable = True,
    ),
    mgl = device('nicos_sinq.devices.epics.motor.SinqMotor',
        description = 'Monochromator goniometer lower',
        motorpv = f'{pvprefix}MGL',
        errormsgpv = f'{pvprefix}MGL-MsgTxt',
        can_disable = True,
    ),
    mgu = device('nicos_sinq.devices.epics.motor.SinqMotor',
        description = 'Monochromator goniometer upper',
        motorpv = f'{pvprefix}MGU',
        errormsgpv = f'{pvprefix}MGU-MsgTxt',
        can_disable = True,
    ),
    mcv = device('nicos_sinq.devices.epics.motor.SinqMotor',
        description = 'Monochromator curvature',
        motorpv = f'{pvprefix}MCV',
        errormsgpv = f'{pvprefix}MCV-MsgTxt',
        can_disable = True,
    ),
    wavelength = device('nicos_sinq.devices.mono.SinqMonochromator',
        description = 'PG analyser (default)',
        unit = 'A',
        theta = 'a1',
        twotheta = 'a2',
        focush = None,
        focusv = 'mcv',
        order = 1,
        abslimits = (2, 5),
        vfocuspars = [-0.025942, 5.351660],
        material = 'PG',
        reflection = (0, 0, 2),
        dvalue = 3.3537,
        scatteringsense = 1,
        crystalside = 1,
    ),
    wavelength_refined = device('nicos.devices.generic.ManualMove',
        description = 'Measured value of the wavelength',
        unit = 'A',
        abslimits = (.1, 10)
    )
)
