# Voronoi-based decision boundaries

This repository contains notebooks focused on decision boundary plotting for high-dimensional data. The main idea is to approximate decision boundaries in 2D by superimposing [Voronoi tessellations](http://datagenetics.com/blog/may12017/index.html) onto the 2D-transformed data. To accomplish this, a 1-nearest-neighbour (1-NN) model is used to approximate the original model's predictive behaviour on the original (N-dimensional) data and apply the same technique on 2D-transformed data.

The plots below illustrate the Voronoi-based decision boundaries estimated for three different models trained on 6D data with 4 target classes. It can be seen that the model is able to make some sense of which model is overfitting and which is not.

![](https://vivianrjkmr.github.io/assets/decbound/6_model_comparison.png)

### Project structure

This project contains two Jupyter notebooks and a utility script. They are organised as follows.

```
.
├── Decision boundary plotting.ipynb    # notebook for decision boundary plotting
├── Voronoi diagram.ipynb               # notebook for Voronoi illustration
├── utils.py                            # utility script containing helper functions for plotting
└── README.md
```

### References

- [Visualizing multi-dimensional decision boundaries in 2D](https://pure.uva.nl/ws/files/2110683/164710_431596.pdf) by Migut et al.
- Wikipedia article on [Voronoi diagrams](https://en.wikipedia.org/wiki/Voronoi_diagram)
