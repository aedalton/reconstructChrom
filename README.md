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

#Approach

When approaching challenges of this nature, I firsk like to break the problem down into its core elements--in this case, determining sequence overlap and order. Then, I rely upon the pattern matching technique in order to generate an efficient and quality solution. In this case, I read the prompt and considered what algorithms or other problems I had seen before that were similar, then modified the solution to the related problem in order to develop an algorithm for the task at hand. In this case, I immediately thought of dynamic programing algorithms that detect the longest common subsequence (LCS) with elements of optimal substructure and overlapping subproblems. In this case, I was inspired to utilize an adjacency matrix by the related problem's use of a lookup table to construct the optimal solution. After generating the adjacency matrix, I had to address the task of finding the correct order of sequences. For this task, I used 'whiteboarding' in order to reveal patterns and elements to the reconstruction such as the unique properties of the last sequence in the chromosome compared to intervening and beginning sequences. Upon establishing my approach to these objectives, the details of the algorithm flowed steadily. 

I created a FASTAFile class in order to simplify file (or string) reading and record holding. This class stores easily accessible FASTARec objects containing name (FASTA id) and seq (DNA sequence). 

I enjoy writing tests in order to evaluate my code, so I evaluated my solution using unittest with the example FASTA input provided in the prompt. 

##Choices

I chose not to use certain libraries such as SeqIO, Numpy, Pandas (etc) in my code for several reasons, but primarily because this was an opportunity to show an algorithm implementation and my own solutions. Of course, one never wants to 'reinvent the wheel', but the small scripts necessary to implement the reconstruction and the nature of the problem (i.e. the chance to discuss my approach) allowed for this freedom. 

##Future

I wanted to be respectful of the time constraint, but in the future, I would like to modify this project in order to include a more complex (possibly web) user interface that would reflect enhancements to the algorithm that would support important details such as overlap specificty adjustments, etc. 

#Included

- Code achieving objective
- README describing general approach
- Additional code written to evaluate solution (test/unit_tests.py).


