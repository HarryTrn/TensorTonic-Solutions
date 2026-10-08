<!-- ⚠️ EDIT THIS FILE, NOT README.md — README.md is regenerated automatically by .github/workflows/update-readme.yml -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=TensorTonic%20Solutions&fontSize=46&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=Machine%20Learning%20from%20First%20Principles&descAlignY=56&descSize=18" width="100%" alt="TensorTonic Solutions banner"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1200&color=36BCF7&center=true&vCenter=true&width=620&lines={{TOTAL}}+ML+algorithms+implemented+from+scratch;Pure+Python+%2B+NumPy+%E2%80%94+no+black+boxes;Optimizers+%E2%80%A2+Losses+%E2%80%A2+RNNs+%E2%80%A2+CNNs+%E2%80%A2+Transformers;New+solutions+pushed+daily" alt="Typing SVG"/>

<br/>

[![Problems Solved](https://img.shields.io/badge/Problems%20Solved-{{TOTAL}}-2ea44f?style=for-the-badge&logo=checkmarx&logoColor=white)](#-solutions)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](#)
[![Last Commit](https://img.shields.io/github/last-commit/HarryTrn/TensorTonic-Solutions?style=for-the-badge&color=orange)](https://github.com/HarryTrn/TensorTonic-Solutions/commits/main)
[![Commit Activity](https://img.shields.io/github/commit-activity/m/HarryTrn/TensorTonic-Solutions?style=for-the-badge&color=blueviolet)](https://github.com/HarryTrn/TensorTonic-Solutions/commits/main)

[![TensorTonic Verified Solutions](https://www.tensortonic.com/api/badge/_shinomiyaa_.svg)](https://www.tensortonic.com/profile/_shinomiyaa_)

**[About](#-about)** · **[Progress](#-progress)** · **[Recent](#-recently-solved)** · **[Featured](#-featured-implementations)** · **[Solutions](#-solutions)** · **[Roadmap](#-roadmap)** · **[Connect](#-connect)**

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

<div align="center">

| 🧩 Solved | 🗂️ Topics | 🔥 Last 7 days | 📅 Last 30 days | 🔄 Last updated |
|:--:|:--:|:--:|:--:|:--:|
| **{{TOTAL}}** | **{{TOPICS}}** | **+{{LAST_7_DAYS}}** | **+{{LAST_30_DAYS}}** | {{LAST_UPDATED}} |

</div>

{{GROWTH_CHART}}

{{PIE_CHART}}

{{TOPIC_TABLE}}

### 🕒 Recently Solved

{{RECENT_TABLE}}

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

{{SOLUTIONS}}

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
