# -*- coding: utf-8 -*-
import unittest
from hangulize import *
from cmds import repl
from tests import HangulizeTestCase


class APITestCase(unittest.TestCase):

    import hangulize.langs
    langs = hangulize.langs.list_langs()

    def test_toplevel_langs(self):
        assert 'ita' in self.langs
        assert 'jpn' in self.langs
        assert 'kat' in self.langs
        assert 'por' in self.langs

    def test_sub_langs(self):
        assert 'kat.narrow' in self.langs
        assert 'por.br' in self.langs

    def test_only_langs(self):
        assert '__init__' not in self.langs

    def test_deprecated_langs(self):
        assert 'it' not in self.langs
        assert 'ja' not in self.langs

    def test_logger(self):
        import logging
        class TestHandler(logging.StreamHandler):
            msgs = []
            def handle(self, record):
                self.msgs.append(record.msg)
            @property
            def result(self):
                return '\n'.join(self.msgs)
        logger = logging.getLogger('test')
        handler = TestHandler()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        hangulize('gloria', 'ita', logger=logger)
        assert ">> 'gloria'" in handler.result

    def test_singleton(self):
        from hangulize import get_lang
        from hangulize.langs.ita import Italian
        from hangulize.langs.jpn import Japanese
        assert Italian() is Italian()
        assert get_lang('ita') is Italian()
        assert get_lang('ita') is get_lang('ita')
        assert Japanese() is Japanese()
        assert get_lang('jpn') is Japanese()
        assert get_lang('jpn') is get_lang('jpn')
        assert Italian() is not Japanese()
        assert get_lang('ita') is not Japanese()
        assert get_lang('ita') is not get_lang('jpn')

    def test_sub_lang(self):
        from hangulize import get_lang
        assert get_lang('kat.narrow')

    def test_normalize(self):
        from hangulize.normalization import normalize_roman
        assert 'abc' == normalize_roman('AbC')
        assert 'a/a' == normalize_roman('Ä/ä')
        assert 'o/o' == normalize_roman('Ö/ö')
        assert 'u/u' == normalize_roman('Ü/ü')
        assert '한글' == normalize_roman('한글')
        assert 'a한글o' == normalize_roman('Ä한글Ö')
        assert 'a한u글o' == normalize_roman('Ä한ü글Ö')
        assert '123aehtw' == normalize_roman('123ǞËḧT̈Ẅ')

    def test_str(self):
        from hangulize import hangulize
        hangulize('Hello', 'ita')

    def test_supports(self):
        from hangulize import supports
        assert supports('lat')
        assert supports('lit')
        assert supports('ell')
        assert not supports('nex')


