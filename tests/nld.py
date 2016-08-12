# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.nld import Dutch


class DutchTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0220.jsp """

    lang = Dutch()

    def test_etc(self):
        self.assert_examples({
            'tuig': '타위흐',
        })

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0118.jsp """
        self.assert_examples({
            'Borst': '보르스트',
            'Bram': '브람',
            'Jacob': '야코프',
            'Campen': '캄펀',
            'Nicolaas': '니콜라스',
            'topic': '토픽',
            'scrupel': '스크뤼펄',
            'cyaan': '시안',
            'Ceelen': '세일런',
            'Volcher': '폴허르',
            'Utrecht': '위트레흐트',
            'Delft': '델프트',
            'Edgar': '엣하르',
            'Hendrik': '헨드릭',
            'Helmond': '헬몬트',
            'Flevoland': '플레볼란트',
            'Graaf': '흐라프',
            'Goes': '후스',
            'Limburg': '림뷔르흐',
            'Heineken': '헤이네컨',
            'Hendrik': '헨드릭',
            'Jongkind': '용킨트',
            'Jan': '얀',
            'Jeroen': '예룬',
            'Kok': '콕',
            'Alkmaar': '알크마르',
            'Zierikzee': '지릭제이',
            'kwaliteit': '크발리테이트',
            'kwellen': '크벨런',
            'kwitantie': '크비탄시',
            'Lasso': '라소',
            'Friesland': '프리슬란트',
            'sabel': '사벌',
            'Meerssen': '메이르선',
            'Zalm': '잘름',
            'Nijmegen': '네이메헌',
            'Jansen': '얀선',
            'Inge': '잉어',
            'Groningen': '흐로닝언',
            'Peper': '페퍼르',
            'Kapteyn': '캅테인',
            'Koopmans': '코프만스',
            'Rotterdam': '로테르담',
            'Asser': '아서르',
            'Spinoza': '스피노자',
            'Hals': '할스',
            'Schiphol': '스히폴',
            'Escher': '에스허르',
            'typisch': '티피스',
            'sjaal': '샬',
            'huisje': '하위셔',
            'ramsj': '람시',
            'fetisj': '페티시',
            'Tinbergen': '틴베르헌',
            'Gerrit': '헤릿',
            'Petrus': '페트뤼스',
            'Aartsen': '아르천',
            'Beets': '베이츠',
            'Veltman': '펠트만',
            'Einthoven': '에인트호번',
            'Weltevree': '벨테브레이',
            'Wim': '빔',
            'cyaan': '시안',
            # u'Lyonnet': u'리오넷',
            'typisch': '티피스',
            'Verwey': '페르베이',
            'Zeeman': '제이만',
            'Huizinga': '하위징아',
            'Asser': '아서르',
            'Frans': '프란스',
            'Egmont': '에흐몬트',
            'Frederik': '프레데릭',
            'Heineken': '헤이네컨',
            'Lubbers': '뤼버르스',
            'Campen': '캄펀',
            'Nicolaas': '니콜라스',
            'Tobias': '토비아스',
            'Pieter': '피터르',
            'Vries': '프리스',
            'Onnes': '오너스',
            'Vondel': '폰덜',
            'Boer': '부르',
            'Boerhaave': '부르하버',
            'Utrecht': '위트레흐트',
            'Petrus': '페트뤼스',
            'Europort': '외로포르트',
            'Deurne': '되르너',
            'ruw': '뤼',
            'duwen': '뒤언',
            'Euwen': '에위언',
            'Bouts': '바우츠',
            'Bouwman': '바우만',
            'Paul': '파울',
            'Lauwersmeer': '라우에르스메이르',
            'Heike': '헤이커',
            'Bolkestein': '볼케스테인',
            'IJssel': '에이설',
            'Huizinga': '하위징아',
            'Zuid-Holland': '자위트홀란트',
            'Buys': '바위스',
            'draaien': '드라이언',
            'fraai': '프라이',
            'zaait': '자이트',
            'Maaikes': '마이커스',
            'Booisman': '보이스만',
            'Hooites': '호이터스',
            'Boeijinga': '부잉아',
            'moeite': '무이터',
            'Leeuwenhoek': '레이우엔훅',
            'Meeuwes': '메이우어스',
            'Lieuwma': '리우마',
            'Rieuwers': '리우어르스',
        })

    def test_1st(self):
        """제1항
        무성 파열음 p, t, k는 자음 앞이나 어말에 올 경우에는 각각 받침
        ‘ㅂ, ㅅ, ㄱ'으로 적는다. 다만, 앞 모음이 이중 모음이거나 장모음(같은
        모음을 겹쳐 적는 경우)인 경우와 앞이나 뒤의 자음이 유음이나 비음인
        경우에는 ‘프, 트, 크'로 적는다.
        """
        self.assert_examples({
            'Wit': '빗',
            'Gennip': '헤닙',
            'Kapteyn': '캅테인',
            'september': '셉템버르',
            'Petrus': '페트뤼스',
            'Arcadelt': '아르카덜트',
            'Hoop': '호프',
            'Eijkman': '에이크만',
        })

    def test_2nd(self):
        """제2항
        유성 파열음 b, d가 어말에 올 경우에는 각각 ‘프, 트'로 적고, 어중에 올
        경우에는 앞이나 뒤의 자음이 유음이나 비음인 경우와 앞 모음이
        이중모음이거나 장모음(같은 모음을 겹쳐 적는 경우)인 경우에는 ‘브, 드'로
        적는다. 그 외에는 모두 받침 ‘ㅂ, ㅅ'으로 적는다.
        """
        self.assert_examples({
            'Bram': '브람',
            'Hendrik': '헨드릭',
            'Jakob': '야코프',
            'Edgar': '엣하르',
            'Zeeland': '제일란트',
            'Koenraad': '쿤라트',
        })

    def test_3rd(self):
        """제3항
        v가 어두에 올 경우에는 ‘ㅍ, 프'로 적고, 그 외에는 모두 ‘ㅂ, 브'로
        적는다.
        """
        self.assert_examples({
            'Veltman': '펠트만',
            'Vries': '프리스',
            'Grave': '흐라버',
            'Weltevree': '벨테브레이',
        })

    def test_4th(self):
        """제4항
        c는 차용어에 쓰이므로 해당 언어의 발음에 따라 ‘ㅋ'이나 ‘ㅅ'으로 적는다.
        """
        self.assert_examples({
            'Nicolaas': '니콜라스',
            'Hendricus': '헨드리퀴스',
            'cyaan': '시안',
            'Franciscus': '프란시스퀴스',
        })

    def test_5th(self):
        """제5항
        g, ch는 ‘ㅎ'으로 적되, 차용어의 경우에는 해당 언어의 발음에 따라
        적는다.
        """
        self.assert_examples({
            'gulden': '휠던',
            'Haag': '하흐',
            'Hooch': '호흐',
            'Volcher': '폴허르',
            'Eugene': '외젠',
            'Michael': '미카엘',
        })

    def test_6th(self):
        """제6항
        -tie는 ‘시'로 적는다.
        """
        self.assert_examples({
            'natie': '나시',
            'politie': '폴리시',
        })

    def test_7th(self):
        """제7항
        어중의 l이 모음 앞에 오거나 모음이 따르지 않는 비음 앞에 올 때에는
        ‘?'로 적는다. 다만, 비음 뒤의 l은 모음 앞에 오더라도 ‘ㄹ'로 적는다.
        """
        self.assert_examples({
            'Tiele': '틸러',
            'Zalm': '잘름',
            'Berlage': '베를라허',
            'Venlo': '펜로',
        })

    def test_8th(self):
        """제8항: nk
        k 앞에 오는 n은 받침 ‘ㅇ'으로 적는다.
        """
        self.assert_examples({
            'Frank': '프랑크',
            'Hiddink': '히딩크',
            'Benk': '벵크',
            'Wolfswinkel': '볼프스빙컬',
        })

    def test_9th(self):
        """제9항
        같은 자음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다.
        """
        self.assert_examples({
            'Hobbema': '호베마',
            'Ballot': '발롯',
            'Emmen': '에먼',
            'Gennip': '헤닙',
        })

    def test_10th(self):
        """제10항
        e는 ‘에'로 적는다. 다만, 이음절 이상에서 마지막 음절에 오는 e와 어말의
        e는 모두 ‘어'로 적는다.
        """
        self.assert_examples({
            'Dennis': '데니스',
            'Breda': '브레다',
            'Stevin': '스테빈',
            'Peter': '페터르',
            'Heineken': '헤이네컨',
            'Campen': '캄펀',
        })

    def test_11st(self):
        """제11항
        같은 모음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다. 다만 ee는
        ‘에이'로 적는다.
        """
        self.assert_examples({
            'Hooch': '호흐',
            'Mondriaan': '몬드리안',
            'Kees': '케이스',
            'Meerssen': '메이르선',
        })

    def test_12nd(self):
        """제12항
        -ig는 ‘어흐'로 적는다.
        """
        self.assert_examples({
            'tachtig': '타흐터흐',
            'hartig': '하르터흐',
        })

    def test_13rd(self):
        """제13항
        -berg는 ‘베르흐'로 적는다.
        """
        self.assert_examples({
            'Duisenberg': '다위센베르흐',
            'Mengelberg': '멩엘베르흐',
        })

    def test_14th(self):
        """제14항
        over-는 ‘오버르'로 적는다.
        """
        self.assert_examples({
            'Overijssel': '오버레이설',
            'overkomst': '오버르콤스트',
        })

    def test_15th(self):
        """제15항
        모음 è, é, ê, ë는 ‘에'로 적고, ï 는 ‘이' 로 적는다.
        """
        self.assert_examples({
            'carré': '카레',
            # u'casuïst': u'카수이스트',
            'drieëntwintig': '드리엔트빈터흐',
        })

    def test_people(self):
        self.assert_examples({
            'Jozias van Aartsen': '요지아스 판아르천',
            'Sharon den Adel': '샤론 덴아덜',
            'Dick Advocaat': '딕 아드보카트',
            'Karel Appel': '카럴 아펄',
            'Jakob Arcadelt': '야코프 아르카덜트',
            'Naomi van As': '나오미 판아스',
            'Tobias Michael Carel Asser': '토비아스 미카엘 카럴 아서르',
            'Ryan Babel': '라이언 바벌',
            'Jan Peter Balkenende': '얀 페터르 발케넨더',
            'Willem Barentsz': '빌럼 바렌츠',
            'Marco van Basten': '마르코 판바스턴',
            'Beatrix Wilhelmina Armgard': '베아트릭스 빌헬미나 아름하르트',
            'Nicolaas Beets': '니콜라스 베이츠',
            'Dennis Bergkamp': '데니스 베르흐캄프',
            'Hendrik Petrus Berlage': '헨드릭 페트뤼스 베를라허',
            'Bernhard Leopold': '베른하르트 레오폴트',
            'Leo Beenhakker': '레오 베인하커르',
            'Willem Blaeu': '빌럼 블라우',
            'Nicolaas Bloembergen': '니콜라스 블룸베르헌',
            'Evert Bloemsma': '에버르트 블룸스마',
            'Herman Boerhaave': '헤르만 부르하버',
            'Frits Bolkestein': '프리츠 볼케스테인',
            'Mark van Bommel': '마르크 판보멀',
            'Corrie ten Boom': '코리 텐봄',
            'Els Borst': '엘스 보르스트',
            'Theo Bos': '테오 보스',
            'Dirck Bouts': '디르크 바우츠',
            'Giovanni van Bronckhorst': '조바니 판브롱크호르스트',
            'Pieter Brueghel': '피터르 브뤼헐',
            'Armin van Buuren': '아르민 판뷔런',
            'Buys Ballot': '바위스 발롯',
            'Frank de Boer': '프랑크 더부르',
            'Gerard ter Borch': '헤라르트 테르보르흐',
            'Hans van den Broek': '한스 판덴브룩',
            'Inge de Bruijn': '잉어 더브라윈',
            'Jacob van Campen': '야코프 판캄펀',
            'Pieter Camper': '피터르 캄퍼르',
            'Phillip Cocu': '필립 코퀴',
            'Volcher Coiter': '폴허르 코이터르',
            'Anton Corbijn': '안톤 코르베인',
            'Johan Cruijff': '요한 크라위프',
            'Paul Crutzen': '파울 크뤼천',
            'Edgar Davids': '엣하르 다비츠',
            'Edith van Dijk': '에딧 판데이크',
            'Edsger Dijkstra': '에츠허르 데이크스트라',
            'Theo van Doesburg': '테오 판두스뷔르흐',
            'Kees van Dongen': '케이스 판동언',
            'Wim Duisenberg': '빔 다위센베르흐',
            'Christiaan Eijkman': '크리스티안 에이크만',
            'Willem Einthoven': '빌럼 에인트호번',
            'Pim Fortuyn': '핌 포르타윈',
            'Louis van Gaal': '루이 판할',
            'Yuri van Gelder': '유리 판헬더르',
            'Karien van Gennip': '카린 판헤닙',
            'Yvonne van Gennip': '이보너 판헤닙',
            'Annette Gerritsen': '아네터 헤리천',
            'Arnold Geulincx': '아르놀트 횔링크스',
            'Hans van Ginkel': '한스 판힝컬',
            'Hugo van der Goes': '휘호 판데르후스',
            'Theo van Gogh': '테오 반고흐',
            'Vincent van Gogh': '빈센트 반고흐',
            'Herman Gorter': '헤르만 호르터르',
            'Jan Gossaert': '얀 호사르트',
            'Reinier de Graaf': '레이니어르 더흐라프',
            'Frank de Grave': '프랑크 더흐라버',
            'Hugo de Groot': '휘호 더흐로트',
            'Ruud Gullit': '뤼트 휠릿',
            'Frans Hals': '프란스 할스',
            'Hendrik Hamel': '헨드릭 하멜',
            'Herman Heijermans': '헤르만 헤이예르만스',
            'Jan Baptista van Helmont': '얀 밥티스타 판헬몬트',
            'Guus Hiddink': '휘스 히딩크',
            'Meindert Hobbema': '메인더르트 호베마',
            'Jacobus Henricus van ’t Hoff': '야코뷔스 헨리퀴스 판엇호프',
            'Pieter de Hooch': '피터르 더호흐',
            'Gerard ’t Hooft': '헤라르트 엇호프트',
            'Pieter van den Hoogenband': '피터르 판덴호헨반트',
            'Jaap de Hoop Scheffer': '야프 더호프 스헤퍼르',
            'Johan Huizinga': '요한 하위징아',
            'Mark Huizinga': '마르크 하위징아',
            'Klaas-Jan Huntelaar': '클라스얀 휜텔라르',
            'Christiaan Huygens': '크리스티안 하위헌스',
            'Jan Ingenhousz': '얀 잉엔하우스',
            'Jozef Israëls': '요제프 이스라엘스',
            'Cornelis Jansen': '코르넬리스 얀선',
            'Famke Janssen': '팜커 얀선',
            'Johan Jongkind': '요한 용킨트',
            'Annemarie Jorritsma': '아네마리 요리츠마',
            'Juliana Louise Emma Marie Wilhelmina':
            '율리아나 루이서 에마 마리 빌헬미나',
            'Heike Kamerlingh Onnes': '헤이커 카메를링 오너스',
            'Jacobus Cornelius Kapteyn': '야코뷔스 코르넬리위스 캅테인',
            'Petrus Jacobus Kipp': '페트뤼스 야코뷔스 킵',
            'Patrick Kluivert': '파트릭 클라위버르트',
            'Ronald Koeman': '로날트 쿠만',
            'Wim Kok': '빔 콕',
            'Willem Johan Kolff': '빌럼 요한 콜프',
            'Pieter Kooijmans': '피터르 코이만스',
            'Rem Koolhaas': '렘 콜하스',
            'Willem de Kooning': '빌럼 더코닝',
            'Tjalling Koopmans': '티알링 코프만스',
            'Benk Korthals': '벵크 코르탈스',
            'Sven Kramer': '스벤 크라머르',
            'Dirk Kuyt': '디르크 카위트',
            'Lamoraal van Egmont': '라모랄 판에흐몬트',
            'Orlando di Lasso': '오를란도 디라소',
            'Jan Leeghwater': '얀 레이흐바터르',
            'Antoni van Leeuwenhoek': '안토니 판레이우엔훅',
            'Lucas van Leyden': '뤼카스 판레이던',
            'Jan Huygen van Linschoten': '얀 하위헌 판린스호턴',
            'Hendrik Willem van Loon': '헨드릭 빌럼 판론',
            'Hendrik Antoon Lorentz': '헨드릭 안톤 로렌츠',
            'Ruud Lubbers': '뤼트 뤼버르스',
            'Karel van Mander': '카럴 판만더르',
            'Bert van Marwijk': '베르트 판마르베이크',
            'Joris Mathijsen': '요리스 마테이선',
            'Simon van der Meer': '시몬 판데르메이르',
            'Willem Mengelberg': '빌럼 멩엘베르흐',
            'Paul Menkveld': '파울 멩크벨트',
            'Gabriël Metsu': '가브리엘 메취',
            'Rinus Michels': '리뉘스 미헐스',
            'Piet Mondriaan': '핏 몬드리안',
            'Harry Mulisch': '하리 뮐리스',
            'Ruud van Nistelrooy': '뤼트 판니스텔로이',
            'Teun de Nooijer': '퇸 더노이여르',
            'Cees Nooteboom': '케이스 노테봄',
            'André Ooijer': '안드레 오이여르',
            'Jan Hendrik Oort': '얀 헨드릭 오르트',
            'Adriaen van Ostade': '아드리안 판오스타더',
            'Marc Overmars': '마르크 오버르마르스',
            'Joachim Patinir': '요아힘 파티니르',
            'Bram Peper': '브람 페퍼르',
            'Robin van Persie': '로빈 판페르시',
            'Frank Rijkaard': '프랑크 레이카르트',
            'Rembrandt Harmenszoon van Rijn': '렘브란트 하르먼스존 판레인',
            'Arjen Robben': '아르연 로번',
            'Guido van Rossum': '히도 판로쉼',
            'André Rouvoet': '안드레 라우붓',
            'Jacob van Ruisdael': '야코프 판라위스달',
            'Mark Rutte': '마르크 뤼터',
            'Michiel de Ruyter': '미힐 더라위터르',
            'Edwin van der Sar': '에드빈 판데르사르',
            'Nicolien Sauerbreij': '니콜린 사우에르브레이',
            'Clarence Seedorf': '클라렌서 세이도르프',
            'Geertgen tot Sint Jans': '헤이르트헌 톳신트얀스',
            'Claus Sluter': '클라우스 슬뤼터르',
            'Rik Smits': '릭 스미츠',
            'Wesley Sneijder': '베슬리 스네이더르',
            'Willebrord Snel van Royen': '빌레브로르트 스넬 판로이언',
            'Baruch Spinoza': '바뤼흐 스피노자',
            'Jan Steen': '얀 스테인',
            'Simon Stevin': '시몬 스테빈',
            'Jan Swammerdam': '얀 스바메르담',
            'Jan Pieterszoon Sweelinck': '얀 피터르스존 스베일링크',
            'Abel Tasman': '아벌 타스만',
            'Cornelis Petrus Tiele': '코르넬리스 페트뤼스 틸러',
            'Tiësto': '티에스토',
            'Jan Tinbergen': '얀 틴베르헌',
            'Nikolaas Tinbergen': '니콜라스 틴베르헌',
            'Mark Tuitert': '마르크 타위터르트',
            'Gerard Unger': '헤라르트 윙어르',
            'Joop den Uyl': '요프 덴아윌',
            'Rafaël van der Vaart': '라파엘 판데르파르트',
            'Adriaen van de Velde': '아드리안 판더펠더',
            'Marleen Veldhuis': '마를레인 펠드하위스',
            'Martinus Veltman': '마르티뉘스 펠트만',
            'Esther Vergeer': '에스터르 페르헤이르',
            'Paul Verhoeven': '파울 페르후번',
            'Johannes Vermeer': '요하네스 페르메이르',
            'Albert Verwey': '알버르트 페르베이',
            'Joost van den Vondel': '요스트 판덴폰덜',
            'Marianne Vos': '마리아너 포스',
            'Hugo de Vries': '휘호 더프리스',
            'Johannes Diderik van der Waals': '요하네스 디데릭 판데르발스',
            'Maarten van der Weijden': '마르턴 판데르베이던',
            'Jan Weltevree': '얀 벨테브레이',
            'Rogier van der Weyden': '로히어르 판데르베이던',
            'Geert Wilders': '헤이르트 빌더르스',
            'Adriaan Willaert': '아드리안 빌라르트',
            'Willem-Alexander Claus George Ferdinand':
            '빌럼알렉산더르 클라우스 헤오르허 페르디난트',
            'Michael Dudok de Wit': '미카엘 뒤독 더빗',
            'Johan de Witt': '요한 더빗',
            'Joost Wolfswinkel': '요스트 볼프스빙컬',
            'Ireen Wüst': '이레인 뷔스트',
            'Gerrit Zalm': '헤릿 잘름',
            'Pieter Zeeman': '피터르 제이만',
            'Frits Zernike': '프리츠 제르니커',
            'Joop Zoetemelk': '요프 주테멜크',
        })

    def test_places(self):
        self.assert_examples({
            'Almelo': '알멜로',
            'Alphen aan den Rijn': '알펀안덴레인',
            'Ameland': '아멜란트',
            'Amersfoort': '아메르스포르트',
            'Amstelveen': '암스텔베인',
            'Amsterdam': '암스테르담',
            'Andelst': '안델스트',
            'Apeldoorn': '아펠도른',
            'Appingedam': '아핑에담',
            'Arnhem': '아른험',
            'Assen': '아선',
            'Asten': '아스턴',
            'Barneveld': '바르네벨트',
            'Bedum': '베뒴',
            'Beilen': '베일런',
            'Bergen op Zoom': '베르헌옵좀',
            'Berkel': '베르컬',
            'Berkhout': '베르크하우트',
            'Best': '베스트',
            'Beverwijk': '베베르베이크',
            'Birdaard': '비르다르트',
            'Bolsward': '볼스바르트',
            'Borne': '보르너',
            'Boxtel': '복스털',
            'Breda': '브레다',
            'Breskens': '브레스컨스',
            'Burgh-Haamstede': '뷔르흐함스테더',
            'Capelle aan de Ijssel': '카펠러안더에이설',
            'Castricum': '카스트리큄',
            'Coevorden': '쿠보르던',
            'Creil': '크레일',
            'Culemborg': '퀼렘보르흐',
            'Delfzijl': '델프제일',
            'Den Bosch': '덴보스',
            'Den Burg': '덴뷔르흐',
            'Den Haag': '덴하흐',
            'Den Helder': '덴헬더르',
            'Deventer': '데벤터르',
            'Diremond': '디레몬트',
            'Doesburg': '두스뷔르흐',
            'Doetinchem': '두틴험',
            'Dokkum': '도큄',
            'Dordrecht': '도르드레흐트',
            'Drachten': '드라흐턴',
            'Drenthe': '드렌터',
            'Dronten': '드론턴',
            'Ede': '에더',
            'Eemskanaal': '에임스카날',
            'Eenrum': '에인륌',
            'Eibergen': '에이베르헌',
            'Eindhoven': '에인트호번',
            'Emmeloord': '에멜로르트',
            'Enkhuizen': '엥크하위전',
            'Enschede': '엔스헤데',
            'Erp': '에르프',
            'Etten-Leur': '에턴뢰르',
            'Ferwerd': '페르버르트',
            'Franeker': '프라네커르',
            'Gelderland': '헬데를란트',
            'Gorinchem': '호린험',
            'Gouda': '하우다',
            'Haarlem': '하를럼',
            'Halsteren': '할스테런',
            'Hapert': '하퍼르트',
            'Hardenberg': '하르덴베르흐',
            'Harderwijk': '하르데르베이크',
            'Harlingen': '하를링언',
            'Heerde': '헤이르더',
            'Heerenveen': '헤이렌베인',
            'Heerhugowaard': '헤이르휘호바르트',
            'Heerlen': '헤이를런',
            'Hellevoetsluis': '헬레부츨라위스',
            'Hengelo': '헹엘로',
            'Herkenbosch': '헤르켄보스',
            'Hillegom': '힐레홈',
            'Hilversum': '힐베르쉼',
            'Hoek van Holland': '훅판홀란트',
            'Hollum': '홀륌',
            'Hoogerheide': '호헤르헤이더',
            'Hoogeveen': '호헤베인',
            'Hoogezand-Sappemeer': '호헤잔트사페메이르',
            'Hoog-Keppel': '호흐케펄',
            'Hoorn': '호른',
            'IJmuiden': '에이마위던',
            'IJsselmeer': '에이설메이르',
            'Kampen': '캄펀',
            'Katwijk aan Zee': '카트베이크안제이',
            'Kerkrade': '케르크라더',
            'Kessel': '케설',
            'Kloosterhaar': '클로스테르하르',
            'Kollum': '콜륌',
            'Koudekerke': '카우데케르커',
            'Kraggenburg': '크라헨뷔르흐',
            'Lauwersmeer': '라우에르스메이르',
            'Leeuwarden': '레이우아르던',
            'Leiden': '레이던',
            'Lelystad': '렐리스타트',
            'Luyksgestel': '라위크스헤스털',
            'Maarssen': '마르선',
            'Maastricht': '마스트리흐트',
            'Markermeer': '마르케르메이르',
            'Marsdiep': '마르스딥',
            'Mechelen': '메헬런',
            'Meppel': '메펄',
            'Middelburg': '미델뷔르흐',
            'Middelharnis': '미델하르니스',
            'Naarden': '나르던',
            'Nieuwegein': '니우에헤인',
            'Nieuwe Niedorp': '니우어니도르프',
            'Nijkerk': '네이커르크',
            'Nijverdal': '네이베르달',
            'Noord-Brabant': '노르트브라반트',
            'Noord-Holland': '노르트홀란트',
            'Oenkerk': '웅커르크',
            'Oldenzaal': '올덴잘',
            'Ommen': '오먼',
            'Oosterhout': '오스테르하우트',
            'Oosterschelde': '오스테르스헬더',
            'Oost-Vlieland': '오스트플릴란트',
            'Oss': '오스',
            'Philippine': '필리피너',
            'Purmerend': '퓌르메런트',
            'Raalte': '랄터',
            'Roermond': '루르몬트',
            'Roordahuizum': '로르다하위쥠',
            'Roosendaal': '로센달',
            'Schagen': '스하헌',
            'Scharendijke': '스하렌데이커',
            'Schiermonnikoog': '스히르모니코흐',
            'Schoonhoven': '스혼호번',
            '’s-Gravenhage': "'스흐라벤하허",
            '’s-Hertogenbosch': "'스헤르토헨보스",
            'Sittarad': '시타라트',
            'Sloten': '슬로턴',
            'Sluis': '슬라위스',
            'Sneek': '스네이크',
            'Spijkenisse': '스페이케니서',
            'Steeswijk': '스테이스베이크',
            'Stein': '스테인',
            'Terneuzen': '테르뇌전',
            'Terschelling': '테르스헬링',
            'Texel': '텍설',
            'Tiel': '틸',
            'Tilburg': '틸뷔르흐',
            'Torenberg': '토렌베르흐',
            'Uden': '위던',
            'Uithuizen': '아위트하위전',
            'Urk': '위르크',
            'Valkenswaard': '팔켄스바르트',
            'Veendam': '페인담',
            'Veenendal': '페이넨달',
            'Veldhoven': '펠트호번',
            'Vlaardingen': '플라르딩언',
            'Vlieland': '플릴란트',
            'Vlissingen': '플리싱언',
            'Vriezenveen': '프리젠베인',
            'Waal': '발',
            'Waalwijk': '발베이크',
            'Wadden': '바던',
            'Waddeneilanden': '바데네일란던',
            'Waddenzee': '바덴제이',
            'Waddinxveen': '바딩크스베인',
            'Wageningen': '바헤닝언',
            'Wanroij': '반로이',
            'Weert': '베이르트',
            'Westerschelde': '베스테르스헬더',
            'Westkapelle': '베스트카펠러',
            'West-Terschelling': '베스트테르스헬링',
            'Wieringerwerf': '비링에르버르프',
            'Wijchen': '베이헌',
            'Winterswijk': '빈테르스베이크',
            'Witmarsum': '비트마르쉼',
            'Wolvega': '볼베하',
            'Wonschoten': '본스호턴',
            'Zaandam': '잔담',
            'Zandvoort': '잔드보르트',
            'Zevenaar': '제베나르',
            'Zevenbergen': '제벤베르헌',
            'Zutphan': '쥣판',
            'Zwolle': '즈볼러',
        })

    def test_miscellaneous(self):
        self.assert_examples({
            'brik': '브릭',
            'Delft Stedelijk': '델프트 스테델레이크',
            'De Stijl': '더스테일',
            'gulden': '휠던',
            'Elfstedentocht': '엘프스테덴토흐트',
        })
