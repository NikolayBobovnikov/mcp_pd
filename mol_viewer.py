from vpython import *
import os

class Atom:
    def __init__(self, tokens):
        self.X = float(tokens[0])
        self.Y = float(tokens[1])
        self.Z = float(tokens[2])
        self.Name = tokens[3]

    def ToString(self):
        return "X: " + str(self.X) + "; Y: " + str(self.Y) + "; Z: " + str(self.Z)


class Bond:
    def __init__(self, tokens):
        self.Start = int(tokens[0])
        self.End = int(tokens[1])
        self.Thickness = tokens[2]

    def ToString(self):
        return "Start: " + str(self.Start) + "; End: " + str(self.End)
    

def CheckExtension(filepath):
    filename, file_extension = os.path.splitext(filepath)
    if file_extension.lower() != ".sdf":
        raise RuntimeError("File format is not supported")


def ParseTableDef(table_def):
    tokens = table_def.split()
    n_atoms = tokens[0]
    n_bonds = tokens[1]
    return (int(n_atoms), int(n_bonds))


def ReadSDF(filepath):
    CheckExtension(filepath)
    with open(filepath) as f:
        lines = f.readlines()
        
        title = lines[0]

        table_def = lines[3]
        n_atoms, n_bonds = ParseTableDef(table_def)

        atoms = []
        bonds = []

        for atom_line in lines[4:n_atoms]:
            tokens = atom_line.split()
            atoms.append(Atom(tokens))

        bond_start = 4 + n_atoms
        bond_end = bond_start + n_bonds
        
        
        for bond_line in lines[bond_start : bond_end]:
            tokens = bond_line.split()
            bond= Bond(tokens)
            bonds.append(Bond(tokens))

        print(atoms[0].ToString())


    
if __name__ == "__main__":
    ReadSDF("test.sdf")