class PatternTestCase(HangulizeTestCase):

    class TestLang(Language):
        vowels = 'a', 'i', 'u', 'e', 'o'
        voiced = 'b', 'd', 'g'
        voiceless = 'ptk'
        longvowels = 'AIUEO'
        cons = 'bcdfghjklmnpqrstvwxyz'
        notation = Notation([
            ('van gogh', split_phonemes('반 고흐')),
            ('^^l', Choseong(L)),
            ('^l', Choseong(N)),
            ('l', Jongseong(L), Choseong(L)),
            ('q$$', split_phonemes('쿸')),
            ('q$', Jongseong(K)),
            ('zu', Choseong(J), Jungseong(EU)),
            ('ju', (Choseong(J), Jungseong(YU))),
            ('y(o)', Jungseong(YO)),
            ('y{a}', Jungseong(YA)),
            ('y{~a}', Jungseong(I)),
            ('t{~a|i}', Choseong(C)),
            ('(sh|xh|z)', 'S'),
            ('(<voiceless>|x){@}', 'X'),
            ('^^{a}b', Choseong(BB)),
            ('^{a}b', Jongseong(P)),
            ('b{o}$', Choseong(P)),
            ('{a}(<voiceless>)', '<voiced>e'),
            ('{<cons>}<vowels>{gh}', '<longvowels>'),
            ("d'i", 'di'),
            ("d i", 'di'),
            ('X', Choseong(GG)),
            ('S', Choseong(SS)),
            ('p', Choseong(P)),
            ('t', Choseong(T)),
            ('k', Choseong(K)),
            ('b', (Choseong(B),)),
            ('d', (Choseong(D),)),
            ('g', (Choseong(G),)),
            ('a', (Jungseong(A),)),
            ('i', (Jungseong(I),)),
            ('u', (Jungseong(U),)),
            ('e', (Jungseong(E),)),
            ('o', (Jungseong(O),)),
            ('c', (Choseong(C),)),
            ('O', (Jungseong(O), Jungseong(U))),
            ('h$', (Jongseong(H))),
        ])
        def normalize(self, string):
            return normalize_roman(string)

    lang = TestLang()

    def test_separator(self):
        self.assert_examples({'shazixhu': '싸씨쑤'})

    def test_variable(self):
        self.assert_examples({
            'xupatiku': '꾸까끼꾸',
            'ptiku': '프끼꾸'
        })

    def test_phonemes(self):
        self.assert_examples({'zuju': '즈쥬'})

    def test_caret_before_curly_bracket(self):
        self.assert_examples({'la abba': '라 앞바'})

    def test_dollar_after_curly_bracket(self):
        self.assert_examples({'bbo': '브포'})

    def test_variable_replacement(self):
        self.assert_examples({
            'gap': '가베',
            'bakk': '바게크',
            'tatkak': '까츠까게',
            'cogh': '초우긓',
        })

    def test_start_of_string(self):
        self.assert_examples({'lalala': '랄랄라'})

    def test_start_of_word(self):
        self.assert_examples({
            'lala lalala': '랄라 날랄라',
            'abba': '아쁘바'
        })

    def test_end_of_string(self):
        self.assert_examples({
            'babeq': '바베쿸',
            'babeq ku': '바벸 꾸'
        })

    def test_special_character(self):
        self.assert_examples({"d'i": '디'})

    def test_space(self):
        self.assert_examples({
            'd i': '디',
            'van Gogh': '반 고흐'
        })

    def test_negative_lookaround(self):
        self.assert_examples({
            'ya': '야아',
            'yo': '요',
            'yu': '이우',
            'titatutote': '끼까추초체'
        })

    def test_zero_width_space(self):
        class AmoLang(Language):
            notation = Notation([
                ('-', '/'),
                ('m$', Jongseong(M)),
                ('m', Choseong(M)),
                ('a', Jungseong(A)),
                ('o', Jungseong(O)),
            ])
        self.assert_examples({
            'am-o': '암오',
            'amo': '아모',
            'am o': '암 오'
        }, lang=AmoLang())

    def test_group_reference(self):
        class GrpRefLang(Language):
            notation = Notation([('(ab)c', r'\1')])
        self.assert_examples({'abc': 'ab'}, lang=GrpRefLang())


