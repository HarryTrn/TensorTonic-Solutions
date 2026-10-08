<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=TensorTonic%20Solutions&fontSize=46&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=Machine%20Learning%20from%20First%20Principles&descAlignY=56&descSize=18" width="100%" alt="TensorTonic Solutions banner"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1200&color=36BCF7&center=true&vCenter=true&width=620&lines=73+ML+algorithms+implemented+from+scratch;Pure+Python+%2B+NumPy+%E2%80%94+no+black+boxes;Optimizers+%E2%80%A2+Losses+%E2%80%A2+RNNs+%E2%80%A2+CNNs+%E2%80%A2+Transformers;New+solutions+pushed+daily" alt="Typing SVG"/>

<br/>

[![Problems Solved](https://img.shields.io/badge/Problems%20Solved-73-2ea44f?style=for-the-badge&logo=checkmarx&logoColor=white)](#-solutions)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](#)
[![Last Commit](https://img.shields.io/github/last-commit/HarryTrn/TensorTonic-Solutions?style=for-the-badge&color=orange)](https://github.com/HarryTrn/TensorTonic-Solutions/commits/main)
[![Commit Activity](https://img.shields.io/github/commit-activity/m/HarryTrn/TensorTonic-Solutions?style=for-the-badge&color=blueviolet)](https://github.com/HarryTrn/TensorTonic-Solutions/commits/main)

[![TensorTonic Verified Solutions](https://www.tensortonic.com/api/badge/_shinomiyaa_.svg)](https://www.tensortonic.com/profile/_shinomiyaa_)

**[About](#-about)** · **[Progress](#-progress)** · **[Featured](#-featured-implementations)** · **[Solutions](#-solutions)** · **[Roadmap](#-roadmap)** · **[Connect](#-connect)**

</div>

---

## 🧠 About

This repository is my daily training log on **[TensorTonic](https://www.tensortonic.com)** — a platform for implementing the core algorithms of Machine Learning **from scratch**.

No high-level ML frameworks. Every optimizer, loss, layer and metric here is written by hand in Python + NumPy, so that the math is understood rather than called.

<table>
<tr>
<td width="33%" valign="top">

**📐 Math first**<br/>
Derive the formula, then write the code. Numerical stability (log-sum-exp, clamping, epsilon terms) is handled explicitly.

</td>
<td width="33%" valign="top">

**⚙️ From first principles**<br/>
From dot products up to GRU cells, attention masks and Nadam — each building block implemented without black boxes.

</td>
<td width="33%" valign="top">

**🎯 Interview & research ready**<br/>
Covers the fundamentals most often asked in ML interviews and used daily when reading papers.

</td>
</tr>
</table>

---

## 📊 Progress

```mermaid
pie showData
    title Solved problems by topic
    "Linear Algebra" : 11
    "Activations" : 9
    "Neural Network Layers" : 8
    "Optimizers & Training" : 7
    "Evaluation Metrics" : 7
    "NLP & Transformers" : 6
    "Classical ML" : 6
    "Loss Functions" : 4
    "Probability & Statistics" : 4
    "Feature Engineering" : 4
    "Computer Vision" : 3
    "Reinforcement Learning" : 2
    "Paper Implementations" : 2
```

| Topic | Solved | Topic | Solved |
|:--|:--:|:--|:--:|
| [📐 Linear Algebra](#linear-algebra) | 11 | [📏 Evaluation Metrics](#metrics) | 7 |
| [⚡ Activations](#activations) | 9 | [🔤 NLP & Transformers](#nlp) | 6 |
| [🧱 Neural Network Layers](#layers) | 8 | [🖼️ Computer Vision](#cv) | 3 |
| [🚀 Optimizers & Training](#optimizers) | 7 | [🎲 Probability & Statistics](#stats) | 4 |
| [📉 Loss Functions](#losses) | 4 | [🛠️ Feature Engineering](#features) | 4 |
| [🌳 Classical ML](#classical) | 6 | [🕹️ Reinforcement Learning](#rl) | 2 |
| [📄 Paper Implementations](#papers) | 2 | **Total** | **73** |

---

## ⭐ Featured Implementations

Some of the problems I found most instructive:

| Implementation | Why it matters |
|:--|:--|
| [**Adam**](./adam-optimizer) → [**Nadam**](./nadam-optimizer) | First/second moments, bias correction, then adding Nesterov look-ahead — the optimizer behind most modern training. |
| [**GRU Cell**](./gru-cell-forward) | Reset/update gating built by hand; the core idea behind gated recurrent memory. |
| [**Causal Masking**](./causal-masking) + [**Positional Encoding**](./positional-encoding) | Two of the essential ingredients of a decoder-only Transformer. |
| [**Simple CNN Layer**](./simple-cnn-layer) | Batched multi-channel convolution without any deep learning framework. |
| [**Expected Calibration Error**](./expected-calibration-error) | Goes beyond accuracy: measures whether a model's confidence can be trusted. |

---

## 📚 Solutions

> Each problem lives in its own folder. **Problem** links to TensorTonic; **Code** links to my solution.

<a id="linear-algebra"></a>
<details open>
<summary><b>📐 Linear Algebra & Vectors (11)</b></summary>
<br/>

| # | Problem | Key idea | Code |
|:-:|:--|:--|:-:|
| 1 | [Dot Product](https://www.tensortonic.com/problems/dot-product) | Sum of element-wise products | [📁](./dot-product) |
| 2 | [Euclidean Distance](https://www.tensortonic.com/problems/euclidean-distance) | √Σ(xᵢ − yᵢ)² | [📁](./euclidean-distance) |
| 3 | [Cosine Similarity](https://www.tensortonic.com/problems/cosine-similarity) | Normalized dot product, zero-vector safe | [📁](./cosine-similarity) |
| 4 | [3D Vector Norm](https://www.tensortonic.com/problems/vector-norm-3d) | L2 norm | [📁](./vector-norm-3d) |
| 5 | [Normalize 3D Vectors](https://www.tensortonic.com/problems/normalize-3d) | Unit vectors, zero-norm handling | [📁](./normalize-3d) |
| 6 | [Angle Between 3D Vectors](https://www.tensortonic.com/problems/angle-between-3d) | arccos with clamped cosine | [📁](./angle-between-3d) |
| 7 | [Matrix Transpose](https://www.tensortonic.com/problems/matrix-transpose) | No built-in helpers | [📁](./matrix-transpose) |
| 8 | [Matrix Trace](https://www.tensortonic.com/problems/matrix-trace) | Sum of the main diagonal | [📁](./matrix-trace) |
| 9 | [Matrix Inverse](https://www.tensortonic.com/problems/matrix-inverse) | Singular / non-square detection | [📁](./matrix-inverse) |
| 10 | [Matrix Normalization](https://www.tensortonic.com/problems/matrix-normalization) | Axis-wise norms | [📁](./matrix-normalization) |
| 11 | [Covariance Matrix](https://www.tensortonic.com/problems/covariance-matrix) | Sample covariance from centered data | [📁](./covariance-matrix) |

</details>

<a id="activations"></a>
<details>
<summary><b>⚡ Activation Functions (9)</b></summary>
<br/>

| # | Problem | Key idea | Code |
|:-:|:--|:--|:-:|
| 1 | [Sigmoid](https://www.tensortonic.com/problems/sigmoid-numpy) | Stable for large ± inputs | [📁](./sigmoid-numpy) |
| 2 | [Tanh](https://www.tensortonic.com/problems/tanh-activation) | Bounded in (−1, 1) | [📁](./tanh-activation) |
| 3 | [ReLU](https://www.tensortonic.com/problems/relu-activation) | max(0, x) | [📁](./relu-activation) |
| 4 | [Leaky ReLU](https://www.tensortonic.com/problems/leaky-relu) | Configurable negative slope α | [📁](./leaky-relu) |
| 5 | [ELU](https://www.tensortonic.com/problems/elu-activation) | Exponential negative branch | [📁](./elu-activation) |
| 6 | [SELU](https://www.tensortonic.com/problems/selu-activation) | Self-normalizing scale | [📁](./selu-activation) |
| 7 | [GELU](https://www.tensortonic.com/problems/gelu) | Gaussian error linear unit | [📁](./gelu) |
| 8 | [Swish](https://www.tensortonic.com/problems/swish-activation) | x · σ(x) | [📁](./swish-activation) |
| 9 | [Softmax](https://www.tensortonic.com/problems/softmax-function) | Max-shift for numerical stability | [📁](./softmax-function) |

</details>

<a id="layers"></a>
<details>
<summary><b>🧱 Neural Network Layers (8)</b></summary>
<br/>

| # | Problem | Key idea | Code |
|:-:|:--|:--|:-:|
| 1 | [Linear Layer Forward](https://www.tensortonic.com/problems/linear-layer-forward) | xW + b | [📁](./linear-layer-forward) |
| 2 | [Batch Normalization](https://www.tensortonic.com/problems/batch-normalization) | Feature-wise stats, γ / β | [📁](./batch-normalization) |
| 3 | [Dropout (Training)](https://www.tensortonic.com/problems/dropout-training) | Inverted dropout scaling | [📁](./dropout-training) |
| 4 | [Simple CNN Layer](https://www.tensortonic.com/problems/simple-cnn-layer) | Batched multi-channel convolution | [📁](./simple-cnn-layer) |
| 5 | [Max Pooling](https://www.tensortonic.com/problems/maxpool-forward) | Window + stride | [📁](./maxpool-forward) |
| 6 | [Global Average Pooling](https://www.tensortonic.com/problems/global-avg-pooling) | Per-channel spatial mean | [📁](./global-avg-pooling) |
| 7 | [RNN Step Forward](https://www.tensortonic.com/problems/rnn-step-forward) | tanh recurrent cell | [📁](./rnn-step-forward) |
| 8 | [GRU Cell Forward](https://www.tensortonic.com/problems/gru-cell-forward) | Reset / update / candidate gates | [📁](./gru-cell-forward) |

</details>

<a id="optimizers"></a>
<details>
<summary><b>🚀 Optimizers & Training (7)</b></summary>
<br/>

| # | Problem | Key idea | Code |
|:-:|:--|:--|:-:|
| 1 | [Gradient Descent (1D Quadratic)](https://www.tensortonic.com/problems/gradient-descent-quadratic) | Iterative parameter updates | [📁](./gradient-descent-quadratic) |
| 2 | [AdaGrad](https://www.tensortonic.com/problems/adagrad-optimizer) | Accumulated squared gradients | [📁](./adagrad-optimizer) |
| 3 | [RMSProp](https://www.tensortonic.com/problems/rmsprop-optimizer) | Exponential moving average of g² | [📁](./rmsprop-optimizer) |
| 4 | [Adam](https://www.tensortonic.com/problems/adam-optimizer) | Moments + bias correction | [📁](./adam-optimizer) |
| 5 | [Nadam](https://www.tensortonic.com/problems/nadam-optimizer) | Adam + Nesterov momentum | [📁](./nadam-optimizer) |
| 6 | [Gradient Clipping](https://www.tensortonic.com/problems/gradient-clipping) | Global L2-norm clipping | [📁](./gradient-clipping) |
| 7 | [Linear LR Scheduler](https://www.tensortonic.com/problems/linear-lr-scheduler) | Linear decay schedule | [📁](./linear-lr-scheduler) |

</details>

<a id="losses"></a>
<details>
<summary><b>📉 Loss Functions (4)</b></summary>
<br/>

| # | Problem | Key idea | Code |
|:-:|:--|:--|:-:|
| 1 | [Mean Squared Error](https://www.tensortonic.com/problems/mean-squared-error) | Mean of squared residuals | [📁](./mean-squared-error) |
| 2 | [Hinge Loss](https://www.tensortonic.com/problems/hinge-loss) | Margin-based SVM loss | [📁](./hinge-loss) |
| 3 | [Focal Loss](https://www.tensortonic.com/problems/focal-loss) | Down-weights easy examples | [📁](./focal-loss) |
| 4 | [Dice Loss](https://www.tensortonic.com/problems/dice-loss) | Overlap loss for segmentation | [📁](./dice-loss) |

</details>

<a id="metrics"></a>
<details>
<summary><b>📏 Evaluation Metrics (7)</b></summary>
<br/>

| # | Problem | Key idea | Code |
|:-:|:--|:--|:-:|
| 1 | [Confusion Matrix](https://www.tensortonic.com/problems/confusion-matrix-norm) | Row / column normalization | [📁](./confusion-matrix-norm) |
| 2 | [Micro-F1](https://www.tensortonic.com/problems/metrics-f1-micro) | Aggregated TP / FP / FN | [📁](./metrics-f1-micro) |
| 3 | [AUC (ROC)](https://www.tensortonic.com/problems/auc) | Trapezoidal integration | [📁](./auc) |
| 4 | [NDCG](https://www.tensortonic.com/problems/ndcg) | Ranking quality at K | [📁](./ndcg) |
| 5 | [Expected Calibration Error](https://www.tensortonic.com/problems/expected-calibration-error) | Confidence vs. accuracy gap | [📁](./expected-calibration-error) |
| 6 | [Silhouette Score](https://www.tensortonic.com/problems/silhouette-score) | Clustering quality | [📁](./silhouette-score) |
| 7 | [Perplexity](https://www.tensortonic.com/problems/perplexity-computation) | Language-model evaluation | [📁](./perplexity-computation) |

</details>

<a id="classical"></a>
<details>
<summary><b>🌳 Classical Machine Learning (6)</b></summary>
<br/>

| # | Problem | Key idea | Code |
|:-:|:--|:--|:-:|
| 1 | [Ridge Regression](https://www.tensortonic.com/problems/ridge-regression) | Closed-form L2 regularization | [📁](./ridge-regression) |
| 2 | [KNN Distance + Lookup](https://www.tensortonic.com/problems/knn-distance) | Nearest-neighbor search | [📁](./knn-distance) |
| 3 | [K-Means Assignment](https://www.tensortonic.com/problems/k-means-assignment) | Nearest-centroid assignment | [📁](./k-means-assignment) |
| 4 | [K-Means Centroid Update](https://www.tensortonic.com/problems/k-means-centroid-update) | Cluster means, empty clusters | [📁](./k-means-centroid-update) |
| 5 | [Information Gain](https://www.tensortonic.com/problems/information-gain) | Entropy-based tree splits | [📁](./information-gain) |
| 6 | [Jaccard Similarity](https://www.tensortonic.com/problems/jaccard-similarity) | Intersection over union of sets | [📁](./jaccard-similarity) |

</details>

<a id="stats"></a>
<details>
<summary><b>🎲 Probability & Statistics (4)</b></summary>
<br/>

| # | Problem | Key idea | Code |
|:-:|:--|:--|:-:|
| 1 | [Mean, Median, Mode](https://www.tensortonic.com/problems/mean-median-mode) | Deterministic tie handling | [📁](./mean-median-mode) |
| 2 | [Expected Value](https://www.tensortonic.com/problems/expected-value-discrete) | Discrete distributions | [📁](./expected-value-discrete) |
| 3 | [Binomial PMF / CDF](https://www.tensortonic.com/problems/binomial-pmf-cdf) | Combinatorics + cumulative sums | [📁](./binomial-pmf-cdf) |
| 4 | [Weighted Moving Average](https://www.tensortonic.com/problems/weighted-moving-average) | Normalized window weights | [📁](./weighted-moving-average) |

</details>

<a id="features"></a>
<details>
<summary><b>🛠️ Feature Engineering (4)</b></summary>
<br/>

| # | Problem | Key idea | Code |
|:-:|:--|:--|:-:|
| 1 | [Binning](https://www.tensortonic.com/problems/binning) | Interval edge handling | [📁](./binning) |
| 2 | [Log Transform](https://www.tensortonic.com/problems/log-transform) | Numerically safe log | [📁](./log-transform) |
| 3 | [Rank Transform](https://www.tensortonic.com/problems/rank-transform) | Tie policies | [📁](./rank-transform) |
| 4 | [Robust Scaling](https://www.tensortonic.com/problems/robust-scaling) | Median + IQR | [📁](./robust-scaling) |

</details>

<a id="nlp"></a>
<details>
<summary><b>🔤 NLP & Transformers (6)</b></summary>
<br/>

| # | Problem | Key idea | Code |
|:-:|:--|:--|:-:|
| 1 | [Word Count Dictionary](https://www.tensortonic.com/problems/word-count-dict) | Token frequencies | [📁](./word-count-dict) |
| 2 | [Remove Stopwords](https://www.tensortonic.com/problems/remove-stopwords) | Order-preserving filtering | [📁](./remove-stopwords) |
| 3 | [Bag-of-Words](https://www.tensortonic.com/problems/bag-of-words) | Count vectors over a vocabulary | [📁](./bag-of-words) |
| 4 | [Text Chunking](https://www.tensortonic.com/problems/text-chunking) | Size + overlap (RAG-style) | [📁](./text-chunking) |
| 5 | [Positional Encoding](https://www.tensortonic.com/problems/positional-encoding) | Sinusoidal sin / cos | [📁](./positional-encoding) |
| 6 | [Causal Masking](https://www.tensortonic.com/problems/causal-masking) | Block attention to future tokens | [📁](./causal-masking) |

</details>

<a id="cv"></a>
<details>
<summary><b>🖼️ Computer Vision (3)</b></summary>
<br/>

| # | Problem | Key idea | Code |
|:-:|:--|:--|:-:|
| 1 | [Image Histogram](https://www.tensortonic.com/problems/image-histogram) | Intensity binning | [📁](./image-histogram) |
| 2 | [IoU (Bounding Box)](https://www.tensortonic.com/problems/iou-bounding-box) | Overlap / union area | [📁](./iou-bounding-box) |
| 3 | [Anchor Box Generation](https://www.tensortonic.com/problems/anchor-box-generation) | Scales × aspect ratios | [📁](./anchor-box-generation) |

</details>

<a id="rl"></a>
<details>
<summary><b>🕹️ Reinforcement Learning (2)</b></summary>
<br/>

| # | Problem | Key idea | Code |
|:-:|:--|:--|:-:|
| 1 | [Monte Carlo Policy Evaluation](https://www.tensortonic.com/problems/mc-policy-evaluation) | Averaging discounted returns | [📁](./mc-policy-evaluation) |
| 2 | [Policy Gradient Loss](https://www.tensortonic.com/problems/policy-gradient-loss) | log π(a\|s) · advantage | [📁](./policy-gradient-loss) |

</details>

<a id="papers"></a>
<details>
<summary><b>📄 Paper Implementations — AlexNet (2)</b></summary>
<br/>

| # | Problem | Key idea | Code |
|:-:|:--|:--|:-:|
| 1 | [Dropout Regularization](https://www.tensortonic.com/research/alexnet/alexnet-dropout) | Seeded masks, train vs. inference | [📁](./alexnet) |
| 2 | [ReLU Activation](https://www.tensortonic.com/research/alexnet/alexnet-relu) | AlexNet's non-saturating activation | [📁](./alexnet) |

</details>

---

## 🗺️ Roadmap

- [x] Linear algebra & statistics foundations
- [x] Activations, losses and optimizers
- [x] RNN / GRU and CNN building blocks
- [ ] Backpropagation for full MLPs
- [ ] Scaled dot-product & multi-head attention
- [ ] More paper implementations (ResNet, Transformer, …)

---

## 📁 Repository Structure

```
TensorTonic-Solutions/
├── adam-optimizer/        # one folder per problem
├── gru-cell-forward/
├── causal-masking/
├── ...
├── alexnet/               # research-track (paper) problems
└── README.md
```

---

## 🤝 Connect

<div align="center">

[![TensorTonic Profile](https://img.shields.io/badge/TensorTonic-Profile-36BCF7?style=for-the-badge)](https://www.tensortonic.com/profile/_shinomiyaa_)
[![GitHub](https://img.shields.io/badge/GitHub-HarryTrn-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/HarryTrn)
<!-- Replace YOUR_LINKEDIN and YOUR_EMAIL below, or delete these two lines -->
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/YOUR_LINKEDIN/)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:YOUR_EMAIL@gmail.com)

**If this repo helps you learn, consider giving it a ⭐**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=100&section=footer" width="100%" alt="footer"/>

</div>
