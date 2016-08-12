# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.por import Portuguese


class PortugueseTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0219.jsp """

    lang = Portuguese()

    def test_1st(self):
        """제1항
        c, g는 a, o, u 앞에서는 각각 ‘ㅋ, ㄱ'으로 적고, e, i 앞에서는
        ‘ㅅ, ㅈ'으로 적는다.
        """
        self.assert_examples({
            'Cabral': '카브랄',
            'Camocim': '카모싱',
            'Egas': '에가스',
            'Gil': '질',
        })

    def test_2nd(self):
        """제2항
        gu, qu는 a, o, u 앞에서는 각각 ‘구, 쿠'로 적고, e, i 앞에서는
        ‘ㄱ, ㅋ'으로 적는다.
        """
        self.assert_examples({
            'Iguaçú': '이구아수',
            'Araquari': '아라쿠아리',
            'Guerra': '게하',
            'Aquilino': '아킬리누',
        })

    def test_3rd(self):
        """제3항
        d, t는 ㄷ, ㅌ으로 적는다.
        """
        self.assert_examples({
            'Amado': '아마두',
            'Costa': '코스타',
            'Diamantina': '디아만티나',
            'Alegrete': '알레그레트',
            'Montes': '몬트스',
        })

    def test_4th(self):
        """제4항
        어말의 -che는 ‘시'로 적는다.
        """
        self.assert_examples({
            'Angoche': '앙고시',
            'Peniche': '페니시',
        })

    def test_5th(self):
        """제5항: l
        1. 어중의 l이 모음 앞에 오거나 모음이 따르지 않는 비음 앞에 오는
           경우에는 ‘?'로 적는다. 다만, 비음 뒤의 l은 모음 앞에 오더라도 ‘ㄹ'로
           적는다.
        2. 어말 또는 자음 앞의 l은 받침 ‘ㄹ'로 적는다.
        """
        self.assert_examples({
            'Carlos': '카를루스',
            'Amalia': '아말리아',
            'Sul': '술',
            'Azul': '아줄',
            'Gilberto': '질베르투',
            'Caracol': '카라콜',
        })

    def test_6th(self):
        """제6항
        m, n은 각각 ㅁ, ㄴ으로 적고, 어말에서는 모두 받침 ‘ㅇ'으로 적는다.
        어말 -ns의 n도 받침 ‘ㅇ'으로 적는다.
        """
        self.assert_examples({
            'Manuel': '마누엘',
            'Moniz': '모니스',
            'Campos': '캄푸스',
            'Vincente': '빈센트',
            'Santarem': '산타렝',
            'Rondon': '혼동',
            'Lins': '링스',
            'Rubens': '후벵스',
        })

    def test_7th(self):
        """제7항
        ng, nc, nq 연쇄에서 ‘g, c, q'가 ‘ㄱ'이나 ‘ㅋ'으로 표기되면 ‘n'은
        받침 ‘ㅇ'으로 적는다.
        """
        self.assert_examples({
            'Angola': '앙골라',
            'Angelo': '안젤루',
            'Branco': '브랑쿠',
            'Francisco': '프란시스쿠',
            'Conquista': '콩키스타',
            'Junqueiro': '중케이루',
        })

    def test_8th(self):
        """제8항
        r는 어두나 n, l, s 뒤에 오는 경우에는 ‘ㅎ'으로 적고, 그 밖의 경우에는
        ‘ㄹ, 르'로 적는다.
        """
        self.assert_examples({
            'Ribeiro': '히베이루',
            'Henrique': '엔히크',
            'Bandeira': '반데이라',
            'Salazar': '살라자르',
        })

    def test_9th(self):
        """제9항: s
        1. 어두나 모음 앞에서는 ‘ㅅ'으로 적고, 모음 사이에서는 ‘ㅈ'으로 적는다.
        2. 무성 자음 앞이나 어말에서는 ‘스'로 적고, 유성 자음 앞에서는 ‘즈'로
           적는다.
        """
        self.assert_examples({
            'Salazar': '살라자르',
            'Afonso': '아폰수',
            'Barroso': '바호주',
            'Gervasio': '제르바지우',
        })

    def test_10th(self):
        """제10항: sc, sç, xc
        sc와 xc는 e, i 앞에서 ‘ㅅ'으로 적는다. sç는 항상 ‘ㅅ'으로 적는다.
        """
        self.assert_examples({
            'Nascimento': '나시멘투',
            'piscina': '피시나',
            'excelente': '이셀렌트',
            'cresça': '크레사',
        })

    def test_11st(self):
        """제11항
        x는 ‘시'로 적되, 어두 e와 모음 사이에 오는 경우에는 ‘ㅈ'으로 적는다.
        """
        self.assert_examples({
            'Teixeira': '테이셰이라',
            'lixo': '리슈',
            'exame': '이자므',
            'exemplo': '이젬플루',
        })

    def test_12nd(self):
        """제12항
        같은 자음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다. 다만, rr는
        ‘ㅎ, 흐'로, ss는 ‘ㅅ, 스'로 적는다.
        """
        self.assert_examples({
            'Garrett': '가헤트',
            'Barroso': '바호주',
            'Mattoso': '마토주',
            'Toress': '토레스',
        })

    def test_13rd(self):
        """제13항
        o는 ‘오'로 적되, 어말이나 -os의 o는 ‘우'로 적는다.
        """
        self.assert_examples({
            'Nobre': '노브르',
            'Antonio': '안토니우',
            'Melo': '멜루',
            'Saramago': '사라마구',
            'Passos': '파수스',
            'Lagos': '라구스',
        })

    def test_14th(self):
        """제14항
        e는 ‘에'로 적되, 어두 무강세 음절에서는 ‘이'로 적는다. 어말에서는
        ‘으'로 적는다.
        """
        self.assert_examples({
            'Montemayor': '몬테마요르',
            'Estremoz': '이스트레모스',
            'Chifre': '시프르',
            'de': '드',
        })

    def test_15th(self):
        """제15항: -es
        1. p, b, m, f, v 다음에 오는 어말 -es는 ‘-에스'로 적는다.
        2. 그 밖의 어말 -es는 ‘-으스'로 적는다.
        """
        self.assert_examples({
            'Lopes': '로페스',
            'Gomes': '고메스',
            'Neves': '네베스',
            'Chaves': '샤베스',
            'Soares': '소아르스',
            'Pires': '피르스',
        })