class AlgorithmTestCase(HangulizeTestCase):

    def test_phunctuation(self):
        """이슈5: 문장부호에 맞붙은 글자가 시작 글자 또는 끝 글자로 인식 안 됨
        http://github.com/sublee/hangulize/issues#issue/5
        """
        assert hangulize('nad', 'pol') + ',' == hangulize('nad,', 'pol')
        assert '.' + hangulize('jak', 'pol') == hangulize('.jak', 'pol')
        self.assert_examples({
            'nad, nad jak .jak': '나트, 나트 야크 .야크',
        }, 'pol')

    def test_wide_letter(self):
        self.assert_examples({'guaguam': '과괌'}, 'spa')

    def test_empty_sequence(self):
        """아무 규칙에도 매치되지 않아 빈 시퀀스가 반환될 때 다음 에러가 발생:

            TypeError: reduce() of empty sequence with no initial value
        """
        self.assert_examples({'h': ''}, 'ita')

    def test_special_chars(self):
        self.assert_examples({
            'leert,': '레이르트,',
            '(leert}': '(레이르트}',
            '"leert"': '"레이르트"',
        }, 'nld')
        self.assert_examples({
            'Търговище,': '터르고비슈테,',
        }, 'bul')

    def test_tmp_chars(self):
        averroes = hangulize('Averroës', 'lat')
        self.assert_examples({
            '%Averroës': '%' + averroes,
            '%Averroës%': '%' + averroes + '%',
            'Averroës%': averroes + '%',
        }, 'lat')

    def test_mixed_with_hangul(self):
        self.assert_examples({
            'とうめい 고속도로': '도메이 고속도로',
            'からふと 섬': '가라후토 섬',
            'とさ 만': '도사 만',
            'This is 삼천えん': 'This is 삼천엔',
        }, 'jpn')
        self.assert_examples({
            '한gloria리랑': '한글로리아리랑',
        }, 'ita')

    def test_remove_char(self):
        #logger = repl.make_logger()
        class TestLang(Language):
            notation = Notation([
                ('k', Choseong(K)), ('i', Jungseong(I)),
                ('a', None), 
            ])
        self.assert_examples({
            'kaaai': '키',
            'aakaaaia': '키',
            'kiaakaaaiakiaaaaaaa': '키키키',
            'aaaiaaakkiaakaaaiakiaaaiaaakaaaa': '이크키키키이크',
            'aiakakaiakaiakaiaiaka': '이크키키키이크',
        }, TestLang())#, logger=logger)

    def test_too_many_rules(self):
        class TooHeavyLang(Language):
            notation = Notation([
                ('a', Jungseong(A)),  ('b', Choseong(B)),
                ('c', Choseong(C)),   ('d', Choseong(D)),
                ('e', Jungseong(E)),  ('f', Choseong(P)),
                ('g', Choseong(G)),   ('h', Choseong(H)),
                ('i', Jungseong(I)),  ('j', Choseong(J)),
                ('k', Choseong(K)),   ('l', Choseong(L)),
                ('m', Choseong(M)),   ('n', Choseong(N)),
                ('o', Jungseong(O)),  ('p', Choseong(P)),
                ('q', Choseong(K)),   ('r', Choseong(L)),
                ('s', Choseong(S)),   ('t', Choseong(T)),
                ('u', Jungseong(U)),  ('v', Choseong(B)),
                ('w', Jungseong(EU)), ('x', Choseong(GG)),
                ('y', Jungseong(I)),  ('z', Choseong(J)),

                ('A', Jungseong(A)),  ('B', Choseong(B)),
                ('C', Choseong(C)),   ('D', Choseong(D)),
                ('E', Jungseong(E)),  ('F', Choseong(P)),
                ('G', Choseong(G)),   ('H', Choseong(H)),
                ('I', Jungseong(I)),  ('J', Choseong(J)),
                ('K', Choseong(K)),   ('L', Choseong(L)),
                ('M', Choseong(M)),   ('N', Choseong(N)),
                ('O', Jungseong(O)),  ('P', Choseong(P)),
                ('Q', Choseong(K)),   ('R', Choseong(L)),
                ('S', Choseong(S)),   ('T', Choseong(T)),
                ('U', Jungseong(U)),  ('V', Choseong(B)),
                ('W', Jungseong(EU)), ('X', Choseong(GG)),
                ('Y', Jungseong(I)),  ('Z', Choseong(J)),

                ('a1', Jungseong(A)),  ('b1', Choseong(B)),
                ('c1', Choseong(C)),   ('d1', Choseong(D)),
                ('e1', Jungseong(E)),  ('f1', Choseong(P)),
                ('g1', Choseong(G)),   ('h1', Choseong(H)),
                ('i1', Jungseong(I)),  ('j1', Choseong(J)),
                ('k1', Choseong(K)),   ('l1', Choseong(L)),
                ('m1', Choseong(M)),   ('n1', Choseong(N)),
                ('o1', Jungseong(O)),  ('p1', Choseong(P)),
                ('q1', Choseong(K)),   ('r1', Choseong(L)),
                ('s1', Choseong(S)),   ('t1', Choseong(T)),
                ('u1', Jungseong(U)),  ('v1', Choseong(B)),
                ('w1', Jungseong(EU)), ('x1', Choseong(GG)),
                ('y1', Jungseong(I)),  ('z1', Choseong(J)),

                ('A1', Jungseong(A)),  ('B1', Choseong(B)),
                ('C1', Choseong(C)),   ('D1', Choseong(D)),
                ('E1', Jungseong(E)),  ('F1', Choseong(P)),
                ('G1', Choseong(G)),   ('H1', Choseong(H)),
                ('I1', Jungseong(I)),  ('J1', Choseong(J)),
                ('K1', Choseong(K)),   ('L1', Choseong(L)),
                ('M1', Choseong(M)),   ('N1', Choseong(N)),
                ('O1', Jungseong(O)),  ('P1', Choseong(P)),
                ('Q1', Choseong(K)),   ('R1', Choseong(L)),
                ('S1', Choseong(S)),   ('T1', Choseong(T)),
                ('U1', Jungseong(U)),  ('V1', Choseong(B)),
                ('W1', Jungseong(EU)), ('X1', Choseong(GG)),
                ('Y1', Jungseong(I)),  ('Z1', Choseong(J)),

                ('a2', Jungseong(A)),  ('b2', Choseong(B)),
                ('c2', Choseong(C)),   ('d2', Choseong(D)),
                ('e2', Jungseong(E)),  ('f2', Choseong(P)),
                ('g2', Choseong(G)),   ('h2', Choseong(H)),
                ('i2', Jungseong(I)),  ('j2', Choseong(J)),
                ('k2', Choseong(K)),   ('l2', Choseong(L)),
                ('m2', Choseong(M)),   ('n2', Choseong(N)),
                ('o2', Jungseong(O)),  ('p2', Choseong(P)),
                ('q2', Choseong(K)),   ('r2', Choseong(L)),
                ('s2', Choseong(S)),   ('t2', Choseong(T)),
                ('u2', Jungseong(U)),  ('v2', Choseong(B)),
                ('w2', Jungseong(EU)), ('x2', Choseong(GG)),
                ('y2', Jungseong(I)),  ('z2', Choseong(J)),

                ('A2', Jungseong(A)),  ('B2', Choseong(B)),
                ('C2', Choseong(C)),   ('D2', Choseong(D)),
                ('E2', Jungseong(E)),  ('F2', Choseong(P)),
                ('G2', Choseong(G)),   ('H2', Choseong(H)),
                ('I2', Jungseong(I)),  ('J2', Choseong(J)),
                ('K2', Choseong(K)),   ('L2', Choseong(L)),
                ('M2', Choseong(M)),   ('N2', Choseong(N)),
                ('O2', Jungseong(O)),  ('P2', Choseong(P)),
                ('Q2', Choseong(K)),   ('R2', Choseong(L)),
                ('S2', Choseong(S)),   ('T2', Choseong(T)),
                ('U2', Jungseong(U)),  ('V2', Choseong(B)),
                ('W2', Jungseong(EU)), ('X2', Choseong(GG)),
                ('Y2', Jungseong(I)),  ('Z2', Choseong(J)),

                ('a3', Jungseong(A)),  ('b3', Choseong(B)),
                ('c3', Choseong(C)),   ('d3', Choseong(D)),
                ('e3', Jungseong(E)),  ('f3', Choseong(P)),
                ('g3', Choseong(G)),   ('h3', Choseong(H)),
                ('i3', Jungseong(I)),  ('j3', Choseong(J)),
                ('k3', Choseong(K)),   ('l3', Choseong(L)),
                ('m3', Choseong(M)),   ('n3', Choseong(N)),
                ('o3', Jungseong(O)),  ('p3', Choseong(P)),
                ('q3', Choseong(K)),   ('r3', Choseong(L)),
                ('s3', Choseong(S)),   ('t3', Choseong(T)),
                ('u3', Jungseong(U)),  ('v3', Choseong(B)),
                ('w3', Jungseong(EU)), ('x3', Choseong(GG)),
                ('y3', Jungseong(I)),  ('z3', Choseong(J)),

                ('A3', Jungseong(A)),  ('B3', Choseong(B)),
                ('C3', Choseong(C)),   ('D3', Choseong(D)),
                ('E3', Jungseong(E)),  ('F3', Choseong(P)),
                ('G3', Choseong(G)),   ('H3', Choseong(H)),
                ('I3', Jungseong(I)),  ('J3', Choseong(J)),
                ('K3', Choseong(K)),   ('L3', Choseong(L)),
                ('M3', Choseong(M)),   ('N3', Choseong(N)),
                ('O3', Jungseong(O)),  ('P3', Choseong(P)),
                ('Q3', Choseong(K)),   ('R3', Choseong(L)),
                ('S3', Choseong(S)),   ('T3', Choseong(T)),
                ('U3', Jungseong(U)),  ('V3', Choseong(B)),
                ('W3', Jungseong(EU)), ('X3', Choseong(GG)),
                ('Y3', Jungseong(I)),  ('Z3', Choseong(J)),

                ('a4', Jungseong(A)),  ('b4', Choseong(B)),
                ('c4', Choseong(C)),   ('d4', Choseong(D)),
                ('e4', Jungseong(E)),  ('f4', Choseong(P)),
                ('g4', Choseong(G)),   ('h4', Choseong(H)),
                ('i4', Jungseong(I)),  ('j4', Choseong(J)),
                ('k4', Choseong(K)),   ('l4', Choseong(L)),
                ('m4', Choseong(M)),   ('n4', Choseong(N)),
                ('o4', Jungseong(O)),  ('p4', Choseong(P)),
                ('q4', Choseong(K)),   ('r4', Choseong(L)),
                ('s4', Choseong(S)),   ('t4', Choseong(T)),
                ('u4', Jungseong(U)),  ('v4', Choseong(B)),
                ('w4', Jungseong(EU)), ('x4', Choseong(GG)),
                ('y4', Jungseong(I)),  ('z4', Choseong(J)),

                ('A4', Jungseong(A)),  ('B4', Choseong(B)),
                ('C4', Choseong(C)),   ('D4', Choseong(D)),
                ('E4', Jungseong(E)),  ('F4', Choseong(P)),
                ('G4', Choseong(G)),   ('H4', Choseong(H)),
                ('I4', Jungseong(I)),  ('J4', Choseong(J)),
                ('K4', Choseong(K)),   ('L4', Choseong(L)),
                ('M4', Choseong(M)),   ('N4', Choseong(N)),
                ('O4', Jungseong(O)),  ('P4', Choseong(P)),
                ('Q4', Choseong(K)),   ('R4', Choseong(L)),
                ('S4', Choseong(S)),   ('T4', Choseong(T)),
                ('U4', Jungseong(U)),  ('V4', Choseong(B)),
                ('W4', Jungseong(EU)), ('X4', Choseong(GG)),
                ('Y4', Jungseong(I)),  ('Z4', Choseong(J)),
            ])
        self.assert_examples({'ab': '아브'}, TooHeavyLang())


