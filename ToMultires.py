import sys
import os

# to bedpe

bin_size = [1000000, 100000000]
rfh = {}
for size in bin_size:
        dfh = open(sys.argv[1])
        rfh[size] = open(sys.argv[1].split(".")[0] + f".{size}.bedpe", "w")
        for line in dfh:
                line = line.rstrip().split("\t")
                sv = line
                bed = line[1].split(" & ")
                [chrom1, pos1] = bed[0].split(":")
                [chrom2, pos2] = bed[1].split(":")
                pos1 = int(pos1)
                pos2 = int(pos2)
                rfh[size].write(f"{chrom1}\t{pos1 - int(size/2)}\t{pos1 + int(size/2)}\t{chrom2}\t{pos2 - int(size/2)}\t{pos2 + int(size/2)}\n")
        dfh.close()
for size in bin_size:
        rfh[size].close()

# aggregate
ref = "hg19"

for size in bin_size:
        input_s = sys.argv[1].split('.')[0] + sys.argv[1].split('.')[1] + f'.{size}.bedpe'
        os.system(
f"clodius aggregate bedpe \
    --assembly {ref} \
    --chr1-col 1 --from1-col 2 --to1-col 3 \
    --chr2-col 4 --from2-col 5 --to2-col 6 \
    --output-file {input_s}.multires \
    {input_s}"
)
        os.system("rm " + sys.argv[1].split(".")[0] + f".{size}.bedpe")
