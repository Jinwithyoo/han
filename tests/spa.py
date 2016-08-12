# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.spa import Spanish


class SpanishTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0204.jsp """

    lang = Spanish()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0102.jsp """
        self.assert_examples({
            'biz': '비스',
            'blandon': '블란돈',
            'braceo': '브라세오',
            'colcren': '콜크렌',
            'Cecilia': '세실리아',
            'coccion': '콕시온',
            'bistec': '비스텍',
            'dictado': '딕타도',
            'chicharra': '치차라',
            'felicidad': '펠리시다드',
            'fuga': '푸가',
            'fran': '프란',
            'ganga': '강가',
            'geologia': '헤올로히아',
            'yungla': '융글라',
            'hipo': '이포',
            'quehacer': '케아세르',
            'jueves': '후에베스',
            'reloj': '렐로',
            'kapok': '카포크',
            'lacrar': '라크라르',
            'Lulio': '룰리오',
            'ocal': '오칼',
            'llama': '야마',
            'lluvia': '유비아',
            'membrete': '멤브레테',
            'noche': '노체',
            'flan': '플란',
            'ñoñez': '뇨녜스',
            'mañana': '마냐나',
            'pepsina': '펩시나',
            'plantón': '플란톤',
            'quisquilla': '키스키야',
            'rascador': '라스카도르',
            'sastreria': '사스트레리아',
            'tetraetro': '테트라에트로',
            'viudedad': '비우데다드',
            'xenón': '세논',
            'laxante': '락산테',
            'yuxta': '육스타',
            'zagal': '사갈',
            'liquidez': '리키데스',
            'walkirias': '왈키리아스',
            'yungla': '융글라',
            'braceo': '브라세오',
            'reloj': '렐로',
            'Lulio': '룰리오',
            'ocal': '오칼',
            'viudedad': '비우데다드',
        })

    def test_1st(self):
        """제1항: gu, qu
        gu, qu는 i, e 앞에서는 각각 'ㄱ, ㅋ'으로 적고, o 앞에서는 '구, 쿠'로
        적는다. 다만, a 앞에서는 그 a와 합쳐 '과, 콰'로 적는다.
        """
        self.assert_examples({
            'guerra': '게라',
            'queso': '케소',
            'Guipuzcoa': '기푸스코아',
            'quisquilla': '키스키야',
            'antiguo': '안티구오',
            'Quorem': '쿠오렘',
            'Nicaragua': '니카라과',
            'Quarai': '콰라이',
        })

    def test_2nd(self):
        """제2항
        같은 자음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다. 다만,
        -cc-는 'ㄱㅅ'으로 적는다.
        """
        self.assert_examples({
            'carrera': '카레라',
            'carreterra': '카레테라',
            'accion': '악시온',
        })

    def test_3rd(self):
        """제3항: c, g
        c와 g 다음에 모음 e와 i가 올 때에는 c는 'ㅅ'으로, g는 'ㅎ'으로 적고,
        그 외는 'ㅋ'과 'ㄱ'으로 적는다.
        """
        self.assert_examples({
            'Cecilia': '세실리아',
            'cifra': '시프라',
            'georgico': '헤오르히코',
            'giganta': '히간타',
            'coquito': '코키토',
            'gato': '가토',
        })

    def test_4th(self):
        """제4항: x
        x가 모음 앞에 오되 어두일 때에는 'ㅅ'으로 적고, 어중일 때에는
        'ㄱㅅ'으로 적는다.
        """
        self.assert_examples({
            'xilofono': '실로포노',
            'laxante': '락산테',
        })

    def test_5th(self):
        """제5항: l
        어말 또는 자음 앞의 l은 받침 'ㄹ'로 적고, 어중의 1이 모음 앞에 올
        때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            'ocal': '오칼',
            'colcren': '콜크렌',
            'blandon': '블란돈',
            'Cecilia': '세실리아',
        })

    def test_6th(self):
        """제6항: nc, ng
        c와 g 앞에 오는 n은 받침 'ㅇ'으로 적는다.
        """
        self.assert_examples({
            'blanco': '블랑코',
            'yungla': '융글라',
        })

    def test_hangulize(self):
        self.assert_examples({
            'ñoñez': '뇨녜스',
            'güerrero': '궤레로',
            'Güicho': '귀초',
            'Gamiño': '가미뇨',
            'Ángeles': '앙헬레스',
            'José Ortega y Gasset': '호세 오르테가 이 가세트',
        })