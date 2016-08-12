# -*- coding: utf-8 -*-
from hangulize import *


class SerboCroatian(Language):
    """For transcribing Serbo-Croatian."""

    __iso639__ = {3: 'hbs'}

    vowels = 'aeiouy'
    consonants = 'cCfhst'
    notation = Notation([
        ('č',                   'C'),
        ('ć',                   'C'),
        ('đ',                   'D'),
        ('š',                   'S'),
        ('dž',                  'D'),
        ('ž',                   'Z'),
        ('tj',                   'C'),
        ('S{@}',                 'sJ'),
        ('S$',                   'si'),
        ('S',                    'sJu'),
        ('^je',                  'Je'),
        ('{@|s}je',              'Je'),
        ('je',                   'e'),
        ('{l|n}j{@}',            'J'),
        ('{l|n}j',               None),
        ('j{@}',                 'J'),
        ('j',                    'i'),
        ('xx',                   'x'),
        ('x',                    'ks'),
        ('qu',                   'kv'),
        ('q',                    'k'),
        ('w',                    'v'),
        ('^y{@}',                'J'),
        ('y',                    'i'),
        ('aa',                   'a'),
        ('bb',                   'b'),
        ('dd',                   'd'),
        ('ee',                   'e'),
        ('ff',                   'f'),
        ('gg',                   'g'),
        ('hh',                   'h'),
        ('ii',                   'i'),
        ('kk',                   'k'),
        ('ll',                   'l'),
        ('{@}mm{@}',             Jongseong(M), Choseong(M)),
        ('mm',                   'm'),
        ('{@}nn{@}',             Jongseong(N), Choseong(N)),
        ('nn',                   'n'),
        ('oo',                   'o'),
        ('pp',                   'p'),
        ('rr',                   'r'),
        ('ss',                   's'),
        ('tt',                   't'),
        ('uu',                   'u'),
        ('vv',                   'v'),
        ('zz',                   'z'),
        ('^k',                   Choseong(K)),
        ('{@}k{<consonants>|p}', Jongseong(G)),
        ('^p',                   Choseong(P)),
        ('{@}p{<consonants>|k}', Jongseong(B)),
        ('k',                    Choseong(K)),
        ('p',                    Choseong(P)),
        ('C{@}',                 Choseong(C)),
        ('C',                    Choseong(C), Jungseong(I)),
        ('b',                    Choseong(B)),
        ('c',                    Choseong(C)),
        ('d',                    Choseong(D)),
        ('D{@}',                 Choseong(J)),
        ('D',                    Choseong(J), Jungseong(I)),
        ('f',                    Choseong(P)),
        ('g',                    Choseong(G)),
        ('h',                    Choseong(H)),
        ('^m',                   'P'),
        ('^n',                   'Q'),
        ('^l',                   Choseong(L)),
        ('{m|n}l',               Choseong(L)),
        ('l{@|J}',               Jongseong(L), Choseong(L)),
        ('l',                    Jongseong(L)),
        ('P',                    Choseong(M)),
        ('m{@|J|l|r|n}',         Choseong(M)),
        ('m',                    Jongseong(M)),
        ('Q',                    Choseong(N)),
        ('n{@|J}',               Choseong(N)),
        ('n',                    Jongseong(N)),
        ('r',                    Choseong(L)),
        ('s',                    Choseong(S)),
        ('t',                    Choseong(T)),
        ('v',                    Choseong(B)),
        ('z',                    Choseong(J)),
        ('Z{@}',                 Choseong(J)),
        ('Z',                    Choseong(J), Jungseong(U)),
        ('Ja',                   Jungseong(YA)),
        ('Je',                   Jungseong(YE)),
        ('Ji',                   Jungseong(I)),
        ('Jo',                   Jungseong(YO)),
        ('Ju',                   Jungseong(YU)),
        ('a',                    Jungseong(A)),
        ('e',                    Jungseong(E)),
        ('i',                    Jungseong(I)),
        ('o',                    Jungseong(O)),
        ('u',                    Jungseong(U))
    ])

    def normalize(self, string):
        return normalize_roman(string, {
            'А': 'a', 'а': 'a', 'Б': 'b', 'б': 'b', 'В': 'v',
            'в': 'v', 'Г': 'g', 'г': 'g', 'Д': 'd', 'д': 'd',
            'Ђ': 'đ', 'ђ': 'đ', 'Е': 'e', 'е': 'e', 'Ж': 'ž',
            'ж': 'ž', 'З': 'z', 'з': 'z', 'И': 'i', 'и': 'i',
            'Ј': 'j', 'ј': 'j', 'К': 'k', 'к': 'k', 'Л': 'l',
            'л': 'l', 'Љ': 'lj', 'љ': 'lj', 'М': 'm', 'м': 'm',
            'Н': 'n', 'н': 'n', 'Њ': 'nj', 'њ': 'nj', 'О': 'o',
            'о': 'o', 'П': 'p', 'п': 'p', 'Р': 'r', 'р': 'r',
            'С': 's', 'с': 's', 'Т': 't', 'т': 't', 'Ћ': 'ć',
            'ћ': 'ć', 'У': 'u', 'у': 'u', 'Ф': 'f', 'ф': 'f',
            'Х': 'h', 'х': 'h', 'Ц': 'c', 'ц': 'c', 'Ч': 'C',
            'ч': 'C', 'Џ': 'dž', 'џ': 'dž', 'Ш': 'š', 'ш': 'š',
            'Č': 'č', 'Ć': 'ć', 'Đ': 'đ', 'Š': 'š', 'Ž': 'ž',
            'Ǆ': 'dž', # DŽ digraph
            'ǅ': 'dž', # Dž digraph
            'Ǉ': 'lj', # LJ digraph
            'ǈ': 'lj', # Lj digraph
            'Ǌ': 'nj', # NJ digraph
            'ǋ': 'nj' # Nj digraph
        })


__lang__ = SerboCroatian
