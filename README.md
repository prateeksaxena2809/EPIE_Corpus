This dataset contains possible idiomatic expressions instances from 717 idioms divided into two folders

1. Formal Idioms - Idioms which undergo lexical changes.

2. Static Idioms - Idioms which stay the same across instances.

## Schema
Each folder contains 3 sentence aligned files with '*' replaced with either 'Static_Idioms' or 'Formal_Idioms'  
*_Words.txt :- Original Sentences  
*_Candidates.txt :- Candidate Idiom whose instance is present in the corresponding sentence.  
*_Tags.txt :- Sequence labelling tags for each token of the sentence. Each entry delimited by space is treated as a separate token. The labelling follows BIO convention using three tags(B-IDIOM,I-IDIOM,O).  
  * B-IDIOM:- beginning of possible idiomatic expression span
  * I-IDIOM:- continuation of possible idiomatic expression span
  * O:- Non-Idiom token  
  
## Citation

We have a [paper](https://arxiv.org/abs/2006.09479) published in the 23rd International Conference on Text, Speech and Dialogue, 2020.
```bibtex
@misc{saxena2020epie,
      title={EPIE Dataset: A Corpus For Possible Idiomatic Expressions}, 
      author={Prateek Saxena and Soma Paul},
      year={2020},
      eprint={2006.09479},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
