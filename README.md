# COLLAGENerator
Use circular permutation approach to solve and visualize chiral assemblies of Type IV collagen protomers. The approach provided here is applicable to other domains of interest, not simply biochemistry. Lastly, please note that the code/method here is rough and the code isn't particularly elegant, but it gets the job done and is easy to read. 

**The biology of collagen**

Collagen is the most abundant protein in animals and during its synthesis, three collagen polypeptide strands are assembled in triple-helix quaternary structure. You can ready all about it [here](https://en.wikipedia.org/wiki/Collagen). These triple-helix assemblies - effectively trimers - are also called protomers.  There are many types of collagens but this page is focused on human Type IV collagen. There are six genes for Type IV Collagen, and their protein products are &alpha;1, &alpha;2, &alpha;3, &alpha;4, &alpha;5, and &alpha;6. These can be mixed into protomers to form functional collagen.

| Subunit  | Representation |
| ------------- | ------------- |
| &alpha;1 | ![Alpha1](processing/extras/sketch_monomer/sketch_monomer_1.png?raw=true) |
| &alpha;2 | ![Alpha2](processing/extras/sketch_monomer/sketch_monomer_2.png?raw=true) |
| &alpha;3 | ![Alpha3](processing/extras/sketch_monomer/sketch_monomer_3.png?raw=true) |
| &alpha;4 | ![Alpha4](processing/extras/sketch_monomer/sketch_monomer_4.png?raw=true) |
| &alpha;5 | ![Alpha5](processing/extras/sketch_monomer/sketch_monomer_5.png?raw=true) |
| &alpha;6 | ![Alpha6](processing/extras/sketch_monomer/sketch_monomer_6.png?raw=true) |

However, only a handful of trimer configurations have been discovered to exist in nature: &alpha;1-&alpha;1-&alpha;2, &alpha;3-&alpha;4-&alpha;5, and &alpha;5-&alpha;5-&alpha;6.

Solved as a linear model, there are 432 possible trimers. However, the circular arrangement of these results in the use of circular permutations to address uniqueness. For example, the timer &alpha;1-&alpha;1-&alpha;2 is the same as &alpha;1-&alpha;2-&alpha;1 and the same as &alpha;2-&alpha;1-&alpha;1. Moreover, even when we solve the number of possible trimers, not all of these have been observed in nature.

## Dependencies
- Python 2.7
- Processing 2.2
 
## Documentation

1. Use `generate-nonredundant-trimers.py` to solve and generate list of chiral trimer assemblies.
2. Take output and inject it into one the `simple*` scripts in the Processing folder

## Processing / Simple
Use processing/simple/simple.py
![Alt text](processing/simple/simple.png?raw=true)


## Processing / Simple with labels
Use processing/simple_with_labels/simple_with_labels.

![Alt text](processing/simple_with_labels/simple_with_labels.png?raw=true)

## Processing / Simple with labels and inner circle
Use processing/simple_with_labels_and_inner_circle/simple_with_labels_and_inner_circle.py

![Alt text](processing/simple_with_labels_and_inner_circle/simple_with_labels_and_inner_circle.png?raw=true)


### Processing / Extras
**sketch_arc_midpoint.py** - calculate and generate arc midpoint

![Alt text](processing/extras/sketch_arc_midpoint/sketch_arc_midpoint.png?raw=true)

**sketch_static.py** - image array generator, this was simply a go-between towards final scripts.

![Alt text](processing/extras/sketch_static/sketch_static.png?raw=true)

