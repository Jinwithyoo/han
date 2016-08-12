# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.jpn import Japanese


class JapaneseTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0206.jsp """

    lang = Japanese()

    def test_1st(self):
        """제1항: 촉음
        촉음(促音) [ッ(っ)]는 'ㅅ'으로 통일해서 적는다.
        """
        self.assert_examples({
            'サッポロ': '삿포로',
            'トットリ': '돗토리',
            'ヨッカイチ': '욧카이치',
        })

    def test_2nd(self):
        """제2항: 장모음
        장모음은 따로 표기하지 않는다.
        """
        self.assert_examples({
            'キュウシュウ': '규슈',
            'ニイガタ': '니가타',
            'トウキョウ': '도쿄',
            'オオサカ': '오사카',
        })

    def test_hangulize(self):
        self.assert_examples({
            'にほん': '니혼',
            'にほんばし': '니혼바시',
            'あかちゃん': '아카찬',
        })

    def test_examples_a_column(self):
        self.assert_examples({
            'あゆみ': '아유미',
            'あつぎ': '아쓰기',
            'あいづわかまつ': '아이즈와카마쓰',
            'あらかわ': '아라카와',
            'へいあん': '헤이안',
            'あきた': '아키타',
            'あきはばら': '아키하바라',
            'あおもり': '아오모리',
            'あまくさ': '아마쿠사',
            'あさま': '아사마',
            'あしお': '아시오',
            'あしかが': '아시카가',
            'あかぎ': '아카기',
            'あかいし': '아카이시',
            'おあかん': '오아칸',
            'あさひかわ': '아사히카와',
            'あご': '아고',
            'あたみ': '아타미',
            'あまみおお': '아마미오',
            'あいち': '아이치',
            'あんじょう': '안조',
            'あつみ': '아쓰미',
            'あかん': '아칸',
            'あそ': '아소',
            'あぶくま': '아부쿠마',
            'あげお': '아게오',
            'おわりあさひ': '오와리아사히',
            'あすか': '아스카',
            'あかし': '아카시',
            'あばしり': '아바시리',
            'あやべ': '아야베',
            'あしのこ': '아시노코',
            'あわじ': '아와지',
            'あまがさき': '아마가사키',
            'くろさわ あきら': '구로사와 아키라',
            'ごとう あつし': '고토 아쓰시',
            'きかい': '기카이',
            'あいづわかまつ': '아이즈와카마쓰',
            'いずみ': '이즈미',
            'かいなん': '가이난',
            'へいあん': '헤이안',
            'はぼまい': '하보마이',
            'すいた': '스이타',
            'こうらくえん': '고라쿠엔',
            'かすみがうら': '가스미가우라',
            'うらわ': '우라와',
            'うらかわ': '우라카와',
            'はちじょう': '하치조',
            'ようかいち': '요카이치',
            'はちおうじ': '하치오지',
            'はっこうだ': '핫코다',
            'てんりゅう': '덴류',
            'かわうち': '가와우치',
            'こまえ': '고마에',
            'こうらくえん': '고라쿠엔',
            'えな': '에나',
            'えとろふ': '에토로후',
            'かわごえ': '가와고에',
            'まえばし': '마에바시',
            'えちご': '에치고',
            'おまえ': '오마에',
            'えひめ': '에히메',
            'まつまえ': '마쓰마에',
            'くろしお': '구로시오',
            'つるおか': '쓰루오카',
            'とよおか': '도요오카',
            'はちおうじ': '하치오지',
            'やお': '야오',
            'ななお': '나나오',
            'おきなわ': '오키나와',
            'あおもり': '아오모리',
        })

    def test_examples_ka_column(self):
        self.assert_examples({
            'なかしべつ': '나카시베쓰',
            'きかい': '기카이',
            'よこすか': '요코스카',
            'あいづわかまつ': '아이즈와카마쓰',
            'あらかわ': '아라카와',
            'からふと': '가라후토',
            'わかやま': '와카야마',
            'げんかいなだ': '겐카이나다',
            'きかい': '기카이',
            'けごんのたき': '게곤노타키',
            'ひろさき': '히로사키',
            'しもきた': '시모키타',
            'しものせき': '시모노세키',
            'おきなわ': '오키나와',
            'あきた': '아키타',
            'くろしお': '구로시오',
            'くろべ': '구로베',
            'こうらくえん': '고라쿠엔',
            'ゆくはし': '유쿠하시',
            'ちくご': '지쿠고',
            'くさつ': '구사쓰',
            'せんかく': '센카쿠',
            'あまくさ': '아마쿠사',
            'くしろ': '구시로',
            'くらしき': '구라시키',
            'けごんのたき': '게곤노타키',
            'はっけん': '핫켄',
            'やりがたけ': '야리가타케',
            'いけだ': '이케다',
            'おんたけ': '온타케',
            'みやけ': '미야케',
            'きただけ': '기타다케',
            'ほっくわん': '홋쿠완',
            'おおたけ': '오타케',
            'なら けん': '나라 겐',
            'こまえ': '고마에',
            'こうらくえん': '고라쿠엔',
            'よこすか': '요코스카',
            'よこて': '요코테',
            'よこはま': '요코하마',
            'はこだて': '하코다테',
            'はっこうだ': '핫코다',
            # u'しれとこ': u'시레토고',
            # => 시레토코
            'とまこまい': '도마코마이',
            'にっこう': '닛코',
        })

    def test_examples_ga_column(self):
        self.assert_examples({
            'かながわ': '가나가와',
            'かすみがうら': '가스미가우라',
            'もがみ': '모가미',
            'やりがたけ': '야리가타케',
            'つがる': '쓰가루',
            'するが': '스루가',
            'さが': '사가',
            'たねが': '다네가',
            'あつぎ': '아쓰기',
            'とちぎ': '도치기',
            'はぎ': '하기',
            'あかぎ': '아카기',
            'ぎの': '기노',
            'ぎんざ': '긴자',
            'むぎ': '무기',
            'ぎふ': '기후',
            'みやぎ': '미야기',
            'けいひん': '게이힌',
            'かわぐち': '가와구치',
            'よなぐに': '요나구니',
            'もりぐち': '모리구치',
            'やまぐち': '야마구치',
            'ぐんま': '군마',
            'さかぐち きんいちろう': '사카구치 긴이치로',
            'ひぐち けいこ': '히구치 게이코',
            'ひぐち たかやす': '히구치 다카야스',
            'さとう めぐむ': '사토 메구무',
            'げんかいなだ': '겐카이나다',
            'あげお': '아게오',
            'くればやし しげお': '구레바야시 시게오',
            'むらかみ しげとし': '무라카미 시게토시',
            'しげみつ まもる': '시게미쓰 마모루',
            'さいとう しげよし': '사이토 시게요시',
            'まちだ しげる': '마치다 시게루',
            'まえお しげさぶろう': '마에오 시게사부로',
            'ながしま しげお': '나가시마 시게오',
            'けごんのたき': '게곤노타키',
            'ぶんご': '분고',
            'ちくご': '지쿠고',
            'かわごえ': '가와고에',
            'ちゅうごく': '주고쿠',
            'えちご': '에치고',
            'ごとう': '고토',
            'あご': '아고',
            'こごた': '고고타',
            'ひょうご': '효고',
        })
