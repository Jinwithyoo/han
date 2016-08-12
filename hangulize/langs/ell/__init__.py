# -*- coding: utf-8 -*-
from hangulize import *


class Greek(Language):
    """For transcribing Modern Greek."""

    __iso639__ = {1: 'el', 2: 'gre', 3: 'ell'}
    __tmp__ = '-,;'

    vowels = 'αάεέηήιίϊοόυύϋωώΥ'
    sv = 'αεηιουω'
    av = 'άέήίόύώ'
    cs = 'βγδζθκλμνξπρστφχψΙΝΤΧ'
    vl = 'θκξπστφχψΤΧ'
    v = 'βγδζλμνρΙΝ'
    s = 'λμνρ'
    notation = Notation([
        ('(<sv>)\u0300', '(<av>)'),
        ('\u0300', None),
        ('(<sv>)\u0301', '(<av>)'),
        ('\u0301', None),
        ('(<sv>)\u0342', '(<av>)'),
        ('\u0342', None),
        ('\u0344', '\u0308'),
        ('ι\u0308', 'ϊ'),
        ('ί\u0308', 'ϊ'),
        ('υ\u0308', 'ϋ'),
        ('ύ\u0308', 'ϋ'),
        ('\u0304', None),
        ('\u0313', None),
        ('\u0343', None),
        ('\u0314', None),
        ('\u1FDD', None),
        ('\u1FDE', None),
        ('\u1FDF', None),
        ('\u1FFE', None),
        ('{@}ϊ{@}', '-ι-'),
        ('{@}ϊ', '-ι'),
        ('ϊ{@}', 'ι-'),
        ('ϊ', 'ι'),
        ('{@}ϋ{@}', '-υ-'),
        ('{@}ϋ', '-υ'),
        ('ϋ{@}', 'υ-'),
        ('ϋ', 'υ'),
        ('{α|ε|η}υ{@|<v>}', 'β'),
        ('{α|ε|η}ύ{@|<v>}', 'β'),
        ('{α|ε|η}υ', 'φ'),
        ('{α|ε|η}ύ', 'φ'),
        ('αι', 'ε'),
        ('ει', 'ι'),
        ('οι', 'ι'),
        ('ου', 'Υ'),
        ('υι', 'ι'),
        ('η', 'ι'),
        ('υ', 'ι'),
        ('{@}γγι', 'Νγ-ι'),
        ('γι{@}', 'Ι'),
        ('αί', 'ε'),
        ('εί', 'ι'),
        ('οί', 'ι'),
        ('ού', 'Υ'),
        ('υί', 'ι'),
        ('ά', 'α'),
        ('έ', 'ε'),
        ('ή', 'ι'),
        ('ί', 'ι'),
        ('ό', 'ο'),
        ('ύ', 'ι'),
        ('ω', 'ο'),
        ('ώ', 'ο'),
        ('{@}γγ{ε|ι}', 'Νγ-'),
        ('γ{ε|ι}', 'Ι'),
        ('{@}νγ{κ|ξ}', 'γ'),
        ('{@}νκτ', 'γκτ'),
        ('{@}γγ', 'Νγ'),
        ('{@}γκ{@|<s>}', 'Νγ'),
        ('{@}γκ', 'Ν'),
        ('{@}γ{ξ|χ}', 'Ν'),
        ('γκ', 'γ'),
        ('μπ{τ}', 'μ'),
        ('{@}μπ', 'μβ'),
        ('{@}μπ', 'μβ'),
        ('μπ', 'β'),
        ('{@}ν{γ|κ|χ}', 'Ν'),
        ('{@}ντζ', 'νζ'),
        ('{@}ντσ', 'νΤ'),
        ('{@}ντ', 'νδ'),
        ('ντ', 'δ'),
        ('τζ', 'ζ'),
        ('τσ', 'Τ'),
        ('ξ', 'κσ'),
        ('ψ', 'πσ'),
        ('ββ', 'β'),
        ('γγ', 'γ'),
        ('δδ', 'δ'),
        ('ζζ', 'ζ'),
        ('θθ', 'θ'),
        ('κκ', 'κ'),
        ('^κχ', 'Χ'),
        ('κχ{β|γ|δ|ζ|κ|μ|ξ|π|σ|φ|χ|ψ|Ι|Τ}', 'Χ'),
        ('λλ', 'λ'),
        ('μμ', 'μ'),
        ('νν', 'ν'),
        ('ππ', 'π'),
        ('πφ', 'φ'),
        ('ρρ', 'ρ'),
        ('σσ', 'σ'),
        ('ττ', 'τ'),
        ('τθ', 'θ'),
        ('φφ', 'φ'),
        ('χχ', 'χ'),
        ('^κ', 'κ;'),
        ('{<cs>}κ', 'κ;'),
        ('κ{<vl>}', 'κ,'),
        ('^π', 'π;'),
        ('{<cs>}π', 'π;'),
        ('π{<vl>}', 'π,'),
        (';', None),
        ('Χ', 'κ'),
        ('^λ', 'λ;'),
        ('^μ', 'μ;'),
        ('^ν', 'ν;'),
        ('λ$', 'λ,'),
        ('μ$', 'μ,'),
        ('ν$', 'ν,'),
        ('λ{@|μ,|ν,}', 'λ;'),
        ('μ{@}', 'μ;'),
        ('ν{@}', 'ν;'),
        ('λ', 'λ,'),
        ('μ', 'μ,'),
        ('ν', 'ν,'),
        ('Ν', 'Ν,'),
        (',,', ','),
        (',;', None),
        (',λ,', 'λ,'),
        (',μ,', 'μ,'),
        (',ν,', 'ν,'),
        ('λ{μ;|ν;}', 'λ,'),
        (';', None),
        ('{<cs>}Ι', 'ΨΙ'),
        ('β', Choseong(B)),
        ('γ', Choseong(G)),
        ('δ', Choseong(D)),
        ('ζ', Choseong(J)),
        ('θ', Choseong(T)),
        ('κ,', Jongseong(G)),
        ('κ', Choseong(K)),
        ('^λ', Choseong(L)),
        ('{,}λ', Choseong(L)),
        ('λ,', Jongseong(L)),
        ('λ', Jongseong(L), Choseong(L)),
        ('μ,', Jongseong(M)),
        ('μ', Choseong(M)),
        ('ν,', Jongseong(N)),
        ('ν', Choseong(N)),
        ('Ν', Jongseong(NG)),
        ('π,', Jongseong(B)),
        ('π', Choseong(P)),
        ('ρ', Choseong(L)),
        ('σ', Choseong(S)),
        ('τ', Choseong(T)),
        ('Τ', Choseong(C)),
        ('φ', Choseong(P)),
        ('χ', Choseong(H)),
        ('Ια', Jungseong(YA)),
        ('Ιε', Jungseong(YE)),
        ('Ιι', Jungseong(I)),
        ('Ιο', Jungseong(YO)),
        ('ΙΥ', Jungseong(YU)),
        ('α', Jungseong(A)),
        ('ε', Jungseong(E)),
        ('ι', Jungseong(I)),
        ('ο', Jungseong(O)),
        ('Υ', Jungseong(U)),
        ('Ψ', Choseong(NG)),
    ])

    def normalize(self, string):
        return normalize_roman(string, {
            'Α': 'α', 'Ἀ': 'α', 'ᾼ': 'α', 'ᾈ': 'α', 'ἀ': 'α',
            'ᾳ': 'α', 'ᾀ': 'α', 'Ᾱ': 'α', 'Ᾰ': 'α', 'ᾱ': 'α',
            'ᾰ': 'α', 'Ἁ': 'α', 'ᾉ': 'α', 'ᾁ': 'α', 'Ά': 'ά',
            'Ὰ': 'ά', 'Ἄ': 'ά', 'Ἂ': 'ά', 'Ἆ': 'ά', 'ᾌ': 'ά',
            'ᾊ': 'ά', 'ᾎ': 'ά', 'ὰ': 'ά', 'ᾶ': 'ά', 'ἄ': 'ά',
            'ἂ': 'ά', 'ἆ': 'ά', 'ᾴ': 'ά', 'ᾲ': 'ά', 'ᾷ': 'ά',
            'ᾄ': 'ά', 'ᾂ': 'ά', 'ᾆ': 'ά', 'Ἅ': 'ά', 'Ἃ': 'ά',
            'Ἇ': 'ά', 'ᾍ': 'ά', 'ᾋ': 'ά', 'ᾏ': 'ά', 'ἃ': 'ά',
            'ἇ': 'ά', 'ᾅ': 'ά', 'ᾃ': 'ά', 'ᾇ': 'ά', 'Β': 'β',
            'Γ': 'γ', 'Δ': 'δ', 'Ε': 'ε', 'Ἐ': 'ε', 'ἐ': 'ε',
            'Ἑ': 'ε', 'Έ': 'έ', 'Ὲ': 'έ', 'Ἔ': 'έ', 'Ἒ': 'έ',
            'έ': 'έ', 'ὲ': 'έ', 'ἔ': 'έ', 'ἒ': 'έ', 'Ἕ': 'έ',
            'Ἓ': 'έ', 'ἓ': 'έ', 'Ζ': 'ζ', 'Η': 'η', 'Ἠ': 'η',
            'ῌ': 'η', 'ᾘ': 'η', 'ἠ': 'η', 'ῃ': 'η', 'ᾐ': 'η',
            'Ἡ': 'η', 'ᾙ': 'η', 'ᾑ': 'η', 'Ή': 'ή', 'Ὴ': 'ή',
            'Ἤ': 'ή', 'Ἢ': 'ή', 'Ἦ': 'ή', 'ᾜ': 'ή', 'ᾚ': 'ή',
            'ᾞ': 'ή', 'ὴ': 'ή', 'ῆ': 'ή', 'ἤ': 'ή', 'ἢ': 'ή',
            'ἦ': 'ή', 'ῄ': 'ή', 'ῂ': 'ή', 'ῇ': 'ή', 'ᾔ': 'ή',
            'ᾒ': 'ή', 'ᾖ': 'ή', 'Ἥ': 'ή', 'Ἣ': 'ή', 'Ἧ': 'ή',
            'ᾝ': 'ή', 'ᾛ': 'ή', 'ᾟ': 'ή', 'ἣ': 'ή', 'ἧ': 'ή',
            'ᾕ': 'ή', 'ᾓ': 'ή', 'ᾗ': 'ή', 'Θ': 'θ', 'Ι': 'ι',
            'Ἰ': 'ι', 'ἰ': 'ι', 'Ῑ': 'ι', 'Ῐ': 'ι', 'ῑ': 'ι',
            'ῐ': 'ι', 'Ἱ': 'ι', 'Ί': 'ί', 'Ὶ': 'ί', 'Ἴ': 'ί',
            'Ἲ': 'ί', 'Ἶ': 'ί', 'ὶ': 'ί', 'ῖ': 'ί', 'ἴ': 'ί',
            'ἲ': 'ί', 'ἶ': 'ί', 'Ἵ': 'ί', 'Ἳ': 'ί', 'Ἷ': 'ί',
            'ἳ': 'ί', 'ἷ': 'ί', 'Ϊ': 'ϊ', 'ΐ': 'ϊ', 'ῒ': 'ϊ',
            'ῗ': 'ϊ', 'Κ': 'κ', 'Λ': 'λ', 'Μ': 'μ', 'Ν': 'ν',
            'Ξ': 'ξ', 'Ο': 'ο', 'Ὀ': 'ο', 'ὀ': 'ο', 'Ὁ': 'ο',
            'Ό': 'ό', 'Ὸ': 'ό', 'Ὄ': 'ό', 'Ὂ': 'ό', 'ὸ': 'ό',
            'ὄ': 'ό', 'ὂ': 'ό', 'Ὅ': 'ό', 'Ὃ': 'ό', 'ὃ': 'ό',
            'Π': 'π', 'Ρ': 'ρ', 'Ῥ': 'ρ', 'ῤ': 'ρ', 'ῥ': 'ρ',
            'Σ': 'σ', 'ς': 'σ', 'Τ': 'τ', 'Υ': 'υ', 'ὐ': 'υ',
            'Ῡ': 'υ', 'Ῠ': 'υ', 'ῡ': 'υ', 'ῠ': 'υ', 'Ὑ': 'υ',
            'Ύ': 'ύ', 'Ὺ': 'ύ', 'ὺ': 'ύ', 'ῦ': 'ύ', 'ὔ': 'ύ',
            'ὒ': 'ύ', 'ὖ': 'ύ', 'Ὕ': 'ύ', 'Ὓ': 'ύ', 'Ὗ': 'ύ',
            'ὓ': 'ύ', 'ὗ': 'ύ', 'Ϋ': 'ϋ', 'ΰ': 'ϋ', 'ῢ': 'ϋ',
            'ῧ': 'ϋ', 'Φ': 'φ', 'Χ': 'χ', 'Ψ': 'ψ', 'Ω': 'ω',
            'Ὠ': 'ω', 'ῼ': 'ω', 'ᾨ': 'ω', 'ὠ': 'ω', 'ῳ': 'ω',
            'ᾠ': 'ω', 'Ὡ': 'ω', 'ᾩ': 'ω', 'ᾡ': 'ω', 'Ώ': 'ώ',
            'Ὼ': 'ώ', 'Ὤ': 'ώ', 'Ὢ': 'ώ', 'Ὦ': 'ώ', 'ᾬ': 'ώ',
            'ᾪ': 'ώ', 'ᾮ': 'ώ', 'ὼ': 'ώ', 'ῶ': 'ώ', 'ὤ': 'ώ',
            'ὢ': 'ώ', 'ὦ': 'ώ', 'ῴ': 'ώ', 'ῲ': 'ώ', 'ῷ': 'ώ',
            'ᾤ': 'ώ', 'ᾢ': 'ώ', 'ᾦ': 'ώ', 'Ὥ': 'ώ', 'Ὣ': 'ώ',
            'Ὧ': 'ώ', 'ᾭ': 'ώ', 'ᾫ': 'ώ', 'ᾯ': 'ώ', 'ὣ': 'ώ',
            'ὧ': 'ώ', 'ᾥ': 'ώ', 'ᾣ': 'ώ', 'ᾧ': 'ώ'
        })


__lang__ = Greek