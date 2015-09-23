# SCFG-shift-reduce
A shift-reduce based linear time procedure for extracting SCFGs from alignments

Based on "Extracting Synchronous Grammar Rules From Word-Level Alignments in Linear Time", Zhang, Gildea and Chiang, Coling 2008

Note :
1. This approach can only create left-branching trees because of the preference
    for left strong intervals.
2. [1, 1] can never be a consistent phrase since y \in [2, n]
