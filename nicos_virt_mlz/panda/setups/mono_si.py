description = 'PANDA Si-monochromator'

group = 'lowlevel'

includes = ['monofoci', 'monoturm', 'panda_mtt']

excludes = ['mono_pg', 'mono_cu', 'mono_heusler']

extended = dict(dynamic_loaded = True)

devices = dict(
    mono_si = device('nicos.devices.tas.Monochromator',
        description = 'PANDA Si monochromator',
        unit = 'A-1',
        theta = 'mth',
        twotheta = 'mtt',
        reltheta = True,
        focush = 'mfh_si',
        focusv =  None,
        hfocuspars = [0],
        vfocuspars = [0],
        abslimits = (1, 10),
        userlimits = (1, 10),
        material = 'Si',
        reflection = (1, 1, 1),
        dvalue = 3.455,
        scatteringsense = -1,
        crystalside = -1,
    ),
    mfh_si_step = device('nicos_virt_mlz.panda.devices.stubs.MccMotor',
        description = 'horizontal focusing MOTOR of Si monochromator',
        fmtstr = '%.3f',
        abslimits = (1, 5),
        userlimits = (1, 5),
        unit = 'mm',
        speed = 5.0 / 54.0,
        visibility = (),
    ),
    mfh_si_enc = device('nicos.devices.generic.VirtualCoder',
        description = 'horizontal focusing CODER of Si monochromator',
        motor = 'mfh_si_step',
        fmtstr = '%.3f',
        unit = 'mm',
        visibility = (),
    ),
    mfh_si = device('nicos_mlz.panda.devices.rot_axis.RefAxis',
        description = 'horizontal focus of Si monochromator',
        motor = 'mfh_si_step',
        coder = 'mfh_si_enc',
        precision = 0.01,
        backlash = -0.2,
        refpos = 1.4,
        refspeed = 0.01,
        autoref = None,
    ),
)

startupcode = '''
try:
    _ = (ana, mono, mfv, mfh, focibox)
except NameError as e:
    printerror("The requested setup 'panda' is not fully loaded!")
    raise NameError('One of the required devices is not loaded : %s, please check!' % e)

if focibox.read(0) == 'Si':
    from nicos import session
    mfh.alias = session.getDevice('mfh_si')
    mfv.alias = None
    mono.alias = session.getDevice('mono_si')
    ana.alias = session.getDevice('ana_pg')
    mfh.motor._pushParams() # forcibly send parameters to HW
    #mfv.motor._pushParams() # forcibly send parameters to HW
    focibox.comm('XMA',forcechannel=False) # enable output for mfh
    #focibox.comm('YMA',forcechannel=False) # enable output for mfv
    focibox.driverenable = True
    #maw(mtx, -12) #correct center of rotation for Si-mono only
    del session
else:
    printerror('WRONG MONO ON TABLE FOR SETUP mono_si !!!')
'''
