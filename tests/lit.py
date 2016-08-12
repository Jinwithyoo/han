# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.lit import Lithuanian


class LithuanianTestCase(HangulizeTestCase):

    lang = Lithuanian()

    def test_people(self):
        self.assert_examples({
            'Valdas Adamkus': '발다스 아담쿠스',
            'Virgilijus Alekna': '비르길리유스 알레크나',
            'Algirdas': '알기르다스',
            'Jurgis Baltrušaitis': '유르기스 발트루샤이티스',
            'Gediminas Baravykas': '게디미나스 바라비카스',
            'Jonas Basanavičius': '요나스 바사나비추스',
            'Bernardas Brazdžionis': '베르나르다스 브라즈조니스',
            'Elena Čiudakova': '엘레나 추다코바',
            'Čiurlionis': '추를료니스',
            'Tomas Danilevičius': '토마스 다닐레비추스',
            'Simonas Daukantas': '시모나스 다우칸타스',
            'Jurgis Dobkevičius': '유르기스 돕케비추스',
            'Gediminas': '게디미나스',
            'Vitas Gerulaitis': '비타스 게룰라이티스',
            'Marija Gimbutienė': '마리야 김부티에네',
            'Dalia Grybauskaitė': '달랴 그리바우스카이테',
            'Laurynas Gucevičius': '라우리나스 구체비추스',
            'Žydrūnas Ilgauskas': '지드루나스 일가우스카스',
            'Jonas Jablonskis': '요나스 야블론스키스',
            'Edgaras Jankauskas': '에드가라스 양카우스카스',
            'Šarūnas Jasikevičius': '샤루나스 야시케비추스',
            'Jogaila': '요가일라',
            'Kęstutis': '케스투티스',
            'Linas Kleiza': '리나스 클레이자',
            'Konstantinas': '콘스탄티나스',
            'Jonas Kubilius': '요나스 쿠빌류스',
            'Vincas Kudirka': '빈차스 쿠디르카',
            'Maironis': '마이로니스',
            'Šarūnas Marčiulionis': '샤루나스 마르출료니스',
            'Mikalojus': '미칼로유스',
            'Mindaugas': '민다우가스',
            'Arminas Narbekovas': '아르미나스 나르베코바스',
            'Salomėja Nėris': '살로메야 네리스',
            'Martynas Mažvydas': '마르티나스 마주비다스',
            'Mykolas Kleopas Oginskis': '미콜라스 클레오파스 오긴스키스',
            'Robertas Poškus': '로베르타스 포슈쿠스',
            'Kazimiera Prunskienė': '카지미에라 프룬스키에네',
            'Jonušas Radvila': '요누샤스 라드빌라',
            'Violeta Riaubiškytė': '뵬레타 랴우비슈키테',
            'Arvydas Sabonis': '아르비다스 사보니스',
            'Antanas Smetona': '안타나스 스메토나',
            'Darius Songaila': '다류스 송가일라',
            'Marius Stankevičius': '마류스 스탕케비추스',
            'Vytautas Straižys': '비타우타스 스트라이지스',
            'Deividas Šemberas': '데이비다스 솀베라스',
            'Ramūnas Šiškauskas': '라무나스 시슈카우스카스',
            'Juozas Urbšys': '유오자스 우르프시스',
            'Vytautas': '비타우타스',
        })

    def test_places(self):
        self.assert_examples({
            'Alytus': '알리투스',
            'Biržai': '비르자이',
            'Dubingiai': '두빙갸이',
            'Įsrutis': '이스루티스',
            'Kaunas': '카우나스',
            'Kernavė': '케르나베',
            'Klaipėda': '클라이페다',
            'Marijampolė': '마리얌폴레',
            'Mažeikiai': '마제이캬이',
            'Panevėžys': '파네베지스',
            'Šiauliai': '샤울랴이',
            'Trakai': '트라카이',
            'Vilnius': '빌뉴스',
        })