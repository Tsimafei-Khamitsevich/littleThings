"""
Contains tests for scraper functions
"""

import unittest
import main


class TestScrapResidentsWebsite(unittest.TestCase):
    

    def test_1(self):
        link = '/residents/innowise/'
        href = main.scrap_residents_website(link)
        self.assertEqual(href, None)


    def test_instinctools(self):
        link = '/residents/instinctools/'
        href = main.scrap_residents_website(link)
        self.assertEqual(href, 'https://instinctools.com')



class TestScrapMulResidentsWebsite(unittest.TestCase):
    

    def test_1(self):
        companies = [
            ['«Бравокадо»', '/residents/bravokado/'],
            ['*instinctools', '/residents/instinctools/'],
            ['1С-Битрикс', '/residents/1s-bitriks/'],
            ['4Логист', '/residents/4logist/'],
            ['69 групп', '/residents/69-grupp/'],
            ['Innowise', '/residents/innowise/']
            ]

        upd_companies_check = [
            ['«Бравокадо»', '/residents/bravokado/', 'https://bravocado.net'], 
            ['*instinctools', '/residents/instinctools/', 'https://instinctools.com'], 
            ['1С-Битрикс', '/residents/1s-bitriks/', 'http://1c-bitrix.by'], 
            ['4Логист', '/residents/4logist/', 'https://www.4logist.com/'], 
            ['69 групп', '/residents/69-grupp/', 'http://69pixels.com']
            ]
        not_found_check = [['Innowise', '/residents/innowise/']]

        upd_companies, not_found = main.scrap_mul_residents_website(companies)
        
        self.assertEqual(upd_companies, upd_companies_check)
        self.assertEqual(not_found, not_found_check)


    def test_2(self):
        companies = [['«Бравокадо»', '/residents/bravokado/']]
        upd_companies_check = [['«Бравокадо»', '/residents/bravokado/', 'https://bravocado.net']]
        not_found_check = []
        upd_companies, not_found = main.scrap_mul_residents_website(companies)
        self.assertEqual(upd_companies, upd_companies_check)
        self.assertEqual(not_found, not_found_check)
 

class TestHasCommon(unittest.TestCase):
    """
    has_common
    """

    def test_1(self):
        l1 = [
            ['«Бравокадо»', '/residents/bravokado/'],
            ['*instinctools', '/residents/instinctools/'],
            ['1С-Битрикс', '/residents/1s-bitriks/'],
            ['4Логист', '/residents/4logist/'],
            ['69 групп', '/residents/69-grupp/']
            ]
        l2 = [['Innowise', '/residents/innowise/']]
        has_common = main.has_common(l1, l2)
        self.assertEqual(has_common, False)


    def test_2(self):
        l1, l2 = [], []
        has_common = main.has_common(l1, l2)
        self.assertEqual(has_common, False)


    def test_3(self):
        l1 = [
            ['«Бравокадо»', '/residents/bravokado/'],
            ['*instinctools', '/residents/instinctools/'],
            ['1С-Битрикс', '/residents/1s-bitriks/'],
            ['4Логист', '/residents/4logist/'],
            ['69 групп', '/residents/69-grupp/'],
            ['Innowise', '/residents/innowise/']
            ]
        l2 = [
            ['Innowise', '/residents/innowise/'],
            ['A1', '/residents/a1/']
            ]
        has_common = main.has_common(l1, l2)
        self.assertEqual(has_common, True)


if __name__ == '__main__':
    unittest.main()
    