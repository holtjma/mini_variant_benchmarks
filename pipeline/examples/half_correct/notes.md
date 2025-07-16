## Notes
This example highlights one of the interesting effects of using a basepair scoring scheme.
In the example, the truth set has a single SNP variant (A>C) while the query set instead detects that the "C" base was inserted.
It is clear that query is not fully correct in this situation, and both GT scoring scheme give this region a 0.0.
However, it _is_ detecting the "C" base where there were none before.
This situation is fairly common in homopolymer stretches where sequencing technologies may "slip" and mistake a SNP for an indel (or vice versa, see [half_correct_rev](../half_correct_rev)).

Interestingly, the basepair scoring scheme will give this partial credit.
It both detects that the "C" base has been correctly added, but also that the "A" base was _not_ removed.
This is the main situation where bases are assigned partially correct scores.
Thus, the recall and precision are both 0.5 in this example.
