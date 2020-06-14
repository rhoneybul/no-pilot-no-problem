CREATE TABLE flight_metrics (
  time            TIMESTAMPTZ       NOT NULL,
  height          DOUBLE PRECISION,
  speed           DOUBLE PRECISION,
  simulation_id   VARCHAR(100),
  device_id       VARCHAR(100)
);

SELECT create_hypertable('flight_metrics', 'time')