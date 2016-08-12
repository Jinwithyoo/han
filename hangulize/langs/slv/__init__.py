# -*- coding: utf-8 -*-
from hangulize import *


class Slovene(Language):
    """For transcribing Slovene."""

    __iso639__ = {1: 'sl', 2: 'slv', 3: 'slv'}
    __tmp__ = ',;'

    vowels = 'aeioOuU'
    vl = 'cCfkpsSt' # voiceless obstruents
    notation = Notation([
        ('č', 'C'),
        ('š', 'S'),
        ('ž', 'Z'),
        ('ö', 'O'),
        ('ü', 'U'),
        ('đ', 'dZ'),
        ('qu', 'kv'),
        ('q', 'k'),
        ('w', 'v'),
        ('x', 'ks'),
        ('^y{@}', 'J'),
        ('{@}y{@}', 'J'),
        ('iy', 'i'),
        ('y', 'i'),
        ('^j{@}', 'J'),
        ('{@}j{@}', 'J'),
        ('{c|C|S|z|Z}j{@}', None),
        ('sje', 'sJe'),
        ('je', 'ie'),
        ('{l|n|s}j{@}', 'J'),
        ('{l|n}j', None),
        ('ij', 'i'),
        ('j', 'i'),
        ('v{@}', 'V'),
        ('v', 'u'),
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
        ('g{<vl>}', 'k'),
        ('g$', 'k'),
        ('z{<vl>}', 's'),
        ('z$', 's'),
        ('Z{<vl>}', 'S'),
        ('Z$', 'S'),
        ('C{@}', 'c'),
        ('C', 'ci'),
        ('SS', 'S'),
        ('S{@}', 'sJ'),
        ('S$', 'si'),
        ('S', 'sJu'),
        ('ZZ', 'Z'),
        ('dZ{@}', 'z'),
        ('dZ', 'zi'),
        ('Z{@}', 'z'),
        ('Z', 'zu'),
        ('aa', 'a'),
        ('bb', 'b'),
        ('dd', 'd'),
        ('ee', 'e'),
        ('ff', 'f'),
        ('gg', 'g'),
        ('hh', 'h'),
        ('ii', 'i'),
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
        ('zz', 'z'),
        ('dz', 'z'),
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
        ('m{@}', 'm;'),
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
        ('V', Choseong(B)),
        ('z', Choseong(J)),
        ('Ja', Jungseong(YA)),
        ('Je', Jungseong(YE)),
        ('Ji', Jungseong(I)),
        ('Jo', Jungseong(YO)),
        ('JO', Jungseong(YO)),
        ('Ju', Jungseong(YU)),
        ('JU', Jungseong(YU)),
        ('a', Jungseong(A)),
        ('e', Jungseong(E)),
        ('i', Jungseong(I)),
        ('o', Jungseong(O)),
        ('O', Jungseong(OE)),
        ('u', Jungseong(U)),
        ('U', Jungseong(WI))
    ])

    def normalize(self, string):
        return normalize_roman(string, {
            'Č': 'č', 'Š': 'š', 'Ž': 'ž', 'Ö': 'ö', 'Ü': 'ü',
            'Ć': 'č', 'ć': 'č', 'Đ': 'đ'
        })


__lang__ = Slovene
