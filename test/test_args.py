import unittest
from wpldump import wpldump


class ParserTestCase(unittest.TestCase):
    def test_infile(self):
        params = wpldump.cmd_parse('infile')
        self.assertEqual(params.infile, 'infile')
        self.assertFalse(params.dir)
        self.assertIsNone(params.outfile)

    def test_inout(self):
        params = wpldump.cmd_parse('infile', 'out')
        self.assertEqual(params.infile, 'infile')
        self.assertFalse(params.dir)
        self.assertEqual('out', params.outfile)

    def test_dir_in(self):
        params = wpldump.cmd_parse('-d', 'infile', 'outfile')
        self.assertEqual(params.infile, 'infile')
        self.assertTrue(params.dir)
        self.assertEqual('outfile', params.outfile)


if __name__ == '__main__':
    unittest.main()
