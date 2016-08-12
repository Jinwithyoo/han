# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.ita import Italian


class ItalianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0205.jsp """

    lang = Italian()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0103.jsp """
        self.assert_examples({
            'Bologna': '볼로냐',
            'bravo': '브라보',
            'Como': '코모',
            'Sicilia': '시칠리아',
            'credo': '크레도',
            'Pinocchio': '피노키오',
            'cherubino': '케루비노',
            'Dante': '단테',
            'drizza': '드리차',
            'Firenze': '피렌체',
            'freddo': '프레도',
            'Galileo': '갈릴레오',
            'Genova': '제노바',
            'gloria': '글로리아',
            'hanno': '안노',
            'oh': '오',
            'Milano': '밀라노',
            'largo': '라르고',
            'palco': '팔코',
            'Macchiavelli': '마키아벨리',
            'mamma': '맘마',
            'Campanella': '캄파넬라',
            'Nero': '네로',
            'Anna': '안나',
            'divertimento': '디베르티멘토',
            'Pisa': '피사',
            'prima': '프리마',
            'quando': '콴도',
            'queto': '퀘토',
            'Roma': '로마',
            'Marconi': '마르코니',
            'Sorrento': '소렌토',
            'asma': '아스마',
            'sasso': '사소',
            'Torino': '토리노',
            'tranne': '트란네',
            'Vivace': '비바체',
            'manovra': '마노브라',
            'nozze': '노체',
            'mancanza': '만칸차',
            'abituro': '아비투로',
            'capra': '카프라',
            'erta': '에르타',
            'padrone': '파드로네',
            'infamia': '인파미아',
            'manica': '마니카',
            'oblio': '오블리오',
            'poetica': '포에티카',
            'uva': '우바',
            'spuma': '스푸마',
        })

    def test_1st(self):
        """제1항: gl
        i 앞에서는 'ㄹㄹ'로 적고, 그 밖의 경우에는 '글ㄹ'로 적는다.
        """
        self.assert_examples({
            'paglia': '팔리아',
            'egli': '엘리',
            'gloria': '글로리아',
            'glossa': '글로사',
        })

    def test_2nd(self):
        """제2항: gn
        뒤따르는 모음과 합쳐 '냐', '녜', '뇨', '뉴', '니'로 적는다.
        """
        self.assert_examples({
            'montagna': '몬타냐',
            'gneiss': '녜이스',
            'gnocco': '뇨코',
            'gnu': '뉴',
            'ogni': '오니',
        })

    def test_3rd(self):
        """제3항: sc
        sce는 '셰'로, sci는 '시'로 적고, 그 밖의 경우에는 '스ㅋ'으로 적는다.
        """
        self.assert_examples({
            'crescendo': '크레셴도',
            'scivolo': '시볼로',
            'Tosca': '토스카',
            'scudo': '스쿠도',
        })

    def test_4th(self):
        """제4항
        같은 자음이 겹쳤을 때에는 겹치지 않은 경우와 같이 적는다. 다만, -mm-,
        -nn-의 경우는 'ㅁㅁ', 'ㄴㄴ'으로 적는다.
        """
        self.assert_examples({
            'Puccini': '푸치니',
            'buffa': '부파',
            'allegretto': '알레그레토',
            'carro': '카로',
            'rosso': '로소',
            'mezzo': '메초',
            'gomma': '곰마',
            'bisnonno': '비스논노',
        })

    def test_5th(self):
        """제5항: c, g
        1. c와 g는 e, i 앞에서 각각 'ㅊ', 'ㅈ'으로 적는다.
        2. c와 g 다음에 ia, io, iu가 올 때에는 각각 '차, 초, 추',
           '자, 조, 주'로 적는다.
        """
        self.assert_examples({
            'cenere': '체네레',
            'genere': '제네레',
            'cima': '치마',
            'gita': '지타',
            'caccia': '카차',
            'micio': '미초',
        })

    def test_6th(self):
        """제6항: qu
        qu는 뒤따르는 모음과 합쳐 '콰, 퀘, 퀴' 등으로 적는다. 다만, o 앞에서는
        '쿠'로 적는다.
        """
        self.assert_examples({
            'soqquadro': '소콰드로',
            'quello': '퀠로',
            'quieto': '퀴에토',
            'quota': '쿠오타',
        })

    def test_7th(self):
        """제7항: l, ll
        어말 또는 자음 앞의 l, ll은 받침으로 적고, 어중의 l, ll이 모음 앞에
        올 때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            'sol': '솔',
            'polca': '폴카',
            'Carlo': '카를로',
            'quello': '퀠로',
        })

    def test_hangulize(self):
        self.assert_examples({
            'italia': '이탈리아',
            'Innocenti': '인노첸티',
            'Cerigotto': '체리고토',
            'Juventus': '유벤투스',
            'Schiavonia': '스키아보니아',
            'Fogli': '폴리',
            'Caravaggio': '카라바조',
            'nephos': '네포스',
            'sbozzacchisce': '스보차키셰',
            'Scalenghe': '스칼렌게',
            'Fabrizio': '파브리치오',
            'Anghiari': '안기아리',
            'soqquadro': '소콰드로',
            'Bologna': '볼로냐',
            'Fognini': '포니니',
            'Ignazio': '이냐치오',
            "Giro d'Italia": '지로 디탈리아',
            "per l'avvenire d'Italia": '페르 라베니레 디탈리아',
            'Rex': '렉스',
        })