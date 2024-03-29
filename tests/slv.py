# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.slv import Slovene


class SloveneTestCase(HangulizeTestCase):

    lang = Slovene()

    def test_people(self):
        self.assert_examples({
            'Milenko Ačimovič': '밀렌코 아치모비치',
            'Anton Aškerc': '안톤 아슈케르츠',
            'Armin Bačinovič': '아르민 바치노비치',
            'Janez Bleiweis': '야네스 블레이베이스',
            'Jože Brumen': '요제 브루멘',
            'Ivan Cankar': '이반 찬카르',
            'Sebastjan Cimirotič': '세바스티안 치미로티치',
            'Zlatko Dedič': '즐라트코 데디치',
            'Janez Drnovšek': '야네스 드르노우셰크',
            'Gregor Fučka': '그레고르 푸치카',
            'Jakob Petelin Gallus': '야코프 페텔린 갈루스',
            'Samir Handanovič': '사미르 한다노비치',
            'Matevž Irt': '마테우시 이르트',
            'Željko Ivanek': '젤코 이바네크',
            'Rihard Jakopič': '리하르트 야코피치',
            'Janez Janša': '야네스 얀샤',
            'Bojan Jokić': '보얀 요키치',
            'Srečko Katanec': '스레치코 카타네츠',
            'Matjaž Kek': '마티아시 케크',
            'Ivana Kobilca': '이바나 코빌차',
            'Oskar Kogoj': '오스카르 코고이',
            'Anže Kopitar': '안제 코피타르',
            'Robert Koren': '로베르트 코렌',
            'Milan Kučan': '밀란 쿠찬',
            'Fran Levstik': '프란 레우스티크',
            'Rudolf Maister': '루돌프 마이스테르',
            'Željko Milinovič': '젤코 밀리노비치',
            'Radoslav Nesterovič': '라도슬라우 네스테로비치',
            'Milivoje Novakovič': '밀리보예 노바코비치',
            'Borut Pahor': '보루트 파호르',
            'Lojze Peterle': '로이제 페테를레',
            'Jože Plečnik': '요제 플레치니크',
            'Bojan Prašnikar': '보얀 프라슈니카르',
            'Friderik Pregl': '프리데리크 프레글',
            'France Prešeren': '프란체 프레셰렌',
            'Uroš Slokar': '우로시 슬로카르',
            'Anton Martin Slomšek': '안톤 마르틴 슬롬셰크',
            'Katarina Srebotnik': '카타리나 스레보트니크',
            'Leon Štukelj': '레온 슈투켈',
            'Dubravka Tomšič': '두브라우카 톰시치',
            'Primož Trubar': '프리모시 트루바르',
            'Danilo Türk': '다닐로 튀르크',
            'Sašo Udovič': '사쇼 우도비치',
            'Beno Udrih': '베노 우드리흐',
            'Janez Vajkard Valvasor': '야네스 바이카르트 발바소르',
            'Jurij Vega': '유리 베가',
            'Zdenko Verdenik': '즈덴코 베르데니크',
            'Saša Vujačič': '사샤 부야치치',
            'Zlatko Zahovič': '즐라트코 자호비치',
            'Slavoj Žižek': '슬라보이 지제크',
        })

    def test_places(self):
        self.assert_examples({
            'Bled': '블레트',
            'Bohinj': '보힌',
            'Celje': '첼리에',
            'Domžale': '돔잘레',
            'Izola': '이졸라',
            'Jesenice': '예세니체',
            'Kamnik': '캄니크',
            'Koper': '코페르',
            'Kranj': '크란',
            'Kras': '크라스',
            'Ljubljana': '류블랴나',
            'Maribor': '마리보르',
            'Murska Sobota': '무르스카 소보타',
            'Nova Gorica': '노바 고리차',
            'Novo mesto': '노보 메스토',
            'Piran': '피란',
            'Pivka': '피우카',
            'Ptuj': '프투이',
            'Slovenija': '슬로베니야',
            'Škofja Loka': '슈코피아 로카',
            'Trbovlje': '트르보울리에',
            'Triglav': '트리글라우',
            'Velenje': '벨레니에',
        })
