# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.fin import Finnish


class FinnishTestCase(HangulizeTestCase):

    lang = Finnish()

    def test_people(self):
        self.assert_examples({
            'Alvar Aalto': '알바르 알토',
            'Juhani Aho': '유하니 아호',
            'Martti Ahtisaari': '마르티 아흐티사리',
            'Akseli Gallen-Kallela': '악셀리 갈렌칼렐라',
            'Veikko Hakulinen': '베이코 하쿨리넨',
            'Pekka Halonen': '페카 할로넨',
            'Tarja Halonen': '타리아 할로넨',
            'Sami Hyypiä': '사미 휘피애',
            'Mika Häkkinen': '미카 해키넨',
            'Jussi Jääskeläinen': '유시 얘스켈래이넨',
            'Aki Kaurismäki': '아키 카우리스매키',
            'Urho Kekkonen': '우르호 케코넨',
            'Miikka Kiprusoff': '미카 키프루소프',
            'Marja-Liisa Kirvesniemi': '마리아리사 키르베스니에미',
            'Mauno Koivisto': '마우노 코이비스토',
            'Saku Koivu': '사쿠 코이부',
            'Hannes Kolehmainen': '한네스 콜레흐마이넨',
            'Jari Kurri': '야리 쿠리',
            'Jari Litmanen': '야리 리트마넨',
            'Eero Mäntyranta': '에로 맨튀란타',
            'Paavo Nurmi': '파보 누르미',
            'Ville Ritola': '빌레 리톨라',
            'Kimi Räikkönen': '키미 래이쾨넨',
            'Eero Saarinen': '에로 사리넨',
            'Teemu Selanne': '테무 셀란네',
            'Frans Eemil Sillanpää': '프란스 에밀 실란패',
            'Tarja Turunen': '타리아 투루넨',
            'Artturi Ilmari Virtanen': '아르투리 일마리 비르타넨',
            'Yrjö Väisälä': '위리외 배이샐래',
            'Tapio Wirkkala': '타피오 비르칼라',
        })

    def test_places(self):
        self.assert_examples({
            'Espoo': '에스포',
            'Helsinki': '헬싱키',
            'Joensuu': '요엔수',
            'Jyväskylä': '위배스퀼래',
            'Kajaani': '카야니',
            'Karjala': '카리알라',
            'Kuopio': '쿠오피오',
            'Lappeenranta': '라펜란타',
            'Mikkeli': '미켈리',
            'Nokia': '노키아',
            'Oulu': '오울루',
            'Rovaniemi': '로바니에미',
            'Saimaa': '사이마',
            'Savonlinna': '사본린나',
            'Suomenlinna': '수오멘린나',
            'Suomi': '수오미',
            'Tampere': '탐페레',
            'Tapiola': '타피올라',
            'Turku': '투르쿠',
            'Vaasa': '바사',
            'Vantaa': '반타',
        })

    def test_mythology(self):
        self.assert_examples({
            'Aino': '아이노',
            'Ilmarinen': '일마리넨',
            'Joukahainen': '요우카하이넨',
            'Kalevala': '칼레발라',
            'Kullervo': '쿨레르보',
            'Lemminkäinen': '렘밍캐이넨',
            'Louhi': '로우히',
            'Marjatta': '마리아타',
            'Pohjola': '포흐욜라',
            'Sampo': '삼포',
            'Ukko': '우코',
            'Väinämöinen': '배이내뫼이넨',
        })

    def test_miscellaneous(self):
        self.assert_examples({
            'kantele': '칸텔레',
            'sauna': '사우나',
            'sisu': '시수',
        })