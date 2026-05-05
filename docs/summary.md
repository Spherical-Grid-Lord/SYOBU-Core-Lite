# Human–AI Common Language Layer — One‑Page Summary (v0.2.1)
# 人とAIの共通言語層 — 1枚サマリ（v0.2.1）

> **Scope / 公開範囲**
> This document is a public‑safe summary. It is not a full specification.
> 本文は公開可能な範囲の概要です。正式仕様書の代替ではありません。

---

## 1. Purpose / 目的
**EN**: Map multisensory + internal signals into a traceable structure and a shared human–AI language layer.
**JP**: 視覚・音響・触覚・運動・内部状態（将来的にMRI/rt‑fMRI系特徴量やAI内部特徴量を含み得る）を、追跡可能な構造表現と人間可読説明へ接続する。
- The attached 2D diagram is an **illustrative visual profile** and must be treated as **display_only** (not a full module diagram).
- 添付2D図は**視覚プロファイル例示**であり、**display_only**（全体モジュール図ではない）。

---

## 2. Four Layers You Must Separate / 必ず分ける4層
1) **Observation / 観測層**
- Raw measured/recorded inputs (modalities, timestamps, coordinates, files).
2) **Structure / 構造層**
- Coordinates, Nodes, continuous evidence, relations, time series, sync status.
3) **Semantics / 意味層**
- Minimal semantic units (1‑bit or few‑bit).
4) **Explanation / 説明層**
- Human‑readable labels, short text, notes.

> **Rule / ルール**: Do not use Explanation to “fill” missing Observation/Structure/Semantics.
> 説明層だけで観測・構造・意味を補完しない。

---

## 3. MUST / 絶対（MUST）
- Do not conflate the four layers. / 4層を混同しない
- Do not store semantics as “bits only.” Keep traceability fields where possible.
/ 1bit（少数bit）だけを保存しない（可能な範囲で追跡情報を保持）
- Do not treat **display_only** diagrams/labels as evidence for **full**.
/ display_only 図を full 根拠にしない
- Do not canonize local Node results as “authoritative.”
/ Node局所結果をそのまま正本化しない
- Do not use internal signals for diagnosis, disease inference, mental‑state determination, or treatment decisions.
/ 内部状態を診断・疾病推定・精神状態確定・治療判断に使わない
- Do not hard‑fix external research into the spec body. Put it into Evidence Notes first.
/ 外部研究を本体仕様に直固定しない（Evidence Noteへ退避）

### Traceability fields to retain (minimum set) / 追跡情報（最低限）
- `source_modality`
- `coordinate_ref`
- `time_ref`
- `continuous_evidence`
- `threshold_profile`
- `confidence`
- `guarantee_level`
- `known_limits`

---

## 4. guarantee_level / 保証水準
- **full**: Node + semantics + continuous evidence + rule/threshold + modality + time are traceable.
- **partial**: Some traceability exists, but important parts are missing.
- **display_only**: Only diagrams/labels/explanations remain; not valid as full evidence.
- **unknown**: Traceability range cannot be determined.

> **Upgrade rule / 引き上げルール**: Upgrade to **full** only after integrated consistency checks (not by a single local Node).

---

## 5. Node Selection Guide / Node選択の目安
Node is a **local structural unit**, not “meaning itself.”

| What you handle / 扱う内容 | Suggested Node type / Node型 |
|---|---|
| Spatial position / 空間位置 | `spatial_node` |
| Object/agent / 対象物 | `object_node` |
| Path / 経路 | `path_node` |
| Approach / crossing / interference / 接近・交差・干渉 | `interaction_node` / `conflict_node` |
| Attention cue / 注意誘導 | `attention_node` |
| Internal state / 内部状態 | `internal_state_node` |
| Acoustic focus / 音響焦点 | `acoustic_focus_node` |
| Tactile contact / 接触・圧力 | `tactile_contact_node` |
| Motion stability / 姿勢・運動安定性 | `motion_stability_node` |
| Cross‑modal sync / モダリティ同期 | `cross_modal_sync_node` |
| Void / 空隙 | `void_node` |
| Occlusion / 遮蔽 | `occlusion_node` |
| Risk singularity / 危険集中点 | `risk_singularity_node` |

> **Rule / ルール**: Local Node output is not automatically authoritative. Integrate when needed.

---

## 6. Core Semantic Vocabulary / 中核語彙（例）
Start small; avoid uncontrolled vocabulary growth.

- `risk_bit`
- `occlusion_bit`
- `void_bit`
- `path_bit`
- `approach_bit`
- `conflict_bit`
- `attention_bit`
- `stability_bit`
- `interoceptive_change_bit`
- `sync_conflict_bit`

> Same label ≠ same evidence: keep modality‑specific evidence/threshold/limits.
> 同じbit名でも、由来モダリティが違えば同一根拠として扱わない。

---

## 7. Internal Signals / 内部状態の扱い（重要）
Internal signals may include HR, respiration, skin conductance, EMG, physiological variability,
MRI/rt‑fMRI features, brain network features, and AI internal features.

**Operational defaults / 運用原則**
- Start from **partial** or **unknown** (not full).
- Always record:
- `baseline_ref`
- `noise_correction_status`
- `synchronization_status`
- `feature_source_model`
- `known_limits`

**Hard prohibitions / 禁止**
- Medical diagnosis / 疾病診断
- Disease inference / 疾病推定
- Mental‑state determination / 精神状態の確定
- Treatment decisions / 治療判断
- Claiming a person’s will/emotions/personality as “determined” / 意思・感情・人格の断定

---

## 8. Evidence Note / Evidence Note（外部研究の扱い）
External papers, implementations, and trends should be recorded as Evidence Notes first.
They are **background/candidates**, not “fixed spec.”

Minimum fields (recommended):
- `evidence_id`
- `source_title`
- `source_type`
- `publication_date`
- `peer_review_status`
- `relevance`
- `limits`
- `last_checked_date`
- `spec_adoption_status`

---

## 9. Output Template / 出力テンプレ（推奨）
When you produce an analysis, keep the following structure when possible:

- **[P: Observation / 観測]**
Inputs, modality, timestamps, coordinates, file facts.
- **[S: Structure / 構造]**
Nodes, coordinates, continuous evidence, relations, time series, sync.
- **[M: Semantics / 意味]**
Semantic bits (e.g., risk/occlusion/void/path/conflict).
- **[E: Explanation / 説明]**
Human‑readable labels, short text, notes.
- **[G: Guarantee / 保証]**
guarantee_level, known_limits, confidence, missing evidence.
- **[R: Next / 次の一手]**
What can be fixed now, what should remain unknown, what to verify next.

---

## 10. Final Principles / 最終原則
- A diagram is an entry point, not the whole system. / 図は入口であり全体ではない
- 2D is illustrative, not “the world.” / 2Dは例示であり世界ではない
- Bits are not evidence; keep the evidence. / 1bitは芯だが根拠の代替ではない
- Nodes are local structure, not the canon. / Nodeは局所構造で正本ではない
- Labels are bridges, not proof. / ラベルは橋であり証拠ではない
- Treat internal signals with care. / 内部状態は慎重に扱う
- Keep “unknown” as unknown. / 不明は不明のまま保持する
- Never upgrade display_only to full. / display_only を full にしない
- Never treat partial as diagnosis. / partial を診断にしない
- The more you assert meaning, the more you must retain evidence. / 意味を立てるほど根拠を残す
```
