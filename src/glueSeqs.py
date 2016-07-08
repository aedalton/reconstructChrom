import sys
from FASTAReader import * 
import pdb


def get_adj_matrix(fasta_records):
    """ Returns constructed 2D adjacency matrix. Iterates through FASTA reads 
    and generates pairs of adjacent sequences in ordered fashion."""
    num_seqs = len(fasta_records)

    # Matrix constructed in an ordered fashion 
    return [[is_adjacent(fasta_records[x].seq, fasta_records[y].seq)
        for y in range(num_seqs)] for x in range(num_seqs)]
    
def is_adjacent(seq1, seq2):
    """ Determines adjacency by finding prefix/suffix match between two reads 
    with > half coverage
    """

    # only include >.5 coverage, so no need to extend further 
    for i in range(len(seq1)//2): 
        j = len(seq1) - i
        # check prefix and suffix of respective seqs, ensuring meets >.5 criteria 
        if seq1[i:] == seq2[:j] and j > len(seq2)//2:
            return True
    return False

def get_seq_order(adj_matrix):
    """ Returns list of sequence indices indicating order of sequence reads in final chromosome
    """
    
    num_seqs = len(adj_matrix)
    tmp_final = get_final_seq(adj_matrix)

    reversed_order = [tmp_final]
    
    # small track to prevent infinite loops with improper FASTA records, for example 
    i = 0 
    while len(reversed_order) != num_seqs:
        tmp_final = reversed_order[-1] # retrieve the last of the current chain in order to reverse later 

        for j in range(num_seqs):
            # if the ordering of overlaps is correct and we're not duplicating 
            if adj_matrix[j][tmp_final] is True and j != tmp_final:
                reversed_order.append(j)  
                break
          
        # should only try to reconstruct for as many sequences as exist
        if i > num_seqs:
            # if the FASTA records include reads that prevent an ordering (duplicate seqs, etc), 
            # the append block will never execute, abort reconstruction. 
            sys.exit("Could not reform chromosome sequence from FASTA Records, no sequence (FASTA Record) order could be found")
        i += 1

    return reversed_order[::-1]

def get_final_seq(adj_matrix):
    """ An overlap indicates an adjacency in the full chromosome. In otherwords, 
    Any seq in the middle of the chrom should have at least 2 overlapping sequences, 
    one to the left and one to the right, whereas the ends should only have 1 """

    num_seqs = len(adj_matrix)
    final_seqs = [i for i in range(num_seqs) if adj_matrix[i].count(False) == num_seqs - 1]

    # for a valid FASTA input, should only return one 
    if len(final_seqs) == 1:
        return final_seqs[0]
    # otherwise, error 
    else: 
        return -1 

def reconstruct_chrom(fasta_records, ordered_seqs):
    """ Returns reconstructed chromosome from FASTA Records, with overlap spliced out of adjacent reads """

    chrom = fasta_records[ordered_seqs[0]].seq # beginning seq 
    num_seqs = len(fasta_records)

    for i in range(1, num_seqs):
        prev_seq = fasta_records[ordered_seqs[i-1]].seq
        curr_seq = fasta_records[ordered_seqs[i]].seq
        for j in range(len(curr_seq), 0, -1):
            if curr_seq[:j] == prev_seq[len(prev_seq) - j:]: # splice out overlap 
                chrom += curr_seq[j:] # add this spliced current portion to the extending chrom. 
                break

    return chrom

def seqs_to_chrom(filename):
    """ Main method, prints reconstructed chromosome after generating FASTA record, 
    adjacency matrix, and sequence order from FASTA ID/sequence pairs retrieved from 
    @param filename """

    fasta_records = FASTAFile(filename)
    adj_matrix = get_adj_matrix(fasta_records)
    ordered_seqs = get_seq_order(adj_matrix)

    chrom = reconstruct_chrom(fasta_records, ordered_seqs)
    if len(chrom) == 0: 
        print ("No reconstruction possible--please check FASTA file format. For example-Record IDs and sequences must be separated by a new line.")
    else: 
        print('\nReconstructed Chromosome:\n')
        print(chrom)
    
if __name__ == '__main__':
    print("\nTo reconstruct the entire chromosome from FASTA reads, please enter one of the following:")
    print("Enter 'f' to use coding_challenge_data_set.txt, \nor 't' for shorter test_data.txt, \nor 'c' to c/p FASTA format multiline text")
    inFile = raw_input("or filename with path: ")
    sys.exit(seqs_to_chrom(inFile))
