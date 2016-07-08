import pdb 
import sys 

class FASTAFile (object):
    """A class to represent sequence data for both proteins and nucleic acids."""
  
    def __init__(self, filename = 'default'):
        """Create a new instance associated with the specified file.
        Options to give either a filename (string) or an open file.
        """
        self.records = []

        if isinstance(filename, str):
            try:
                self.fp = open(filename, 'r')
            except IOError:
                if filename.lower() == "t":
                    self.fp = open('../data/test_data.txt')
                elif filename.lower() == "f":
                    self.fp = open('../data/coding_challenge_data_set.txt')
                
                else:
                    print('\nNo valid file(name) provided or keycode provided. Please C/P or enter manually the records below, must be FASTA format.')
                    print('Conclude entry by hitting return then Ctrl-D\n')
               
                    names = sys.stdin.readlines()
                    self.fp = names

        elif isinstance(filename, file):
            self.fp = filename

        else:
            raise TypeError("Parameter must be a filename, multiline string, or file object")
    
        self._read()

    def _read(self): # double check to support simple iter 
        if isinstance(self.fp, file):
            self._read_file()
        else: 
            self._read_string()

    def _read_file(self):
        """ Generates records of FASTA name and sequence from open file
        if file in incorrect FASTA format, chromosome reconstruction will be unsuccessful"""
        ln = self.fp.readline()
        while(ln != ''):
            ln = ln.strip()
            if ln[:1] == '>':
                name = ln[1:]
                seq = ''
                ln = self.fp.readline()
                while ln != '' and ln[:1] != '>':
                    seq += ln.strip()
                    ln = self.fp.readline()
                self.records.append(FastaRec(name, seq))
            else:
                ln = self.fp.readline()

    def _read_string(self):
        """ Generates records of FASTA name and sequence from multiline string
        Improper FASTA format strings will produce index error, error printed 
        if first line (FASTA record name/id) ommited at any point in file, subsequent seq will be ignored """
        i = -1
        num_lines = len(self.fp)

        while (i < num_lines -1):
            i += 1
            ln = self.fp[i].strip()
            if ln[:1] == '>' and i < num_lines: 
                name = ln[1:]
                seq = ''
                
                try: 
                    ln = self.fp[i + 1]
                except IndexError:
                    sys.exit("Read Error: Please check FASTA format. Record IDs and sequences must be paired and separated by a new line.")

                if ln[:1] != '>' and i < num_lines - 1:
                    seq += str(ln).strip()

                self.records.append(FastaRec(name, seq))
    
    def __iter__(self):
        self._read() 
        return iter(self.records)

    def __len__(self):
        return len(self.records)
    
    def __getitem__(self, pos):
        return self.records.__getitem__(pos)
        
class FastaRec:
    """ FASTA Record object with alphanumeric attributes name (FASTA ID) and sequence """
    def __init__(self, n, s):
        self.name = n
        self.seq = s
        
    def __getitem__(self, pos):
        return self.seq.__getitem__(pos)

    def __len__(self):
        return len(self.seq)