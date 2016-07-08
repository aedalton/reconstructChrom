import unittest
import sys, os 
curr_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.normpath(os.path.join(curr_dir, '../src')))

from FASTAReader import *
from glueSeqs import * 

class TestSeqMethods(unittest.TestCase):
    """ Test input: 
        >Frag_56
        ATTAGACCTG
        >Frag_57
        CCTGCCGGAA
        >Frag_58
        AGACCTGCCG
        >Frag_59
        GCCGGAATAC
    """

    def test_readin(self):
        # test a file of known length 
        fasta_records = FASTAFile('../data/test_data.txt')

        self.assertEqual(len(fasta_records), 4);
        
        self.assertTrue(hasattr(fasta_records[0], 'name'))
        self.assertTrue(hasattr(fasta_records[0], 'seq'))
        
        self.assertTrue(fasta_records[0].seq.isupper())
        self.assertTrue(fasta_records[0].seq != fasta_records[0].name)

        with self.assertRaises(TypeError):
            f = FASTAFile(7251920)

    def test_adjacent(self):
        # check that two seqs in test data known to not be adjacent are not 
        fasta_records = FASTAFile('../data/test_data.txt')

        # known non-overlaps 
        self.assertFalse(is_adjacent(fasta_records[0], fasta_records[1]))
        # known overlaps 
        self.assertTrue(is_adjacent(fasta_records[0], fasta_records[2]))

    def test_adj_matrix(self):
        fasta_records = FASTAFile('../data/test_data.txt')
        adj_matrix = get_adj_matrix(fasta_records)

        # check size of adj matrix, must be 2D array of len seqs in order to fill out checks for seq pairs 
        self.assertEqual(len(adj_matrix), len(fasta_records));

        # known overlaps 
        self.assertEqual(adj_matrix[0][2], True) 
        # known non-overlaps 
        self.assertEqual(adj_matrix[2][0], False)

    def test_seq_order(self):

        fasta_records = FASTAFile('../data/err_test_fasta.txt')
        adj_matrix = get_adj_matrix(fasta_records)
        
        with self.assertRaises(SystemExit):
            get_seq_order(adj_matrix)

        fasta_records = FASTAFile('../data/test_data.txt')
        adj_matrix = get_adj_matrix(fasta_records)
        final_seq = get_final_seq(adj_matrix)

        self.assertEqual(adj_matrix[final_seq].count(False), len(fasta_records) -1);

        order_of_seqs =  get_seq_order(adj_matrix)

        # known order based on test data is [0, 2, 1, 3]
        self.assertEquals(order_of_seqs, [0, 2, 1, 3])


suite = unittest.TestLoader().loadTestsFromTestCase(TestSeqMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
