import numpy as np
from time import time

class AIssGridCore:
    """
    AIss-Grid Core Ver 1.4 "Safe-Spine"
    反射（執行レイヤー）と思考（解析レイヤー）を分断し、0.05秒先の未来を実時間執行する。
    """
    def __init__(self, tau_base=0.05):
        # サンプリング周波数の階層化
        self.f_spine = 1000  # 1000Hzサンプリング
        self.f_brain = 1     # 1Hz（石碑化）
        
        # 動的進相制御（τ）
        self.tau_max = tau_base 
        self.tau_active = 0.0
        
        self.background_cache = None
        self.last_brain_update = 0
        self.stress_level = 0.5  # リスク勾配 Δrisk に相当

    def process_sensory_input(self, raw_wave, distance_r):
        current_t = time()
        
        # 1. 動的進相制御: τ = τ_max * tanh(k * Δrisk)
        # READMEの数式通り、tanhで未来予測量を動的に収束させる
        self.tau_active = self.tau_max * np.tanh(5.0 * self.stress_level)

        # A. 反射層 (Reflex Layer): 近距離執行
        if distance_r < 1.0:
            # 未来予測パルスの生成（進相投影）
            delta_v = np.gradient(raw_wave)
            future_pulse = raw_wave + (delta_v * self.tau_active)
            
            # 閾値 0.85 による判定執行
            decision = 1 if np.max(future_pulse) > 0.85 else 0
            return self._apply_orthogonal_friction(decision)

        # B. 思考層 (Reflection Layer): 構造のキャッシュ（石碑）化
        else:
            if current_t - self.last_brain_update > (1.0 / self.f_brain):
                # SHAP値解析の結果などを想定し、情報を静的キャッシュに格納
                self.background_cache = "CACHE_STABLE_MONOLITH"
                self.last_brain_update = current_t
            return self.background_cache

    def _apply_orthogonal_friction(self, decision):
        """
        認知的摩擦 (Orthogonal Friction)
        P_out(t) = f(t) + ε * noise(⊥) 
        AIへの完全同期を阻害し、ユーザーの主体性を保護する
        """
        if decision == 1:
            # 決定信号に微小な直交ノイズ（摩擦）を想定した出力を付与
            return "1_PULSE_WITH_FRICTION"
        return 0
