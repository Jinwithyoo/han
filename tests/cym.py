# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.cym import Welsh


class WelshTestCase(HangulizeTestCase):

    lang = Welsh()

    def test_examples_of_iceager(self):
        self.assert_examples({
            'Cymru': '컴리',
            'Cymraeg': '컴라이그',
            'Caernarfon': '카이르나르본',
            'Ceredigion': '케레디기온',
            'Aberystwyth': '아베러스투이스',
            'Brynmawr': '브런마우르',
            'Llangollen': '흘란고흘렌',
            'Llanelli': '흘라네흘리',
            'Gwynedd': '귀네드',
            'Ystradgynlais': '어스트라드건라이스',
            'Tawe': '타웨',
            'Powys': '포위스',
            'Meredith': '메레디스',
            'Glyndŵr': '글런두르',
            'Rhys': '흐리스',
            'Ifans': '이반스',
            'Emrys': '엠리스',
            'Hywel': '허웰',
            'Gwilym': '귈림',
            'Llinor': '흘리노르',
            'Ieuan': '예이안',
            'Cerys': '케리스',
            'Dafydd': '다비드',
            'Iwan': '이완',
            'Huw': '히우',
            'Ciaran': '키아란',
            'Myfanwy': '머바누이',
            'Llywelyn': '흘러웰린',
            'Calennig': '칼레니그',
            'cnapan': '크나판',
            'cwm': '쿰',
            'fy ngwely': '벙 웰리',
            'fy nhadau': '번 하다이',
            "Banc Ty'nddôl": '방크 턴돌',
        })