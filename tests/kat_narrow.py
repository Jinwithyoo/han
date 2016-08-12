# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.kat.narrow import NarrowGeorgian


class NarrowGeorgianTestCase(HangulizeTestCase):

    lang = NarrowGeorgian()

    def test_examples_of_iceager(self):
        self.assert_examples({
            'თბილისი': '트빌리시',
            'ქუთაისი': '쿠타이시',
            'ბათუმი': '바투미',
            'რუსთავი': '루스타비',
            'ზუგდიდი': '주그디디',
            'გორი': '고리',
            'ფოთი': '포티',
            'დავით': '다비트',
            'გიორგი': '기오르기',
            'ფარნავაზი': '파르나바지',
            'მითრიდატე': '미트리다떼',
            'თამარი': '타마리',
            'ზვიად': '즈위아드',
            'გამსახურდია': '감사후르디아',
            'ალექსანდრე': '알레크산드레',
            'დიმიტრი': '디미뜨리',
            'ამილახვარი': '아밀라흐와리',
            'გიორგი': '기오르기',
            'სააკაძე': '사까제',
            'ვახუშტი': '바후슈띠',
            'ზურაბ': '주라브',
            'ავალიშვილი': '아발리슈윌리',
            'ლევან': '레반',
            'ჭილაშვილი': '찔라슈윌리',
            'კახაბერ': '까하베르',
            'კახა': '까하',
            'კალაძე': '깔라제',
            'ზურაბ': '주라브',
            'აზმაიფარაშვილი': '아즈마이파라슈윌리',
            'კონსტანტინე': '꼰스딴띠네',
            'გამსახურდია': '감사후르디아',
            'მიხეილ': '미헤일',
            'ჯავახიშვილი': '자바히슈윌리',
            'კიტა': '끼따',
            'აბაშიძე': '아바시제',
            'არნოლდ': '아르놀드',
            'ჩიქობავა': '치코바바',
            'ანა': '아나',
            'კალანდაძე': '깔란다제',
            'იოსებ': '이오세브',
            'გრიშაშვილი': '그리샤슈윌리',
            'კახაბერ': '까하베르',
            'კახა': '까하',
            'კალაძე': '깔라제',
            'მთაწმინდა': '음타쯔민다',
            'მერაბ': '메라브',
            'კოსტავა': '꼬스따바',
            'შოთა': '쇼타',
            'არველაძე': '아르벨라제',
            'დიმიტრი': '디미뜨리',
            'არაყიშვილი': '아라끼슈윌리',
            'ელენე': '엘레네',
            'ახვლედიანი': '아흐블레디아니',
            'მაყვალა': '마끄왈라',
            'ქასრაშვილი': '카스라슈윌리',
            'პეტრე': '뻬뜨레',
            'მიხეილ': '미헤일',
            'სააკაშვილი': '사까슈윌리',
            'ედუარდ': '에두아르드',
            'შევარდნაძე': '셰바르드나제',
            'ზურაბ': '주라브',
            'ჟვანია': '주와니아',
            'ნიკოლოზ': '니꼴로즈',
            'ნიკა': '니까',
            'გილაური': '길라우리',
            'გრიგოლ': '그리골',
            'მგალობლიშვილ': '음갈로블리슈윌',
            'ნინო': '니노',
            'ბურჯანაძე': '부르자나제',
            'თათია': '타티아',
            'მანაგაძე': '마나가제',
            'გიორგი': '기오르기',
            'ღონღაძე': '곤가제',
            'ზაზა': '자자',
            'ფაჩულია': '파출리아',
            'ნიკოლოზ': '니꼴로즈',
            'ბარათაშვილი': '바라타슈윌리',
            'რაფიელ': '라피엘',
            'ერისთავი': '에리스타비',
            'ჯვარი': '즈와리',
            'მტკვარი': '음뜨끄와리',
            'ზარზმა': '자르즈마',
            'ავტო': '아프또',
        })