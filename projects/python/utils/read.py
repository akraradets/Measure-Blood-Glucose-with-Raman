import numpy as np
from spectrochempy import NDDataset
from spectrochempy.core.dataset.baseobjects.meta import Meta
from spectrochempy.core.dataset.coord import Coord
import os

def read_txt(filename):
    dataset = NDDataset()
    # Metadata
    meta = Meta()
    path, fullname = os.path.split(filename)
    name, ext = os.path.splitext(fullname)
    meta.__setitem__('Date',name[-22:])
    meta.__setitem__('Exposition',name.split('_')[3].split(' ')[0])
    meta.__setitem__('Accumulation',name.split('_')[4])
    
    content = open(filename, "r").read()
    lines = content.splitlines()
    i = 0
    while lines[i].startswith("#"):
        key, val = lines[i].split("=")
        key = key[1:]
        if key in meta.keys():
            key = f"{key} {i}"
        meta[key] = val.strip()
        i += 1
    # read spec
    rawdata = np.genfromtxt(lines[i:], delimiter="\t")
    data = rawdata[:, 1][np.newaxis]
    _x = Coord(rawdata[:, 0], title="Raman shift", units="1/cm")
    _y = Coord(None, title="Time", units="s")
    date_acq, _y = _transf_meta(_y, meta)

    # set dataset metadata
    dataset.data = data
    dataset.set_coordset(y=_y, x=_x)
    dataset.title = "Counts"
    dataset.units = None
    dataset.name = fullname
    dataset.filename = filename
    dataset.meta = meta

    # date_acq is Acquisition date at start (first moment of acquisition)
    dataset.description = "Spectrum acquisition : " + str(date_acq)

    # Set origin, description and history
    dataset.history = f"Imported from LabSpec6 text file {filename}"

    # reset modification date to cretion date
    dataset._modified = dataset._created

    return dataset

def _transf_meta(y, meta):
    import datetime
    # Reformats some of the metadata from Labspec6 information
    # such as the acquisition date of the spectra and returns a list with the acquisition in datetime format,
    # the list of effective dates for each spectrum

    # def val_from_key_wo_time_units(k):
    #     for key in meta:
    #         h, m, s = 0, 0, 0
    #         if k in key:
    #             _, units = key.split(k)
    #             units = units.strip()[1:-1]
    #             if units == 's':
    #                 s = meta[key]
    #             elif units == 'mm:ss':
    #                 m, s = meta[key].split(':')
    #             elif units == 'hh:mm':
    #                 h, m = meta[key].split(':')
    #             break
    #     return datetime.timedelta(seconds=int(s), minutes=int(m), hours=int(h))

    if meta:
        try:
            dateacq = datetime.datetime.strptime(meta["Acquired"], "%d.%m.%Y %H:%M:%S")
        except TypeError:
            dateacq = datetime.datetime.strptime(meta["Date"], "%Y_%m_%d_%H_%M_%S_%f")
        
        acq = int(meta.get("Acq. time (s)", meta["Exposition"]))
        accu = int(meta.get("Accumulations", meta.get("Accumulation")))
        delay = int(meta.get("Delay time (s)", 0))
        # total = val_from_key_wo_time_units('Full time')

    else:
        dateacq = datetime.datetime(2000, 1, 1, 0, 0, 0)
        # datestr = '01/01/2000 00:00:00'
        acq = 0
        accu = 0
        delay = 0
        # total = datetime.timedelta(0)

    # delay between spectra
    delayspectra = datetime.timedelta(seconds=acq * accu + delay)

    # Date d'acquisition : le temps indiqué est celui où l'on démarre l'acquisition
    dateacq = dateacq - delayspectra

    # Dates effectives de chacun des spectres de la série : le temps indiqué est celui où l'on démarre l'acquisition
    # Labels for time : dates with the initial time for each spectrum
    try:
        y.labels = [dateacq + delayspectra * i for i in range(len(y))]
    except Exception as e:
        print(e)

    return dateacq, y