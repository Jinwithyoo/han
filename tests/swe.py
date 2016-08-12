# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.swe import Swedish


class SwedishTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0213.jsp """

    lang = Swedish()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0111.jsp """
        self.assert_examples({
            'bal': '발',
            'snabbt': '스납트',
            'Jacob': '야코브',
            'Carlsson': '칼손',
            'Celsius': '셀시우스',
            'Ericson': '에릭손',
            'charm': '샤름',
            'och': '오크',
            'dag': '다그',
            'dricka': '드리카',
            'Halmstad': '할름스타드',
            'Djurgården': '유르고르덴',
            'adjö': '아예',
            'Sundsvall': '순스발',
            'Falun': '팔룬',
            'luft': '루프트',
            'Gustav': '구스타브',
            'helgon': '헬곤',
            'Göteborg': '예테보리',
            'Geijer': '예이예르',
            'Gislaved': '이슬라베드',
            'älg': '엘리',
            'Strindberg': '스트린드베리',
            'Borg': '보리',
            'Magnus': '망누스',
            'Ragnar': '랑나르',
            'Agnes': '앙네스',
            'högst': '획스트',
            'Grönberg': '그뢴베리',
            'Gjerstad': '예르스타드',
            'Gjörwell': '예르벨',
            'Hälsingborg': '헬싱보리',
            'hyra': '휘라',
            'Dahl': '달',
            'Hjälmaren': '옐마렌',
            'Hjalmar': '얄마르',
            'Hjort': '요르트',
            'Jansson': '얀손',
            'Jönköping': '옌셰핑',
            'Johansson': '요한손',
            'börja': '뵈리아',
            'fjäril': '피에릴',
            'mjuk': '미우크',
            'mjöl': '미엘',
            'Karl': '칼',
            'Kock': '코크',
            'Kungsholm': '쿵스홀름',
            'Kerstin': '셰르스틴',
            'Norrköping': '노르셰핑',
            'Lysekil': '뤼세실',
            'oktober': '옥토베르',
            'Fredrik': '프레드리크',
            'kniv': '크니브',
            'vacker': '바케르',
            'Stockholm': '스톡홀름',
            'bock': '보크',
            'Kjell': '셸',
            'Kjula': '슐라',
            'Linköping': '린셰핑',
            'tala': '탈라',
            'tal': '탈',
            'Ljusnan': '유스난',
            'Södertälje': '쇠데르텔리에',
            'detalj': '데탈리',
            'Malmö': '말뫼',
            'samtal': '삼탈',
            'hummer': '훔메르',
            'Norrköping': '노르셰핑',
            'Vänern': '베네른',
            'land': '란드',
            'Karlshamn': '칼스함',
            'Borlänge': '볼렝에',
            'kung': '쿵',
            'lång': '롱',
            'anka': '앙카',
            'Sankt': '상트',
            'bank': '방크',
            'Piteå': '피테오',
            'knappt': '크납트',
            'Uppsala': '웁살라',
            'kamp': '캄프',
            'Malmqvist': '말름크비스트',
            'Lindqvist': '린드크비스트',
            'röd': '뢰드',
            'Wilander': '빌란데르',
            'Björk': '비에르크',
            'Erlander': '엘란데르',
            'Karlgren': '칼그렌',
            'Jarl': '얄',
            'sommar': '솜마르',
            'Storvik': '스토르비크',
            'dans': '단스',
            'Schack': '샤크',
            'Schein': '셰인',
            'revansch': '레반슈',
            'Nässjö': '네셰',
            'sjukhem': '슈크헴',
            'Sjöberg': '셰베리',
            'Skoglund': '스코글룬드',
            'Skellefteå': '셸레프테오',
            'Skövde': '셰브데',
            'Skeppsholmen': '솁스홀멘',
            'Hammarskjöld': '함마르셸드',
            'Skjöldebrand': '셸데브란드',
            'Stjärneborg': '셰르네보리',
            'Oxenstjerna': '옥센셰르나',
            'Göta': '예타',
            'Botkyrka': '봇쉬르카',
            'Trelleborg': '트렐레보리',
            'båt': '보트',
            'Luther': '루테르',
            'Thunberg': '툰베리',
            'lektion': '렉숀',
            'station': '스타숀',
            'tjeck': '셰크',
            'Tjåkkå': '쇼코',
            'tjäna': '셰나',
            'tjugo': '슈고',
            'Sverige': '스베리예',
            'Wasa': '바사',
            'Swedenborg': '스베덴보리',
            'Eslöv': '에슬뢰브',
            'Axel': '악셀',
            'Alexander': '알렉산데르',
            'sex': '섹스',
            'Zachris': '사크리스',
            'zon': '손',
            'Lorenzo': '로렌소',
            'Kalix': '칼릭스',
            'Falun': '팔룬',
            'Alvesta': '알베스타',
            'Enköping': '엔셰핑',
            'Svealand': '스베알란드',
            'Mälaren': '멜라렌',
            'Vänern': '베네른',
            'Trollhättan': '트롤헤탄',
            'Idre': '이드레',
            'Kiruna': '키루나',
            'Åmål': '오몰',
            'Västerås': '베스테로스',
            'Småland': '스몰란드',
            'Boden': '보덴',
            'Stockholm': '스톡홀름',
            'Örebro': '외레브로',
            'Östersund': '외스테르순드',
            'Björn': '비에른',
            'Linköping': '린셰핑',
            'Umeå': '우메오',
            'Luleå': '룰레오',
            'Lund': '룬드',
            'Ystad': '위스타드',
            'Nynäshamn': '뉘네스함',
            'Visby': '비스뷔',
        })

    def test_1st(self):
        """제1항
        1. b, g가 무성 자음 앞에 올 때에는 받침 'ㅂ, ㄱ'으로 적는다.
        2. k, ck, p, t는 무성 자음 앞에서 받침 'ㄱ, ㄱ, ㅂ, ㅅ'으로 적는다.
        """
        self.assert_examples({
            'snabbt': '스납트',
            'högst': '획스트',
            'oktober': '옥토베르',
            'Stockholm': '스톡홀름',
            'Uppsala': '웁살라',
            'Botkyrka': '봇쉬르카',
        })

    def test_2nd(self):
        """제2항: c는 'ㅋ'으로 적되, e, i, a, y, o 앞에서는 'ㅅ'으로 적는다."""
        self.assert_examples({
            'campa': '캄파',
            'Celsius': '셀시우스',
        })

    def test_3rd(self):
        """제3항: g
        1. 모음 앞의 g는 'ㄱ'으로 적되, e, i, a, y, o 앞에서는 '이'로 적고
           뒤따르는 모음과 합쳐 적는다.
        2. lg, rg의 g는 '이'로 적는다
        3. n 앞의 g는 'ㅇ'으로 적는다.
        4. 무성 자음 앞의 g는 받침 'ㄱ'으로 적는다.
        5. 그 밖의 자음 앞과 어말에서는 '그'로 적는다.
        """
        self.assert_examples({
            'Gustav': '구스타브',
            'Göteborg': '예테보리',
            'älg': '엘리',
            'Borg': '보리',
            'Magnus': '망누스',
            'högst': '획스트',
            'Ludvig': '루드비그',
            'Greta': '그레타',
        })

    def test_4th(self):
        """제4항: j는 자음과 모음 사이에 올 때에 앞의 자음과 합쳐서 적는다."""
        self.assert_examples({
            'fjäril': '피에릴',
            'mjuk': '미우크',
            'kedja': '셰디아',
            'Björn': '비에른',
        })

    def test_5th(self):
        """제5항
        k는 'ㅋ'으로 적되, e, i, a, y, o 앞에서는 '시'로 적고 뒤따르는 모음과
        합쳐 적는다.
        """
        self.assert_examples({
            'Kungsholm': '쿵스홀름',
            'Norrköping': '노르셰핑',
        })

    def test_6th(self):
        """제6항
        어말 또는 자음 앞의 l은 받침 'ㄹ'로 적고, 어중의 l이 모음 앞에 올
        때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            'folk': '폴크',
            'tal': '탈',
            'tala': '탈라',
        })

    def test_7th(self):
        """제7항
        어두의 lj는 '이'로 적되 뒤따르는 모음과 합쳐 적고, 어중의 lj는
        'ㄹ리'로 적는다.
        """
        self.assert_examples({
            'Ljusnan': '유스난',
            'Södertälje': '쇠데르텔리에',
        })

    def test_8th(self):
        """제8항
        n은 어말에서 m 다음에 올 때 적지 않는다.
        """
        self.assert_examples({
            'Karlshamn': '칼스함',
            'namn': '남',
        })

    def test_9th(self):
        """제9항
        nk는 자음 t 앞에서는 'ㅇ'으로, 그 밖의 경우에는 'ㅇ크'로 적는다.
        """
        self.assert_examples({
            'anka': '앙카',
            'Sankt': '상트',
            'punkt': '풍트',
            'bank': '방크',
        })

    def test_10th(self):
        """제10항
        sk는 '스ㅋ'으로 적되 e, i, a, y, o 앞에서는 '시'로 적고, 뒤따르는
        모음과 합쳐 적는다.
        """
        self.assert_examples({
            'Skoglund': '스코글룬드',
            'skuldra': '스쿨드라',
            'skål': '스콜',
            'skörd': '셰르드',
            'skydda': '쉬다',
        })

    def test_11st(self):
        """제11항
        o는 '외'로 적되 g, j, k, kj, lj, skj 다음에서는 '에'로 적고, 앞의
        '이' 또는 '시'와 합쳐서 적는다. 다만, jo 앞에 그 밖의 자음이 올 때에는
        j는 앞의 자음과 합쳐 적고, o는 '에'로 적는다.
        """
        self.assert_examples({
            'Örebro': '외레브로',
            'Göta': '예타',
            'Jönköping': '옌셰핑',
            'Björn': '비에른',
            'Björling': '비엘링',
            'mjöl': '미엘',
        })

    def test_12nd(self):
        """제12항
        같은 자음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다. 단, mm,
        nn은 모음 앞에서 'ㅁㅁ', 'ㄴㄴ'으로 적는다.
        """
        self.assert_examples({
            'Kattegatt': '카테가트',
            'Norrköping': '노르셰핑',
            'Uppsala': '웁살라',
            'Bromma': '브롬마',
            'Dannemora': '단네모라',
        })

    def test_people(self):
        self.assert_examples({
            'Sankta Ragnhild': '상타 랑힐드',
        })