# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.tur import Turkish


class TurkishTestCase(HangulizeTestCase):

    lang = Turkish()

    def test_people(self):
        self.assert_examples({
            'Sait Faik Abasıyanık': '사이트 파이크 아바스야느크',
            'Ali Kuşçu': '알리 쿠슈추',
            'Hamit Altıntop': '하미트 알튼토프',
            'Mustafa Kemal Atatürk': '무스타파 케말 아타튀르크',
            'Garabet Amira Balyan': '가라베트 아미라 발리안',
            'Krikor Balyan': '크리코르 발리안',
            'Nigoğos Balyan': '니고오스 발리안',
            'Battani': '바타니',
            'Hüseyin Çağlayan': '휘세인 찰라얀',
            'Süleyman Çelebi': '쉴레이만 첼레비',
            'Rauf Denktaş': '라우프 뎅크타슈',
            'Bülent Ecevit': '뷜렌트 에제비트',
            'Ahmet Mithat Efendi': '아흐메트 미타트 에펜디',
            'Yunus Emre': '유누스 엠레',
            'Recep Tayyip Erdoğan': '레제프 타이이프 에르도안',
            'Sertab Erener': '세르타브 에레네르',
            'Tevfik Fikret': '테브피크 피크레트',
            'Ertuğrul Gazi': '에르투룰 가지',
            'Ziya Gökalp': '지야 괴칼프',
            'Abdullah Gül': '아브둘라흐 귈',
            'Şenol Güneş': '셰놀 귀네슈',
            'Reşat Nuri Güntekin': '레샤트 누리 귄테킨',
            'Ahmed Hâşim': '아흐메드 하심',
            'Nâzım Hikmet': '나즘 히크메트',
            'Nihat Kahveci': '니하트 카흐베지',
            'Yakup Kadri Karaosmanoğlu': '야쿠프 카드리 카라오스마놀루',
            'Nâmık Kemal': '나므크 케말',
            'Yaşar Kemal': '야샤르 케말',
            'Fazıl Küçük': '파즐 퀴취크',
            'İlhan Mansız': '일한 만스즈',
            'Nakkaş Osman': '나카슈 오스만',
            'Orhan Pamuk': '오르한 파무크',
            'Ajda Pekkan': '아주다 페칸',
            'Osman Hamdi Bey': '오스만 함디 베이',
            'Pir Sultan Abdal': '피르 술탄 아브달',
            'Rüştü Reçber': '뤼슈튀 레치베르',
            'Ziynet Sali': '지네트 살리',
            'Ömer Seyfettin': '외메르 세이페틴',
            'Kanuni Sultan Süleyman': '카누니 술탄 쉴레이만',
            'Tuncay Şanlı': '툰자이 샨르',
            'Âşık Veysel Şatıroğlu': '아시으크 베이셀 샤트롤루',
            'Mahzuni Şerif': '마흐주니 셰리프',
            'Hakan Şükür': '하칸 쉬퀴르',
            'Takiyüddin ibn Manıf': '타키위딘 이븐 마느프',
            'Tarkan Tevetoğlu': '타르칸 테베톨루',
            'Arda Turan': '아르다 투란',
            'Halit Ziya Uşaklıgil': '할리트 지야 우샤클르길',
        })

    def test_places(self):
        self.assert_examples({
            'Adana': '아다나',
            'Ağrı': '아르',
            'Ankara': '앙카라',
            'Antakya': '안타키아',
            'Antalya': '안탈리아',
            'Arykanda': '아리칸다',
            'Beşiktaş': '베식타슈',
            'Bursa': '부르사',
            'Çanakkale': '차나칼레',
            'Çatalhöyük': '차탈회위크',
            'Denizli': '데니즐리',
            'Divriği': '디브리이',
            'Dolmabahçe': '돌마바흐체',
            'Gaziantep': '가지안테프',
            'Hattuşaş': '하투샤슈',
            'İstanbul': '이스탄불',
            'İzmir': '이즈미르',
            'Kapadokya': '카파도키아',
            'Kayseri': '카이세리',
            'Konya': '코니아',
            'Mersin': '메르신',
            'Pamukkale': '파무칼레',
            'Patara': '파타라',
            'Safranbolu': '사프란볼루',
            'Selçuk': '셀추크',
            'Topkapı': '톱카프',
            'Trabzon': '트라브존',
            'Türkiye': '튀르키예',
        })