![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC--BY--NC--ND%204.0-blue)
![Addendum: eriOS Thought Protection](https://img.shields.io/badge/Addendum-eriOS%20Thought%20Protection-orange)

SPDX-License-Identifier: CC-BY-NC-ND-4.0  
eriOS-Addendum: eriOS Thought Protection Addendum v1.0  
Copyright (c) 2026 Yasunari

## License

This repository is licensed under:

- **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**
- **eriOS Thought Protection Addendum v1.0**

All code, documents, structures, protocols, and conceptual components in this repository  
are covered by this combined license.

See [LICENSE](./LICENSE) for full text.  
See [docs/eriOS-Addendum-v1.0.md](./docs/eriOS-Addendum-v1.0.md) for full text.

ライセンスに関する問い合わせ・許可申請はこちら：  
**X（旧Twitter）：https://x.com/moonpour_c**

---
# SYOBU-Core-Lite
# Human–AI Common Language Layer (Summary) / 人とAIの共通言語層（概要）
**Multisensory + Internal → Traceable Structure → Shared Language**
**多感覚＋内部 → 追跡可能な構造化 → 共通言語化**

---

## 日本語（Purpose）
本プロジェクトは、視覚・音響・触覚・運動・内部状態（将来的にMRI/rt-fMRI系特徴量やAI内部特徴量を含み得る）を、
共通の意味座標・Node・意味構造素へ写像し、説明責任と検証を支える「共通言語層」を作る枠組みを提案します。
入力は **観測 / 構造 / 意味 / 説明** の4層へ分離し、層の混同を避けます。

### 何が新しいか（差分）
- **4層分離**：説明だけで根拠（観測・構造・意味）を補完しません。
- **追跡可能性の宣言**：guarantee_level（full / partial / display_only / unknown）で追跡可能性を示し、known_limits を隠しません。
- **モダリティ差の保持**：統合で消すのではなく、由来モダリティ差を保持したまま比較可能な構造へ写像します。

### 安全・誤用防止（Non-goals）
- 添付図や説明のみの情報は **display_only** として扱い、**full 根拠にしません**（図は入口であり全体ではありません）。
- **Node局所結果を正本化しません**（正式反映前は統合Nodeで整合確認を行います）。
- 内部状態は **医療診断・疾病推定・精神状態確定・治療判断に使用しません**（断定を避け、known_limits を明示します）。

---

## English (Purpose)
We propose a framework that projects multisensory signals (vision, audio, tactile, motion) and internal signals
(potentially including MRI/rt-fMRI-derived features and AI internal features) into a shared representation:
common coordinates, nodes, and minimal semantic units—forming a **common language layer** for accountability and verification.
Inputs are separated into four layers: **Observation / Structure / Semantics / Explanation**.

### What’s Different
- **Four-layer separation**: never let explanations replace evidence (observation/structure/semantics).
- **Traceability labeling**: declare traceability via guarantee_level (full/partial/display_only/unknown) and always retain known_limits.
- **Preserve modality provenance**: do not “erase” modalities by naive fusion; keep provenance while enabling comparison.

### Safety & Non-goals
- Treat diagrams/labels as **display_only** and never upgrade them to **full** evidence (a diagram is an entry point, not the whole system).
- Do not canonize local node outputs; require integration and consistency checks before any authoritative use.
- Internal signals must not be used for medical diagnosis, disease inference, mental-state determination, or treatment decisions; avoid over-claims and state known_limits.

---

## Contents / 収録物
- `docs/summary.md` : 公開可能な範囲の1枚サマリ / Public-facing one-page summary

## Scope Note / 公開範囲の注記
This repository is intended to host **public-safe summaries** only.
本リポジトリは **公開可能な概要** のみを扱い、詳細仕様や実装用の指示・検討中の差分は含みません。

---

## License / ライセンス
Licensed under the **Apache License, Version 2.0**. See `LICENSE`.
**Apache License 2.0** で提供します。詳細は `LICENSE` を参照してください。
( Apache-2.0 includes an explicit patent grant from contributors and a termination clause for patent litigation. )
（Apache-2.0 には貢献者からの明示的な特許許諾と、特許訴訟に関する終了条項が含まれます。）

## NOTICE (Optional) / NOTICE（任意）
If a `NOTICE` file is present, retain it in redistributions.
`NOTICE` ファイルが存在する場合は、再配布時に保持してください。

---

## AI-Assistance Note (Recommended) / AI利用に関する注記（推奨）
Contributions must be made with rights to submit under Apache-2.0.
If AI tools are used, contributors are responsible for avoiding copying third-party copyrighted content and for disclosing material AI assistance when appropriate.
Apache-2.0 の下で提出する権利がある内容のみ投稿してください。
AIツールを利用する場合も、第三者著作物の混入回避と、必要に応じたAI支援の開示は投稿者責任です。

## Patent Notice (Optional) / 特許に関する注意（任意）
No patent review has been performed. Nothing here should be interpreted as a non-infringement guarantee.
特許調査は実施していません。非侵害を保証するものではありません。
```
