# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.ces import Czech


class CzechTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0209.jsp """

    lang = Czech()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0107.jsp """
        self.assert_examples({
            'barva': '바르바',
            'obchod': '옵호트',
            'dobrý': '도브리',
            'jeřab': '예르자프',
            'cigareta': '치가레타',
            'nemocnice': '네모츠니체',
            'nemoc': '네모츠',
            'čapek': '차페크',
            'kulečnik': '쿨레치니크',
            'míč': '미치',
            'dech': '데흐',
            'divadlo': '디바들로',
            'led': '레트',
            "ďábel": '댜벨',
            "loďka": '로티카',
            "hruď": '흐루티',
            'fík': '피크',
            'knoflík': '크노플리크',
            'gramofon': '그라모폰',
            'hadr': '하드르',
            'hmyz': '흐미스',
            'bůh': '부흐',
            'choditi': '호디티',
            'chlapec': '흘라페츠',
            'prach': '프라흐',
            'kachna': '카흐나',
            'nikdy': '니크디',
            'padák': '파다크',
            'lev': '레프',
            'šplhati': '슈플하티',
            'postel': '포스텔',
            'most': '모스트',
            'mrak': '므라크',
            'podzim': '포드짐',
            'noha': '노하',
            'podmínka': '포드민카',
            'němý': '네미',
            'sáňky': '산키',
            'Plzeň': '플젠',
            'Praha': '프라하',
            'koroptev': '코롭테프',
            'strop': '스트로프',
            'quasi': '크바시',
            'ruka': '루카',
            'harmonika': '하르모니카',
            'mír': '미르',
            'řeka': '르제카',
            'námořník': '나모르주니크',
            'hořký': '호르슈키',
            'kouř': '코우르시',
            'sedlo': '세들로',
            'máslo': '마슬로',
            'nos': '노스',
            'šaty': '샤티',
            'šternberk': '슈테른베르크',
            'koš': '코시',
            'tam': '탐',
            'matka': '마트카',
            'bolest': '볼레스트',
            'tělo': '텔로',
            'štěstí': '슈테스티',
            "oběť": '오베티',
            'vysoký': '비소키',
            'knihovna': '크니호브나',
            'kov': '코프',
            'xerox': '제록스',
            'saxofón': '삭소폰',
            'zámek': '자메크',
            'pozdní': '포즈드니',
            'bez': '베스',
            'žižka': '지슈카',
            'žvěřina': '주베르지나',
            'Brož': '브로시',
            'jaro': '야로',
            'pokoj': '포코이',
            'balík': '발리크',
            'komár': '코마르',
            'dech': '데흐',
            'léto': '레토',
            'šest': '셰스트',
            'věk': '베크',
            'kino': '키노',
            'míra': '미라',
            'obec': '오베츠',
            'nervózni': '네르보즈니',
            'buben': '부벤',
            'úrok': '우로크',
            'dům': '둠',
            'jazýk': '야지크',
            'líný': '리니',
        })

    def test_1st(self):
        """제1항: k, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        self.assert_examples({
            'mozek': '모제크',
            'koroptev': '코롭테프',
        })

    def test_2nd(self):
        """제2항: b, d, d', g
        1. 어말에 올 때에는 '프', '트', '티', '크'로 적는다.
        2. 유성 자음 앞에서는 '브', '드', '디', '그'로 적는다.
        3. 무성 자음 앞에서 b, g는 받침으로 적고, d, d'는 '트', '티'로 적는다.
        """
        self.assert_examples({
            'led': '레트',
            'ledvina': '레드비나',
            'obchod': '옵호트',
            'odpadky': '오트파트키',
        })

    def test_3nd(self):
        """제3항: v, w, z, ř, ž, š
        1. v, w, z가 무성 자음 앞이나 어말에 올 때에는 '프, 프, 스'로 적는다.
        2. ř, ž가 유성 자음 앞에 올 때에는 '르주', '주', 무성 자음 앞에 올
           때에는 '르슈', '슈', 어말에 올 때에는 '르시', '시'로 적는다.
        3. š는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        self.assert_examples({
            'hmyz': '흐미스',
            'námořník': '나모르주니크',
            'hořký': '호르슈키',
            'kouř': '코우르시',
            'puška': '푸슈카',
            'myš': '미시',
        })

    def test_4th(self):
        """제4항: l, lj
        어중의 l, lj가 모음 앞에 올 때에는 'ㄹㄹ', 'ㄹ리'로 적는다.
        """
        self.assert_examples({
            'kolo': '콜로',
        })

    def test_5th(self):
        """제5항: m
        m이 r 앞에 올 때에는 '으'를 붙여 적는다.
        """
        self.assert_examples({
            'humr': '후므르',
        })

    def test_6th(self):
        """제6항
        자음에 '예'가 결합되는 경우에는 '예' 대신에 '에'로 적는다. 다만,
        자음이 'ㅅ'인 경우에는 '셰'로 적는다.
        """
        self.assert_examples({
            'věk': '베크',
            'šest': '셰스트',
        })