class TestCaseTestCase(unittest.TestCase):

    def test_capture_examples(self):
        return
        import hangulize.langs
        langs = hangulize.langs.list_langs()
        for i in range(len(langs)):
            lang = langs.pop(0)
            test = lang.replace('.', '_')
            test = getattr(__import__('tests.%s' % test), test)
            try:
                test_case = getattr(test, [x for x in dir(test) \
                                             if x.endswith('TestCase')][0])
                test_method = [x for x in dir(test_case) \
                               if x.startswith('test')][0]
            except IndexError:
                continue
            assert isinstance(test_case.get_examples(test_method), dict)


try:
    get_lang('it', iso639=1)
    class LanguageCodeTestCase(unittest.TestCase):

        table = [('bg', 'bul', 'bul'),
                 ('ca', 'cat', 'cat'),
                 ('cs', 'cze', 'ces'),
                 ('cy', 'wel', 'cym'),
                 ('de', 'ger', 'deu'),
                 ('el', 'gre', 'ell'),
                 ('et', 'est', 'est'),
                 ('fi', 'fin', 'fin'),
                 (None, 'grc', 'grc'),
                 (None, None, 'hbs'),
                 ('hu', 'hun', 'hun'),
                 ('ja', 'jpn', 'jpn')]

        def test_regard_iso639_1(self):
            assert type(get_lang('bg', iso639=1)) is type(get_lang('bg'))
            assert type(get_lang('ja', iso639=1)) is type(get_lang('ja'))

        def test_iso639_1(self):
            for iso639_1, iso639_2, iso639_3 in self.table:
                if not iso639_1:
                    continue
                assert type(get_lang(iso639_3)) is type(get_lang(iso639_1,
                                                                 iso639=1))

        def test_iso639_2(self):
            for iso639_1, iso639_2, iso639_3 in self.table:
                if not iso639_2:
                    continue
                assert type(get_lang(iso639_3)) is type(get_lang(iso639_2,
                                                                 iso639=2))

        def test_iso639_3(self):
            for iso639_1, iso639_2, iso639_3 in self.table:
                assert type(get_lang(iso639_3)) is type(get_lang(iso639_3,
                                                                 iso639=3))
except ImportError:
    pass
