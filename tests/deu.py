# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.deu import German


class GermanTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0202.jsp """

    lang = German()

    def test_1st(self):
        """제1항: 
        1. 자음 앞의 는 '으'를 붙여 적는다.
        2. 어말의 '는 '어'로 적는다.
        3. 복합어 및 파생어의 선행 요소가 로 끝나는 경우는 2의 규정을 준용한다.
        """
        self.assert_examples({
            'Hormon': '호르몬',
            'Hermes': '헤르메스',
            'Herr': '헤어',
            'Rasur': '라주어',
            'Tür': '튀어',
            'Ohr': '오어',
            'Vater': '파터',
            'Schiller': '실러',
        # 합성어
        #    u'verarbeiten': u'페어아르바이텐',
        #    u'zerknirschen': u'체어크니르셴',
        #    u'Fürsorge': u'퓌어조르게',
        #    u'Vorbild': u'포어빌트',
        #    u'außerhalb': u'아우서할프',
        #    u'Urkunde': u'우어쿤데',
        #    u'Vaterland': u'파터란트',
        })

    def test_2nd(self):
        """제2항: 어말의 파열음은 '으'를 붙여 적는 것을 원칙으로 한다."""
        self.assert_examples({
            'Rostock': '로스토크',
            'Stadt': '슈타트',
        })

    def test_3rd(self):
        """제3항: 철자 'berg', 'burg'는 '베르크', '부르크'로 통일해서 적는다."""
        self.assert_examples({
            'Heidelberg': '하이델베르크',
            'Hamburg': '함부르크',
        })

    def test_4th(self):
        """제4항: 
        1. 어말 또는 자음 앞에서는 '슈'로 적는다.
        2.  앞에서는 'ㅅ'으로 적는다.
        3. 그 밖의 모음 앞에서는 뒤따르는 모음에 따라 '샤, 쇼, 슈' 등으로 적는다.
        """
        self.assert_examples({
            'Mensch': '멘슈',
            'Mischling': '미슐링',
            'Schüler': '쉴러',
            'schön': '쇤',
            'Schatz': '샤츠',
            'schon': '숀',
            'Schule': '슐레',
            'Schelle': '셸레',
        })

    def test_5th(self):
        """제5항: 로 발음되는 äu, eu는 '오이'로 적는다."""
        self.assert_examples({
            'läuten': '로이텐',
            'Fräulein': '프로일라인',
            'Europa': '오이로파',
            'Freundin': '프로인딘',
        })

    def test_6th(self):
        """연음, -st, ich/achlaut, 움라우트, 강세음절의 r"""
        self.assert_examples({
            'ein': '아인',
            'einer': '아이너',
            'einen': '아이넨',
            'ist': '이스트',
            'bist': '비스트',
            'Buch': '부흐',
            'ich': '이히',
            'Königen': '쾨니겐',
            'für': '퓌어',
            'der': '데어',
        })

    def test_7th(self):
        """준칙: 모음 또는 l 앞의 ng에는 'ㄱ'을 첨가하여 표기한다."""
        self.assert_examples({
            'Tübingen': '튀빙겐',
            'Spengler': '슈펭글러',
        })

    def test_8th(self):
        """기타 용례"""
        self.assert_examples({
            'Fischer': '피셔',
            'Richard': '리하르트',
            'Niclas': '니클라스',
            'Kupfer': '쿠퍼',
            'Beelitz': '벨리츠',
            'Heidegger': '하이데거',
            'Guggenheim': '구겐하임',
            'Fuggerei': '푸게라이',
            'Grotesk': '그로테스크',
            'norddeutsch': '노르트도이치',
            'Berggarten': '베르크가르텐',
            'Augsburg': '아우크스부르크',
            'Herbst': '헤르프스트',
            'Alexander': '알렉산더',
            'Max': '막스',
            'Sachsen': '작센',
            'Habsburg': '합스부르크',
            'Feuer': '포이어',
            'Bayern': '바이에른',
            'Meyer': '마이어',
            'Köln': '쾰른',
            'Wilhelm': '빌헬름',
            'Helmut': '헬무트',
            'Kellner': '켈너',
            'Michael': '미하엘',
            'Daniel': '다니엘',
            'Samuel': '자무엘',
            'Henrietta': '헨리에타',
            'Christine': '크리스티네',
            'Amadeus': '아마데우스',
            'Matthäus': '마테우스',
            'Steffen': '슈테펜',
            'Reval': '레발',
            'Frank': '프랑크',
            'Emmy': '에미',
            'Freiherr': '프라이헤어',
            'Karlsruhe': '카를스루에',
        })
