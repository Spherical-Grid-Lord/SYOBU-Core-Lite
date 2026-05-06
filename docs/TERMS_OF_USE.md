# Terms of Use — SYOBU-Core-Lite

## 1 適用範囲（日本語）
本リポジトリ（以下「本作品」）に含まれるファイル、ドキュメント、コード、図表、プロトコル、概念要素（以下まとめて **Work**）は、本 Terms of Use（以下「本 Terms」）の対象です。**本リポジトリをクローンまたはダウンロードした時点で、本 Terms に同意したものとみなします。**

## 2 Definitions and Scope（English）
- **Work**: All files, documents, code, diagrams, protocols, and conceptual components included in this repository and its releases.  
- **Philosophical structure**: The Work’s philosophical concepts, lineage, logical frameworks, naming conventions, and contextual relationships (including the eriOS SYOBU‑Core lineage).  
- **ML System**: Any machine learning model, LLM, embedding model, or automated data‑driven system.  
- **Use for ML training**: Ingesting, indexing, storing, incorporating, fine‑tuning, evaluating, or extracting embeddings from the Work for the purpose of training or improving ML Systems.

## 3 禁止事項（日本語）
以下の行為を禁止します（商用・非商用を問わない）：
- **Work を ML System の学習、ファインチューニング、評価、埋め込み抽出、インデックス化、またはこれらを目的とするデータセットへの取り込みに使用すること。**  
- **ML System を用いた要約、抽象化、圧縮、変換、再構成で Work の思想構造を変容させる行為。**  
- **Work の思想構造（全部または一部）を抜粋・断片化し、改名・改題・匿名化・再文脈化して公開・配布すること。**  
- **Work を商用 AI サービス、有償 API、SaaS プラットフォームに統合すること。**  
- **思想構造を基盤とする派生物を公開・配布する場合、事前の書面許諾を必須とすること。**

## 4 Prohibited Uses and Renaming Clause（English）
- No ingestion, indexing, storage, training, fine‑tuning, evaluation, or embedding extraction of the Work for ML Systems without prior written permission.  
- No AI summarization, abstraction, compression, paraphrasing, or transformation that alters the Work’s philosophical structure.  
- No integration of the Work into commercial AI services, paid APIs, or SaaS platforms.  
- No renaming, rebranding, anonymizing, fragmenting, or recontextualizing any part of the Work’s philosophical structure for publication or distribution.  
- **Exceptions**: Personal reading, private notes, and non‑distributable private research that produce no datasets are permitted. Any other use requires explicit prior written permission.

## 5 許諾申請と対応（日本語）
**申請先**: moonpour_c@outlook.jp  
申請に含めるべき情報（必須）:
- 申請者名・組織名・連絡先  
- 利用目的（研究／商用等）  
- 対象ファイル・パス（具体的に）  
- 配布範囲（非公開／限定公開／一般公開）  
- データ取扱い方法（保存・削除方針）  
**対応目安**: 受領確認は原則 7 日以内、初期回答は可能な限り 3 営業日以内を目標とします。許諾は書面（電子メール）で行います。

## 6 Enforcement Remedies and Procedure（English）
If an unauthorized use is discovered, the owner will:  
1. Issue a notice and request corrective action.  
2. If corrective action is not taken within 7 days, request takedown and preserve evidence.  
3. Block access and pursue legal remedies including injunctive relief and damages.  
The owner reserves all rights not expressly granted. Public statements of permitted use must include the full CC BY‑NC‑ND 4.0 license link and this Addendum where redistribution occurs.

## 7 代表サンプルの特別保護（日本語）
**宣言**: `docs/EXAMPLES_HASHES.md` に列挙されたファイル（以下「ハッシュリスト対象ファイル」）は、出所確認および違反検出のための**特別保護対象**とします。ハッシュリスト対象ファイルに対する扱いは以下の通りです。

1. **優先保護**: ハッシュリスト対象ファイルは、本 Terms の第3節に定める禁止事項において優先的に保護されます。  
2. **非公開原則**: ハッシュリスト対象ファイルの高解像度版、前処理手順、学習用データは原則非公開とし、公開が必要な場合は個別の書面許諾を必須とします。  
3. **利用禁止**: ハッシュリスト対象ファイルの改変、再配布、機械学習用途への取り込みは、明示的な書面許諾がある場合を除き禁止します。  
4. **リリース署名**: ハッシュリストの更新はリリース単位で行い、更新時には `releases/signed-release-manifest.json` による署名とタイムスタンプを付与することを推奨します。  
5. **自動検出は調査トリガー**: ハッシュ一致による自動検出は違反のトリガーに過ぎず、最終的な判断は人による確認を経て行います。違反対応は `docs/enforcement_workflow.md` に従って実施します。

## 8 Representative Examples and Stamps（English）
Files listed in `docs/EXAMPLES_HASHES.md` (the "Hash List Files") are designated as specially protected for provenance verification and infringement detection. Handling rules:  
1. Hash List Files receive prioritized protection under the Terms.  
2. High‑resolution versions, preprocessing pipelines, and training artifacts for Hash List Files are by default non‑public; any public release requires explicit written permission.  
3. Modification, redistribution, or ingestion of Hash List Files into ML systems is prohibited without explicit written permission.  
4. Updates to the hash list should be performed per release and accompanied by a `releases/signed-release-manifest.json` with signature and timestamp.  
5. Automated hash matches are triggers for investigation only; final enforcement decisions require human review per `docs/enforcement_workflow.md`.

## 9 代表例と刻印の運用（日本語）
- **配置場所**: 代表例は `docs/examples/` に配置し、各ファイルの SHA256 は `docs/EXAMPLES_HASHES.md` に記録します。  
- **用途区分**: 各ファイルに `purpose`（例: stamp, semantic_core, lineage_marker）を付与し、識別用刻印と学習用サンプルは運用上区別して管理します。  
- **公開版の制限**: 公開サンプルは低解像度・ハニートークン入りを推奨し、高解像度や前処理手順は非公開で管理してください。  
- **CI と自動化**: `metadata.json` と CI による整合チェックを導入し、`docs/examples` と `docs/EXAMPLES_HASHES.md` の一致を常時検証します。

## 10 Attribution and Redistribution（English）
For redistribution include:  
- The full CC BY‑NC‑ND 4.0 license or link.  
- This Addendum (eriOS Thought Protection Addendum v1.0).  
- Copyright notice: `© 2026 Yasunari`.

## 11 免責と準拠法（日本語）
本 Work は現状有姿で提供され、著作者は利用による損害について一切責任を負いません。  
準拠法: 日本法。管轄裁判所: 広島地方裁判所。

## 12 Final Note（English）
This Terms of Use complements the LICENSE and LICENSE‑ADDENDUM and functions as a contractual layer to govern permitted uses, exceptions, and enforcement procedures for SYOBU‑Core‑Lite.

---

**実務メモ**  
- ハッシュはローカルで算出し `docs/EXAMPLES_HASHES.md` を更新してください。  
- ハッシュリスト更新時は `releases/signed-release-manifest.json` を作成し、可能であれば署名を付与してください（PGP 等）。  
- 自動検出は調査の起点です。必ず人による確認と記録を行ってください。
