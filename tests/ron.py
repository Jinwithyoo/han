# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.ron import Romanian


class RomanianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0211.jsp """

    lang = Romanian()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0109.jsp """
        self.assert_examples({
            'bibliotecă': '비블리오테커',
            'alb': '알브',
            'Cîntec': '큰테크',
            'Cine': '치네',
            'factură': '팍투러',
            'Moldova': '몰도바',
            'Brad': '브라드',
            'Focşani': '폭샤니',
            'Cartof': '카르토프',
            'Galaţi': '갈라치',
            'Gigel': '지젤',
            'hering': '헤린그',
            'haţeg': '하체그',
            'duh': '두흐',
            'Jiu': '지우',
            'Cluj': '클루지',
            'kilogram': '킬로그람',
            'bibliotecă': '비블리오테커',
            'hotel': '호텔',
            'Maramureş': '마라무레슈',
            'Avram': '아브람',
            'Nucet': '누체트',
            'Bran': '브란',
            'pumn': '품느',
            'pianist': '피아니스트',
            'septembrie': '셉템브리에',
            'cap': '카프',
            'radio': '라디오',
            'dor': '도르',
            'Sibiu': '시비우',
            'pas': '파스',
            'şag': '샤그',
            'Mureş': '무레슈',
            'telefonist': '텔레포니스트',
            'bilet': '빌레트',
            'ţigară': '치가러',
            'braţ': '브라츠',
            'Victoria': '빅토리아',
            'Braşov': '브라쇼브',
            'taxi': '탁시',
            'examen': '에그자멘',
            'ziar': '지아르',
            'autobuz': '아우토부즈',
            'Cheia': '케이아',
            'Gheorghe': '게오르게',
            'Arad': '아라드',
            'Bacău': '바커우',
            'Elena': '엘레나',
            'pianist': '피아니스트',
            'Cîmpina': '큼피나',
            'România': '로므니아',
            'Oradea': '오라데아',
            'Nucet': '누체트',
        })

    def test_1st(self):
        """제1항: c, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        self.assert_examples({
            'cap': '카프',
            'Cîntec': '큰테크',
            'factură': '팍투러',
            'septembrie': '셉템브리에',
        })

    def test_2nd(self):
        """제2항: c, g
        c, g는 e, i 앞에서는 각각 'ㅊ', 'ㅈ'으로, 그 밖의 모음 앞에서는 'ㅋ',
        'ㄱ'으로 적는다.
        """
        self.assert_examples({
            'cap': '카프',
            'centru': '첸트루',
            'Galaţi': '갈라치',
            'Gigel': '지젤',
        })

    def test_3rd(self):
        """제3항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            'clei': '클레이',
        })

    def test_4th(self):
        """제4항: n
        n이 어말에서 m 뒤에 올 때는 '으'를 붙여 적는다.
        """
        self.assert_examples({
            'lemn': '렘느',
            'pumn': '품느',
        })

    def test_5th(self):
        """제5항: e
        e는 '에'로 적되, 인칭 대명사 및 동사 este, era 등의 어두 모음 e는
        '예'로 적는다.
        """
        self.assert_examples({
            'Emil': '에밀',
            'eu': '예우',
            'el': '옐',
            'este': '예스테',
            'era': '예라',
        })

    def test_etc(self):
        self.assert_examples({
            'Sturdza': '스투르자',
            'Theodor': '테오도르',
        })