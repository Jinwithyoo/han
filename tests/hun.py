# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.hun import Hungarian


class HungarianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0212.jsp """

    lang = Hungarian()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0110.jsp """
        self.assert_examples({
            'bab': '버브',
            'ablak': '어블러크',
            'citrom': '치트롬',
            'nyolcvan': '뇰츠번',
            'arc': '어르츠',
            'csavar': '처버르',
            'kulcs': '쿨치',
            'daru': '더루',
            'medve': '메드베',
            'gond': '곤드',
            'dzsem': '젬',
            'elfog': '엘포그',
            'gumi': '구미',
            'nyugta': '뉴그터',
            'csomag': '초머그',
            'gyár': '자르',
            'hagyma': '허지머',
            'nagy': '너지',
            'hal': '헐',
            'juh': '유흐',
            'béka': '베커',
            'keksz': '켁스',
            'szék': '세크',
            'len': '렌',
            'meleg': '멜레그',
            'dél': '델',
            'málna': '말너',
            'bomba': '봄버',
            'álom': '알롬',
            'néma': '네머',
            'bunda': '분더',
            'pihen': '피헨',
            'nyak': '녀크',
            'hányszor': '하니소르',
            'irány': '이라니',
            'árpa': '아르퍼',
            'csipke': '칩케',
            'hónap': '호너프',
            'róka': '로커',
            'barna': '버르너',
            'ár': '아르',
            'sál': '샬',
            'puska': '푸슈커',
            'aratás': '어러타시',
            'alszik': '얼시크',
            'asztal': '어스털',
            'húsz': '후스',
            'ajto': '어이토',
            'borotva': '보로트버',
            'csont': '촌트',
            'atya': '어처',
            'vesz': '베스',
            'évszázad': '에브사저드',
            'enyv': '에니브',
            'zab': '저브',
            'kezd': '케즈드',
            'blúz': '블루즈',
            'zsák': '자크',
            'tőzsde': '퇴주데',
            'rozs': '로주',
            'ajak': '어여크',
            'fej': '페이',
            'január': '여누아르',
            'lyuk': '유크',
            'mélység': '메이셰그',
            'király': '키라이',
            'lakat': '러커트',
            'máj': '마이',
            'mert': '메르트',
            'mész': '메스',
            'isten': '이슈텐',
            'sí': '시',
            'torna': '토르너',
            'róka': '로커',
            'sör': '쇠르',
            'nő': '뇌',
            'bunda': '분더',
            'hús': '후시',
            'füst': '퓌슈트',
            'fű': '퓌',
        })

    def test_1st(self):
        """제1항: k, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        self.assert_examples({
            'ablak': '어블러크',
            'csipke': '칩케',
        })

    def test_2nd(self):
        """제2항
        bb, cc, dd, ff, gg, ggy, kk, ll, lly, nn, nny, pp, rr, ss, ssz, tt,
        tty는 b, c, d, f, g, gy, k, l, ly, n, ny, p, r, s, sz, t, ty와 같이
        적는다. 다만, 어중의 nn, nny와 모음 앞의 ll은 'ㄴㄴ', 'ㄴ니',
        'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            'között': '쾨죄트',
            'dinnye': '딘네',
            'nulla': '눌러',
        })

    def test_3rd(self):
        """제3항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            'olaj': '올러이',
        })

    def test_4th(self):
        """제4항: s
        s는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        self.assert_examples({
            'Pest': '페슈트',
            'lapos': '러포시',
        })

    def test_5th(self):
        """제5항
        자음에 '예'가 결합되는 경우에는 '예' 대신에 '에'로 적는다. 다만,
        자음이 'ㅅ'인 경우에는 '셰'로 적는다.
        """
        self.assert_examples({
            'nyer': '네르',
            'selyem': '셰옘',
        })