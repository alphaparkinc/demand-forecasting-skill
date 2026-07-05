"""
example_usage.py -- Demonstrates the DemandForecastingClient SDK.
"""
from client import DemandForecastingClient

def main():
    client = DemandForecastingClient()

    # 18 months of historical sales with seasonal pattern
    history = [
        {"period": "Jan-25", "units_sold": 120}, {"period": "Feb-25", "units_sold": 105},
        {"period": "Mar-25", "units_sold": 145}, {"period": "Apr-25", "units_sold": 160},
        {"period": "May-25", "units_sold": 175}, {"period": "Jun-25", "units_sold": 190},
        {"period": "Jul-25", "units_sold": 210}, {"period": "Aug-25", "units_sold": 205},
        {"period": "Sep-25", "units_sold": 185}, {"period": "Oct-25", "units_sold": 220},
        {"period": "Nov-25", "units_sold": 310}, {"period": "Dec-25", "units_sold": 380},
        {"period": "Jan-26", "units_sold": 130}, {"period": "Feb-26", "units_sold": 115},
        {"period": "Mar-26", "units_sold": 158}, {"period": "Apr-26", "units_sold": 172},
        {"period": "May-26", "units_sold": 190}, {"period": "Jun-26", "units_sold": 205},
    ]

    print("[Demand Forecasting -- 6-Month Outlook]")
    result = client.forecast(
        sales_history=history,
        forecast_periods=6,
        lead_time_periods=2,
        safety_stock_factor=1.5,
    )
    print(f"Summary: {result['summary']}")
    print(f"Trend: {result['trend']} (slope: {result['trend_slope']:+})")
    print(f"Avg Historical Demand: {result['avg_historical_demand']} units/period")
    print(f"Seasonality Index: {result['seasonality_index']}")
    print(f"\n6-Month Forecast:")
    print(f"{'Period':<8} {'Predicted':>12} {'Low':>10} {'High':>10}")
    for f in result["forecast"]:
        print(f"{f['period']:<8} {f['predicted_units']:>12.1f} {f['lower_bound']:>10.1f} {f['upper_bound']:>10.1f}")
    r = result["reorder_recommendation"]
    print(f"\nReorder Recommendation:")
    print(f"  Reorder Point: {r['reorder_point_units']} units")
    print(f"  Safety Stock:  {r['safety_stock_units']} units")
    print(f"  Order Qty:     {r['suggested_order_qty']} units")

if __name__ == "__main__":
    main()
