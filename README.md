This dataset contains possible idiomatic expressions instances from 717 idioms divided into two folders

1. Formal Idioms - Idioms which undergo lexical changes.

2. Static Idioms - Idioms which stay the same across instances.

Each folder contains 3 sentence aligned files with '*' replaced with either 'Static_Idioms' or 'Formal_Idioms'
*_Words.txt :- Original Sentences
*_Tags.txt :- Sequence labelling tags for each token of the sentence. Each entry delimited by space is treated as a separate token. The labelling follows BIO convention using three tags(B-IDIOM,I-IDIOM,O).
	B-IDIOM:- beginning of possible idiomatic expression span
	I-IDIOM:- continuation of possible idiomatic expression span
	O:-	Non-Idiom token

*_Candidates.txt :- Candidate Idiom whose instance is present in the corresponding sentence.
