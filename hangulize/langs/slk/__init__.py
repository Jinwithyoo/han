# -*- coding: utf-8 -*-
from hangulize import *


class Slovak(Language):
    """For transcribing Slovak."""

    __iso639__ = {1: 'sk', 2: 'slo', 3: 'slk'}
    __tmp__ = ',;'

    vowels = 'aAPeEiIoOWuUyY'
    cs = 'bcCdDfghjklLmnNpqQrRsStTvwxzZ'
    vl = 'cCfkpsStT' # voiceless obstruents
    notation = Notation([
        ('á', 'A'),
        ('ä', 'P'),
        ('č', 'C'),
        ('ď', 'D'),
        ('é', 'E'),
        ('í', 'I'),
        ('ĺ', 'L'),
        ('ľ', 'Q'),
        ('ň', 'N'),
        ('ó', 'O'),
        ('ô', 'W'),
        ('ŕ', 'R'),
        ('š', 'S'),
        ('ť', 'T'),
        ('ú', 'U'),
        ('ý', 'Y'),
        ('ž', 'Z'),
        ('^bielov{<cs>}', 'bieloV'),
        ('^bratovr', 'bratoVr'),
        ('^cArov{<cs>}', 'cAroV'),
        ('^cudzov{<cs>}', 'cudzoV'),
        ('^Carov{<cs>}', 'CaroV'),
        ('^dov{<cs>}', 'doV'),
        ('^drevov{<cs>}', 'drevoV'),
        ('^hrWzov{<cs>}', 'hrWzoV'),
        ('^krutov{<cs>}', 'krutoV'),
        ('^mAlov{<cs>}', 'mAloV'),
        ('^mimov{<cs>}', 'mimoV'),
        ('^mnohov{<cs>}', 'mnohoV'),
        ('^nav{l|r|z}', 'naV'),
        ('^nAvr', 'nAVr'),
        ('^nev{<cs>}', 'neV'),
        ('^ov{dov|lAd|laZ|p|r}', 'oV'),
        ('^polov{<cs>}', 'poloV'),
        ('^poStov{<cs>}', 'poStoV'),
        ('^povra', 'poura'),
        ('^pov{<cs>}', 'poV'),
        ('^povyv{<cs>}', 'povyV'),
        ('^povzb', 'poVzb'),
        ('^pravl', 'praVl'),
        ('^prev{<cs>}', 'preV'),
        ('^priv{<cs>}', 'priV'),
        ('spoluv{<cs>}', 'spoluV'),
        ('^sUv{<cs>}', 'sUV'),
        ('^vov{<cs>}', 'voV'),
        ('^vyv{<cs>}', 'vyV'),
        ('^zav{<cs>}', 'zaV'),
        ('^zov{<cs>}', 'zoV'),
        ('^uv{<cs>}', 'uV'),
        ('v{Cera|lAd|las|rAs|rav|rat|rAt|Simn|tAk|tip|zdu|zTah|zTaZ}', 'V'),
        ('v{lC|QC|lh|lk}', 'v'),
        ('vl{C|h|k|n}', 'Vl'),
        ('vr{h|ch|kn|l|stv|z|Zl}', 'Vr'),
        ('vR{S|t|z}', 'VR'),
        ('vz{d|h|n|T}', 'Vz'),
        ('v{n|N}', 'V'),
        ('{@}v{<cs>}', 'u'),
        ('{@}v$', 'u'),
        ('V', 'v'),
        ('A', 'a'),
        ('P', 'e'),
        ('E', 'e'),
        ('I', 'i'),
        ('L', 'l'),
        ('O', 'o'),
        ('R', 'r'),
        ('W', 'uo'),
        ('U', 'u'),
        ('w', 'v'),
        ('ts', 'c'),
        ('tS', 'C'),
        ('b{<vl>}', 'p'),
        ('b$', 'p'),
        ('d{<vl>}', 't'),
        ('d$', 't'),
        ('dz{<vl>}', 'c'),
        ('dz$', 'c'),
        ('dZ{<vl>}', 'C'),
        ('dZ$', 'C'),
        ('D{<vl>}', 'T'),
        ('D$', 'T'),
        ('g{<vl>}', 'k'),
        ('g$', 'k'),
        ('v{<vl>}', 'f'),
        ('v$', 'f'),
        ('z{<vl>}', 's'),
        ('z$', 's'),
        ('Z{<vl>}', 'S'),
        ('Z$', 'S'),
        ('C{@}', 'c'),
        ('C', 'ci'),
        ('D{@}', 'dJ'),
        ('D', 'di'),
        ('Q{@}', 'lJ'),
        ('Q', 'l'),
        ('N{@}', 'nJ'),
        ('N', 'n'),
        ('S{@}', 'sJ'),
        ('S$', 'si'),
        ('S', 'sJu'),
        ('T{@}', 'tJ'),
        ('T', 'ti'),
        ('dZ{@}', 'z'),
        ('dZ', 'zi'),
        ('Z{@}', 'z'),
        ('Z', 'zu'),
        ('xx', 'x'),
        ('^x', 'z'),
        ('x', 'ks'),
        ('qu', 'kv'),
        ('q', 'k'),
        ('ch', 'h'),
        ('aa', 'a'),
        ('bb', 'b'),
        ('dd', 'd'),
        ('ee', 'e'),
        ('ff', 'f'),
        ('gg', 'g'),
        ('hh', 'h'),
        ('jj', 'ij'),
        ('ii', 'i'),
        ('^j{@}', 'J'),
        ('{@}j{@}', 'J'),
        ('sje', 'sJe'),
        ('je', 'e'),
        ('{l|n|d|s|t}j{@}', 'J'),
        ('{l|n}j', None),
        ('j', 'i'),
        ('ij', 'i'),
        ('yj', 'y'),
        ('kk', 'k'),
        ('ll', 'l'),
        ('{@}mm{@}', 'm,m'),
        ('mm', 'm'),
        ('{@}nn{@}', 'n,n'),
        ('nn', 'n'),
        ('oo', 'o'),
        ('pp', 'p'),
        ('rr', 'r'),
        ('ss', 's'),
        ('tt', 't'),
        ('uu', 'u'),
        ('vv', 'v'),
        ('^y{@}', 'J'),
        ('{@}y{@}', 'J'),
        ('yy', 'y'),
        ('y', 'i'),
        ('Y', 'i'),
        ('zz', 'z'),
        ('dz', 'z'),
        ('je', 'e'),
        ('{@}k{<vl>}', 'k,'),
        ('{@}p{<vl>}', 'p,'),
        ('^l', 'l;'),
        ('^m', 'm;'),
        ('^n', 'n;'),
        ('l$', 'l,'),
        ('m$', 'm,'),
        ('n$', 'n,'),
        ('l{@|J|m,|n,}', 'l;'),
        ('{,}l', 'l;'),
        ('m{@|r}', 'm;'),
        ('n{@|J}', 'n;'),
        ('l', 'l,'),
        ('m', 'm,'),
        ('n', 'n,'),
        (',,', ','),
        (',;', None),
        (',l,', 'l,'),
        (',m,', 'm,'),
        (',n,', 'n,'),
        ('l{m;|n;}', 'l,'),
        (';', None),
        ('b', Choseong(B)),
        ('c', Choseong(C)),
        ('d', Choseong(D)),
        ('f', Choseong(P)),
        ('g', Choseong(G)),
        ('h', Choseong(H)),
        ('H', Choseong(H)),
        ('k,', Jongseong(G)),
        ('k', Choseong(K)),
        ('^l', Choseong(L)),
        ('{,}l', Choseong(L)),
        ('l,', Jongseong(L)),
        ('l', Jongseong(L), Choseong(L)),
        ('m,', Jongseong(M)),
        ('m', Choseong(M)),
        ('n,', Jongseong(N)),
        ('n', Choseong(N)),
        ('p,', Jongseong(B)),
        ('p', Choseong(P)),
        ('r', Choseong(L)),
        ('s', Choseong(S)),
        ('t', Choseong(T)),
        ('v', Choseong(B)),
        ('z', Choseong(J)),
        ('Ja', Jungseong(YA)),
        ('Je', Jungseong(YE)),
        ('Ji', Jungseong(I)),
        ('Jo', Jungseong(YO)),
        ('Ju', Jungseong(YU)),
        ('a', Jungseong(A)),
        ('e', Jungseong(E)),
        ('i', Jungseong(I)),
        ('o', Jungseong(O)),
        ('u', Jungseong(U))
    ])

    def normalize(self, string):
        def normalize_only_unsafe(string):
            map = {'Á': 'á',
                   'Ä': 'ä',
                   'Č': 'č',
                   'Ď': 'ď',
                   'É': 'é',
                   'Í': 'í',
                   'Ĺ': 'ĺ',
                   'Ľ': 'ľ',
                   'Ň': 'ň',
                   'Ó': 'ó',
                   'Ô': 'ô',
                   'Ŕ': 'ŕ',
                   'Š': 'š',
                   'Ť': 'ť',
                   'Ú': 'ú',
                   'Ý': 'ý',
                   'Ž': 'ž'}
            safe = list(map.keys()) + list(map.values())
            for c in string:
                if c not in safe:
                    yield normalize_roman(c)
                elif c in map:
                    yield map[c]
                else:
                    yield c
        return ''.join(normalize_only_unsafe(string))


__lang__ = Slovak
