from rdkit import Chem
from rdkit.Chem import Draw


def transition(number, descriptor):
    smiles = descriptor
    mol = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(mol, size=(300, 300), )
    Draw.MolToImageFile(mol, f"E:/Works/mol{number}.jpg")
    img.show()

# 1. 四氰基吡啶
transition(1, "N#Cc1ccncc1")
# 2. 三-五氟苯基硼烷
transition(2, "B(C1=C(C(=C(C(=C1F)F)F)F)F)(C2=C(C(=C(C(=C2F)F)F)F)F)C3=C(C(=C(C(=C3F)F)F)F)F")
# 3. 4,4,5,5-四甲基-2-苯基-1,3,2-二氧杂硼烷
transition(3, "B1(OC(C(O1)(C)C)(C)C)C2=CC=CC=C2")
# 4. 联硼酸频那醇酯
transition(4, "B1(OC(C(O1)(C)C)(C)C)B2OC(C(O2)(C)C)(C)C")
# 5. 二甲基苯硅烷基硼酸频那醇酯
transition(5, "B1(OC(C(O1)(C)C)(C)C)[Si](C)(C)C2=CC=CC=C2")
