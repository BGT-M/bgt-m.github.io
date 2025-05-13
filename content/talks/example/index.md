---
title: "HoloScope: Topology-and-Spike Aware Fraud Detection on Big Graphs"

event: Network Science Institute
event_url: ''

location: Network Science Institute
address:
  street: ''
  city: ''
  region: ''
  postcode: ''
  country: ''

summary: Shenghua Liu presents HoloScope, a method for detecting online fraud using graph topology and temporal spikes.
abstract: "As people spend more time on platforms like YouTube, Facebook, and Twitter, and rely on reviews from Amazon and Yelp, online fraud has become a significant issue due to the high profits it offers to fraudsters. Online fraudsters invest in resources such as fake user accounts and dedicated IPs, making fraudulent activities less obvious and harder to detect. HoloScope is proposed to use graph topology and temporal spikes to detect fraudulent user groups more accurately. It introduces \"contrast suspiciousness,\" a dynamic weighting approach for detecting fraudulent blocks, especially low-density ones. HoloScope also considers sudden bursts and drops in fraudsters' attack patterns and provides theoretical bounds on the increased time cost for adversarial attacks. With a concise framework and sub-quadratic time complexity, HoloScope is reproducible and scalable, showing significant accuracy improvements in experiments."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2018-05-22T13:00:00Z'
date_end: '2018-05-22T15:00:00Z'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2018-05-22T00:00:00Z'

authors:
  - Shenghua Liu

tags: []

# Is this a featured talk? (true/false)
featured: true

image:
  caption: ''
  focal_point: ''

url_code: 'https://github.com/shenghua-liu/HoloScope'
# url_pdf: 'https://shenghua-liu.github.io/files/Holoscope_frauddetect-cikm2017.pdf'
url_slides: 'https://shenghua-liu.github.io/files/Holoscope_frauddetect-cikm2017.pdf'
url_video: 'https://www.youtube.com/watch?v=Cl1tlv5a-Js'

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects:
  - holoscope
---

<!-- {{% callout note %}}
Click on the **Slides** button above to view the built-in slides feature.
{{% /callout %}}

Slides can be added in a few ways:

- **Create** slides using Hugo Blox Builder's [_Slides_](https://docs.hugoblox.com/reference/content-types/) feature and link using `slides` parameter in the front matter of the talk file
- **Upload** an existing slide deck to `static/` and link using `url_slides` parameter in the front matter of the talk file
- **Embed** your slides (e.g. Google Slides) or presentation video on this page using [shortcodes](https://docs.hugoblox.com/reference/markdown/).

Further event details, including [page elements](https://docs.hugoblox.com/reference/markdown/) such as image galleries, can be added to the body of this page. -->


# Abstract
As people spend more time on platforms like YouTube, Facebook, and Twitter, and rely on reviews from Amazon and Yelp, online fraud has become a significant issue due to the high profits it offers to fraudsters. Online fraudsters invest in resources such as fake user accounts and dedicated IPs, making fraudulent activities less obvious and harder to detect. HoloScope is proposed to use graph topology and temporal spikes to detect fraudulent user groups more accurately. It introduces \"contrast suspiciousness,\" a dynamic weighting approach for detecting fraudulent blocks, especially low-density ones. HoloScope also considers sudden bursts and drops in fraudsters' attack patterns and provides theoretical bounds on the increased time cost for adversarial attacks. With a concise framework and sub-quadratic time complexity, HoloScope is reproducible and scalable, showing significant accuracy improvements in experiments.