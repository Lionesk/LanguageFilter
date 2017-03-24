raw = open('emw.csv', 'r')
data = raw.read().splitlines()
for line in range(len(data)):
    data[line] = data[line].split(',')

wordListRaw = open('profaneWords.txt', 'r')
wordListRaw2 = wordListRaw.readlines()
wordList = []
for line in range(len(wordListRaw2)):
    wordList.append(wordListRaw2[line].split('\t')[0])
print(wordList)

suffixes = ['a', 'ability', 'able', 'ably', 'ac', 'acean', 'aceous', 'ad', 'ade', 'aemia', 'age', 'agog', 'agogue',
            'aholic', 'al', 'algia', 'all', 'amine', 'an', 'ana', 'ance', 'ancy', 'androus', 'andry', 'ane', 'ant',
            'ar', 'arch', 'archy', 'ard', 'arian', 'arium', 'art', 'ary', 'ase', 'ate', 'athon', 'ation', 'ative',
            'ator', 'atory', 'biont', 'biosis', 'blast', 'bot', 'cade', 'caine', 'carp', 'carpic', 'carpous', 'cele',
            'cene', 'centric', 'cephalic', 'cephalous', 'cephaly', 'chore', 'chory', 'chrome', 'cide', 'clast',
            'clinal', 'cline', 'clinic', 'coccus', 'coel', 'coele', 'colous', 'cracy', 'crat', 'cratic', 'cratical',
            'cy', 'cyte', 'dale', 'derm', 'derma', 'dermatous', 'dom', 'drome', 'dromous', 'ean', 'eaux', 'ectomy',
            'ed', 'ee', 'eer', 'ein', 'eme', 'emia', 'en', 'ence', 'enchyma', 'ency', 'ene', 'ent', 'eous', 'er',
            'ergic', 'ergy', 'es', 'escence', 'escent', 'ese', 'esque', 'ess', 'est', 'et', 'eth', 'etic', 'ette', 'ey',
            'facient', 'faction', 'fer', 'ferous', 'fic', 'fication', 'fid', 'florous', 'fold', 'foliate', 'foliolate',
            'form', 'fuge', 'ful', 'fy', 'gamous', 'gamy', 'gate', 'gen', 'gene', 'genesis', 'genetic', 'genic',
            'genous', 'geny', 'gnathous', 'gon', 'gony', 'gram', 'graph', 'grapher', 'graphy', 'gyne', 'gynous', 'gyny',
            'hood', 'i', 'ia', 'ial', 'ian', 'iana', 'iasis', 'iatric', 'iatrics', 'iatry', 'ibility', 'ible', 'ic',
            'ician', 'icide', 'ick', 'ics', 'id', 'ide', 'ie', 'ify', 'ile', 'in', 'ine', 'ing', 'ion', 'ious',
            'isation', 'ise', 'ish', 'ism', 'ist', 'istic', 'istical', 'istically', 'ite', 'itious', 'itis', 'ity',
            'ium', 'ive', 'ix', 'ization', 'ize', 'kin', 'kinesis', 'kins', 'latry', 'le', 'lepry', 'less', 'let',
            'like', 'ling', 'lite', 'lith', 'lithic', 'log', 'logue', 'logic', 'logical', 'logist', 'logy', 'ly',
            'lyse', 'lysis', 'lyte', 'lytic', 'lyze', 'mancy', 'mania', 'meister', 'ment', 'mer', 'mere', 'merous',
            'meter', 'metric', 'metrics', 'metry', 'mire', 'mo', 'morph', 'morphic', 'morphism', 'morphous', 'most',
            'mycete', 'mycin', 'nasty', 'ness', 'nik', 'nomics', 'nomy', 'n', 't', 'o', 'o-', 'ode', 'odon', 'odont',
            'odontia', 'oholic', 'oic', 'oid', 'ol', 'ole', 'oma', 'ome', 'omics', 'on', 'one', 'ont', 'onym', 'onymy',
            'opia', 'opsis', 'opsy', 'or', 'orama', 'ory', 'ose', 'osis', 'otic', 'otomy', 'ous', 'para', 'parous',
            'path', 'pathy', 'ped', 'pede', 'penia', 'petal', 'phage', 'phagia', 'phagous', 'phagy', 'phane', 'phasia',
            'phil', 'phile', 'philia', 'philiac', 'philic', 'philous', 'phobe', 'phobia', 'phobic', 'phone', 'phony',
            'phore', 'phoresis', 'phorous', 'phrenia', 'phyll', 'phyllous', 'plasia', 'plasm', 'plast', 'plastic',
            'plasty', 'plegia', 'plex', 'ploid', 'pod', 'pode', 'podous', 'poieses', 'poietic', 'pter', 'punk', 'ric',
            'rrhagia', 'rrhea', 'ry', 's', 'scape', 'scope', 'scopy', 'scribe', 'script', 'sect', 'sepalous', 'ship',
            'some', 'speak', 'sperm', 'sphere', 'sporous', 'st', 'stasis', 'stat', 'ster', 'stome', 'stomy', 'taxis',
            'taxy', 'tend', 'th', 'therm', 'thermal', 'thermic', 'thermy', 'thon', 'thymia', 'tion', 'tome', 'tomy',
            'tonia', 'trichous', 'trix', 'tron', 'trophic', 'trophy', 'tropic', 'tropism', 'tropous', 'tropy', 'tude',
            'ture', 'ty', 'ular', 'ule', 'ure', 'urgy', 'uria', 'uronic', 'urous', 'valent', 'virile', 'vorous', 'ward',
            'wards', 'ware', 'ways', 'wear', 'wide', 'wise', 'worthy', 'xor', 'y', 'yl', 'yne', 'zilla', 'zoic', 'zoon',
            'zygous', 'zyme', 'sion', 'ssion']
print(suffixes)
