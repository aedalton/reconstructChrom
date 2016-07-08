#Introduction and Objective

Sequencing the DNA for a given individual typically involves fragmenting each chromosome into many small pieces that can be sequenced in parallel and then re-assembling the sequenced fragments into one long DNA sequence. If the sequences are all different fragments of one chromosome, then there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length. This algorithm reconstructs the chromosome utilizing this special property. 

#Use
###Local Use
**Download the repository**

    git clone https://github.com/aedalton16/reconstructChrom.git

** Navigate to src directory and run **
    
    python glueSeqs.py

#Input

These sequences must be all different fragments of one chromosome. Upon prompt, user can input a filename, provide a key entry for preset example files, or choose to copy/paste a multiline FASTA format string. 

Example input:

	>Frag_56
	ATTAGACCTG
	>Frag_57
	CCTGCCGGAA
	>Frag_58
	AGACCTGCCG
	>Frag_59
	GCCGGAATAC

#Output: 

The output of the program is the unique sequence that contains each of the given input strings as a substring.

Example output:

	ATTAGACCTGCCGGAATAC


#Included

- Code achieving objective
- README describing general approach
- Additional code written to evaluate solution (test/unit_tests.py).

