# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.pol import Polish


class PolishTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0208.jsp """

    lang = Polish()

    def test_people(self):
        self.assert_examples({
            'Jerzy Andrzejewski': '예지 안제예프스키',
            'Stefan Banach': '스테판 바나흐',
            'Stanisław Barańczak': '스타니스와프 바란차크',
            'Marek Belka': '마레크 벨카',
            'Seweryn Bialer': '세베린 비알레르',
            'Bolesław Bierut': '볼레스와프 비에루트',
            'Zbigniew Boniek': '즈비그니에프 보니에크',
            'Bogdan Borusewicz': '보그단 보루세비치',
            'Zbigniew Bujak': '즈비그니에프 부야크',
            'Jerzy Buzek': '예지 부제크',
            'Włodzimierz Cimoszewicz': '브워지미에시 치모셰비치',
            'Józef Cyrankiewicz': '유제프 치란키에비치',
            'Ignacy Daszyński': '이그나치 다신스키',
            'Kazimierz Deyna': '카지미에시 데이나',
            'Roman Dmowski': '로만 드모프스키',
            'Jerzy Dudek': '예지 두데크',
            'Dariusz Dziekanowski': '다리우시 지에카노프스키',
            'Feliks Dzierżyński': '펠릭스 지에르진스키',
            'Kazimierz Fajans': '카지미에시 파얀스',
            'Magdalena Frackowiak': '마그달레나 프라츠코비아크',
            'Kazimierz Funk': '카지미에시 푼크',
            'Edward Gierek': '에드바르트 기에레크',
            'Józef Glemp': '유제프 글렘프',
            'Leopold Godowsky': '레오폴트 고도프스키',
            'Witold Gombrowicz': '비톨트 곰브로비치',
            'Władysław Gomułka': '브와디스와프 고무우카',
            'Jerzy Grotowski': '예지 그로토프스키',
            'Zbigniew Herbert': '즈비그니에프 헤르베르트',
            'Leonid Hurwicz': '레오니트 후르비치',
            'Jarosław Iwaszkiewicz': '야로스와프 이바슈키에비치',
            'Aleksander Jabłoński': '알렉산데르 야브원스키',
            'Jadwiga Andegaweńska': '야드비가 안데가벤스카',
            'Jagiełło': '야기에워',
            'Wanda Jakubowska': '반다 야쿠보프스카',
            'Henryk Jankowski': '헨리크 얀코프스키',
            'Wojciech Jaruzelski': '보이치에흐 야루젤스키',
            'Otylia Jędrzejczak': '오틸리아 옝제이차크',
            'Jan Andrzej Paweł Kaczmarek': \
                '얀 안제이 파베우 카치마레크',
            'Jarosław Kaczyński': '야로스와프 카친스키',
            'Lech Kaczyński': '레흐 카친스키',
            'Stanisław Kania': '스타니스와프 카니아',
            'Krzysztof Kieślowski': '크시슈토프 키에실로프스키',
            'Stefan Kisielewski': '스테판 키시엘레프스키',
            'Leszek Kołakowski': '레셰크 코와코프스키',
            'Bronisław Komorowski': '브로니스와프 코모로프스키',
            'Paweł Korzeniowski': '파베우 코제니오프스키',
            'Tadeusz Kościuszko': '타데우시 코시치우슈코',
            'Justyna Kowalczyk': '유스티나 코발치크',
            'Zygmunt Krasiński': '지그문트 크라신스키',
            'Jacek Krzynówek': '야체크 크시누베크',
            'Jacek Kuroń': '야체크 쿠론',
            'Aleksander Kwaśniewski': '알렉산데르 크바시니에프스키',
            'Wanda Landowska': '반다 란도프스카',
            'Grzegorz Lato': '그제고시 라토',
            'Joachim Lelewel': '요아힘 렐레벨',
            'Włodzimierz Lubański': '브워지미에시 루반스키',
            'Jan Łukasiewicz': '얀 우카시에비치',
            'Bronisław Malinowski': '브로니스와프 말리노프스키',
            'Adam Małysz': '아담 마위시',
            'Kazimierz Marcinkiewicz': '카지미에시 마르친키에비치',
            'Tadeusz Mazowiecki': '타데우시 마조비에츠키',
            'Zbigniew Messner': '즈비그니에프 메스네르',
            'Adam Michnik': '아담 미흐니크',
            'Adam Mickiewicz': '아담 미츠키에비치',
            'Stanisław Mikołajczyk': '스타니스와프 미코와이치크',
            'Leszek Miller': '레셰크 밀레르',
            'Czesław Miłosz': '체스와프 미워시',
            'Sławomir Mrożek': '스와보미르 므로제크',
            'Cyprian Kamil Norwid': '치프리안 카밀 노르비트',
            'Edward Ochab': '에드바르트 오하프',
            'Eliza Orzeszkowa': '엘리자 오제슈코바',
            'Ignacy Jan Paderewski': '이그나치 얀 파데레프스키',
            'Krzysztof Penderecki': '크시슈토프 펜데레츠키',
            'Józef Piłsudski': '유제프 피우수트스키',
            'Jacek Podsiadło': '야체크 포트시아드워',
            'Anja Rubik': '아냐 루비크',
            'Mateusz Sawrymowicz': '마테우시 사브리모비치',
            'Wacław Sierpiński': '바츠와프 시에르핀스키',
            'Maria Skłodowska': '마리아 스크워도프스카',
            'Włodzimierz Smolarek': '브워지미에시 스몰라레크',
            'Katarzyna Sowula': '카타지나 소불라',
            'Andrzej Stasiuk': '안제이 스타시우크',
            'Andrzej Szarmach': '안제이 샤르마흐',
            'Wojciech Szczęsny': '보이치에흐 슈쳉스니',
            'Piotr Szewc': '피오트르 셰프츠',
            'Sławomir Szmal': '스와보미르 슈말',
            'Rafał Szukała': '라파우 슈카와',
            'Alfred Tarski': '알프레트 타르스키',
            'Stefan Themerson': '스테판 테메르손',
            'Olga Tokarczuk': '올가 토카르추크',
            'Jan Tomaszewski': '얀 토마셰프스키',
            'Donald Tusk': '도날트 투스크',
            'Andrzej Wajda': '안제이 바이다',
            'Lech Wałęsa': '레흐 바웬사',
            'Mia Wasikowska': '미아 바시코프스카',
            'Wanda Wasilewska': '반다 바실레프스카',
            'Adam Ważyk': '아담 바지크',
            'Aleksander Wielopolski': '알렉산데르 비엘로폴스키',
            'Henryk Wieniawski': '헨리크 비에니아프스키',
            'Ernest Wilimowski': '에르네스트 빌리모프스키',
            'Stanisław Ignacy Witkiewicz': \
                '스타니스와프 이그나치 비트키에비치',
            'Michał Witkowski': '미하우 비트코프스키',
            'Karol Wojtyła': '카롤 보이티와',
            'Katarzyna Woźniak': '카타지나 보지니아크',
            'Stanisław Wyspiański': '스타니스와프 비스피안스키',
            'Stefan Wyszyński': '스테판 비신스키',
            'Ludwik Łazarz Zamenhof': '루드비크 와자시 자멘호프',
            'Krystian Zimerman': '크리스티안 지메르만',
            'Luiza Złotkowska': '루이자 즈워트코프스카',
            'Florian Znaniecki': '플로리안 즈나니에츠키',
            'Stefan Żeromski': '스테판 제롬스키',
            'Maciej Żurawski': '마치에이 주라프스키',
        })

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0106.jsp """
        self.assert_examples({
            'burak': '부라크',
            'szybko': '십코',
            'dobrze': '도브제',
            'chleb': '흘레프',
            'cel': '첼',
            'Balicki': '발리츠키',
            'noc': '노츠',
            'dać': '다치',
            'dach': '다흐',
            'zdrowy': '즈드로비',
            'słodki': '스워트키',
            'pod': '포트',
            'fasola': '파솔라',
            'befsztyk': '베프슈티크',
            'góra': '구라',
            'grad': '그라트',
            'targ': '타르크',
            'herbata': '헤르바타',
            'Hrubieszów': '흐루비에슈프',
            'kino': '키노',
            'daktyl': '닥틸',
            'król': '크룰',
            'bank': '반크',
            'lis': '리스',
            'kolano': '콜라노',
            'motyl': '모틸',
            'most': '모스트',
            'zimno': '짐노',
            'sam': '삼',
            'nerka': '네르카',
            'dokument': '도쿠멘트',
            'dywan': '디반',
            'Gdańsk': '그단스크',
            'Poznań': '포즈난',
            'para': '파라',
            'Słupsk': '스웁스크',
            'chłop': '흐워프',
            'rower': '로베르',
            'garnek': '가르네크',
            'sznur': '슈누르',
            'serce': '세르체',
            'srebro': '스레브로',
            'pas': '파스',
            'ślepy': '실레피',
            'dziś': '지시',
            'tam': '탐',
            'matka': '마트카',
            'but': '부트',
            'Warszawa': '바르샤바',
            'piwnica': '피브니차',
            'krew': '크레프',
            'zamek': '자메크',
            'zbrodnia': '즈브로드니아',
            'wywóz': '비부스',
            'gwoździk': '그보지지크',
            'więź': '비엥시',
            'żyto': '지토',
            'różny': '루주니',
            'łyżka': '위슈카',
            'straż': '스트라시',
            'chory': '호리',
            'kuchnia': '쿠흐니아',
            'dach': '다흐',
            'dziura': '지우라',
            'dzwon': '즈본',
            'mosiądz': '모시옹츠',
            'niedźwiedź': '니에치비에치',
            'drzewo': '제보',
            'łodż': '워치',
            'czysty': '치스티',
            'beczka': '베치카',
            'klucz': '클루치',
            'szary': '샤리',
            'musztarda': '무슈타르다',
            'kapelusz': '카펠루시',
            'rzeka': '제카',
            'Przemyśl': '프셰미실',
            'kołnierz': '코우니에시',
            'jasny': '야스니',
            'kraj': '크라이',
            'łono': '워노',
            'głowa': '그워바',
            'bułka': '부우카',
            'kanał': '카나우',
            'trawa': '트라바',
            'trąba': '트롱바',
            'mąka': '몽카',
            'kąt': '콩트',
            'tą': '통',
            'zero': '제로',
            'kępa': '켕파',
            'węgorz': '벵고시',
            'Częstochowa': '쳉스토호바',
            'proszę': '프로셰',
            'zima': '지마',
            'udo': '우도',
            'próba': '프루바',
            'kula': '쿨라',
            'daktyl': '닥틸',
        })

    def test_1st(self):
        """제1항: k, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        self.assert_examples({
            'zamek': '자메크',
            'mokry': '모크리',
            'Słupsk': '스웁스크',
        })

    def test_2nd(self):
        """제2항: b, d, g
        1. 어말에 올 때에는 '프', '트', '크'로 적는다.
        2. 유성 자음 앞에서는 '브', '드', '그'로 적는다.
        3. 무성 자음 앞에서 b, g는 받침으로 적고, d는 '트'로 적는다.
        """
        self.assert_examples({
            'od': '오트',
            'zbrodnia': '즈브로드니아',
            'Grabski': '그랍스키',
            'odpis': '오트피스',
        })

    def test_3rd(self):
        """제3항: w, z, ź, dz, ż, rz, sz
        1. w, z, ź, dz가 무성 자음 앞이나 어말에 올 때에는 '프, 스, 시, 츠'로
           적는다.
        2. ż와 rz는 모음 앞에 올 때에는 'ㅈ'으로 적되, 앞의 자음이 무성
           자음일 때에는 '시'로 적는다. 유성 자음 앞에 올 때에는 '주', 무성
           자음 앞에 올 때에는 '슈', 어말에 올 때에는 '시'로 적는다.
        3. sz는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        self.assert_examples({
            'zabawka': '자바프카',
            'obraz': '오브라스',
            'Rzeszów': '제슈프',
            'Przemyśl': '프셰미실',
            'grzmot': '그주모트',
            'łóżko': '우슈코',
            'pęcherz': '펭헤시',
            'koszt': '코슈트',
            'kosz': '코시',
        })

    def test_4th(self):
        """제4항: ł
        1. ł는 뒤따르는 모음과 결합할 때 합쳐서 적는다. (ło는 '워'로 적는다.)
           다만, 자음 뒤에 올 때에는 두 음절로 갈라 적는다.
        2. oł는 '우'로 적는다.
        """
        self.assert_examples({
            'łono': '워노',
            'głowa': '그워바',
            'przyjaciół': '프시야치우',
        })

    def test_5th(self):
        """제5항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            'olej': '올레이',
        })

    def test_6th(self):
        """제6항: m
        어두의 m이 l, r 앞에 올 때에는 '으'를 붙여 적는다.
        """
        self.assert_examples({
            'mleko': '믈레코',
            'mrówka': '므루프카',
        })

    def test_7th(self):
        """제7항: ę
        ę은 '엥'으로 적는다. 다만, 어말의 ę는 '에'로 적는다.
        """
        self.assert_examples({
            'ręka': '렝카',
            'proszę': '프로셰',
        })

    def test_8th(self):
        """제8항
        'ㅈ', 'ㅊ'으로 표기되는 자음(c, z) 뒤의 이중 모음은 단모음으로 적는다.
        """
        self.assert_examples({
            'stacja': '스타차',
            'fryzjer': '프리제르',
        })

    def test_etc(self):
        self.assert_examples({
            'przjyaciół': '프시아치우',
        })