from Bio import SeqIO
input_file = "../data/antibody_sequences.fasta"
output_file = "../results/stats.txt"
# 定义氨基酸分类
hydrophobic = set("AVILMFWY")
charged = set("DEKRH")
with open(output_file,"w")as out:
    out.write("name\tlength\thydrophobic_pct\tcharged_pct\n")
    for record in SeqIO.parse(input_file,"fasta"):
        seq = str(record.seq)
        length = len(seq)
        hydro_count = sum(1 for aa in seq if aa in hydrophobic)
        charged_count = sum(1 for aa in seq if aa in charged)
        hydro_pct = hydro_count / length * 100
        charged_pct = charged_count / length * 100
        out.write(f"{record.id}\t{length}\t{hydro_pct:.2f}%\t{charged_pct:.2f}%\n")
        print(f"{record.id}\t{length}\t{hydro_pct:.2f}%\t{charged_pct:.2f}%")

