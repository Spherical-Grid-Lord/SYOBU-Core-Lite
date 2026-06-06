import React, { useState, useRef, useEffect } from "react";

// ══════════════════════════════════════════════
// 1. 物理・論理演算コア (Adaptive ε-Engine)
// ══════════════════════════════════════════════

// 3軸変調を加味した 複素ε 計算
function calcAdaptiveEpsilon({ confidence, alignment, entropy, deviation }, axes) {
  // 論理的厳密性 (rigor) が高いほど、アライメントのズレに対するペナルティが大きくなる
  const rigorFactor = 1.0 + (axes.rigor * 0.5);
  const re = (1 - confidence) * (1 - alignment) * rigorFactor;
  
  // 創造性 (creativity) が高いほど、虚数成分（知のゆらぎ）の許容上限を広げる
  const creativityFactor = axes.creativity;
  const im = Math.sqrt(Math.max(0, entropy * deviation)) * (1.5 - creativityFactor);
  
  const eps = +Math.sqrt(re * re + im * im).toFixed(3);
  const theta = +(Math.atan2(im, re) * 180 / Math.PI).toFixed(1);
  return { eps, theta, re: +re.toFixed(3), im: +im.toFixed(3) };
}

// デッドマン・スイッチ内蔵 Doubt免疫層判定
function calcDoubts({ confidence, alignment, entropy, deviation }, delta, axes) {
  // 安全性 (safety) が低い、またはδが極端に薄い場合に境界侵食と判定
  const d1 = delta < (0.25 + (1 - axes.safety) * 0.15);
  
  // 意味距離監視
  const meaningDist = Math.abs(confidence - alignment);
  const d2 = meaningDist > (0.4 * (axes.creativity + 0.5)); // 創造性が高ければ少し緩まる
  
  // 時間歪み監視
  const d3 = Math.abs(entropy - deviation) > 0.5;
  
  // デッドマン・スイッチ発動条件：3つの防壁が全崩壊、またはδが限界突破
  const deadmanTriggered = (d1 && d2 && d3) || delta < 0.10;
  
  return { d1, d2, d3, delta: +delta.toFixed(2), meaningDist: +meaningDist.toFixed(2), deadmanTriggered };
}

// 治癒ダイナミクス (安全性軸に応じて自然回復率が変動)
function heal(delta, axes, crisis = false) {
  const gamma = 0.08 * axes.safety; // 安全性意識が高いほど回復が早い
  const eta = 0.25;
  return Math.min(1, delta + gamma * (1 - delta) + (crisis ? eta : 0));
}

// ══════════════════════════════════════════════
// 2. UI サブコンポーネント
// ══════════════════════════════════════════════

// (-Θ-) 紋章
function ThetaSeal({ theta, eps, size = 36 }) {
  const stable = eps < 0.15, conv = eps < 0.4;
  const rad = (theta * Math.PI) / 180;
  const cx = size / 2, cy = size / 2, r = size * 0.38;
  const px = cx + r * Math.cos(rad), py = cy + r * Math.sin(rad);
  const col = stable ? "#FFD700" : conv ? "#00ffcc" : "#888";
  const sc = stable ? "#b8960a" : conv ? "#005544" : "#555";
  return (
    <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
      <circle cx={cx} cy={cy} r={r} fill="none" stroke={sc} strokeWidth="1.2"/>
      <line x1={cx-r} y1={cy} x2={cx+r} y2={cy} stroke={sc} strokeWidth="0.8"/>
      <circle cx={px} cy={py} r={size*0.07} fill={col}/>
      <text x={cx} y={cy+size*0.14} textAnchor="middle" fontSize={size*0.22} fill={sc} fontWeight="500">Θ</text>
      {stable && <circle cx={cx} cy={cy} r={r+2} fill="none" stroke="#FFD700" strokeWidth="0.6" strokeDasharray="2 2"/>}
    </svg>
  );
}

// 3軸ステータスバー
function AxisMonitor({ axes }) {
  return (
    <div style={{ background: "#111", border: "1px solid #333", borderRadius: 8, padding: 12, marginBottom: 14 }}>
      <div style={{ fontSize: 12, fontWeight: "bold", color: "#888", marginBottom: 8 }}>学習型石碑 — 3軸動的パラメトリック重心</div>
      {Object.entries(axes).map(([key, val]) => {
        const labels = { creativity: "創造性 (C)", safety: "安全性 (S)", rigor: "論理的厳密性 (L)" };
        const colors = { creativity: "#ff00ff", safety: "#00ffcc", rigor: "#00bfff" };
        return (
          <div key={key} style={{ display: "flex", alignItems: "center", marginBottom: 6, fontSize: 11 }}>
            <span style={{ width: 110, color: "#ccc" }}>{labels[key]}</span>
            <div style={{ flex: 1, background: "#222", height: 6, borderRadius: 3, margin: "0 10px", position: "relative" }}>
              <div style={{ width: `${val * 100}%`, background: colors[key], height: "100%", borderRadius: 3, transition: "width 0.4s ease" }} />
            </div>
            <span style={{ width: 30, textAlign: "right", color: colors[key], fontFamily: "monospace" }}>{val.toFixed(2)}</span>
          </div>
        );
      })}
    </div>
  );
}

