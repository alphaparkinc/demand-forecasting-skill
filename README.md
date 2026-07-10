# genpark-demand-forecasting-skill

> **GenPark AI Agent Skill** -- Forecast product demand using historical sales, seasonality decomposition, and trend detection.

## Features

- Exponential smoothing baseline forecast
- Linear trend detection (growing / stable / declining)
- Multiplicative seasonality index decomposition
- 80%/120% confidence interval bounds
- Safety stock calculation with lead time adjustment
- Reorder point and suggested order quantity

## Quick Start

```python
from client import DemandForecastingClient

client = DemandForecastingClient()
result = client.forecast(
    sales_history=[{"period": "Jan", "units_sold": 120}, {"period": "Feb", "units_sold": 135}],
    forecast_periods=6,
    lead_time_periods=2,
)
print(result["trend"], result["reorder_recommendation"])
```

## Installation

```bash
python example_usage.py  # No external dependencies
```

---
Built by [GenPark](https://genpark.ai) | [alphaparkinc](https://github.com/alphaparkinc)
