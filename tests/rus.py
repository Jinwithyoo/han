# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.rus import Russian


class RussianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0221.jsp """

    lang = Russian()

    def test_examples_of_iceager(self):
        self.assert_examples({
            'Премьер': '프레미예르',
            'Авксесия': '압크세시야',
        })

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0119.jsp """
        self.assert_examples({
            'Болотов': '볼로토프',
            'Бобров': '보브로프',
            'Курбский': '쿠릅스키',
            'Глеб': '글레프',
            'Гончаров': '곤차로프',
            'Манечка': '마네치카',
            'Якубович': '야쿠보비치',
            'Дмитрий': '드미트리',
            'Бенедиктов': '베네딕토프',
            'Находка': '나홋카',
            'Восход': '보스호트',
            'Фёдор': '표도르',
            'Ефремов': '예프레모프',
            'Иосиф': '이오시프',
            'Гоголь': '고골',
            'Мусоргский': '무소륵스키',
            'Богдан': '보그단',
            'Андарбаг': '안다르바크',
            'Хабаровск': '하바롭스크',
            'Ахматова': '아흐마토바',
            'Ойстрах': '오이스트라흐',
            'Калмык': '칼미크',
            'Аксаков': '악사코프',
            'Квас': '크바스',
            'Владивосток': '블라디보스토크',
            'Ленин': '레닌',
            'Николай': '니콜라이',
            'Крылов': '크릴로프',
            'Павел': '파벨',
            'Михаийл': '미하일',
            'Максим': '막심',
            'Мценск': '므첸스크',
            'Надя': '나댜',
            'Стефан': '스테판',
            'Пётр': '표트르',
            'Ростопчиня': '로스톱치냐',
            'Псков': '프스코프',
            'Майкоп': '마이코프',
            'Рыбинск': '리빈스크',
            'Лермонтов': '레르몬토프',
            'Артём': '아르툠',
            'Василий': '바실리',
            'Стефан': '스테판',
            'Борис': '보리스',
            'Шелгунов': '셸구노프',
            'Шишков': '시시코프',
            'Щербаков': '셰르바코프',
            'Щирец': '시레츠',
            'борщ': '보르시',
            'Татьяна': '타티야나',
            'Хватков': '흐밧코프',
            'Тверь': '트베리',
            'Бурят': '부랴트',
            'Гатчина': '가치나',
            'Тютчев': '튜체프',
            'Капица': '카피차',
            'Цветаева': '츠베타예바',
            'Брятск': '브랴츠크',
            'Якутск': '야쿠츠크',
            'Веревкин': '베렙킨',
            'Достоевский': '도스토옙스키',
            'Владивосток': '블라디보스토크',
            'Марков': '마르코프',
            'Зайчев': '자이체프',
            'Кузнецов': '쿠즈네초프',
            'Агрыз': '아그리스',
            'Жадовская': '자돕스카야',
            'Жданов': '즈다노프',
            'Лужков': '루시코프',
            'Кебеж': '케베시',
            'Юрий': '유리',
            'Андрей': '안드레이',
            'Белый': '벨리',
            'Аксаков': '악사코프',
            'Абакан': '아바칸',
            'Петров': '페트로프',
            'Евгений': '예브게니',
            'Алексеев': '알렉세예프',
            'Эртель': '예르텔',
            'Иванов': '이바노프',
            'Иосиф': '이오시프',
            'Хомяков': '호먀코프',
            'Ока': '오카',
            'Ушаков': '우샤코프',
            'Сарапул': '사라풀',
            'Салтыков': '살티코프',
            'Кыра': '키라',
            'Белый': '벨리',
            'Ясинский': '야신스키',
            'Адыгея': '아디게야',
            'Соловьёв': '솔로비요프',
            'Артём': '아르툠',
            'Юрий': '유리',
            'Юрга': '유르가',
        })

    def test_1st(self):
        """제1항: p(п), t(т), k(к), b(б), d(д), g(г), f(ф), v(в)
        파열음과 마찰음 f(ф)·v(в)는 무성 자음 앞에서는 앞 음절의 받침으로
        적고, 유성 자음 앞에서는 ‘으'를 붙여 적는다.
        """
        self.assert_examples({
            'Садко': '삿코',
            'Агрыз': '아그리스',
            'Акбаур': '아크바우르',
            'Ростопчиня': '로스톱치냐',
            'Акмеизм': '아크메이즘',
            'Рубцовск': '룹촙스크',
            'Брятск': '브랴츠크',
            'Лопатка': '로팟카',
            'Ефремов': '예프레모프',
            'Достоевский': '도스토옙스키',
        })

    def test_2nd(self):
        """제2항: z(з), zh(ж)
        z(з)와 zh(ж)는 유성 자음 앞에서는 ‘즈'로 적고 무성 자음 앞에서는
        각각 ‘스, 시'로 적는다.
        """
        self.assert_examples({
            'Назрань': '나즈란',
        #    u'Нижний Тагил': u'니즈니타길',
            'Нижний Тагил': '니즈니 타길',
            'Острогожск': '오스트로고시스크',
            'Лужков': '루시코프',
        })

    def test_3rd(self):
        """제3항
        지명의 -grad(град)와 -gorod(город)는 관용을 살려 각각 ‘-그라드',
        ‘-고로드'로 표기한다.
        """
        self.assert_examples({
            'Волгоград': '볼고그라드',
            'Калининград': '칼리닌그라드',
            'Славгород': '슬라브고로드',
        })

    def test_4th(self):
        """제4항
        자음 앞의 -ds(дс)-는 ‘츠'로 적는다.
        """
        self.assert_examples({
            'Петрозаводск': '페트로자보츠크',
            'Вернадский': '베르나츠키',
        })

    def test_5th(self):
        """제5항
        어말 또는 자음 앞의 l(л)은 받침 ‘ㄹ'로 적고, 어중의 l이 모음 앞에
        올 때에는 ‘ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            'Павел': '파벨',
            'Николаевич': '니콜라예비치',
            'Земля': '제믈랴',
            'Цимлянск': '치믈랸스크',
        })

    def test_6th(self):
        """제6항
        l'(ль), m(м)이 어두 자음 앞에 오는 경우에는 각각 ‘리', ‘므'로 적는다.
        """
        self.assert_examples({
            'Льбовна': '리보브나',
            'Мценск': '므첸스크',
        })

    def test_7th(self):
        """제7항
        같은 자음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다. 다만,
        mm(мм), nn(нн)은 모음 앞에서 ‘ㅁㅁ', ‘ㄴㄴ'으로 적는다.
        """
        self.assert_examples({
            'Гиппиус': '기피우스',
            'Аввакум': '아바쿰',
            'Одесса': '오데사',
            'Акколь': '아콜',
            'Соллогуб': '솔로구프',
            'Анна': '안나',
            'Гамма': '감마',
        })

    def test_8th(self):
        """제8항
        e(е, э)는 자음 뒤에서는 ‘에'로 적고, 그 외의 경우에는 ‘예'로 적는다.
        """
        self.assert_examples({
            'Алексей': '알렉세이',
            'Егвекинот': '예그베키노트',
        })

    def test_9th(self):
        """제9항: 연음 부호 '(ь)
        연음 부호 '(ь)은 ‘이'로 적는다. 다만 l', m', n'(ль, мь, нь)이 자음
        앞이나 어말에 오는 경우에는 적지 않는다.
        """
        self.assert_examples({
            'Льбовна': '리보브나',
            'Игорь': '이고리',
            'Илья': '일리야',
            'Дьяково': '디야코보',
            'Ольга': '올가',
        #    u'Пермь': u'페름',
            'Рязань': '랴잔',
            'Гоголь': '고골',
        })

    def test_10th(self):
        """제10항
        dz(дз), dzh(дж)는 각각 z, zh와 같이 적는다.
        """
        self.assert_examples({
            'Дзержинский': '제르진스키',
            'Таджикистан': '타지키스탄',
        })