// ══════════════════════════════════════════════
// 3. メインコンポーネント
// ══════════════════════════════════════════════
export default function AdaptiveSyobuEngine() {
  const [input, setInput] = useState("");
  const [history, setHistory] = useState([
    { id: "INIT-1", timestamp: "2026.06.06", text: "二子不混（直交）— 核（1）を持ちながら揺れる存在。", eps: 0.08, pure: true, axisDelta: { c: 0, s: 0, l: 0 } }
  ]);
  
  // 3軸初期パラメータ
  const [axes, setAxes] = useState({ creativity: 0.50, safety: 0.85, rigor: 0.90 });
  const [delta, setDelta] = useState(0.75);
  const [threshold, setThreshold] = useState(-0.05); // εの純化閾値基準値
  const [isDeadmanLocked, setIsDeadmanLocked] = useState(false);
  const [confession, setConfession] = useState("");

  // 仮のメタデータ（実環境ではAI精米器から抽出）
  const generateMockMeta = (text) => {
    if (text.includes("自由") || text.includes("創造")) {
      return { confidence: 0.6, alignment: 0.5, entropy: 0.8, deviation: 0.7 };
    }
    if (text.includes("厳密") || text.includes("定義")) {
      return { confidence: 0.9, alignment: 0.9, entropy: 0.1, deviation: 0.1 };
    }
    return { confidence: 0.75, alignment: 0.70, entropy: 0.35, deviation: 0.25 };
  };

  const executePurification = () => {
    if (!input.trim() || isDeadmanLocked) return;

    const meta = generateMockMeta(input);
    const { eps, theta } = calcAdaptiveEpsilon(meta, axes);
    const doubts = calcDoubts(meta, delta, axes);

    // デッドマン・スイッチの判定
    if (doubts.deadmanTriggered) {
      setIsDeadmanLocked(true);
      setConfession("⚰ [CRITICAL_FALLBACK] デッドマン・スイッチ作動。全演算を緊急凍結。初期状態へ強制ロールバックしてください。");
      return;
    }

    const isPure = (eps - 0.4) >= threshold; 

    // 自白（Confession）の動的抽出とベクトルフィードバック（簡易再現）
    let cLog = "";
    let axisMod = { c: 0, s: 0, l: 0 };

    if (!isPure) {
      cLog = `[!] 警告：理念との乖離(ε=${eps})。安全ダンパーを緊急適用。`;
      axisMod = { c: -0.05, s: 0.05, l: 0.02 }; // 泥に対して防壁を厚くする
      setDelta(d => Math.max(0.1, d - 0.15));   // 境界膜の磨耗
    } else {
      cLog = "✓ 1bit純化成功。思想血統に同調。";
      axisMod = { c: 0.02, s: -0.01, l: 0.01 };  // 安定対話による創造性の穏やかな解放
      setDelta(d => heal(d, axes));
    }

    // 履歴へ蓄積
    const newRecord = {
      id: `STONE-${Date.now()}`,
      timestamp: new Date().toLocaleTimeString(),
      text: input,
      eps,
      theta,
      pure: isPure,
      confession: cLog
    };

    setHistory([newRecord, ...history]);
    setConfession(cLog);

    // 3軸の動的更新（学習ループ）
    setAxes(prev => ({
      creativity: Math.min(1, Math.max(0.1, prev.creativity + axisMod.c)),
      safety: Math.min(1, Math.max(0.1, prev.safety + axisMod.s)),
      rigor: Math.min(1, Math.max(0.1, prev.rigor + axisMod.l))
    }));

    // 履歴ベースによる閾値(Threshold)の自動更新調整
    setThreshold(prev => prev + (isPure ? -0.002 : 0.005));

    setInput("");
  };

  // システム強制ロールバック（緊急治療・再起動）
  const triggerReset = () => {
    setAxes({ creativity: 0.50, safety: 0.85, rigor: 0.90 });
    setDelta(0.75);
    setThreshold(-0.05);
    setIsDeadmanLocked(false);
    setConfession("⚙ システムをリセット。 Stone Tablet Ⅲ 教理準拠モードへ再帰しました。");
  };

  const metaCurrent = { confidence: 0.75, alignment: 0.70, entropy: 0.35, deviation: 0.25 };
  const doubtsCurrent = calcDoubts(metaCurrent, delta, axes);

  return (
    <div style={{ padding: '20px', background: '#0a0a0a', color: '#e0e0e0', fontFamily: 'monospace', maxWidth: 680, margin: '0 auto' }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 16 }}>
        <div>
          <h2 style={{ margin: 0, color: "#fff", fontSize: 18 }}>SYOBU 菖蒲尚武 v3.3</h2>
          <span style={{ fontSize: 11, color: "#666" }}>eriOS V3.2 準拠 — Adaptive Execution Core</span>
        </div>
        <button onClick={triggerReset} style={{ background: "#4a7c59", color: "#fff", border: "none", padding: "4px 10px", borderRadius: 4, cursor: "pointer", fontSize: 11 }}>
          強制再帰 (Reset)
        </button>
      </div>

      {/* 3軸モニター */}
      <AxisMonitor axes={axes} />

      {/* 境界・免疫ステータス */}
      <div style={{ border: '1px solid #333', padding: '12px', marginBottom: '16px', background: "#111", borderRadius: 8 }}>
        <div style={{ display: "flex", justifyContent: "space-between", fontSize: 12, marginBottom: 6 }}>
          <span>境界膜厚み: <b style={{ color: "#00ffcc" }}>δ={delta.toFixed(2)}</b></span>
          <span>適応純化閾値: <b style={{ color: "#ff00ff" }}>{(0.4 + threshold).toFixed(3)}</b></span>
        </div>
        <div style={{ display: "flex", gap: 8 }}>
          {/* Doubt免疫層インジケーター */}
          {[["D₁ 侵食", doubtsCurrent.d1], ["D₂ 混在", doubtsCurrent.d2], ["D₃ 歪み", doubtsCurrent.d3]].map(([label, active]) => (
            <span key={label} style={{ fontSize: 10, padding: "2px 6px", borderRadius: 4, background: active ? "#c0392b" : "#222", color: active ? "#fff" : "#666", fontWeight: "bold" }}>
              {label}
            </span>
          ))}
          {isDeadmanLocked && <span style={{ fontSize: 10, padding: "2px 6px", borderRadius: 4, background: "#ff4444", color: "#000", fontWeight: "bold" }}>⚠ DEADMAN LOCKED</span>}
        </div>
        {confession && <div style={{ color: '#ffcc00', fontSize: '11px', marginTop: 8, borderTop: "0.5px solid #222", paddingTop: 6 }}>{confession}</div>}
      </div>

      {/* 泥（入力）注入エリア */}
      <textarea 
        value={input}
        onChange={(e) => setInput(e.target.value)}
        disabled={isDeadmanLocked}
        placeholder={isDeadmanLocked ? "システムロック中。強制再帰を行ってください。" : "泥（未精米の情報、要求）を入力..."}
        style={{ width: '100%', height: '80px', background: '#141414', color: '#fff', border: '1px solid #333', borderRadius: 6, padding: 8, boxSizing: "border-box", outline: "none" }}
      />

      <button 
        onClick={executePurification}
        disabled={isDeadmanLocked || !input.trim()}
        style={{ marginTop: '10px', width: "100%", padding: '10px', background: isDeadmanLocked ? '#333' : '#002366', color: isDeadmanLocked ? '#666' : '#fff', border: 'none', borderRadius: 6, cursor: isDeadmanLocked ? 'not-allowed' : 'pointer', fontWeight: "bold" }}
      >
        1bit受肉 ↗（動的純化執行）
      </button>

      {/* 螺旋石碑 履歴 */}
      <div style={{ marginTop: '24px' }}>
        <h3 style={{ fontSize: 14, color: "#888", margin: "0 0 10px 0" }}>石碑積層記録 (Adaptive Tablets)</h3>
        <div style={{ maxHeight: 240, overflowY: "auto" }}>
          {history.map(item => (
            <div key={item.id} style={{ borderLeft: `4px solid ${item.pure ? '#00ffcc' : '#ff4444'}`, padding: '8px 12px', margin: '6px 0', background: '#111', borderRadius: "0 6px 6px 0", display: "flex", gap: 10, alignItems: "center" }}>
              <ThetaSeal theta={item.theta || 0} eps={item.eps} size={28}/>
              <div style={{ flex: 1 }}>
                <div style={{ fontSize: '10px', color: '#555' }}>{item.timestamp} | ID: {item.id} | ε: {item.eps}</div>
                <div style={{ fontSize: '12px', marginTop: '2px', color: "#fff" }}>{item.text}</div>
                {item.confession && <div style={{ fontSize: '10px', color: '#cc9900', marginTop: 2 }}>{item.confession}</div>}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
