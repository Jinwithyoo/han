# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.est import Estonian


class EstonianTestCase(HangulizeTestCase):

    lang = Estonian()

    def test_people(self):
        self.assert_examples({
            'Andrus Ansip': '안드루스 안시프',
            'Jakob Hurt': '야코브 후르트',
            'Maarja-Liis Ilus': '마리아리스 일루스',
            'Ernst Jaakson': '에른스트 약손',
            'Carl Robert Jakobson': '카를 로베르트 야콥손',
            'Siim Kallas': '심 칼라스',
            'Kaia Kanepi': '카이아 카네피',
            'Gerd Kanter': '게르드 칸테르',
            'Jaan Kaplinski': '얀 카플린스키',
            'Paul Keres': '파울 케레스',
            'Jaan Kirsipuu': '얀 키르시푸',
            'Lydia Koidula': '뤼디아 코이둘라',
            'Jaan Kross': '얀 크로스',
            'Kerli Kõiv': '케를리 커이브',
            'Mart Laar': '마르트 라르',
            'Lennart Meri': '렌나르트 메리',
            'Markko Märtin': '마르코 매르틴',
            'Georg Ots': '게오르그 오츠',
            'Juhan Parts': '유한 파르츠',
            'Indrek Pertelson': '인드레크 페르텔손',
            'Arvo Pärt': '아르보 패르트',
            'Konstantin Päts': '콘스탄틴 패츠',
            'Johannes Pääsuke': '요한네스 패수케',
            'Kristjan Raud': '크리스티안 라우드',
            'Arnold Rüütel': '아르놀드 뤼텔',
            'Gustav Suits': '구스타브 수이츠',
            'Kristina Šmigun': '크리스티나 슈미군',
            'Anton Hansen Tammsaare': '안톤 한센 탐사레',
            'Rudolf Tobias': '루돌프 토비아스',
            'Villu Toots': '빌루 토츠',
            'Veljo Tormis': '벨리오 토르미스',
            'Jüri Uluots': '위리 울루오츠',
            'Andrus Veerpalu': '안드루스 베르팔루',
            'Veiko Õunpuu': '베이코 어운푸',
        })

    def test_places(self):
        self.assert_examples({
            'Haapsalu': '합살루',
            'Kohtla-Järve': '코흐틀라얘르베',
            'Koiva': '코이바',
            'Kuressaare': '쿠레사레',
            'Narva': '나르바',
            'Paide': '파이데',
            'Pärnu': '패르누',
            'Rakvere': '라크베레',
            'Tallinn': '탈린',
            'Tartu': '타르투',
            'Toompea': '톰페아',
            'Valga': '발가',
            'Viljandi': '빌리안디',
            'Võru': '버루',
        })

    def test_miscellaneous(self):
        self.assert_examples({
            'Kalevipoeg': '칼레비포에그',
            'kannel': '칸넬',
        })
