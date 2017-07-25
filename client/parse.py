import xml.etree.ElementTree as ET


__all__ = ['parse']


def parse(path):
    all_l = []

    tree = ET.parse(path)
    root = tree.getroot()

    for measure in root.findall('./part/'):
        measure_l = []
        all_l.append(measure_l)

        for note in measure:
            if note.tag != 'note':
                continue

            note_d = {}
            pitch = note.find('pitch')
            step = pitch.find('step').text
            octave = int(pitch.find('octave').text)
            note_d['pitch'] = ({'step': step, 'octave': octave})

            note_d['duration'] = int(note.find('duration').text)
            measure_l.append(note_d)

    return all_l
