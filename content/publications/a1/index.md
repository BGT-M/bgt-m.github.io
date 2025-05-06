---
title: 'a1꞉ Steep Test-time Scaling Law via Environment Augmented Generation'
share: false
authors:
  - Lingrui Mei
  - admin
  - Yiwei Wang
  - Baolong Bi
  - Yuyao Ge
  - Jun Wan
  - Yurong Wu
  - Xueqi Cheng

date: '2025-04-20T19:00:00Z'
doi: 'https://doi.org/10.48550/arXiv.2504.14597'

# Schedule page publish date (NOT publication's date).
publishDate: '2025-04-20'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['3']
publication: arXiv

abstract: Large Language Models (LLMs) have made remarkable breakthroughs in reasoning, yet continue to struggle with hallucinations, logical errors, and inability to self-correct during complex multi-step tasks. Current approaches like chain-of-thought prompting offer limited reasoning capabilities that fail when precise step validation is required. We propose Environment Augmented Generation (EAG), a framework that enhances LLM reasoning through꞉  (1) real-time environmental feedback validating each reasoning step, (2) dynamic branch exploration for investigating alternative solution paths when faced with errors, and (3) experience-based learning from successful reasoning trajectories. Unlike existing methods, EAG enables deliberate backtracking and strategic replanning through tight integration of execution feedback with branching exploration. Our a1-32B model achieves state-of-the-art performance among similar-sized models across all benchmarks, matching larger models like o1 on competition mathematics while outperforming comparable models by up to 24.4 percentage points. Analysis reveals EAG's distinctive scaling pattern꞉  initial token investment in environment interaction yields substantial long-term performance dividends, with advantages amplifying proportionally to task complexity. EAG's theoretical framework demonstrates how environment interactivity and systematic branch exploration together establish a new paradigm for reliable machine reasoning, particularly for problems requiring precise multi-step calculation and logical verification.

# Summary. An optional shortened abstract.
# summary: In this work, we propose a Dynamically Adaptive Density Control Strategy based on the degree of reconstruction of the background of the scene, which adaptive the spatial sample point generation strategy dynamically according to the training results and prevents the generation of redundant data in the model.

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://arxiv.org/pdf/2504.14597'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ''
  focal_point: ''
  placement: 2
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.


# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: CCET2022
---



