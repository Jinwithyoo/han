# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.wlm import MiddleWelsh


class MiddleWelshTestCase(HangulizeTestCase):

    lang = MiddleWelsh()

    def test_examples_of_iceager(self):
        self.assert_examples({
            'Mabinogion': '마비노기온',
            'Culhwch': '퀼후흐',
            'Olwen': '올웬',
            'Taliesin': '탈리에신',
            'Peredur': '페레뒤르',
            'Geraint': '게라인트',
            'Rhonabwy': '흐로나부이',
            'Rhiannon': '흐리아논',
            'Annwn': '아눈',
            'Pryderi': '프러데리',
            'Brânwen': '브란웬',
            'Llŷr': '흘리르',
            'Gwawl': '과울',
            'Beli Mawr': '벨리 마우르',
            'Gofannon': '고바논',
            'Gwynedd': '귀네드',
            'Arianrhod': '아리안흐로드',
            'Manawydan': '마나위단',
            'Gwenhwyfar': '궨후이바르',
            'Aneirin': '아네이린',
            'Myrddin': '머르딘',
            'Llywarch': '흘러와르흐',
            'Cad Godeu': '카드 고데이',
            'Lleu Llaw Gyffes': '흘레이 흘라우 거페스',
            'tynged': '텅에드',
            'Chwedlau Odo': '훼들라이 오도',
            'Culhwch ac Olwen': '퀼후흐 악 올웬',
            'Math fab Mathonwy': '마스 바브 마소누이',
            'Pwyll Pendefig Dyfed': '푸이흘 펜데비그 더베드',
        })