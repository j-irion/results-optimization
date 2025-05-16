import hydra
import pandas as pd

@hydra.main(config_path=".", config_name="config", version_base=None)
def main(cfg):
  df = pd.read_csv(cfg.results_csv)
  wind_cap, solar_cap, batt_cap = cfg.wind_system_capacity, cfg.solar_system_capacity, cfg.battery_capacity

  embodied_emissions_initial_g = df.loc[
      (df['wind'] == wind_cap) &
      (df['solar'] == solar_cap) &
      (df['battery'] == batt_cap),
      'embodied_emissions_initial_g'
  ].values[0]

  total_grid_draw_kwh = df.loc[
      (df['wind'] == wind_cap) &
      (df['solar'] == solar_cap) &
      (df['battery'] == batt_cap),
      'total_grid_draw_kwh'
  ].values[0]

  operational_emissions_total_g = df.loc[
      (df['wind'] == wind_cap) &
      (df['solar'] == solar_cap) &
      (df['battery'] == batt_cap),
      'operational_emissions_total_g'
  ].values[0]

  operational_carbon_intensity = operational_emissions_total_g / total_grid_draw_kwh


  return operational_carbon_intensity, embodied_emissions_initial_g


if __name__ == "__main__":
    main()