import sys

n = 0
ori_score = []
sv_dict = {}

rfh = open(sys.argv[1] + ".svlist.txt", "w")
for line in open(sys.argv[1]):
        line = line.rstrip().split()
        if n == 0:
                ori_score = line[4:]
                n = 1
        else:
                chr1 = line[:4][0]
                pos1 = line[:4][1]
                chr2 = line[:4][2]
                pos2 = line[:4][3]
                sv = ""

                D = dict(zip(ori_score, [float(i) for i in line[4:]]))
                L = [(D[x], x) for x in sorted(D.keys(), key = lambda x: D[x])]
                L1 = []
                for i in L:
                        if i[0] > 0.6:
                                L1.append(i)
                if len(L1) > 0:
                        ori_num = 1
                        if len(L1) == 2:
                                ori_num = 2

                        if chr1 != chr2:
                                if ori_num == 2:
                                        ori_duo = [i[-1] for i in L1]
                                        if set(ori_duo) == set(["++","--"]):
                                                sv = "interchromosomal translocation (3'->3' & 5'->5')"
                                        elif set(ori_duo) == set(["+-","-+"]):
                                                sv = "interchromosomal translocation (3'->5' & 5'->3')"

                                else:
                                        ori = L1[0][-1]
                                        if ori == "+-":
                                                sv = "interchromosomal translocation (3'->5')"
                                        elif ori == "-+":
                                                sv = "interchromosomal translocation (5'->3')"
                                        elif ori == "++":
                                                sv = "interchromosomal translocation (3'->3')"
                                        elif ori == "--":
                                                sv = "interchromosomal translocation (5'->5')"
                                                 elif ori_num == 2:
                                                 
                                ori_duo = [i[-1] for i in L1]
                                if set(ori_duo) == set(["++","--"]):
                                        sv = "inversion (3'->3' & 5'->5')"
                        else:
                                ori = L1[0][-1]
                                if ori == "+-":
                                        sv = "deletion (3'->5')"
                                elif ori == "-+":
                                        sv = "tandem duplication (->->)"
                                elif ori == "--":
                                        sv = "inverted duplication (-><-)"
                                elif ori == "++":
                                        sv = "inverted duplication (<-->)"
                        interaction = f"{chr1}:{pos1} & {chr2}:{pos2}"
                        if sv not in sv_dict:
                                sv_dict[sv] = [interaction]
                        else:
                                sv_dict[sv].append(interaction)

for sv in sv_dict:
        for interaction in sv_dict[sv]:
                print(sv, interaction)
                rfh.write(sv + "\t" + interaction + "\n")

rfh.close()
