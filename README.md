# Low-N Protein Engineering
This repository contains a complete, open-source, end-to-end re-implementation of the Church Lab's eUniRep in silico protein engineering pipeline as presented in Biswas et al. Details on our implementation can be read here [INSERT LINK TO PUBLISHED AUTHOREA], the original Church lab paper can be read [here](https://www.biorxiv.org/content/10.1101/2020.01.23.917682v1), with their repository [here](https://github.com/churchlab/UniRep). The JAX-unirep re-implementation we use in our implementation can be found [here](https://github.com/ElArkk/jax-unirep).

## How to use:
Each in silico step in the protein engineering pipeline has a jupyter notebook that will execute that step as well as an individual README file. The pipeline steps have been broken down as follows:

1. Training UniRep: either use the weights provided by the [Church lab](https://github.com/churchlab/UniRep) or use the JAX-unirep reimplementation to re-train from scratch, which is well documented [here](https://github.com/ElArkk/jax-unirep)
2. Curating pre-training set for evotuning: [pre-training]()
3. Evotuning: we pushed an [example script](https://github.com/ElArkk/jax-unirep/blob/master/examples/evotuning.py) to the jax-unirep repo.
4. Top model selection and hyperparamter tuning: [top-model]()
5. Markov Chain Monte Carlo (MCMC) directed evolution: [directed-evo]()
6. Additional: scripts to do further analysis such as PCA and epistasis evaluation: [analysis]()

If you want to request any modifications / additions or want to collaborate feel free to start an issue / PR!
