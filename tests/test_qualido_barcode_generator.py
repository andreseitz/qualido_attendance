import unittest

import os

from qualido_barcode_generator import qualido_barcode_generator as gen

test_path = "./tests/test.xlsx"

def get_test_sheet():
    return gen.get_sheet(test_path)

class TestExcelParsing(unittest.TestCase):

    expect_header = [u'ID', u'Status', u'Nachname', u'Vorname', u'Benutzername', u'Benutzerquelle/n', u'Telefon', u'Gruppen', u'Email', u'PLZ', u'Stadt', u'Stra\xdfe']

    def test_readSheetFromFileSuccessfully(self):
        sheet = get_test_sheet()
        self.assertEqual(12, sheet.row_len(1))

    def test_readSheetFromNonexistingFileWithError(self):
        error_path = "./tests/notest.xlsx"
        with self.assertRaises(FileNotFoundError):
            sheet = gen.get_sheet(error_path)

    def test_getHeader(self):
        sheet = get_test_sheet()
        header = gen.get_header(sheet)
        self.assertCountEqual(self.expect_header, header)

    def test_sheetContainsValidHeader(self):
        sheet = get_test_sheet()
        self.assertTrue(gen.sheet_contains_data(sheet))

    def test_sheetWithNoIDContainsNoValidHeader(self):
        noid_path = "./tests/noid_test.xlsx"
        sheet = gen.get_sheet(noid_path)
        self.assertFalse(gen.sheet_contains_valid_header(sheet))

    def test_parseUserDataSuccessfully(self):
        users = gen.parseUserData(test_path)
        self.assertEqual(1, len(users))
        
    def test_parseUserDataWithNoAvailableUserData(self):
        nodata_path = "./tests/nodata_test.xlsx"
        with self.assertRaises(gen.NoUserDataException):
            users = gen.parseUserData(nodata_path)

class TestBarcodeGeneration(unittest.TestCase):

    def clean_environment(self):
        if os.path.exists('barcodes'):
            shutil.rmtree('barcodes')

    def setUp(self):
        clean_environment()

    def tearDown(self):
        clean_environment()

    def test_prepareBarcodeTargetWhenExists(self):
        pass

    def test_prepareBarcodeTargetWhenClean(self):
        clean_barcode_target()
        assertFalse(os.path.exists('barcodes'))
        pass



if __name__ == '__main__':
    unittest.main()