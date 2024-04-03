class StrandsDNA:
    def __init__(self):
        self.all_strands = []

    def add_strands(self, strands):
        self.strands = strands.split()
        self.all_strands.append(self.strands)

    def get_max_strands(self):
        new_strands = []
        for strands in self.all_strands:
            for strand in strands:
                if strand not in new_strands:
                    new_strands.append(strand)
        new_strands.sort()
        max_lenght = max(len(strand) for strand in new_strands)
        max_strands = [strand for strand in new_strands if len(strand) == max_lenght]
        return ' '.join(max_strands)

dna = StrandsDNA()
dna.add_strands("ATCGA TCCTA CGT")
dna.add_strands("ATC CGT ATCG AC")
print(dna.get_max_strands())
