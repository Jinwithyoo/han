# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.aze import Azerbaijani


class AzerbaijaniTestCase(HangulizeTestCase):

    lang = Azerbaijani()

    def test_people(self):
        self.assert_examples({
            'Namiq Abdullayev': '나미크 아브둘라예프',
            'Qəmər Almaszadə': '게메르 알마스자데',
            'Heydər Əliyev': '헤이데르 엘리예프',
            'İlham Əliyev': '일함 엘리예프',
            'Hüseyn Ərəblinski': '휘세인 에레블린스키',
            'Rəşid Behbudov': '레시트 베흐부도프',
            'Bülbül': '뷜뷜',
            'Cəfər Cabbarlı': '제페르 자발르',
            'Vaqif Cavadov': '바기프 자바도프',
            'Hüseyn Cavid': '휘세인 자비트',
            'Füzuli': '퓌줄리',
            'Üzeyir Hacıbəyov': '위제이르 하즈베요프',
            'Mehdi Hüseynzadə': '메흐디 휘세인자데',
            'Kərim Kərimov': '케림 케리모프',
            'Fərid Mansurov': '페리트 만수로프',
            'Elnur Məmmədli': '엘누르 멤메들리',
            'Məhəmməd Mövlazadə': '메헴메트 뫼블라자데',
            'Əzizə Mustafazadə': '에지제 무스타파자데',
            'Vaqif Mustafazadə': '바기프 무스타파자데',
            'Mikayıl Müşfiq': '미카이을 뮈슈피크',
            'Xurşidbanu Natəvan': '후르시드바누 나테반',
            'Hüseyn xan Naxçıvanski': '휘세인 한 나흐츠반스키',
            'Nəriman Nərimanov': '네리만 네리마노프',
            'İmadəddin Nəsimi': '이마데딘 네시미',
            'Mir-Möhsün Nəvvab': '미르뫼흐쉰 네바프',
            'Ramil Quliyev': '라밀 굴리예프',
            'Nigar Rəfibəyli': '니가르 레피베일리',
            'Artur Rəsizadə': '아르투르 레시자데',
            'Məhəmməd Əmin Rəsulzadə': '메헴메트 에민 레술자데',
            'Süleyman Rüstəm': '쉴레이만 뤼스템',
            'Rəsul Rza': '레술 르자',
            'Rəşad Sadıqov': '레샤트 사드고프',
            'Məmməd ağa Şahtaxtinski': '멤메트 아가 샤흐타흐틴스키',
            'Məhəmmədhüseyn Şəhriyar': '메헴메트휘세인 셰흐리야르',
            'Nigar Şıxlinskaya': '니가르 시으흘린스카야',
            'Zeynalabdin Tağıyev': '제이날라브딘 타그예프',
            'Aysel Teymurzadə': '아이셀 테이무르자데',
            'Səməd Vurğun': '세메트 부르군',
            'Fətəli xan Xoyski': '페텔리 한 호이스키',
        })

    def test_places(self):
        self.assert_examples({
            'Abşeron': '압셰론',
            'Ağdam': '아그담',
            'Azərbaycan': '아제르바이잔',
            'Bakı': '바크',
            'Gəncə': '겐제',
            'İçəri Şəhər': '이체리 셰헤르',
            'Lənkəran': '렌케란',
            'Mingəçevir': '민게체비르',
            'Naftalan': '나프탈란',
            'Naxçıvan': '나흐츠반',
            'Qəbələ': '게벨레',
            'Qobustan': '고부스탄',
            'Salyan': '살리안',
            'Sumqayıt': '숨가이으트',
            'Şəki': '셰키',
            'Şəmkir': '솀키르',
            'Şirvan': '시르반',
            'Talış': '탈르슈',
            'Tovuz': '토부스',
            'Xaçmaz': '하치마스',
            'Xınalıq': '흐날르크',
            'Xırdalan': '흐르달란',
            'Yevlax': '예블라흐',
            'Zaqatala': '자가탈라',
        })

    def test_others(self):
        self.assert_examples({
            'jurnal': '주르날',
        })
