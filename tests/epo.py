# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.epo import Esperanto


class EsperantoTestCase(HangulizeTestCase):

    lang = Esperanto()

    def test_examples_in_wikipedia(self):
        """ http://ko.wikipedia.org/wiki/에스페란토 """
        self.assert_examples({
            'Supersigno': '수페르시그노',
            'Ĉapelo': '차펠로',
            'Saluton': '살루톤',
            'Ĝis revido': '지스 레비도',
            'Adiaŭ': '아디아우',
            'Jes': '예스',
            'Ne': '네',
            'Dankon': '단콘',
            'Mi tre ĝojas renkonti vin': '미 트레 조야스 렌콘티 빈',
            'Ĉu vi fartas bone': '추 비 파르타스 보네',
            'Mi estas koreo': '미 에스타스 코레오',
            'iĉismo': '이치스모',
            'riismo': '리이스모',
            'lingve universala': '린그베 우니베르살라',
            'La Esperantisto': '라 에스페란티스토',
        })

    def test_examples_of_iceager(self):
        self.assert_examples({
            'Pasporta Servo': '파스포르타 세르보',
            'Fonto': '폰토',
            'Esperantujo': '에스페란투요',
            'Literatura Foiro': '리테라투라 포이로',
            'La Espero': '라 에스페로',
            'Finvenkismo': '핀벤키스모',
            'Raŭmismo': '라우미스모',
            'Civitanismo': '치비타니스모',
            'Unua Libro': '우누아 리브로',
            'Dua Libro': '두아 리브로',
            'Lingvo Internacia': '린그보 인테르나치아',
            'Fundamento de Esperanto': '푼다멘토 데 에스페란토',
            'La Ondo de Esperanto': '라 온도 데 에스페란토',
            'La Teatra Movado dum la Milito': '라 테아트라 모바도 둠 라 밀리토',
            'Gogo kaj liaj amikoj': '고고 카이 리아이 아미코이',
            'Serio Oriento-Okcidento': '세리오 오리엔토옥치덴토',
            'Ĉu vi pretas?': '추 비 프레타스?',
        })