# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.cat import Catalan


class CatalanTestCase(HangulizeTestCase):

    lang = Catalan()

    def test_people(self):
        self.assert_examples({
            'Arantxa': '아란차',
            'Valentí Almirall': '발렌티 알미랄',
            'Jaume Bartumeu': '자우메 바르투메우',
            'Sergi Bruguera': '세르지 브루게라',
            'Montserrat Caballé': '몬세라트 카발례',
            'Santiago Calatrava': '산티아고 칼라트라바',
            'Joan Capdevila': '조안 캅데빌라',
            'Josep Carner': '조제프 카르네르',
            'Pau Casals': '파우 카잘스',
            'Lluís Companys': '류이스 콤파니스',
            'Àlex Corretja': '알렉스 코레자',
            'Albert Costa': '알베르트 코스타',
            'Salvador Dalí': '살바도르 달리',
            'Salvador Espriu': '살바도르 에스프리우',
            'Cesc Fàbregas': '세스크 파브레가스',
            'Pau Gasol': '파우 가졸',
            'Antoni Gaudí': '안토니 가우디',
            'Josep Guardiola': '조제프 과르디올라',
            'Xavi Hernández': '샤비 에르난데스',
            'Ramon Llull': '라몬 률',
            'Francesc Macià i Llussà': '프란세스크 마시아 이 류사',
            'Joan Maragall': '조안 마라갈',
            'Ausiàs March': '아우지아스 마르크',
            'Joanot Martorell': '조아노트 마르토렐',
            'Joan Miró': '조안 미로',
            'Gerard Piqué': '제라르트 피케',
            'Josep Pla': '조제프 플라',
            'Eudald Pradell': '에우달 프라델',
            'Carles Puyol': '카를레스 푸욜',
            'Mercè Rodoreda': '메르세 로도레다',
            'Jordi Savall': '조르디 사발',
            'Joan Manuel Serrat': '조안 마누엘 세라트',
            'Joaquim Sorolla': '조아킴 소롤랴',
            'Antoni Tàpies': '안토니 타피에스',
            'Josep Tarradellas': '조제프 타라델랴스',
            'Jordi Tarrés': '조르디 타레스',
            'Jacint Verdaguer': '자신 베르다게르',
        })

    def test_places(self):
        self.assert_examples({
            'Alacant': '알라칸',
            'Andorra': '안도라',
            'Andorra la Vella': '안도라 라 벨랴',
            'Barcelona': '바르셀로나',
            'Berga': '베르가',
            'Besalú': '베잘루',
            'Catalunya': '카탈루냐',
            'Cerdanya': '세르다냐',
            'Conflent': '콘플렌',
            'Eivissa': '에이비사',
            'Elx': '엘시',
            'Empúries': '엠푸리에스',
            'Figueres': '피게레스',
            'Girona': '지로나',
            'Lleida': '례이다',
            'Manresa': '만레자',
            'Montjuïc': '몬주이크',
            'Montserrat': '몬세라트',
            'Osona': '오조나',
            'Pallars': '팔랴르스',
            'Pallars Jussà': '팔랴르스 주사',
            'Pallars Sobirà': '팔랴르스 소비라',
            'Palma': '팔마',
            'Ribagorça': '리바고르사',
            'Rosselló': '로셀료',
            'Tarragona': '타라고나',
            'Urgell': '우르젤',
            'València': '발렌시아',
        })

    def test_miscellaneous(self):
        self.assert_examples({
            'Barça': '바르사',
            'Camp Nou': '캄 노우',
            'Canigó': '카니고',
            'Espanyol': '에스파뇰',
            'estel·lar': '에스텔라르',
            'llengua': '롕과',
            'modernisme': '모데르니즈메',
            'Renaixença': '레나셴사',
            'Sagrada Família': '사그라다 파밀리아',
        })