# SVToMultires
convert sv.txt into multires file for visualization at higlass

Input.sv.txt format:

chrom1  pos1    chrom2  pos2    ++      +-      -+      --
chr14   66620000        chr19   57440000        5.615e-16       8.688e-12       0.9231  9.703e-15
chr1    72755000        chr1    72810000        7.628e-16       0.9963  4.233e-17       3.625e-12
chr1    144835000       chr2    91755000        0.001647        3.806e-16       1.481e-20       0.858
.
.
.

Command 1: IdentifySV.py Input.sv.txt

-> Output.identified.sv.list.txt format:

interchromosomal translocation (5'->3') chr4:93175000 & chr14:66605000
deletion (3'->5')       chr1:72755000 & chr1:72810000
interchromosomal translocation (5'->5') chr4:5175000 & chr22:30125000
tandem duplication (->->)       chr21:16125000 & chr21:23390000
.
.
.

Command 2: ToMultires.py Output.identified.sv.list.txt

-> Final output file: out.100000000.bedpe.multires, out.10000000.bedpe.multires 
