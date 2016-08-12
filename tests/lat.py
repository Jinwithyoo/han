# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.lat import Latin


class LatinTestCase(HangulizeTestCase):

    lang = Latin()

    def test_people_roman(self):
        self.assert_examples({
            'Flavius Aëtius': '플라비우스 아에티우스',
            'FLAVIVS AËTIVS': '플라비우스 아에티우스',
            'Gnaeus Julius Agricola': '그나이우스 율리우스 아그리콜라',
            'GNAEUS IVLIVS AGRICOLA': '그나이우스 율리우스 아그리콜라',
            'Marcus Vipsanius Agrippa': '마르쿠스 빕사니우스 아그리파',
            'MARCVS VIPSANIVS AGRIPPA': '마르쿠스 빕사니우스 아그리파',
            'Julia Augusta Agrippina': '율리아 아우구스타 아그리피나',
            'IVLIA AVGVSTA AGRIPPINA': '율리아 아우구스타 아그리피나',
            'Marcus Antonius': '마르쿠스 안토니우스',
            'MARCVS ANTONIVS': '마르쿠스 안토니우스',
            'Apuleius': '아풀레이우스',
            'APVLEIVS': '아풀레이우스',
            'Gaius Julius Caesar Augustus': \
                '가이우스 율리우스 카이사르 아우구스투스',
            'GAIVS IVLIVS CAESAR AVGVSTVS': \
                '가이우스 율리우스 카이사르 아우구스투스',
            'Gaius Julius Caesar': '가이우스 율리우스 카이사르',
            'GAIVS IVLIVS CAESAR': '가이우스 율리우스 카이사르',
            'Gaius Valerius Catullus': '가이우스 발레리우스 카툴루스',
            'GAIVS VALERIVS CATVLLVS': '가이우스 발레리우스 카툴루스',
            'Marcus Tullius Cicero': '마르쿠스 툴리우스 키케로',
            'MARCVS TVLLIVS CICERO': '마르쿠스 툴리우스 키케로',
            'Tiberius Claudius Caesar Augustus Germanicus': \
                '티베리우스 클라우디우스 카이사르 아우구스투스 게르마니쿠스',
            'TIBERIVS CLAVDIVS CAESAR AVGVSTVS GERMANICVS': \
                '티베리우스 클라우디우스 카이사르 아우구스투스 게르마니쿠스',
            'Lucius Aurelius Commodus Antoninus': \
                '루키우스 아우렐리우스 콤모두스 안토니누스',
            'LVCIVS AVRELIVS COMMODVS ANTONINVS': \
                '루키우스 아우렐리우스 콤모두스 안토니누스',
            'Flavius Valerius Aurelius Constantinus': \
                '플라비우스 발레리우스 아우렐리우스 콘스탄티누스',
            'FLAVIVS VALERIVS AVRELIVS CONSTANTINVS': \
                '플라비우스 발레리우스 아우렐리우스 콘스탄티누스',
            'Cornelia Scipionis Africana': \
                '코르넬리아 스키피오니스 아프리카나',
            'CORNELIA SCIPIONIS AFRICANA': \
                '코르넬리아 스키피오니스 아프리카나',
            'Marcus Licinius Crassus': '마르쿠스 리키니우스 크라수스',
            'MARCVS LICINIVS CRASSVS': '마르쿠스 리키니우스 크라수스',
            'Gaius Aurelius Valerius Diocletianus': \
                '가이우스 아우렐리우스 발레리우스 디오클레티아누스',
            'GAIVS AVRELIVS VALERIVS DIOCLETIANVS': \
                '가이우스 아우렐리우스 발레리우스 디오클레티아누스',
            'Publius Aelius Hadrianus': '푸블리우스 아일리우스 하드리아누스',
            'PVBLIVS AELIVS HADRIANVS': '푸블리우스 아일리우스 하드리아누스',
            'Quintus Horatius Flaccus': '퀸투스 호라티우스 플라쿠스',
            'QVINTVS HORATIVS FLACCVS': '퀸투스 호라티우스 플라쿠스',
            'Flavius Petrus Sabbatius Justinianus': \
                '플라비우스 페트루스 사바티우스 유스티니아누스',
            'FLAVIVS PETRVS SABBATIVS IVSTINIANVS': \
                '플라비우스 페트루스 사바티우스 유스티니아누스',
            'Titus Livius': '티투스 리비우스',
            'TITVS LIVIVS': '티투스 리비우스',
            'Gaius Marius': '가이우스 마리우스',
            'GAIVS MARIVS': '가이우스 마리우스',
            'Nero Claudius Caesar Augustus Germanicus': \
                '네로 클라우디우스 카이사르 아우구스투스 게르마니쿠스',
            'NERO CLAVDIVS CAESAR AVGVSTVS GERMANICVS': \
                '네로 클라우디우스 카이사르 아우구스투스 게르마니쿠스',
            'Gaius Octavius': '가이우스 옥타비우스',
            'GAIVS OCTAVIVS': '가이우스 옥타비우스',
            'Titus Maccius Plautus': '티투스 마키우스 플라우투스',
            'TITVS MACCIVS PLAVTVS': '티투스 마키우스 플라우투스',
            'Gaius Plinius Secundus': '가이우스 플리니우스 세쿤두스',
            'GAIVS PLINIVS SECVNDVS': '가이우스 플리니우스 세쿤두스',
            'Gaius Plinius Caecilius Secundus': \
                '가이우스 플리니우스 카이킬리우스 세쿤두스',
            'GAIVS PLINIVS CAECILIVS SECVNDVS': \
                '가이우스 플리니우스 카이킬리우스 세쿤두스',
            'Gnaeus Pompeius Magnus': '그나이우스 폼페이우스 마그누스',
            'GNAEVS POMPEIVS MAGNVS': '그나이우스 폼페이우스 마그누스',
            'Sextus Aurelius Propertius': \
                '섹스투스 아우렐리우스 프로페르티우스',
            'SEXTVS AVRELIVS PROPERTIVS': \
                '섹스투스 아우렐리우스 프로페르티우스',
            'Gaius Sallustius Crispus': '가이우스 살루스티우스 크리스푸스',
            'GAIVS SALLVSTIVS CRISPVS': '가이우스 살루스티우스 크리스푸스',
            'Lucius Annaeus Seneca': '루키우스 안나이우스 세네카',
            'LVCIVS ANNAEUS SENECA': '루키우스 안나이우스 세네카',
            'Spartacus': '스파르타쿠스',
            'SPARTACVS': '스파르타쿠스',
            'Gaius Suetonius Tranquillus': '가이우스 수에토니우스 트랑퀼루스',
            'GAIVS SVETONIVS TRANQVILLVS': '가이우스 수에토니우스 트랑퀼루스',
            'Lucius Cornelius Sulla Felix': \
                '루키우스 코르넬리우스 술라 펠릭스',
            'LVCIVS CORNELIVS SVLLA FELIX': \
                '루키우스 코르넬리우스 술라 펠릭스',
            'Publius Cornelius Tacitus': '푸블리우스 코르넬리우스 타키투스',
            'PVBLIVS CORNELIVS TACITVS': '푸블리우스 코르넬리우스 타키투스',
            'Marcus Ulpius Nerva Trajanus': \
                '마르쿠스 울피우스 네르바 트라야누스',
            'MARCUS VLPIVS NERVA TRAIANVS': \
                '마르쿠스 울피우스 네르바 트라야누스',
            'Publius Vergilius Maro': '푸블리우스 베르길리우스 마로',
            'PVBLIVS VERGILIVS MARO': '푸블리우스 베르길리우스 마로',
            'Titus Flavius Vespasianus': '티투스 플라비우스 베스파시아누스',
            'TITVS FLAVIVS VESPASIANVS': '티투스 플라비우스 베스파시아누스',
            'Marcus Vitruvius Pollio': '마르쿠스 비트루비우스 폴리오',
            'MARCVS VITRVVIVS POLLIO': '마르쿠스 비트루비우스 폴리오',
        })

    def test_people_nonroman(self):
        self.assert_examples({
            'Georgius Agricola': '게오르기우스 아그리콜라',
            'Anselmus': '안셀무스',
            'Averroës': '아베로에스',
            'Aurelius Augustinus Hipponensis': \
                '아우렐리우스 아우구스티누스 히포넨시스',
            'Carolus Magnus': '카롤루스 마그누스',
            'Nicolaus Copernicus': '니콜라우스 코페르니쿠스',
            'Cyrus': '키루스',
            'Darius': '다리우스',
            'Gotarzes': '고타르제스',
            'Hannibal': '한니발',
            'Flavius Josephus': '플라비우스 요세푸스',
            'Mithridates': '미트리다테스',
            'Flavius Odoacer': '플라비우스 오도아케르',
        })

    def test_places(self):
        self.assert_examples({
            'Aegyptus': '아이깁투스',
            'Asia': '아시아',
            'Assyria': '아시리아',
            'Britannia': '브리탄니아',
            'Carthago': '카르타고',
            'Cannae': '칸나이',
            'Galatia': '갈라티아',
            'Gallia': '갈리아',
            'Germania': '게르마니아',
            'Hispania': '히스파니아',
            'Illyricum': '일리리쿰',
            'Iudaea': '유다이아',
            'Latium': '라티움',
            'Lusitania': '루시타니아',
            'Numidia': '누미디아',
            'Padus': '파두스',
            'Parthia': '파르티아',
        #    u'Pompeii': u'폼페이',
            'Roma': '로마',
            'Sicilia': '시킬리아',
            'Syracusae': '시라쿠사이',
            'Thracia': '트라키아',
            'Mons Vesuvius': '몬스 베수비우스',
        })

    def test_texts(self):
        self.assert_examples({
            'Aeneis': '아이네이스',
            'Naturalis Historia': '나투랄리스 히스토리아',
            'Commentarii de Bello Gallico': '콤멘타리이 데 벨로 갈리코',
            'Confessiones': '콘페시오네스',
            'Metamorphoseon': '메타모르포세온',
            'Philosophiæ Naturalis Principia Mathematica': \
                '필로소피아이 나투랄리스 프링키피아 마테마티카',
        })

    def test_mythology(self):
        self.assert_examples({
            'Apollo': '아폴로',
            'Bacchus': '바쿠스',
            'Ceres': '케레스',
            'Diana': '디아나',
            'Ianus': '야누스',
            'Iuno': '유노',
            'Iupitter': '유피테르',
            'Mars': '마르스',
            'Mercurius': '메르쿠리우스',
            'Minerva': '미네르바',
            'Neptunus': '넵투누스',
            'Pluto': '플루토',
            'Saturnus': '사투르누스',
            'Venus': '베누스',
            'Vesta': '베스타',
            'Vulcanus': '불카누스',
        })

    def test_miscellaneous(self):
        self.assert_examples({
            'consul': '콘술',
            'Pax Romana': '팍스 로마나',
            'res publica': '레스 푸블리카',
            'senatus': '세나투스',
        })
