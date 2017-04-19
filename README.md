# COLLAGENerator
Use circular permutation approach to solve and visualize chiral assemblies of Type IV collagen protomers.

Each collagen protomer is a trimer. In humans, there are six (6) possible variants that can be selected from known as "alpha subunits/chains", labeled &alpha;1, &alpha;2, &alpha;3, &alpha;4, &alpha;5, and &alpha;6:

| Subunit  | Representation |
| ------------- | ------------- |
| &alpha;1 | ![Alpha1](processing/extras/sketch_monomer/sketch_monomer_1.png?raw=true) |
| &alpha;2 | ![Alpha2](processing/extras/sketch_monomer/sketch_monomer_2.png?raw=true) |
| &alpha;3 | ![Alpha3](processing/extras/sketch_monomer/sketch_monomer_3.png?raw=true) |
| &alpha;4 | ![Alpha4](processing/extras/sketch_monomer/sketch_monomer_4.png?raw=true) |
| &alpha;5 | ![Alpha5](processing/extras/sketch_monomer/sketch_monomer_5.png?raw=true) |
| &alpha;6 | ![Alpha6](processing/extras/sketch_monomer/sketch_monomer_6.png?raw=true) |

There X number of possible combinations of these subunits into trimers. However, not every combination has been observed in nature. 

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

