# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.slk import Slovak


class SlovakTestCase(HangulizeTestCase):

    lang = Slovak()

    def test_people(self):
        self.assert_examples({
            'Ján Bahýľ': '얀 바힐',
            'Štefan Banič': '슈테판 바니치',
            'Anton Bernolák': '안톤 베르놀라크',
            'Peter Bondra': '페테르 본드라',
            'Zdeno Chára': '즈데노 하라',
            'Dominika Cibulková': '도미니카 치불코바',
            'Ján Čarnogurský': '얀 차르노구르스키',
            'Štefan Marko Daxner': '슈테판 마르코 닥스네르',
            'Pavol Demitra': '파볼 데미트라',
            'Alexander Dubček': '알렉산데르 둡체크',
            'Mikuláš Dzurinda': '미쿨라시 주린다',
            'Marián Gáborík': '마리안 가보리크',
            'Marek Hamšík': '마레크 함시크',
            'Daniela Hantuchová': '다니엘라 한투호바',
            'Andrej Hlinka': '안드레이 흘린카',
            'Milan Hodža': '밀란 호자',
            'Marian Hossa': '마리안 호사',
            'Dominik Hrbatý': '도미니크 흐르바티',
            'Pavol Hurajt': '파볼 후라이트',
            'Jozef Miloslav Hurban': '요제프 밀로슬라우 후르반',
            'Gustáv Husák': '구스타우 후사크',
            'Hviezdoslav': '흐비에즈도슬라우',
            'Dionýz Ilkovič': '디오니스 일코비치',
            'Elena Kaliská': '엘레나 칼리스카',
            'Michaela Kocianová': '미하엘라 코치아노바',
            'Karol Kučera': '카롤 쿠체라',
            'Anastasiya Kuzmina': '아나스타시야 쿠즈미나',
            'Michal Martikán': '미할 마르티칸',
            'Janko Matúška': '얀코 마투슈카',
            'Vladimír Mečiar': '블라디미르 메치아르',
            'Martina Moravcová': '마르티나 모라우초바',
            'Jozef Murgaš': '요제프 무르가시',
            'Natália Prekopová': '나탈리아 프레코포바',
            'Jozef Roháček': '요제프 로하체크',
            'Magdaléna Rybáriková': '마그달레나 리바리코바',
            'Zuzana Sekerová': '주자나 세케로바',
            'Aurel Stodola': '아우렐 스토돌라',
            'Eugen Suchoň': '에우겐 수혼',
            'Martin Škrtel': '마르틴 슈크르텔',
            'Milan Rastislav Štefánik': '밀란 라스티슬라우 슈테파니크',
            'Zuzana Štefečeková': '주자나 슈테페체코바',
            'Peter Šťastný': '페테르 슈탸스트니',
            'Ľudovít Štúr': '류도비트 슈투르',
            'Jozef Tiso': '요제프 티소',
            'Vavrinec': '바우리네츠',
            'Rudolf Vrba': '루돌프 브르바',
            'Vladimír Weiss': '블라디미르 베이스',
        })

    def test_places(self):
        self.assert_examples({
            'Banská Bystrica': '반스카 비스트리차',
            'Bardejov': '바르데요우',
            'Bratislava': '브라티슬라바',
            'Komárno': '코마르노',
            'Košice': '코시체',
            'Manínska tiesňava': '마닌스카 티에스냐바',
            'Martin': '마르틴',
            'Michalovce': '미할로우체',
            'Nitra': '니트라',
            'Poprad': '포프라트',
            'Považská': '포바슈스카',
            'Prešov': '프레쇼우',
            'Rožňava': '로주냐바',
            'Slavín': '슬라빈',
            'Spiš': '스피시',
            'Trenčín': '트렌친',
            'Trnava': '트르나바',
            'Váh': '바흐',
            'Vlkolínec': '블콜리네츠',
            'Vydrica': '비드리차',
            'Zvolen': '즈볼렌',
            'Žilina': '질리나',
            'Žehra': '제흐라',
        })

    def test_miscellaneous(self):
        self.assert_examples({
            'deväť': '데베티',
            'jahôd': '야후오트',
            'mäkčeň': '멕첸',
            'pätnásť': '페트나스티',
        })