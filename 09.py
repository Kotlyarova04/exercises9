class StrandsDNA:
    all_strands = []
    def __init__(self,strands):
        self.strands = strands.split()
    def add_strands(self,strands):
        self.all_strands.append(self.strands)

    def get_max_strands(self):
        return None
