# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.hbs import SerboCroatian


class SerboCroatianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0210.jsp """

    lang = SerboCroatian()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0108.jsp """
        self.assert_examples({
            'bog': '보그',
            'drobnjak': '드로브냐크',
            'pogreb': '포그레브',
            'cigara': '치가라',
            'novac': '노바츠',
            'čelik': '첼리크',
            'točka': '토치카',
            'kolač': '콜라치',
            'naći': '나치',
            'sestrić': '세스트리치',
            'desno': '데스노',
            'drvo': '드르보',
            'medved': '메드베드',
            'džep': '제프',
            'narudžba': '나루지바',
        #    u'Ðurađ': u'주라지',
            'fasada': '파사다',
            'kifla': '키플라',
            'šaraf': '샤라프',
            'gost': '고스트',
            'dugme': '두그메',
            'krug': '크루그',
            'hitan': '히탄',
            'šah': '샤흐',
            'korist': '코리스트',
            'krug': '크루그',
            'jastuk': '야스투크',
            'levo': '레보',
            'balkon': '발콘',
            'šal': '샬',
            'ljeto': '레토',
            'pasulj': '파술',
            'malo': '말로',
            'mnogo': '므노고',
            'osam': '오삼',
            'nos': '노스',
            'banka': '반카',
            'loman': '로만',
            'Njegoš': '네고시',
            'svibanj': '스비반',
            'peta': '페타',
            'opština': '옵슈티나',
            'lep': '레프',
            'riba': '리바',
            'torba': '토르바',
            'mir': '미르',
            'sedam': '세담',
            'posle': '포슬레',
            'glas': '글라스',
            'šal': '샬',
            'vlasništvo': '블라스니슈트보',
            'broš': '브로시',
            'telo': '텔로',
            'ostrvo': '오스트르보',
            'put': '푸트',
            'vatra': '바트라',
            'olovka': '올로브카',
            'proliv': '프롤리브',
            'zavoj': '자보이',
            'pozno': '포즈노',
            'obraz': '오브라즈',
            'žena': '제나',
            'izložba': '이즐로주바',
            'muž': '무주',
            'pojas': '포야스',
            'zavoj': '자보이',
            'odjelo': '오델로',
            'bakar': '바카르',
            'cev': '체브',
            'dim': '딤',
            'molim': '몰림',
            'zubar': '주바르',
        })

    def test_1st(self):
        """제1항: k, p
        k, p는 어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        self.assert_examples({
            'jastuk': '야스투크',
            'јастук': '야스투크',
            'opština': '옵슈티나',
            'општина': '옵슈티나',
        })

    def test_2nd(self):
        """제2항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            'kula': '쿨라',
            'кула': '쿨라',
        })

    def test_3rd(self):
        """제3항: m
        어두의 m이 l, r, n 앞에 오거나 어중의 m이 r 앞에 올 때에는 '으'를
        붙여 적는다.
        """
        self.assert_examples({
            'mlad': '믈라드',
            'млад': '믈라드',
            'mnogo': '므노고',
            'много': '므노고',
            'smrt': '스므르트',
            'смрт': '스므르트',
        })

    def test_4th(self):
        """제4항: š
        š는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        self.assert_examples({
            'šljivovica': '슐리보비차',
            'шљивовица': '슐리보비차',
            'Niš': '니시',
            'Ниш': '니시',
        })

    def test_5th(self):
        """제5항
        자음에 '예'가 결합되는 경우에는 '예' 대신에 '에'로 적는다. 다만,
        자음이 'ㅅ'인 경우에는 '셰'로 적는다.
        """
        self.assert_examples({
            'bjedro': '베드로',
            'бједро': '베드로',
            'sjedlo': '셰들로',
            'сједло': '셰들로',
        })
