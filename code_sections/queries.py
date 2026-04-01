from typing import Dict
from datetime import datetime

def get_queries(start_time: datetime, end_time: datetime) -> Dict[str, str]:
    """Gibt NUR Basis-PromQL-Metriken zurück (KEINE Aggregationen)."""
    return {
        # System Status
        "attack_ongoing": "attack_ongoing",

        # Power Metrics (Basis)
        "ids_power_bus_voltage": "ids_power_bus_voltage_V",
        "ids_power_current": "ids_power_current_mA",
        "ids_power_power": "ids_power_power_mW",
        "ids_power_shunt_voltage": "ids_power_shunt_voltage_mV",
        "ids_power_lstm_mse": "ids_power_lstm_mse",                  
        "ids_power_isolation_score": "ids_power_isolation_score",  

        # Temperature Metrics (Basis)
        "ids_temperature": "ids_temperature",
        "evse_thermo_current_temp": "evse_thermo_current_temp_celsius",

        # Wattmeter Status
        "ids_wattmeter": "ids_wattmeter",

        # Anomaly Detection
        "ids_power_isolation_forest_anomaly": "ids_power_isolation_forest_anomaly",
        "ids_power_lstm_anomaly": "ids_power_lstm_anomaly",

        # Transformer ML Predictions (Basis)
        "transformer_prediction": "transformer_prediction",
        "ids_transformer_attack_probability": "ids_transformer_attack_probability",
        "ids_transformer_shunt_voltage": "ids_transformer_shunt_voltage",
        "ids_transformer_bus_voltage": "ids_transformer_bus_voltage",
        "ids_transformer_current": "ids_transformer_current",
        "ids_transformer_power": "ids_transformer_power",
        "ids_transformer_raw_prediction": "ids_transformer_raw_prediction",

        # xLSTM Metrics
        "ids_xlstm_prediction": "ids_xlstm_prediction",
        "ids_xlstm_attack_probability": "ids_xlstm_attack_probability",
        "ids_xlstm_reconstruction_loss": "ids_xlstm_reconstruction_loss",

        # Ensemble
        "ids_ensemble_final_decision": "ids_ensemble_final_decision",

        # Hardware Features (Basis)
        "ids_hardware_feature_node_stores": "ids_hardware_feature_node_stores",
        "ids_hardware_feature_bus_access": "ids_hardware_feature_bus_access",
        "ids_hardware_feature_skb_kfree_skb": "ids_hardware_feature_skb_kfree_skb",
        "ids_hardware_feature_cpu_cycles": "ids_hardware_feature_cpu_cycles",
        "ids_hardware_feature_l2d_cache_wb_victim": "ids_hardware_feature_l2d_cache_wb_victim",
        "ids_hardware_feature_syscalls_sys_enter_fcntl": "ids_hardware_feature_syscalls_sys_enter_fcntl",
        "ids_hardware_feature_sched_sched_stat_runtime": "ids_hardware_feature_sched_sched_stat_runtime",
        "ids_hardware_feature_st_spec": "ids_hardware_feature_st_spec",
        "ids_hardware_feature_syscalls_sys_enter_kill": "ids_hardware_feature_syscalls_sys_enter_kill",
        "ids_hardware_feature_fib_fib_table_lookup": "ids_hardware_feature_fib_fib_table_lookup",
        "ids_hardware_feature_sock_inet_sock_set_state": "ids_hardware_feature_sock_inet_sock_set_state",
        "ids_hardware_feature_l2d_cache_wb": "ids_hardware_feature_l2d_cache_wb",
        "ids_hardware_feature_unaligned_st_spec": "ids_hardware_feature_unaligned_st_spec",
        "ids_hardware_feature_mem_access_rd": "ids_hardware_feature_mem_access_rd",
        "ids_hardware_feature_l2d_cache_refill_wr": "ids_hardware_feature_l2d_cache_refill_wr",
        "ids_hardware_feature_mmc_mmc_request_start": "ids_hardware_feature_mmc_mmc_request_start",
        "ids_hardware_feature_br_mis_pred": "ids_hardware_feature_br_mis_pred",

        # Hardware Attack Detection
        "ids_hardware_attack_probability": "ids_hardware_attack_probability",
        "ids_hardware_benign_probability": "ids_hardware_benign_probability",
        "ids_hardware_attack_prediction": "ids_hardware_attack_prediction",

        # IoT Platform Metrics (neu hinzugefügt aus neuen Metriken)
        "iotplatform_meter_bus_voltage": "iotplatform_meter_bus_voltage_V",
        "iotplatform_meter_current": "iotplatform_meter_current_mA",
        "iotplatform_meter_power": "iotplatform_meter_power_mW",
        "iotplatform_meter_shunt_voltage": "iotplatform_meter_shunt_voltage_mV",
    }