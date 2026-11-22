def add_features(data):
    """Признаки одного клиента, доступные до решения об уходе."""
    result = data.copy()
    extras = ["OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport",
              "StreamingTV", "StreamingMovies"]
    result["extra_count"] = data[extras].eq("Yes").sum(axis=1)
    result["new_customer"] = data["tenure"].le(12).astype(int)
    result["automatic_payment"] = data["PaymentMethod"].isin(
        ["Bank transfer (automatic)", "Credit card (automatic)"]).astype(int)
    return result
